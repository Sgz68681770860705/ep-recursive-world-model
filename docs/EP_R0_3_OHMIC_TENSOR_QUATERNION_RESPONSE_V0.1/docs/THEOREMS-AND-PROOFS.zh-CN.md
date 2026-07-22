# EP-R0.3：定理与证明

## T1：内部变量耦合的Euclidean对称性

### 命题

设：

\[
Q\mapsto RQR^T,
\qquad
B\mapsto RBR^T,
\]

\[
\boldsymbol\theta\mapsto R\boldsymbol\theta,
\qquad
\mathbf R_b\mapsto R\mathbf R_b,
\]

且形状函数只依赖：

\[
\mathbf x-\mathbf X.
\]

则：

\[
\int w(\mathbf x-\mathbf X)Q:B\,d^3x
\]

和：

\[
\int w(\mathbf x-\mathbf X)
\boldsymbol\theta\cdot\mathbf R_b\,d^3x
\]

在共同平移和共同旋转下不变。

### 证明

共同平移不改变 \(\mathbf x-\mathbf X\)。

共同旋转下：

\[
(RQR^T):(RBR^T)
=
\operatorname{tr}
(RQR^TRBR^T)
=
\operatorname{tr}(QB)
=
Q:B.
\]

轴矢量内积满足：

\[
(R\boldsymbol\theta)\cdot(R\mathbf R_b)
=
\boldsymbol\theta\cdot\mathbf R_b.
\]

证毕。

---

## T2：内部场的Ohmic谱

### 命题

三维无隙线性色散内部场，若与内部标量、张量或轴矢量坐标作非导数局域耦合，则每个独立分量满足：

\[
J_A(\Omega)\sim\Omega.
\]

### 证明

每个分量的态密度与R0.2相同。内部张量或轴矢量指标只提供有限简并度，不改变低频幂次。

在：

\[
d=3,
\qquad
m=0
\]

时：

\[
J_A(\Omega)
\sim
\Omega^{d-2+2m}
=
\Omega.
\]

证毕。

---

## T3：Isotropic投影分解

### 命题

四阶张量：

\[
P^{\rm dev},
\quad
P^{\rm vol},
\quad
P^{\rm anti}
\]

满足：

\[
(P^A)^2=P^A,
\]

\[
P^AP^B=0
\qquad
(A\ne B),
\]

并分别投影到对称无迹、纯体积和反对称子空间。

### 证明

直接使用Kronecker delta缩并即可。三个子空间构成二阶张量空间的正交分解：

\[
\mathbb R^{3\times3}
=
\operatorname{Sym}_0
\oplus
\operatorname{span}\{I\}
\oplus
\operatorname{Anti}.
\]

证毕。

---

## T4：被动性

### 命题

若：

\[
\eta_T,\zeta_L,\eta_R,\eta_Q\ge0,
\]

则：

\[
\sigma
=
2\eta_TD^{\rm dev}
+
\zeta_L(\operatorname{tr}D)I
+
2\eta_RW
+
2\eta_QA(A:D)
\]

满足：

\[
\sigma:(D+W)\ge0.
\]

### 证明

对称与反对称张量正交：

\[
D:W=0.
\]

同时：

\[
D^{\rm dev}:I=0.
\]

因此：

\[
\sigma:(D+W)
=
2\eta_T|D^{\rm dev}|^2
+
\zeta_L(\operatorname{tr}D)^2
+
2\eta_R|W|^2
+
2\eta_Q(A:D)^2
\ge0.
\]

证毕。

---

## T5：相对转子耦合守恒总角动量

### 命题

Hamilton量：

\[
H_R
=
\frac{|\mathbf S_0|^2}{2I_0}
+
\sum_\alpha
\frac{|\mathbf S_\alpha|^2}{2I_\alpha}
+
\frac12
\sum_\alpha
\kappa_\alpha
|\boldsymbol\theta_\alpha-\boldsymbol\theta_0|^2
\]

满足：

\[
\frac{d}{dt}
\left(
\mathbf S_0+\sum_\alpha\mathbf S_\alpha
\right)
=
0.
\]

### 证明

势能只依赖角度差，所以在所有角度共同平移下不变。相应Noether荷为所有共轭角动量之和。

也可直接计算：

\[
\dot{\mathbf S}_0
=
\sum_\alpha
\kappa_\alpha
(
\boldsymbol\theta_\alpha-\boldsymbol\theta_0
),
\]

\[
\dot{\mathbf S}_\alpha
=
-\kappa_\alpha
(
\boldsymbol\theta_\alpha-\boldsymbol\theta_0
).
\]

求和为零。证毕。

---

## T6：四元数单位范数

### 命题

若：

\[
\dot q
=
\frac12q\otimes(0,\boldsymbol\omega),
\]

且：

\[
|q(0)|=1,
\]

则：

\[
|q(t)|=1.
\]

### 证明

纯虚四元数：

\[
\Omega=(0,\boldsymbol\omega)
\]

满足：

\[
\Omega^*=-\Omega.
\]

因此：

\[
\frac{d}{dt}(q^*q)
=
\dot q^*q+q^*\dot q
=
-\frac12\Omega q^*q
+
\frac12q^*q\Omega
=
0,
\]

因为 \(q^*q\)为实标量。证毕。

---

## T7：取向法向应力差

### 命题

在简单剪切中：

\[
D_{xy}=D_{yx}=\dot\gamma/2,
\]

若：

\[
\sigma^Q=2\eta_QA(A:D),
\]

则：

\[
N_1^Q
=
2\eta_Q
(A_{xx}-A_{yy})
A_{xy}\dot\gamma.
\]

### 证明

有：

\[
A:D
=
A_{xy}D_{xy}
+
A_{yx}D_{yx}
=
A_{xy}\dot\gamma.
\]

所以：

\[
\sigma_{xx}^Q-\sigma_{yy}^Q
=
2\eta_Q
(A_{xx}-A_{yy})
(A:D),
\]

代入即得。证毕。

### 推论

各向同性取向平均下，四阶球面对称性给出：

\[
\langle
(A_{xx}-A_{yy})A_{xy}
\rangle=0.
\]

所以线性单体取向项不能独自解释各向同性流体的稳态法向应力差。
