# EP-R0.1：可逆背景响应与广义粘性基础

版本：`V0.1`

## 0. 科学状态

本文只冻结一个最小数学桥：

\[
S_0+S_{-1}\text{可逆动力学}
\rightarrow
S_{-1}\text{响应记忆}
\rightarrow
\widehat\eta(k,\omega).
\]

状态标签：

- `[DEFINITION]`：本文采用的数学定义；
- `[POSTULATE R0.1]`：最小模型输入；
- `[DERIVED R0.1]`：在该输入下推出；
- `[NUMERICAL R0.1]`：由随包代码验证；
- `[OPEN]`：尚未从有限 \(N\) EP碰撞推出。

本文不声称：

- 已经解释现实粘性；
- 已经推导Navier–Stokes；
- 已经证明 \(S_0\)或 \(S_{-1}\)对应现实基本粒子；
- 已经解释引力、光或量子现象。

---

# 1. 当前目标

我们需要证明的第一条链是：

\[
\boxed{
\text{完整系统可逆}
\Longrightarrow
\text{约化系统存在因果记忆}
\Longrightarrow
\text{低频长波极限存在有限粘度}
}
\]

然后建立最小逆向链：

\[
\boxed{
\widehat\eta(k,\omega)
\Longrightarrow
(\tau,\xi,\Delta\eta)
}
\]

这里反演的是限定模型类别中的慢自由度参数，不是恢复全部微观轨迹。

---

# 2. 最小对象

## 2.1 \(S_0\)广义构型

R0.1暂时不加入四元数、自旋和复杂相场，只保留广义构型：

\[
\mathcal Q(t)
=
(Q_1,\ldots,Q_m).
\]

它可以代表：

- 两个 \(S_0\)之间的相对位移；
- 某个剪切Fourier模的幅度；
- 某个边界低阶形变坐标。

其共轭动量为：

\[
\mathcal P=M_0\dot{\mathcal Q}.
\]

## 2.2 \(S_{-1}\)背景

背景由连续谱谐振模组成：

\[
x_{k,\Omega}(t),
\qquad
p_{k,\Omega}(t),
\qquad
\Omega>0.
\]

其中：

- \(k\)：空间波数；
- \(\Omega\)：背景内部频率；
- 不同极化方向可通过附加张量指标扩展。

R0.1只保留一个剪切通道。

---

# 3. 一般场—结构作用量

为了保证背景不是被动容器，先定义一个一般的连续场模型。

设：

\[
\Phi(\mathbf x,t)
\]

为 \(S_{-1}\)背景场，\(C[\mathcal Q](\mathbf x)\)为 \(S_0\)在背景中规定的平滑目标构型。取：

\[
\boxed{
\mathcal S
=
\int dt\,
\left[
T_0(\dot{\mathcal Q})
-
V_{\rm core}(\mathcal Q)
+
\frac12
\langle
\dot\Phi,M_b\dot\Phi
\rangle
-
\frac12
\langle
\Phi,A_b\Phi
\rangle
-
\frac{\lambda}{2}
\|\Phi-C[\mathcal Q]\|^2
\right].
}
\]

要求：

\[
M_b>0,
\qquad
A_b\ge0,
\qquad
\lambda>0.
\]

背景方程为：

\[
\boxed{
M_b\ddot\Phi
+
(A_b+\lambda I)\Phi
=
\lambda C[\mathcal Q].
}
\]

\(S_0\)方程为：

\[
\boxed{
M_0\ddot{\mathcal Q}
+
\nabla_{\mathcal Q}V_{\rm core}
=
\lambda
\left\langle
\Phi-C[\mathcal Q],
\frac{\partial C}{\partial\mathcal Q}
\right\rangle.
}
\]

这构成：

\[
S_0\rightarrow S_{-1}\rightarrow S_0
\]

的双向闭环。

---

# 4. 守恒账本

总能量为：

\[
\boxed{
E_{\rm tot}
=
T_0
+
V_{\rm core}
+
\frac12
\langle
\dot\Phi,M_b\dot\Phi
\rangle
+
\frac12
\langle
\Phi,A_b\Phi
\rangle
+
\frac{\lambda}{2}
\|\Phi-C[\mathcal Q]\|^2.
}
\]

因为每一项均非负或有下界，所以：

\[
E_{\rm tot}\ge E_{\min}.
\]

当作用量不显含时间时：

\[
\frac{dE_{\rm tot}}{dt}=0.
\]

时间反演定义为：

\[
t\mapsto-t,
\qquad
\dot{\mathcal Q}\mapsto-\dot{\mathcal Q},
\qquad
\dot\Phi\mapsto-\dot\Phi.
\]

位置和构型不变。

若 \(C[\mathcal Q]\)、\(A_b\)和 \(V_{\rm core}\)在平移和旋转下协变，则由Noether定理得到总线动量和总角动量守恒。

此处的总角动量包括：

\[
\mathbf J_{\rm total}
=
\mathbf L_{S_0}
+
\mathbf J_{S_{-1}}.
\]

四元数内部自旋将在R0.4以后加入。

---

# 5. 剪切单模的精确Hamilton约化

为了获得可解的记忆核，对每个波数 \(k\)取一个 \(S_0\)剪切坐标 \(X_k\)，背景为连续振子浴：

\[
\boxed{
H_k
=
\frac{P_k^2}{2M_k}
+
\frac{K_k}{2}X_k^2
+
\frac12
\int_0^\infty d\Omega
\left[
p_{k,\Omega}^2
+
\Omega^2
\left(
x_{k,\Omega}
-
\frac{c_k(\Omega)}{\Omega^2}X_k
\right)^2
\right].
}
\]

这是一个严格非负的Hamilton量。

其中：

- \(X_k\)：宏观剪切构型；
- \(\dot X_k\)：剪切速率；
- \(x_{k,\Omega}\)：被消去的 \(S_{-1}\)背景模式；
- \(c_k(\Omega)\)：耦合谱。

该模型没有基本阻力项。

---

# 6. 消去 \(S_{-1}\)背景

背景振子方程：

\[
\ddot x_{k,\Omega}
+
\Omega^2x_{k,\Omega}
=
c_k(\Omega)X_k.
\]

采用延迟解并代回 \(X_k\)方程，经过一次分部积分，得到：

\[
\boxed{
M_k\ddot X_k(t)
+
K_kX_k(t)
+
\int_0^t
K_\eta(k,t-s)\dot X_k(s)\,ds
=
F_{\rm init}(k,t).
}
\]

其中：

\[
\boxed{
K_\eta(k,t)
=
\frac{2}{\pi}
\int_0^\infty
\frac{J_k(\Omega)}{\Omega}
\cos(\Omega t)\,d\Omega.
}
\]

谱密度定义为：

\[
J_k(\Omega)
=
\frac{\pi}{2}
\frac{c_k(\Omega)^2}{\Omega}.
\]

\(F_{\rm init}\)由背景初态决定。若背景以给定 \(X_k(0)\)的条件平衡态初始化，初始滑移项被消除。

因此：

\[
\boxed{
\text{可逆总系统}
\Longrightarrow
\text{约化系统中的因果历史项}.
}
\]

“耗散”来自背景连续谱中的相位混合；有限振子近似在足够长时间仍可能出现Poincaré回归。

---

# 7. EP广义粘性定义

## 7.1 定义

> **[DEFINITION–EP GENERALIZED VISCOSITY]**  
> EP广义粘性是 \(S_0\)广义剪切速率对 \(S_{-1}\)背景产生扰动后，背景剪切应力的因果记忆核在频率—波数空间中的响应函数。

时域：

\[
\boxed{
\sigma^{\rm dev}(k,t)
=
2\eta_\infty D^{\rm dev}(k,t)
+
2\int_0^\infty
K_\eta(k,s)
D^{\rm dev}(k,t-s)\,ds.
}
\]

频域约定：

\[
\widehat f(\omega)
=
\int_{-\infty}^{\infty}
f(t)e^{i\omega t}\,dt.
\]

于是：

\[
\boxed{
\widehat\sigma^{\rm dev}(k,\omega)
=
2\widehat\eta(k,\omega)
\widehat D^{\rm dev}(k,\omega),
}
\]

\[
\boxed{
\widehat\eta(k,\omega)
=
\eta_\infty
+
\int_0^\infty
K_\eta(k,t)e^{i\omega t}\,dt.
}
\]

## 7.2 普通粘度

若积分存在，则：

\[
\boxed{
\eta_0
=
\widehat\eta(0,0)
=
\eta_\infty
+
\int_0^\infty K_\eta(0,t)\,dt.
}
\]

因此传统粘度是：

\[
\boxed{
\text{EP响应谱的长波、零频极限}.
}
\]

---

# 8. 单慢模可解模型

定义：

\[
\lambda_k
=
\frac{1+\xi^2k^2}{\tau}.
\]

选择谱密度：

\[
\boxed{
J_k(\Omega)
=
\frac{\Delta\eta}{\tau}
\frac{\Omega\lambda_k}
{\Omega^2+\lambda_k^2}.
}
\]

则：

\[
\boxed{
K_\eta(k,t)
=
\frac{\Delta\eta}{\tau}
\exp
\left[
-\frac{1+\xi^2k^2}{\tau}t
\right]
H(t).
}
\]

Fourier变换得到：

\[
\boxed{
\widehat\eta(k,\omega)
=
\eta_\infty
+
\frac{\Delta\eta}
{1+\xi^2k^2-i\omega\tau}.
}
\]

参数解释：

\[
\eta_\infty
=
\text{快速通道的高频背景值},
\]

\[
\Delta\eta
=
\text{该慢模在 }k=\omega=0\text{时的粘度增量},
\]

\[
\tau
=
\text{慢模松弛时间},
\]

\[
\xi
=
\text{慢模空间相关长度}.
\]

实部为：

\[
\boxed{
\operatorname{Re}\widehat\eta
=
\eta_\infty
+
\Delta\eta
\frac{1+\xi^2k^2}
{(1+\xi^2k^2)^2+\omega^2\tau^2}.
}
\]

若：

\[
\eta_\infty\ge0,
\qquad
\Delta\eta\ge0,
\]

则：

\[
\operatorname{Re}\widehat\eta(k,\omega)\ge0.
\]

这给出被动性和非负平均耗散。

虚部为：

\[
\boxed{
\operatorname{Im}\widehat\eta
=
\Delta\eta
\frac{\omega\tau}
{(1+\xi^2k^2)^2+\omega^2\tau^2}.
}
\]

它表示储能和相位滞后。

---

# 9. Navier–Stokes局域极限

当：

\[
\omega\tau\ll1,
\qquad
k\xi\ll1,
\]

有：

\[
\widehat\eta(k,\omega)
=
\eta_0
-
\Delta\eta\,\xi^2k^2
+
i\Delta\eta\,\omega\tau
+
O(k^4,\omega^2,k^2\omega),
\]

其中：

\[
\eta_0=\eta_\infty+\Delta\eta.
\]

最低阶：

\[
\boxed{
\sigma^{\rm dev}
=
2\eta_0D^{\rm dev}.
}
\]

这只是本构关系的Navier–Stokes极限；完整动量方程和严格流体极限仍属后续阶段。

---

# 10. 正向—逆向闭环

定义正向映射：

\[
\mathfrak F:
(\eta_\infty,\Delta\eta,\tau,\xi)
\mapsto
\widehat\eta(k,\omega).
\]

在单极点模型类别内，逆向参数可由：

\[
\eta_\infty
=
\lim_{|\omega|\to\infty}
\widehat\eta(k,\omega),
\]

\[
\Delta\eta
=
\widehat\eta(0,0)-\eta_\infty,
\]

\[
\tau^{-1}
=
|\operatorname{Im}\omega_{\rm pole}(k=0)|,
\]

\[
\xi^2
=
\frac{1}{k^2}
\left[
\frac{\Delta\eta}
{\widehat\eta(k,0)-\eta_\infty}
-1
\right]
\]

恢复。

因此在该模型类别内：

\[
\boxed{
\widehat\eta(k,\omega)
\Longleftrightarrow
(\eta_\infty,\Delta\eta,\tau,\xi).
}
\]

这不是对任意微观模型的唯一反演。

---

# 11. 数值基准

## 11.1 T1：有限振子浴可逆性

用240个背景频率离散连续谱，构造二次Hamilton矩阵并进行精确正规模演化。

结果：

\[
\|\mathcal Q_{\rm back}-\mathcal Q_0\|
=
2.06\times10^{-15},
\]

\[
\|\dot{\mathcal Q}_{\rm back}+\dot{\mathcal Q}_0\|
=
3.81\times10^{-14},
\]

最大相对能量漂移：

\[
1.08\times10^{-13}.
\]

状态：

\[
\boxed{
[\mathrm{NUMERICAL\ —\ T1\ PASSED}]
}
\]

## 11.2 T2：离散背景核逼近连续Drude核

目标：

\[
K(t)=\eta\Lambda e^{-\Lambda t}.
\]

在测试窗口 \(0\le t\le2\) 上，离散核相对 \(L^2\)误差：

\[
5.08\times10^{-3}.
\]

状态：

\[
\boxed{
[\mathrm{NUMERICAL\ —\ T2\ PASSED\ IN\ TESTED\ WINDOW}]
}
\]

## 11.3 T3：低频极限和被动性

使用：

\[
\eta_\infty=0.35,
\quad
\Delta\eta=1.25,
\quad
\tau=0.45,
\quad
\xi=0.70.
\]

得到：

\[
\widehat\eta(0,0)=1.60
=
\eta_\infty+\Delta\eta,
\]

测试网格上：

\[
\min\operatorname{Re}\widehat\eta>0.
\]

状态：

\[
\boxed{
[\mathrm{DERIVED+NUMERICAL\ —\ T3\ PASSED}]
}
\]

## 11.4 T4：含噪反演

对五个波数、三十个频率点生成 \(0.3\%\)复噪声数据。

真实值与拟合值：

| 参数 | 真实值 | 拟合值 | 相对误差 |
|---|---:|---:|---:|
| \(\eta_\infty\) | 0.350000 | 0.350319 | \(9.11\times10^{-4}\) |
| \(\Delta\eta\) | 1.250000 | 1.249912 | \(7.08\times10^{-5}\) |
| \(\tau\) | 0.450000 | 0.450405 | \(9.00\times10^{-4}\) |
| \(\xi\) | 0.700000 | 0.700469 | \(6.70\times10^{-4}\) |

状态：

\[
\boxed{
[\mathrm{NUMERICAL\ —\ T4\ PASSED\ FOR\ THE\ ONE\ POLE\ MODEL}]
}
\]

---

# 12. 失败条件

R0.1在以下任一情况出现时应判定失败或退回：

1. 总Hamilton量无下界；
2. 时间反演不能恢复初态；
3. 消去背景后得到超前响应；
4. \(\operatorname{Re}\widehat\eta<0\)且无外部能量输入解释；
5. \(\widehat\eta(0,0)\)不存在或发散；
6. 反演Jacobian退化，参数在所选数据窗口中不可辨认；
7. 只有调节目标粘度才能得到所需谱；
8. 无法把离散背景极限与连续核区分于有限时间数值假象。

---

# 13. 已完成与未完成的边界

## 已完成

\[
\boxed{
\text{可逆背景连续谱能够产生因果记忆核。}
}
\]

\[
\boxed{
\text{该记忆核可定义频率—波数依赖广义粘性。}
}
\]

\[
\boxed{
\text{单慢模的尺度与时间参数可以从响应谱反演。}
}
\]

## 未完成

\[
\boxed{
[\mathrm{OPEN}]
\quad
\text{从EP有限 }N\text{碰撞推导 }J_k(\Omega).
}
\]

\[
\boxed{
[\mathrm{OPEN}]
\quad
\text{从四元数自旋、形变和相场得到张量 }\eta_{ijmn}.
}
\]

\[
\boxed{
[\mathrm{OPEN}]
\quad
\text{由动理学取矩并严格恢复Navier–Stokes。}
\]

\[
\boxed{
[\mathrm{OPEN}]
\quad
\text{证明现实流体测量中的谱结构对应EP层级。}
\]

---

# 14. 下一阶段

下一阶段应定为：

\[
\boxed{
\text{EP-R0.2：从显式空间背景场导出 }J_k(\Omega)
}
\]

只解决三个问题：

1. 选定一个局域、平移和旋转协变的 \(S_0-S_{-1}\)耦合；
2. 从背景色散关系和耦合形状函数计算谱密度；
3. 判断得到的是Ohmic、sub-Ohmic还是super-Ohmic低频结构。

只有R0.2完成后，才把：

\[
\tau,\quad\xi,\quad\Delta\eta
\]

从“响应模型参数”推进为“由具体EP背景计算得到的参数”。
