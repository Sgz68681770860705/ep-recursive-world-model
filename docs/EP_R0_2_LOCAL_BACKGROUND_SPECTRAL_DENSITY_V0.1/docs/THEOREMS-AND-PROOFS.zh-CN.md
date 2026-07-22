# EP-R0.2：定理与证明

## T1：局域场产生的谱密度

### 命题

设：

\[
\Omega_{\mathbf q}=c_bq,
\]

\[
c_k(\mathbf q)
=
g\widetilde w_a(\mathbf q-\mathbf k),
\]

\[
|\widetilde w_a(\mathbf p)|^2
=
\left(
\frac{a^2}{\pi}
\right)^{3/2}
e^{-a^2p^2}.
\]

则：

\[
J_k(\Omega)
=
\frac{\pi}{2}
\int d^3q
\frac{|c_k(\mathbf q)|^2}{c_bq}
\delta(\Omega-c_bq)
\]

等于：

\[
J_k(\Omega)
=
\gamma\Omega
e^{-a^2(k^2+\Omega^2/c_b^2)}
\operatorname{sinhc}
\left(
\frac{2a^2k\Omega}{c_b}
\right),
\]

其中：

\[
\gamma
=
\frac{2\sqrt{\pi}g^2a^3}{c_b^3}.
\]

### 证明

取球坐标，令 \(\mu=\cos\theta\)：

\[
|\mathbf q-\mathbf k|^2
=
q^2+k^2-2qk\mu.
\]

径向积分：

\[
\int_0^\infty
q^2dq\,
\frac1{c_bq}
\delta(\Omega-c_bq)
=
\frac{\Omega}{c_b^3}.
\]

角积分：

\[
\int d\Omega_{\mathbf q}
e^{-a^2(q^2+k^2-2qk\mu)}
=
4\pi
e^{-a^2(q^2+k^2)}
\frac{\sinh(2a^2qk)}
{2a^2qk}.
\]

代入 \(q=\Omega/c_b\)，整理归一化常数即得。证毕。

---

## T2：Ohmic指数定理

### 命题

在 \(d\)维中，若：

\[
\Omega_q=c_bq,
\qquad
c(q)\sim q^m
\quad(q\to0),
\]

则：

\[
J(\Omega)
\sim
\Omega^{d-2+2m}.
\]

### 证明

谱密度的低频幂次来自：

\[
d^dq
\sim
q^{d-1}dq,
\]

\[
|c(q)|^2
\sim
q^{2m},
\]

\[
\Omega_q^{-1}
\sim
q^{-1},
\]

以及：

\[
\delta(\Omega-c_bq)dq
\sim
c_b^{-1}.
\]

乘积的波数幂次为：

\[
q^{d-1+2m-1}
=
q^{d-2+2m}.
\]

由于 \(q=\Omega/c_b\)，结论成立。证毕。

### 推论

有限且非零的：

\[
\lim_{\Omega\to0}
\frac{J(\Omega)}{\Omega}
\]

要求：

\[
d-2+2m=1,
\]

即：

\[
d+2m=3.
\]

---

## T3：高斯记忆核

### 命题

若：

\[
J_0(\Omega)
=
\gamma\Omega
e^{-(\Omega/\Omega_c)^2},
\]

则：

\[
K_\eta(0,t)
=
\frac{\gamma\Omega_c}{\sqrt{\pi}}
e^{-\Omega_c^2t^2/4}.
\]

### 证明

由定义：

\[
K_\eta(0,t)
=
\frac{2\gamma}{\pi}
\int_0^\infty
e^{-(\Omega/\Omega_c)^2}
\cos(\Omega t)d\Omega.
\]

使用高斯余弦变换：

\[
\int_0^\infty
e^{-(\Omega/\Omega_c)^2}
\cos(\Omega t)d\Omega
=
\frac{\sqrt{\pi}\Omega_c}{2}
e^{-\Omega_c^2t^2/4}.
\]

代入即得。证毕。

---

## T4：空间尺度可辨认性

### 命题

若精确知道：

\[
\eta(k,0)=\gamma e^{-a^2k^2}
\]

在包含 \(k=0\)和任意 \(k\ne0\)的区间上的值，则 \(\gamma\)和 \(a\)唯一。

### 证明

首先：

\[
\gamma=\eta(0,0).
\]

其次：

\[
a^2
=
-\frac{1}{k^2}
\log
\left(
\frac{\eta(k,0)}{\eta(0,0)}
\right).
\]

因此 \(\gamma\)和非负 \(a\)唯一。若 \(c_b\)已知，则：

\[
g
=
\left(
\frac{\gamma c_b^3}
{2\sqrt{\pi}a^3}
\right)^{1/2}
\]

也唯一。证毕。

---

## T5：有隙背景不能产生DC粘度

### 命题

若：

\[
\Omega_q
=
\sqrt{\omega_g^2+c_b^2q^2},
\qquad
\omega_g>0,
\]

则该通道满足：

\[
J(\Omega)=0
\quad
(\Omega<\omega_g),
\]

从而：

\[
\lim_{\Omega\to0}
\frac{J(\Omega)}{\Omega}=0.
\]

### 证明

对任意实 \(q\)：

\[
\Omega_q\ge\omega_g.
\]

当 \(\Omega<\omega_g\)时：

\[
\delta(\Omega-\Omega_q)=0.
\]

因此谱密度在零频附近恒为零。证毕。
