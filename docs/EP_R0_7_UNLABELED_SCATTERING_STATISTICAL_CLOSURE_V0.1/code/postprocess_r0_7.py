from pathlib import Path
import csv, json
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import label as cc_label
from scipy.optimize import curve_fit

ROOT=Path('/mnt/data/EP_R0_7_UNLABELED_SCATTERING_STATISTICAL_CLOSURE_V0.1')
RES=ROOT/'results'; FIG=ROOT/'figures'; FIG.mkdir(exist_ok=True)
G,H6=2.0,1.0; AMP,WIDTH,SEP=1.4,2.2,12.0; THR=.2
SPEEDS=np.array([.35,.55,.75,.95,1.15]); PHASES=np.array([0,np.pi/6,np.pi/3,np.pi/2,2*np.pi/3,5*np.pi/6,np.pi]); IMPACTS=np.array([0,.8,1.6])

def grid(n,L):
    x=np.linspace(-L/2,L/2,n,endpoint=False); dx=L/n
    X,Y=np.meshgrid(x,x,indexing='xy'); k=2*np.pi*np.fft.fftfreq(n,d=dx); KX,KY=np.meshgrid(k,k,indexing='xy')
    return dx,X,Y,KX,KY,KX*KX+KY*KY

def initial(X,Y,v,p,b):
    r1=(X+SEP/2)**2+(Y+b/2)**2; r2=(X-SEP/2)**2+(Y-b/2)**2
    return AMP*np.exp(-r1/WIDTH**2)*np.exp(1j*v*X)+AMP*np.exp(-r2/WIDTH**2)*np.exp(-1j*v*X+1j*p)

def step(psi,lin,dt):
    rho=np.abs(psi)**2; psi*=np.exp(1j*(G*rho-H6*rho*rho)*dt/2)
    psi=np.fft.ifft2(np.fft.fft2(psi)*lin)
    rho=np.abs(psi)**2; psi*=np.exp(1j*(G*rho-H6*rho*rho)*dt/2)
    return psi

def count_components(psi,minpix):
    lab,n=cc_label(np.abs(psi)**2>=THR,structure=np.array([[0,1,0],[1,1,1],[0,1,0]]))
    return sum(int((lab==i).sum())>=minpix for i in range(1,n+1))

def compact(seq):
    out=[]
    for x in seq:
        if not out or out[-1]!=x: out.append(int(x))
    return out

def classify(seq):
    final=seq[-1]; mn=min(seq)
    if final>=3:return 'fragmentation'
    if final==1:return 'persistent_fusion_candidate'
    if mn==1 and final==2:return 'fusion_fission_scattering'
    if mn==2 and final==2:return 'two_component_scattering'
    if final==0:return 'dispersal'
    return 'unresolved'

def classify_run(v,p,b,n=88,L=40,dt=.005,T=12,sample_dt=.16):
    dx,X,Y,KX,KY,K2=grid(n,L); psi=initial(X,Y,v,p,b); lin=np.exp(-.5j*K2*dt)
    steps=round(T/dt); stride=max(1,round(sample_dt/dt)); minpix=round(20*(n/64)**2)
    counts=[]
    for s in range(steps+1):
        if s%stride==0 or s==steps: counts.append(count_components(psi,minpix))
        if s<steps: psi=step(psi,lin,dt)
    seq=compact(counts); return classify(seq),seq

def derivs(psi,KX,KY):
    F=np.fft.fft2(psi); return np.fft.ifft2(1j*KX*F),np.fft.ifft2(1j*KY*F)

def inv(psi,X,Y,KX,KY,dx):
    rho=np.abs(psi)**2; px,py=derivs(psi,KX,KY)
    H=np.sum(.5*(np.abs(px)**2+np.abs(py)**2)-.5*G*rho**2+H6*rho**3/3)*dx*dx
    jx=np.imag(np.conj(psi)*px); jy=np.imag(np.conj(psi)*py)
    return np.array([np.sum(rho)*dx*dx,np.real(H),np.sum(jx)*dx*dx,np.sum(jy)*dx*dx],float)

rows=list(csv.DictReader(open(RES/'event_scan.csv',encoding='utf-8')))
counts=Counter(r['event_class'] for r in rows)
# validation uses scan row as coarse truth
reps=[(.35,0,0),(.35,2*np.pi/3,0),(.55,np.pi/2,0),(1.15,np.pi/2,0),(.35,0,.8),(.75,np.pi/2,.8),(.95,np.pi,.8),(.55,np.pi/3,1.6)]
val=[]; agree=0
for i,(v,p,b) in enumerate(reps,1):
    coarse=next(r for r in rows if abs(float(r['speed'])-v)<1e-9 and abs(float(r['phase'])-p)<1e-9 and abs(float(r['impact_parameter'])-b)<1e-9)
    fine,fseq=classify_run(v,p,b)
    ok=coarse['event_class']==fine; agree+=ok
    val.append({'validation_id':i,'speed':v,'phase_over_pi':p/np.pi,'impact_parameter':b,'coarse_class':coarse['event_class'],'fine_class':fine,'coarse_sequence':coarse['topology_sequence'],'fine_sequence':'-'.join(map(str,fseq)),'class_agreement':bool(ok)})
with open(RES/'high_resolution_validation.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=val[0].keys()); w.writeheader(); w.writerows(val)
agreement=agree/len(val)

# conservation at medium-high resolution
n=88;L=40;dt=.005;T=10;dx,X,Y,KX,KY,K2=grid(n,L);psi0=initial(X,Y,.55,np.pi/2,0);psi=psi0.copy();lin=np.exp(-.5j*K2*dt);steps=round(T/dt)
series=[]
for s in range(steps+1):
    if s%25==0: series.append(inv(psi,X,Y,KX,KY,dx))
    if s<steps: psi=step(psi,lin,dt)
series=np.array(series); base=series[0]
norm_drift=np.max(np.abs(series[:,0]-base[0]))/abs(base[0]); energy_drift=np.max(np.abs(series[:,1]-base[1]))/max(abs(base[1]),1e-14); mom_drift=np.max(np.linalg.norm(series[:,2:4]-base[2:4],axis=1))
reverse=np.conj(psi)
for _ in range(steps): reverse=step(reverse,lin,dt)
rev=np.linalg.norm(reverse-np.conj(psi0))/np.linalg.norm(psi0)

# kernel and fit
krows=list(csv.DictReader(open(RES/'empirical_kernel.csv',encoding='utf-8')))
kt=np.array([float(r['time']) for r in krows]); km=np.array([float(r['mean_normalized_activity']) for r in krows]); ks=np.array([float(r['std_normalized_activity']) for r in krows])
def expm(t,A,tau):return A*np.exp(-t/tau)
popt,_=curve_fit(expm,kt,km,p0=[1,4],bounds=([0,.01],[2,50]),maxfev=10000); kfit=expm(kt,*popt); r2=1-np.sum((km-kfit)**2)/np.sum((km-km.mean())**2)
eq=np.array([float(r['equivalent_time']) for r in rows]); eqmean=eq.mean(); eqstd=eq.std(ddof=1); eqcv=eqstd/eqmean

# class summary load
class_rows=list(csv.DictReader(open(RES/'class_summary.csv',encoding='utf-8')))
class_summary={r['event_class']:{k:(int(v) if k=='count' else float(v)) for k,v in r.items() if k!='event_class'} for r in class_rows}

# figures
order=['persistent_fusion_candidate','fusion_fission_scattering','two_component_scattering','fragmentation','dispersal','unresolved']; codes={x:i for i,x in enumerate(order)}
for b in IMPACTS:
    M=np.zeros((len(SPEEDS),len(PHASES)))
    for i,v in enumerate(SPEEDS):
        for j,p in enumerate(PHASES):
            r=next(r for r in rows if abs(float(r['impact_parameter'])-b)<1e-9 and abs(float(r['speed'])-v)<1e-9 and abs(float(r['phase'])-p)<1e-9)
            M[i,j]=codes[r['event_class']]
    plt.figure(); im=plt.imshow(M,origin='lower',aspect='auto',extent=[0,1,SPEEDS[0],SPEEDS[-1]],interpolation='nearest'); cb=plt.colorbar(im);cb.set_ticks(range(len(order)));cb.set_ticklabels(order);plt.xlabel('relative phase / pi');plt.ylabel('speed');plt.tight_layout();plt.savefig(FIG/f'scattering_map_b_{b:.1f}.png',dpi=180);plt.close()
plt.figure()
for cls in sorted(counts): plt.hist([float(r['equivalent_time']) for r in rows if r['event_class']==cls],bins=10,alpha=.5,label=cls)
plt.xlabel('equivalent event time');plt.ylabel('count');plt.legend();plt.tight_layout();plt.savefig(FIG/'equivalent_time_distribution.png',dpi=180);plt.close()
plt.figure()
for cls in sorted(counts):
    s=[r for r in rows if r['event_class']==cls];plt.scatter([float(r['speed']) for r in s],[float(r['activity_impulse']) for r in s],label=cls)
plt.xlabel('speed');plt.ylabel('anisotropic-stress activity impulse');plt.legend();plt.tight_layout();plt.savefig(FIG/'stress_impulse_vs_speed.png',dpi=180);plt.close()
plt.figure();plt.plot(kt,km,label='empirical mean envelope');plt.fill_between(kt,np.maximum(km-ks,0),km+ks,alpha=.2,label='one standard deviation');plt.plot(kt,kfit,linestyle='--',label='single exponential fit');plt.xlabel('time after stress peak');plt.ylabel('normalized activity');plt.legend();plt.tight_layout();plt.savefig(FIG/'empirical_memory_envelope.png',dpi=180);plt.close()
sp=list(csv.DictReader(open(RES/'empirical_kernel_spectrum.csv',encoding='utf-8')));om=np.array([float(r['omega']) for r in sp]);re=np.array([float(r['real']) for r in sp]);im=np.array([float(r['imag']) for r in sp]);plt.figure();plt.plot(om,re,label='real');plt.plot(om,im,label='imaginary');plt.xlabel('angular frequency');plt.ylabel('event-envelope spectrum');plt.legend();plt.tight_layout();plt.savefig(FIG/'empirical_kernel_spectrum.png',dpi=180);plt.close()

map_pass=bool(len(rows)==105 and len(counts)>=4); robust=bool(agreement>=.875); cons=bool(norm_drift<1e-10 and energy_drift<1e-4 and mom_drift<1e-4 and rev<1e-9); single=bool(r2>=.90 and eqcv<=.30)
result={'model':{'equation':'i psi_t = -1/2 Delta psi - g |psi|^2 psi + h |psi|^4 psi','g':G,'h':H6,'density_threshold':THR},'T1_unlabeled_scattering_map':{'number_of_cases':len(rows),'speeds':SPEEDS.tolist(),'phases_over_pi':(PHASES/np.pi).tolist(),'impact_parameters':IMPACTS.tolist(),'class_counts':dict(counts),'class_summary':class_summary,'map_gate_passed':map_pass},'T2_resolution_robustness':{'representative_cases':len(reps),'classification_agreement_fraction':agreement,'robustness_gate_passed':robust},'T3_conservation':{'norm_relative_drift':float(norm_drift),'energy_relative_drift':float(energy_drift),'momentum_absolute_drift':float(mom_drift),'time_reversal_relative_L2_error':float(rev),'conservation_gate_passed':cons},'T4_event_statistics':{'equivalent_time_mean':float(eqmean),'equivalent_time_std':float(eqstd),'equivalent_time_coefficient_of_variation':float(eqcv),'activity_threshold_fraction':.10,'kernel_zero_frequency_area':float(np.trapezoid(km,kt))},'T5_single_pole_closure':{'fit_amplitude':float(popt[0]),'fit_relaxation_time':float(popt[1]),'fit_r_squared':float(r2),'required_r_squared':.90,'required_equivalent_time_cv_max':.30,'single_pole_gate_passed':single,'interpretation':'Failure requires class-conditioned or multi-timescale closure.'},'formal_status':{'scattering_map_gate_passed':map_pass,'resolution_robustness_gate_passed':robust,'conservation_gate_passed':cons,'single_pole_closure_gate_passed':single}}
json.dump(result,open(RES/'benchmark_results.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False,indent=2))
