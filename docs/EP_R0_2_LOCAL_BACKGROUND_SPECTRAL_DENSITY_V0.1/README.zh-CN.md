# EP-R0.2：从显式局域背景场导出谱密度

版本：`V0.1`

状态：

\[
\boxed{
[\mathrm{DERIVED\ IN\ THE\ LOCAL\ LINEAR\ FIELD\ MODEL}]
+
[\mathrm{NUMERICAL\ GATE\ PASSED}]
+
[\mathrm{FINITE\text{-}N\ EP\ ORIGIN\ OPEN}]
}
\]

## 本包完成的下一道门

R0.1从给定谱密度 \(J_k(\Omega)\)出发，建立了：

\[
J_k(\Omega)
\rightarrow
K_\eta(k,t)
\rightarrow
\widehat\eta(k,\omega).
\]

R0.2进一步建立：

\[
\boxed{
\text{局域 }S_0-S_{-1}\text{耦合}
+
\text{背景色散关系}
+
\text{有限尺度源形状}
\rightarrow
J_k(\Omega).
}
\]

在三维、无隙、线性色散、非导数局域耦合下，得到：

\[
\boxed{
J_k(\Omega)
=
\gamma\Omega\,
e^{-a^2(k^2+\Omega^2/c_b^2)}
\operatorname{sinhc}
\left(
\frac{2a^2k\Omega}{c_b}
\right)
}
\]

其中：

\[
\gamma
=
\frac{2\sqrt{\pi}\,g^2a^3}{c_b^3},
\qquad
\operatorname{sinhc}(z)=\frac{\sinh z}{z}.
\]

在 \(k=0\)：

\[
J_0(\Omega)
=
\gamma\Omega
e^{-(\Omega/\Omega_c)^2},
\qquad
\Omega_c=\frac{c_b}{a}.
\]

因此低频为Ohmic：

\[
J_0(\Omega)\sim\gamma\Omega.
\]

普通零频粘度由微观参数给出：

\[
\boxed{
\eta_0=\gamma
=
\frac{2\sqrt{\pi}\,g^2a^3}{c_b^3}.
}
\]

## 关键新结论

对 \(d\)维、线性色散和 \(m\)阶导数耦合：

\[
\boxed{
J(\Omega)\sim
\Omega^{d-2+2m}.
}
\]

有限且非零的Newton粘度要求：

\[
d+2m=3.
\]

所以在三维中，当前通道必须具有等效的非导数Ohmic耦合。纯一阶导数耦合给出：

\[
J(\Omega)\sim\Omega^3,
\]

其零频粘度为零。

若背景存在频隙 \(\omega_g>0\)，则：

\[
J(\Omega)=0
\qquad
(\Omega<\omega_g),
\]

该通道也不能产生非零DC粘度。

## 文件

- `docs/EP-R0.2-LOCAL-BACKGROUND-SPECTRAL-DENSITY.zh-CN.md`
- `docs/THEOREMS-AND-PROOFS.zh-CN.md`
- `docs/EP-R0.2-LOCAL-BACKGROUND-SPECTRAL-DENSITY.md`
- `code/run_r0_2_benchmark.py`
- `results/benchmark_results.json`
- `results/inverse_spatial_fit.csv`
- `figures/`
- `PRE_REGISTRATION.json`
- `STATUS.md`

## 运行

```bash
python code/run_r0_2_benchmark.py
```

建议Git提交说明：

```text
theory: derive EP-R0.2 local-background spectral density
```
