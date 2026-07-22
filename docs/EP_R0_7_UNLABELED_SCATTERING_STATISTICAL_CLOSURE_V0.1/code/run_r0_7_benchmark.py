
from pathlib import Path
import csv, json
from collections import Counter, defaultdict
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import label as cc_label
from scipy.optimize import curve_fit

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
RESULTS.mkdir(exist_ok=True)
FIGURES.mkdir(exist_ok=True)

G, H6 = 2.0, 1.0
AMP, WIDTH, SEP = 1.4, 2.2, 12.0
THRESHOLD = 0.20
ACTIVITY_FRACTION = 0.10

SPEEDS = np.array([0.35, 0.55, 0.75, 0.95, 1.15])
PHASES = np.array([0, np.pi/6, np.pi/3, np.pi/2, 2*np.pi/3, 5*np.pi/6, np.pi])
IMPACTS = np.array([0.0, 0.8, 1.6])

def grid(n, length):
    x = np.linspace(-length/2, length/2, n, endpoint=False)
    dx = length / n
    X, Y = np.meshgrid(x, x, indexing="xy")
    k = 2*np.pi*np.fft.fftfreq(n, d=dx)
    KX, KY = np.meshgrid(k, k, indexing="xy")
    return dx, X, Y, KX, KY, KX*KX + KY*KY

def initial_field(X, Y, speed, phase, impact):
    r1 = (X + SEP/2)**2 + (Y + impact/2)**2
    r2 = (X - SEP/2)**2 + (Y - impact/2)**2
    p1 = AMP*np.exp(-r1/WIDTH**2)*np.exp(1j*speed*X)
    p2 = AMP*np.exp(-r2/WIDTH**2)*np.exp(-1j*speed*X + 1j*phase)
    return p1 + p2

def step(psi, linear, dt):
    rho = np.abs(psi)**2
    psi = psi*np.exp(1j*(G*rho - H6*rho*rho)*dt/2)
    psi = np.fft.ifft2(np.fft.fft2(psi)*linear)
    rho = np.abs(psi)**2
    return psi*np.exp(1j*(G*rho - H6*rho*rho)*dt/2)

def derivs(psi, KX, KY):
    F = np.fft.fft2(psi)
    return np.fft.ifft2(1j*KX*F), np.fft.ifft2(1j*KY*F)

def components(psi, X, Y, KX, KY, dx, min_pixels):
    rho = np.abs(psi)**2
    labels, raw = cc_label(rho >= THRESHOLD, structure=np.array([[0,1,0],[1,1,1],[0,1,0]]))
    dxp, dyp = derivs(psi, KX, KY)
    jx = np.imag(np.conj(psi)*dxp)
    jy = np.imag(np.conj(psi)*dyp)
    out = []
    for idx in range(1, raw+1):
        mask = labels == idx
        if int(mask.sum()) < min_pixels:
            continue
        mass = float(np.sum(rho[mask])*dx*dx)
        cx = float(np.sum(rho[mask]*X[mask])*dx*dx/mass)
        cy = float(np.sum(rho[mask]*Y[mask])*dx*dx/mass)
        px = float(np.sum(jx[mask])*dx*dx)
        py = float(np.sum(jy[mask])*dx*dx)
        phase = float(np.angle(np.sum(psi[mask]*rho[mask])*dx*dx))
        xx, yy = X[mask]-cx, Y[mask]-cy
        Q = np.array([
            [np.sum(rho[mask]*xx*xx), np.sum(rho[mask]*xx*yy)],
            [np.sum(rho[mask]*xx*yy), np.sum(rho[mask]*yy*yy)]
        ])*dx*dx/mass
        eig, vec = np.linalg.eigh(Q)
        principal = vec[:, np.argmax(eig)]
        out.append({
            "mass": mass,
            "centroid_x": cx,
            "centroid_y": cy,
            "momentum_x": px,
            "momentum_y": py,
            "mean_phase": phase,
            "orientation": float(np.arctan2(principal[1], principal[0])),
            "anisotropy": float((eig.max()-eig.min())/max(eig.sum(), 1e-14))
        })
    out.sort(key=lambda z: z["centroid_x"])
    return out

def sequence(values):
    out = []
    for v in values:
        v = int(v)
        if not out or out[-1] != v:
            out.append(v)
    return out

def classify(counts):
    seq = sequence(counts)
    final, mn = seq[-1], min(seq)
    if final >= 3:
        cls = "fragmentation"
    elif final == 1:
        cls = "persistent_fusion_candidate"
    elif mn == 1 and final == 2:
        cls = "fusion_fission_scattering"
    elif mn == 2 and final == 2:
        cls = "two_component_scattering"
    elif final == 0:
        cls = "dispersal"
    else:
        cls = "unresolved"
    return cls, seq

def invariants(psi, X, Y, KX, KY, dx):
    rho = np.abs(psi)**2
    dxp, dyp = derivs(psi, KX, KY)
    H = np.sum(0.5*(np.abs(dxp)**2+np.abs(dyp)**2) - 0.5*G*rho**2 + H6*rho**3/3)*dx*dx
    jx = np.imag(np.conj(psi)*dxp)
    jy = np.imag(np.conj(psi)*dyp)
    return {
        "norm": float(np.sum(rho)*dx*dx),
        "energy": float(np.real(H)),
        "px": float(np.sum(jx)*dx*dx),
        "py": float(np.sum(jy)*dx*dx),
        "Lz": float(np.sum(np.imag(np.conj(psi)*(X*dyp-Y*dxp)))*dx*dx),
    }

def run_case(speed, phase, impact, n=64, length=36.0, dt=0.008, T=12.0, sample_dt=0.16, min_pixels=20):
    dx, X, Y, KX, KY, K2 = grid(n, length)
    psi0 = initial_field(X, Y, speed, phase, impact)
    psi = psi0.copy()
    linear = np.exp(-0.5j*K2*dt)
    steps = int(round(T/dt))
    stride = max(1, int(round(sample_dt/dt)))

    times, counts, sn, sxy = [], [], [], []
    for s in range(steps+1):
        if s % stride == 0 or s == steps:
            c = components(psi, X, Y, KX, KY, dx, min_pixels)
            dxp, dyp = derivs(psi, KX, KY)
            times.append(s*dt)
            counts.append(len(c))
            sn.append(float(np.sum(np.abs(dxp)**2 - np.abs(dyp)**2)*dx*dx))
            sxy.append(float(np.sum(np.real(np.conj(dxp)*dyp))*dx*dx))
        if s < steps:
            psi = step(psi, linear, dt)

    times = np.array(times)
    counts = np.array(counts)
    sn = np.array(sn)
    sxy = np.array(sxy)
    base_n, base_xy = np.mean(sn[:3]), np.mean(sxy[:3])
    activity = np.sqrt((sn-base_n)**2 + 4*(sxy-base_xy)**2)
    peak = float(activity.max())
    peak_idx = int(activity.argmax())
    active = activity > ACTIVITY_FRACTION*max(peak, 1e-14)
    duration = float(np.sum(np.diff(times)*active[:-1]))
    impulse = float(np.trapezoid(activity, times))
    eq_time = float(impulse/max(peak, 1e-14))
    cls, seq = classify(counts)
    return {
        "speed": float(speed), "phase": float(phase), "impact": float(impact),
        "class": cls, "seq": seq, "counts": counts, "times": times,
        "activity": activity, "peak": peak, "peak_idx": peak_idx,
        "duration": duration, "impulse": impulse, "eq_time": eq_time,
        "initial": psi0, "final": psi,
        "grid": (dx, X, Y, KX, KY, K2),
        "initial_components": components(psi0, X, Y, KX, KY, dx, min_pixels),
        "final_components": components(psi, X, Y, KX, KY, dx, min_pixels),
    }

# ------------------------------------------------------------
# 105-case frozen scan
# ------------------------------------------------------------
records, cases = [], []
case_id = 0
for impact in IMPACTS:
    for speed in SPEEDS:
        for phase in PHASES:
            c = run_case(speed, phase, impact)
            case_id += 1
            records.append({
                "case_id": case_id,
                "speed": c["speed"],
                "phase": c["phase"],
                "phase_over_pi": c["phase"]/np.pi,
                "impact_parameter": c["impact"],
                "event_class": c["class"],
                "topology_sequence": "-".join(map(str, c["seq"])),
                "minimum_component_count": int(c["counts"].min()),
                "maximum_component_count": int(c["counts"].max()),
                "final_component_count": int(c["counts"][-1]),
                "activity_duration": c["duration"],
                "activity_impulse": c["impulse"],
                "equivalent_time": c["eq_time"],
                "peak_activity": c["peak"],
                "peak_time": float(c["times"][c["peak_idx"]]),
            })
            cases.append(c)

with open(RESULTS/"event_scan.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(records[0].keys()))
    w.writeheader()
    w.writerows(records)

counts = Counter(r["event_class"] for r in records)
metrics = defaultdict(lambda: defaultdict(list))
for r in records:
    for key in ["activity_duration", "activity_impulse", "equivalent_time", "peak_activity"]:
        metrics[r["event_class"]][key].append(r[key])

class_summary = {}
for cls, group in metrics.items():
    row = {"count": len(group["equivalent_time"])}
    for key, vals in group.items():
        arr = np.asarray(vals)
        row[key+"_mean"] = float(arr.mean())
        row[key+"_std"] = float(arr.std(ddof=1) if len(arr)>1 else 0)
    class_summary[cls] = row

with open(RESULTS/"class_summary.csv", "w", newline="", encoding="utf-8") as f:
    fields = ["event_class","count","activity_duration_mean","activity_duration_std",
              "activity_impulse_mean","activity_impulse_std","equivalent_time_mean",
              "equivalent_time_std","peak_activity_mean","peak_activity_std"]
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for cls in sorted(class_summary):
        row = {"event_class": cls}
        row.update(class_summary[cls])
        w.writerow(row)

# ------------------------------------------------------------
# Empirical aligned memory envelope
# ------------------------------------------------------------
kernel_t = np.arange(0, 5.0, 0.16)
curves = []
for c in cases:
    t0 = c["times"][c["peak_idx"]]
    y = np.interp(t0+kernel_t, c["times"], c["activity"], left=np.nan, right=np.nan)
    curves.append(y/max(c["peak"], 1e-14))
curves = np.asarray(curves)
kernel_mean = np.nanmean(curves, axis=0)
kernel_std = np.nanstd(curves, axis=0)

def exp_model(t, A, tau):
    return A*np.exp(-t/tau)

popt, _ = curve_fit(exp_model, kernel_t, kernel_mean, p0=[1,4],
                    bounds=([0,0.01],[2,50]), maxfev=10000)
kernel_fit = exp_model(kernel_t, *popt)
sst = np.sum((kernel_mean-kernel_mean.mean())**2)
r2 = float(1 - np.sum((kernel_mean-kernel_fit)**2)/sst)
eq_times = np.array([r["equivalent_time"] for r in records])
eq_mean = float(eq_times.mean())
eq_std = float(eq_times.std(ddof=1))
eq_cv = float(eq_std/eq_mean)

omega = np.linspace(0,8,161)
spectrum = np.array([np.trapezoid(kernel_mean*np.exp(1j*w*kernel_t), kernel_t) for w in omega])

with open(RESULTS/"empirical_kernel.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["time","mean_normalized_activity","std_normalized_activity","single_exponential_fit"])
    for i,t in enumerate(kernel_t):
        w.writerow([t,kernel_mean[i],kernel_std[i],kernel_fit[i]])

with open(RESULTS/"empirical_kernel_spectrum.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["omega","real","imag","magnitude"])
    for i,x in enumerate(omega):
        w.writerow([x,spectrum[i].real,spectrum[i].imag,abs(spectrum[i])])

# ------------------------------------------------------------
# Resolution validation
# ------------------------------------------------------------
representatives = [
    (0.35,0.0,0.0),
    (0.35,2*np.pi/3,0.0),
    (0.55,np.pi/2,0.0),
    (1.15,np.pi/2,0.0),
    (0.35,0.0,0.8),
    (0.75,np.pi/2,0.8),
    (0.95,np.pi,0.8),
    (0.55,np.pi/3,1.6),
]
validation = []
agree = 0
for i,(v,p,b) in enumerate(representatives,1):
    lo = run_case(v,p,b)
    hi = run_case(v,p,b,n=96,length=40,dt=0.004,T=12,
                  sample_dt=0.16,min_pixels=45)
    ok = lo["class"] == hi["class"]
    agree += int(ok)
    validation.append({
        "validation_id": i, "speed": v, "phase_over_pi": p/np.pi,
        "impact_parameter": b, "coarse_class": lo["class"],
        "fine_class": hi["class"], "coarse_sequence": "-".join(map(str,lo["seq"])),
        "fine_sequence": "-".join(map(str,hi["seq"])), "class_agreement": ok
    })

with open(RESULTS/"high_resolution_validation.csv","w",newline="",encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(validation[0].keys()))
    w.writeheader()
    w.writerows(validation)
agreement = agree/len(validation)

# ------------------------------------------------------------
# High-resolution conservation and time reversal
# ------------------------------------------------------------
dx,X,Y,KX,KY,K2 = grid(96,40)
psi0 = initial_field(X,Y,0.55,np.pi/2,0.0)
psi = psi0.copy()
dt, T = 0.004, 12.0
linear = np.exp(-0.5j*K2*dt)
steps = int(round(T/dt))
series = []
for s in range(steps+1):
    if s % 30 == 0:
        series.append(invariants(psi,X,Y,KX,KY,dx))
    if s < steps:
        psi = step(psi,linear,dt)

inv0 = series[0]
norm_drift = max(abs(z["norm"]-inv0["norm"]) for z in series)/abs(inv0["norm"])
energy_drift = max(abs(z["energy"]-inv0["energy"]) for z in series)/max(abs(inv0["energy"]),1e-14)
momentum_drift = max(np.linalg.norm([z["px"]-inv0["px"],z["py"]-inv0["py"]]) for z in series)

reverse = np.conj(psi)
for _ in range(steps):
    reverse = step(reverse,linear,dt)
reversal_error = np.linalg.norm(reverse-np.conj(psi0))/np.linalg.norm(psi0)

# ------------------------------------------------------------
# Figures
# ------------------------------------------------------------
order = ["persistent_fusion_candidate","fusion_fission_scattering",
         "two_component_scattering","fragmentation","dispersal","unresolved"]
codes = {name:i for i,name in enumerate(order)}

for impact in IMPACTS:
    M = np.zeros((len(SPEEDS),len(PHASES)))
    for i,v in enumerate(SPEEDS):
        for j,p in enumerate(PHASES):
            rec = next(r for r in records if np.isclose(r["impact_parameter"],impact)
                       and np.isclose(r["speed"],v) and np.isclose(r["phase"],p))
            M[i,j] = codes[rec["event_class"]]
    plt.figure()
    im = plt.imshow(M,origin="lower",aspect="auto",
                    extent=[0,1,SPEEDS[0],SPEEDS[-1]],interpolation="nearest")
    cb = plt.colorbar(im)
    cb.set_ticks(range(len(order)))
    cb.set_ticklabels(order)
    plt.xlabel("relative phase / pi")
    plt.ylabel("speed")
    plt.tight_layout()
    plt.savefig(FIGURES/f"scattering_map_b_{impact:.1f}.png",dpi=180)
    plt.close()

plt.figure()
for cls in sorted(metrics):
    plt.hist(metrics[cls]["equivalent_time"],bins=10,alpha=0.5,label=cls)
plt.xlabel("equivalent event time")
plt.ylabel("count")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES/"equivalent_time_distribution.png",dpi=180)
plt.close()

plt.figure()
for cls in sorted(metrics):
    sub = [r for r in records if r["event_class"]==cls]
    plt.scatter([r["speed"] for r in sub],[r["activity_impulse"] for r in sub],label=cls)
plt.xlabel("speed")
plt.ylabel("anisotropic-stress activity impulse")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES/"stress_impulse_vs_speed.png",dpi=180)
plt.close()

plt.figure()
plt.plot(kernel_t,kernel_mean,label="empirical mean envelope")
plt.fill_between(kernel_t,np.maximum(kernel_mean-kernel_std,0),kernel_mean+kernel_std,
                 alpha=0.2,label="one standard deviation")
plt.plot(kernel_t,kernel_fit,linestyle="--",label="single exponential fit")
plt.xlabel("time after stress peak")
plt.ylabel("normalized activity")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES/"empirical_memory_envelope.png",dpi=180)
plt.close()

plt.figure()
plt.plot(omega,spectrum.real,label="real")
plt.plot(omega,spectrum.imag,label="imaginary")
plt.xlabel("angular frequency")
plt.ylabel("event-envelope spectrum")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES/"empirical_kernel_spectrum.png",dpi=180)
plt.close()

# ------------------------------------------------------------
# Frozen gates
# ------------------------------------------------------------
map_pass = bool(len(records)==105 and len(counts)>=4)
robust_pass = bool(agreement >= 0.875)
cons_pass = bool(norm_drift < 1e-10 and energy_drift < 1e-4 and momentum_drift < 1e-4 and reversal_error < 1e-9)
single_pole_pass = bool(r2 >= 0.90 and eq_cv <= 0.30)

results = {
    "model": {
        "equation": "i psi_t = -1/2 Delta psi - g |psi|^2 psi + h |psi|^4 psi",
        "g": G, "h": H6, "amplitude": AMP, "width": WIDTH,
        "separation": SEP, "density_threshold": THRESHOLD
    },
    "T1_unlabeled_scattering_map": {
        "number_of_cases": len(records),
        "speeds": SPEEDS.tolist(),
        "phases_over_pi": (PHASES/np.pi).tolist(),
        "impact_parameters": IMPACTS.tolist(),
        "class_counts": dict(counts),
        "class_summary": class_summary,
        "map_gate_passed": map_pass
    },
    "T2_resolution_robustness": {
        "representative_cases": len(representatives),
        "classification_agreement_fraction": agreement,
        "robustness_gate_passed": robust_pass
    },
    "T3_conservation": {
        "norm_relative_drift": float(norm_drift),
        "energy_relative_drift": float(energy_drift),
        "momentum_absolute_drift": float(momentum_drift),
        "time_reversal_relative_L2_error": float(reversal_error),
        "conservation_gate_passed": cons_pass
    },
    "T4_event_statistics": {
        "equivalent_time_mean": eq_mean,
        "equivalent_time_std": eq_std,
        "equivalent_time_coefficient_of_variation": eq_cv,
        "activity_threshold_fraction": ACTIVITY_FRACTION,
        "kernel_zero_frequency_area": float(np.trapezoid(kernel_mean,kernel_t))
    },
    "T5_single_pole_closure": {
        "fit_amplitude": float(popt[0]),
        "fit_relaxation_time": float(popt[1]),
        "fit_r_squared": r2,
        "required_r_squared": 0.90,
        "required_equivalent_time_cv_max": 0.30,
        "single_pole_gate_passed": single_pole_pass,
        "interpretation": "Failure requires class-conditioned or multi-timescale closure."
    },
    "formal_status": {
        "scattering_map_gate_passed": map_pass,
        "resolution_robustness_gate_passed": robust_pass,
        "conservation_gate_passed": cons_pass,
        "single_pole_closure_gate_passed": single_pole_pass
    }
}

with open(RESULTS/"benchmark_results.json","w",encoding="utf-8") as f:
    json.dump(results,f,ensure_ascii=False,indent=2)

print(json.dumps(results,ensure_ascii=False,indent=2))
