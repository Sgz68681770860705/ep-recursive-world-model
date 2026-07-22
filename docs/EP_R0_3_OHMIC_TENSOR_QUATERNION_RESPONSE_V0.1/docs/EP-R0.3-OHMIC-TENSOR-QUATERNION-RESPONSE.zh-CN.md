# EP-R0.3：对称相容的Ohmic通道、张量响应与四元数旋转

版本：`V0.1`

## 0. 科学边界

本阶段的目标不是直接解释现实流体，而是回答R0.2暴露出的数学问题：

> 三维Ohmic谱要求等效非导数耦合，这种耦合能否在不把背景解释为绝对空间位移、并保持平移和旋转对称性的条件下自然出现？

R0.3的答案是：

\[
\boxed{
\text{可以，但耦合对象应是内部序参量场，}
\quad
\text{不是绝对空间位移Goldstone场。}
}
\]

状态：

\[
[\mathrm{DERIVED\ IN\ R0.3}]
\]

只限于线性内部场、小四元数转角和给定有限形状函数。

尚未完成：

- 完整非线性 \(SU(2)\)场；
- 不规则相场边界的碰撞、断裂和重组；
- 有限 \(N\) EP碰撞到这些内部场的严格极限；
- Navier–Stokes严格极限；
- 现实流体参数拟合。

---

# 1. \(S_0\)的最小内部变量

在R0.3中，一个有限 \(S_0\)保留三个内部通道。

## 1.1 剪切形态

\[
Q_{ij}^{\rm dev}
=
Q_{ji}^{\rm dev},
\qquad
Q_{ii}^{\rm dev}=0.
\]

它描述低阶不规则形态和无体积剪切形变。

在空间旋转 \(R\in SO(3)\)下：

\[
Q\mapsto RQR^T.
\]

在整体空间平移下：

\[
Q\mapsto Q.
\]

## 1.2 体积或紧致度

\[
\vartheta
\]

为旋转标量，描述体积、紧致度或各向同性压缩。

## 1.3 四元数取向

\[
q
=
q_0+q_1I+q_2J+q_3K,
\qquad
|q|=1.
\]

取向动力学：

\[
\boxed{
\dot q
=
\frac12q\otimes(0,\boldsymbol\omega).
}
\]

小转角极限中：

\[
q
\approx
\left(
1,\frac{\boldsymbol\theta}{2}
\right).
\]

因此旋转通道可以先由轴矢量：

\[
\boldsymbol\theta
\]

线性表示。

---

# 2. \(S_{-1}\)内部背景场

为三个通道分别引入：

\[
B_{ij}^{\rm dev}(\mathbf x,t),
\]

\[
\phi_L(\mathbf x,t),
\]

\[
\mathbf R(\mathbf x,t).
\]

它们分别按：

- 对称无迹张量；
- 标量；
- 轴矢量；

在旋转下变换。

自由作用量：

\[
\boxed{
\mathcal S_{-1}
=
\frac12
\int dt\,d^3x
\left[
|\dot B^{\rm dev}|^2
-c_T^2|\nabla B^{\rm dev}|^2
+
\dot\phi_L^2
-c_L^2|\nabla\phi_L|^2
+
|\dot{\mathbf R}|^2
-c_R^2|\nabla\mathbf R|^2
\right].
}
\]

三个通道均无隙。

---

# 3. 对称相容的局域耦合

设 \(w_A(\mathbf x-\mathbf X)\)为以 \(S_0\)质心为中心的有限尺度形状函数。

定义：

\[
\boxed{
\mathcal S_{\rm int}
=
\int dt\,d^3x
\left[
g_Tw_TQ_{ij}^{\rm dev}B_{ij}^{\rm dev}
+
g_Lw_L\vartheta\phi_L
+
g_Rw_R\boldsymbol\theta\cdot\mathbf R
\right].
}
\]

这些耦合是非导数的，但并不依赖绝对位置。

## 3.1 平移

当：

\[
\mathbf x\mapsto\mathbf x+\mathbf a,
\qquad
\mathbf X\mapsto\mathbf X+\mathbf a,
\]

有：

\[
w_A(\mathbf x-\mathbf X)
\mapsto
w_A(\mathbf x-\mathbf X).
\]

所以作用量不变。

## 3.2 旋转

在共同旋转下：

\[
Q:B
\mapsto
(RQR^T):(RBR^T)
=
Q:B,
\]

\[
\boldsymbol\theta\cdot\mathbf R
\mapsto
(R\boldsymbol\theta)\cdot(R\mathbf R)
=
\boldsymbol\theta\cdot\mathbf R.
\]

因此耦合保持旋转标量。

关键点是：

\[
\boxed{
Q,\vartheta,\boldsymbol\theta
\text{是内部变量，}
}
\]

它们不具有绝对空间位移场的整体移位对称性，所以非导数耦合并不违反空间平移对称性。

---

# 4. 三通道谱密度

对每个通道：

\[
A\in\{T,L,R\},
\]

取归一化高斯源：

\[
|\widetilde w_A(\mathbf q)|^2
=
\left(
\frac{a_A^2}{\pi}
\right)^{3/2}
e^{-a_A^2q^2}.
\]

背景色散：

\[
\Omega_A(\mathbf q)
=
c_Aq.
\]

于是每个独立分量的谱密度为：

\[
\boxed{
J_A(k,\Omega)
=
\gamma_A\Omega
e^{-a_A^2(k^2+\Omega^2/c_A^2)}
\operatorname{sinhc}
\left(
\frac{2a_A^2k\Omega}{c_A}
\right),
}
\]

其中：

\[
\boxed{
\gamma_A
=
\frac{2\sqrt{\pi}g_A^2a_A^3}{c_A^3}.
}
\]

所以：

\[
J_A(0,\Omega)
\sim
\gamma_A\Omega.
\]

三个通道均为Ohmic。

---

# 5. Isotropic张量分解

定义四阶投影：

\[
\boxed{
P_{ijmn}^{\rm dev}
=
\frac12
(
\delta_{im}\delta_{jn}
+
\delta_{in}\delta_{jm}
)
-
\frac13
\delta_{ij}\delta_{mn},
}
\]

\[
\boxed{
P_{ijmn}^{\rm vol}
=
\frac13
\delta_{ij}\delta_{mn},
}
\]

\[
\boxed{
P_{ijmn}^{\rm anti}
=
\frac12
(
\delta_{im}\delta_{jn}
-
\delta_{in}\delta_{jm}
).
}
\]

它们分别作用于：

- 对称无迹应变率；
- 体积应变率；
- 相对旋转率。

各向同性广义粘度张量为：

\[
\boxed{
\widehat\eta_{ijmn}^{\rm iso}
=
\widehat\eta_TP_{ijmn}^{\rm dev}
+
\widehat\zeta_LP_{ijmn}^{\rm vol}
+
\widehat\eta_RP_{ijmn}^{\rm anti}.
}
\]

其中：

\[
\widehat\eta_A(k,\omega)
=
\int_0^\infty
K_A(k,t)e^{i\omega t}dt.
\]

低频长波极限：

\[
\eta_T(0,0)=\gamma_T,
\]

\[
\zeta_L(0,0)=\gamma_L,
\]

\[
\eta_R(0,0)=\gamma_R.
\]

---

# 6. 四元数取向与不规则边界各向异性

取物体坐标中的主轴：

\[
\mathbf e_3.
\]

由四元数得到空间取向：

\[
\boxed{
\mathbf n(q)
=
q\otimes(0,\mathbf e_3)\otimes q^{-1}.
}
\]

取其矢量部分。

定义无迹取向张量：

\[
\boxed{
A_{ij}(q)
=
n_i(q)n_j(q)
-
\frac13\delta_{ij}.
}
\]

最小各向异性响应：

\[
\boxed{
\widehat\eta_{ijmn}^{Q}
=
\widehat\eta_Q
A_{ij}(q)A_{mn}(q).
}
\]

完整响应：

\[
\boxed{
\widehat{\mathbb\eta}
=
\widehat\eta_T\mathbb P^{\rm dev}
+
\widehat\zeta_L\mathbb P^{\rm vol}
+
\widehat\eta_R\mathbb P^{\rm anti}
+
\widehat\eta_Q A\otimes A.
}
\]

该项不是任意张量堆叠，而是当前只有一个主取向轴时的最小正半定各向异性修正。

---

# 7. 被动性

令：

\[
D=D^{\rm dev}+\frac13(\operatorname{tr}D)I,
\]

\[
W=-W^T.
\]

短记忆极限的应力为：

\[
\sigma
=
2\eta_TD^{\rm dev}
+
\zeta_L(\operatorname{tr}D)I
+
2\eta_RW
+
2\eta_QA(A:D).
\]

功率密度：

\[
\boxed{
\mathcal P
=
\sigma:(D+W)
}
\]

利用对称和反对称张量正交，得到：

\[
\boxed{
\mathcal P
=
2\eta_T|D^{\rm dev}|^2
+
\zeta_L(\operatorname{tr}D)^2
+
2\eta_R|W|^2
+
2\eta_Q(A:D)^2.
}
\]

若：

\[
\eta_T,\zeta_L,\eta_R,\eta_Q\ge0,
\]

则：

\[
\mathcal P\ge0.
\]

频率域中，只需把这些条件替换为各响应函数实部非负。

---

# 8. 相对旋转耦合与总角动量

为了不把旋转粘性写成基本阻尼，取有限转子浴：

\[
\boxed{
H_R
=
\frac{|\mathbf S_0|^2}{2I_0}
+
\sum_{\alpha}
\frac{|\mathbf S_\alpha|^2}{2I_\alpha}
+
\frac12
\sum_\alpha
\kappa_\alpha
|\boldsymbol\theta_\alpha-\boldsymbol\theta_0|^2.
}
\]

该Hamilton量只依赖相对角度。

在共同旋转平移：

\[
\boldsymbol\theta_0\mapsto
\boldsymbol\theta_0+\boldsymbol\epsilon,
\]

\[
\boldsymbol\theta_\alpha\mapsto
\boldsymbol\theta_\alpha+\boldsymbol\epsilon
\]

下不变。

由Noether定理：

\[
\boxed{
\mathbf J_{\rm total}
=
\mathbf S_0+\sum_\alpha\mathbf S_\alpha
}
\]

严格守恒。

消去背景转子后，中心转子得到旋转记忆核，但完整系统保持可逆。

在低频Markov近似下：

\[
I_0\ddot{\boldsymbol\theta}
+
\gamma_R\dot{\boldsymbol\theta}
+
K_R\boldsymbol\theta
=
\boldsymbol\tau_{\rm ext}.
\]

旋转响应函数：

\[
\boxed{
\chi_R(\omega)
=
\frac{1}
{K_R-I_0\omega^2-i\gamma_R\omega}.
}
\]

其极点为：

\[
\boxed{
\omega_\pm
=
\frac{
-i\gamma_R
\pm
\sqrt{4I_0K_R-\gamma_R^2}
}
{2I_0}.
}
\]

这些极点属于约化旋转响应，不表示完整Hamilton系统存在基本耗散。

---

# 9. 法向应力差

考虑简单剪切：

\[
D_{xy}=D_{yx}=\frac{\dot\gamma}{2},
\]

其余分量为零。

各向同性Newton项给出：

\[
N_1^{\rm iso}
=
\sigma_{xx}-\sigma_{yy}
=
0.
\]

取向项给出：

\[
\sigma_{ij}^{Q}
=
2\eta_QA_{ij}(A:D).
\]

因为：

\[
A:D
=
A_{xy}\dot\gamma,
\]

所以：

\[
\boxed{
N_1^{Q}
=
2\eta_Q
(A_{xx}-A_{yy})
A_{xy}
\dot\gamma.
}
\]

因此：

\[
\boxed{
\text{有取向的不规则单个 }S_0
\text{可以在线性响应中产生法向应力差。}
}
\]

但对各向同性取向分布：

\[
\langle
(A_{xx}-A_{yy})A_{xy}
\rangle_{\rm iso}
=
0.
\]

所以：

\[
\boxed{
\text{各向同性流体的稳态法向应力差，}
}
\]

仍然需要剪切诱导取向、非线性相场或二阶响应，不能由这一线性单体项直接得到。

---

# 10. 四元数运输

四元数方程：

\[
\dot q
=
\frac12q\otimes(0,\boldsymbol\omega)
\]

满足：

\[
\frac{d}{dt}|q|^2=0.
\]

有限步长可以使用群指数：

\[
\delta q
=
\left(
\cos\frac{|\boldsymbol\omega|\Delta t}{2},
\,
\widehat{\boldsymbol\omega}
\sin\frac{|\boldsymbol\omega|\Delta t}{2}
\right),
\]

\[
q(t+\Delta t)
=
q(t)\otimes\delta q.
\]

这种更新天然保留单位四元数约束。

---

# 11. 参数反演

旋转通道在 \(k=0\)的高斯记忆响应为：

\[
\boxed{
\widehat\eta_R(0,\omega)
=
\gamma_R
e^{-(\omega/\Omega_{c,R})^2}
\left[
1+
i\,\operatorname{erfi}
\left(
\frac{\omega}{\Omega_{c,R}}
\right)
\right],
}
\]

其中：

\[
\Omega_{c,R}
=
\frac{c_R}{a_R}.
\]

静态空间响应：

\[
\boxed{
\eta_R(k,0)
=
\gamma_R
e^{-a_R^2k^2}.
}
\]

因此：

- \(k\)依赖确定 \(a_R\)；
- \(\omega\)依赖确定 \(c_R/a_R\)；
- 零频幅度确定：
  \[
  \gamma_R
  =
  \frac{2\sqrt{\pi}g_R^2a_R^3}{c_R^3}.
  \]

合起来可以反演：

\[
\boxed{
(g_R,a_R,c_R).
}
\]

---

# 12. 数值结果

## T1：张量投影代数

数值验证：

\[
P^{\rm dev}P^{\rm dev}=P^{\rm dev},
\]

\[
P^{\rm vol}P^{\rm vol}=P^{\rm vol},
\]

\[
P^{\rm anti}P^{\rm anti}=P^{\rm anti},
\]

且相互正交。

最大代数残差：

\[
\boxed{
1.36e-16
}
\]

状态：

\[
[\mathrm{NUMERICAL\ —\ T1\ PASSED}]
\]

## T2：被动性

随机生成5000组：

\[
(D,W,q).
\]

测试中最小功率：

\[
\boxed{
1.03e+00>0.
}
\]

状态：

\[
[\mathrm{NUMERICAL\ —\ T2\ PASSED}]
\]

## T3：四元数运输

经过10000次时变角速度群更新：

\[
\max
\left|
|q|-1
\right|
=
\boxed{
4.55e-15.
}
\]

状态：

\[
[\mathrm{NUMERICAL\ —\ T3\ PASSED}]
\]

## T4：转子浴总角动量与时间反演

总角动量最大漂移：

\[
\boxed{
4.44e-16.
}
\]

构型反演误差：

\[
\boxed{
4.19e-16.
}
\]

速度反演误差：

\[
\boxed{
9.11e-16.
}
\]

相对能量漂移：

\[
\boxed{
8.88e-16.
}
\]

状态：

\[
[\mathrm{NUMERICAL\ —\ T4\ PASSED}]
\]

## T5：法向应力差

取向角：

\[
\alpha=25^\circ.
\]

直接张量计算与解析公式的相对误差：

\[
\boxed{
0.00e+00.
}
\]

使用Fibonacci球面对各向同性取向平均：

\[
\left|
\langle N_1^Q\rangle
\right|
=
\boxed{
1.33e-14.
}
\]

状态：

\[
[\mathrm{NUMERICAL\ —\ T5\ PASSED}]
\]

## T6：旋转通道参数反演

使用 \(0.3\%\)复噪声，同时拟合空间和频率响应。

真实参数：

\[
g_R=0.900000,
\qquad
a_R=0.650000,
\qquad
c_R=1.300000.
\]

反演结果：

\[
g_R^{\rm fit}=0.900661,
\]

\[
a_R^{\rm fit}=0.649640,
\]

\[
c_R^{\rm fit}=1.300066.
\]

相对误差均低于：

\[
2.2\times10^{-4}.
\]

状态：

\[
[\mathrm{NUMERICAL\ —\ T6\ PASSED}]
\]

---

# 13. 本阶段真正完成的桥

\[
\boxed{
\text{内部形态/体积/旋转变量}
\rightarrow
\text{对称相容Ohmic场耦合}
\rightarrow
\text{张量广义粘度}
}
\]

以及：

\[
\boxed{
\text{四元数取向}
\rightarrow
\text{各向异性应力与法向应力差}.
}
\]

这说明R0.2所需的非导数Ohmic通道不必依赖绝对空间位移。

---

# 14. 未完成问题

1. \(Q,\vartheta,q\)尚未从真实相场边界计算；
2. 当前四元数通道采用小角度线性化；
3. 取向各向异性系数 \(\eta_Q\)尚未从边界几何积分推出；
4. 各向同性流体的法向应力差仍需非线性取向动力学；
5. 多个 \(S_0\)碰撞后的融合、散开和重组尚未加入；
6. 还没有从有限 \(N\)递归碰撞得到三个背景场；
7. 尚未取矩恢复普通流体方程。

---

# 15. 下一阶段

下一道门建议冻结为：

\[
\boxed{
\text{EP-R0.4：有限相场边界、四元数取向与碰撞应力账本}
}
\]

其任务是：

1. 用相场 \(\chi(\mathbf x,t)\)定义真实有限 \(S_0\)边界；
2. 从边界几何计算：
   \[
   Q_{ij},\quad A_{ij},\quad g_T,\quad g_R;
   \]
3. 统一正碰、不对心碰撞和边界重叠；
4. 计算线动量、轨道角动量、内部自旋和背景角动量账本；
5. 区分散开、融合和重组；
6. 检验碰撞后应力核是否确实具有R0.3预测的张量结构。
