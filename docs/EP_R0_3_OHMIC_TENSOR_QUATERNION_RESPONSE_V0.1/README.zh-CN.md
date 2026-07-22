# EP-R0.3：对称相容的Ohmic通道、张量响应与四元数旋转

版本：`V0.1`

状态：

\[
\boxed{
[\mathrm{DERIVED\ IN\ THE\ LINEAR\ INTERNAL\text{-}FIELD\ MODEL}]
+
[\mathrm{NUMERICAL\ —\ ALL\ PREREGISTERED\ GATES\ PASSED}]
+
[\mathrm{NONLINEAR\ FINITE\text{-}BOUNDARY\ ORIGIN\ OPEN}]
}
\]

## 本阶段解决的问题

R0.2表明：三维普通粘度需要等效的无隙Ohmic通道，但若背景变量被解释为具有整体平移移位对称性的空间位移场，非导数耦合可能不自然。

R0.3给出的修正是：

\[
\boxed{
\text{Ohmic通道不耦合绝对空间位移，}
\quad
\text{而耦合 }S_0\text{内部形态、体积和旋转变量。}
}
\]

这些内部变量在空间平移下不变，在旋转下按标量、张量或轴矢量协变，所以非导数局域耦合不破坏Euclidean对称性。

## 三个最小通道

\[
Q_{ij}^{\rm dev}
\longleftrightarrow
B_{ij}^{\rm dev}
\qquad
\text{剪切/形态通道},
\]

\[
\vartheta
\longleftrightarrow
\phi_L
\qquad
\text{体积通道},
\]

\[
\boldsymbol\theta
\longleftrightarrow
\mathbf R
\qquad
\text{四元数小角度/旋转通道}.
\]

每个三维无隙通道均得到：

\[
J_A(k,\Omega)
=
\gamma_A\Omega
e^{-a_A^2(k^2+\Omega^2/c_A^2)}
\operatorname{sinhc}
\left(
\frac{2a_A^2k\Omega}{c_A}
\right),
\]

\[
\gamma_A
=
\frac{2\sqrt{\pi}g_A^2a_A^3}{c_A^3}.
\]

## 张量本构

\[
\widehat{\mathbb\eta}
=
\widehat\eta_T\mathbb P^{\rm dev}
+
\widehat\zeta_L\mathbb P^{\rm vol}
+
\widehat\eta_R\mathbb P^{\rm anti}
+
\widehat\eta_Q\,A(q)\otimes A(q).
\]

其中：

\[
A(q)
=
\mathbf n(q)\mathbf n(q)^T-\frac13I.
\]

普通各向同性流体极限为：

\[
\eta_Q\to0,
\qquad
\eta_R\to0,
\]

只保留剪切和体积通道。

## 关键结果

- 内部张量和轴矢量场允许对称相容的非导数Ohmic耦合；
- 旋转背景与 \(S_0\)自旋之间的相对耦合严格守恒总角动量；
- 四元数运输保持 \(|q|=1\)；
- 有取向的不规则 \(S_0\)可在线性响应中产生法向应力差；
- 各向同性取向平均使该线性法向应力差消失；
- 旋转响应增加独立的记忆尺度和低频旋转阻尼；
- 从 \(k\)和 \(\omega\)响应可以同时反演 \(g_R,a_R,c_R\)。

## 文件

- `docs/EP-R0.3-OHMIC-TENSOR-QUATERNION-RESPONSE.zh-CN.md`
- `docs/THEOREMS-AND-PROOFS.zh-CN.md`
- `docs/EP-R0.3-OHMIC-TENSOR-QUATERNION-RESPONSE.md`
- `code/run_r0_3_benchmark.py`
- `results/benchmark_results.json`
- `PRE_REGISTRATION.json`
- `STATUS.md`

## 运行

```bash
python code/run_r0_3_benchmark.py
```

建议Git提交说明：

```text
theory: add EP-R0.3 Ohmic tensor and quaternion response
```
