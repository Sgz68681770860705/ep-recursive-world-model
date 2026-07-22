# EP-R0.1：T1—T4定理与证明

## T1：可逆性与能量守恒

### 命题

对Hamilton量：

\[
H_k
=
\frac{P_k^2}{2M_k}
+
\frac{K_k}{2}X_k^2
+
\frac12
\int_0^\infty
\left[
p_{k,\Omega}^2+
\Omega^2
\left(
x_{k,\Omega}
-
\frac{c_k(\Omega)}{\Omega^2}X_k
\right)^2
\right]d\Omega,
\]

若：

\[
M_k>0,\qquad K_k>0,
\]

且积分有限，则：

1. \(H_k\ge0\)；
2. Hamilton演化保持 \(H_k\)；
3. 变换
   \[
   (t,P_k,p_{k,\Omega})
   \mapsto
   (-t,-P_k,-p_{k,\Omega})
   \]
   保持方程不变。

### 证明

Hamilton量是平方项之和，因此有下界。Hamilton方程给出：

\[
\frac{dH_k}{dt}
=
\{H_k,H_k\}=0.
\]

Hamilton量只含动量平方，不含奇次动量项，因此时间反演后Hamilton方程保持不变。证毕。

---

## T2：背景消去产生因果记忆

### 命题

对条件平衡初始化的背景，消去 \(x_{k,\Omega}\) 后，\(X_k\)满足：

\[
M_k\ddot X_k
+
K_kX_k
+
\int_0^t
K_\eta(k,t-s)\dot X_k(s)\,ds
=
F_{\rm init}(k,t),
\]

其中：

\[
K_\eta(k,t)
=
\frac{2}{\pi}
\int_0^\infty
\frac{J_k(\Omega)}{\Omega}
\cos\Omega t\,d\Omega.
\]

### 证明

背景方程：

\[
\ddot x_\Omega+\Omega^2x_\Omega=c(\Omega)X.
\]

延迟解：

\[
x_\Omega(t)
=
x_\Omega^{h}(t)
+
\frac{c(\Omega)}{\Omega}
\int_0^t
\sin[\Omega(t-s)]X(s)\,ds.
\]

对积分分部：

\[
\frac{1}{\Omega}
\int_0^t
\sin[\Omega(t-s)]X(s)\,ds
=
\frac{X(t)}{\Omega^2}
-
\frac{X(0)\cos\Omega t}{\Omega^2}
-
\frac1{\Omega^2}
\int_0^t
\cos[\Omega(t-s)]\dot X(s)\,ds.
\]

代回 \(X\)方程后，瞬时反作用项与Hamilton量中的配平方项抵消，剩余卷积核和背景初态项。积分上限为 \(t\)，因此响应因果。证毕。

---

## T3：一极点广义粘性

### 命题

若：

\[
J_k(\Omega)
=
\frac{\Delta\eta}{\tau}
\frac{\Omega\lambda_k}
{\Omega^2+\lambda_k^2},
\qquad
\lambda_k=\frac{1+\xi^2k^2}{\tau},
\]

则：

\[
K_\eta(k,t)
=
\frac{\Delta\eta}{\tau}
e^{-\lambda_kt}H(t),
\]

并且：

\[
\widehat\eta(k,\omega)
=
\eta_\infty+
\frac{\Delta\eta}
{1+\xi^2k^2-i\omega\tau}.
\]

### 证明

利用积分恒等式：

\[
\int_0^\infty
\frac{\cos\Omega t}
{\Omega^2+\lambda^2}
d\Omega
=
\frac{\pi}{2\lambda}
e^{-\lambda t},
\qquad t\ge0.
\]

代入核定义即可得到指数核。再计算：

\[
\int_0^\infty
\frac{\Delta\eta}{\tau}
e^{-(1+\xi^2k^2)t/\tau}
e^{i\omega t}\,dt
=
\frac{\Delta\eta}
{1+\xi^2k^2-i\omega\tau}.
\]

证毕。

### 推论：被动性

若：

\[
\eta_\infty,\Delta\eta\ge0,
\]

则：

\[
\operatorname{Re}\widehat\eta(k,\omega)\ge0.
\]

因此对周期剪切，平均功率不为负。

---

## T4：单极点参数可辨认性

### 命题

在参数域：

\[
\eta_\infty\ge0,\quad
\Delta\eta>0,\quad
\tau>0,\quad
\xi\ge0
\]

中，若精确知道：

\[
\widehat\eta(k,\omega)
=
\eta_\infty+
\frac{\Delta\eta}
{1+\xi^2k^2-i\omega\tau}
\]

在包含 \(k=0\)、\(\omega=0\)且有频率变化和至少一个 \(k\ne0\)的开集上的值，则四个参数唯一。

### 证明

高频极限给出：

\[
\eta_\infty
=
\lim_{|\omega|\to\infty}
\widehat\eta(k,\omega).
\]

零频零波数给出：

\[
\Delta\eta
=
\widehat\eta(0,0)-\eta_\infty.
\]

\(k=0\)时的唯一极点位于：

\[
\omega=-i/\tau,
\]

因此 \(\tau\)唯一。

最后由任意 \(k\ne0\)的零频数据：

\[
\widehat\eta(k,0)-\eta_\infty
=
\frac{\Delta\eta}{1+\xi^2k^2}
\]

唯一得到 \(\xi^2\)。证毕。

### 限制

该唯一性只在单极点模型类别内成立。多模、连续谱或不同微观模型可能在有限数据窗口中近似不可区分。
