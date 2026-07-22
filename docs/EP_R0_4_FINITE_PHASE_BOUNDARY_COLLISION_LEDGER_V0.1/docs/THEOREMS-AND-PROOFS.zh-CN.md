# EP-R0.4：定理与证明

## T1：高斯相场矩

### 命题

若：

\[
\chi(\mathbf x)
=
\exp
\left[
-\frac12
(\mathbf x-\mathbf X)^TA(\mathbf x-\mathbf X)
\right],
\]

其中 \(A>0\)，则二维中：

\[
V=\int\chi d^2x
=
\frac{2\pi}{\sqrt{\det A}},
\]

\[
\mathbf X^\chi=\mathbf X,
\]

\[
M
=
\frac1V
\int
(\mathbf x-\mathbf X)
\otimes
(\mathbf x-\mathbf X)
\chi d^2x
=
A^{-1}.
\]

### 证明

作变量变换：

\[
\mathbf z=A^{1/2}(\mathbf x-\mathbf X).
\]

积分化为标准二维高斯积分。奇次矩为零，二次矩为单位矩，变换回原坐标即得。证毕。

---

## T2：边界梯度张量

### 命题

对同一高斯相场：

\[
B
=
\int
\nabla\chi\otimes\nabla\chi\,d^2x
=
\frac{\pi}{2\sqrt{\det A}}A.
\]

### 证明

有：

\[
\nabla\chi
=
-A\mathbf y\chi.
\]

所以：

\[
B
=
A
\left[
\int
\mathbf y\otimes\mathbf y
e^{-\mathbf y^TA\mathbf y}
d^2y
\right]
A.
\]

标准高斯矩为：

\[
\int
\mathbf y\otimes\mathbf y
e^{-\mathbf y^TA\mathbf y}
d^2y
=
\frac{\pi}{2\sqrt{\det A}}A^{-1}.
\]

代入即得。证毕。

---

## T3：两个边界的闭式重叠

### 命题

令：

\[
\chi_i
=
\exp
\left[
-\frac12
(\mathbf x-\mathbf X_i)^TA_i
(\mathbf x-\mathbf X_i)
\right].
\]

则：

\[
\mathcal O_{12}
=
\int\chi_1\chi_2d^2x
=
\frac{2\pi}{\sqrt{\det(A_1+A_2)}}
\exp
\left[
-\frac12\mathbf d^TC\mathbf d
\right],
\]

其中：

\[
\mathbf d=\mathbf X_1-\mathbf X_2,
\]

\[
C
=
A_1-A_1(A_1+A_2)^{-1}A_1.
\]

### 证明

把两个二次型相加并配方。积分后的常数项就是：

\[
\mathbf d^TC\mathbf d.
\]

剩余积分为协方差：

\[
(A_1+A_2)^{-1}
\]

的标准高斯积分。证毕。

---

## T4：力与线动量守恒

### 命题

若：

\[
U=\varepsilon_b\mathcal O_{12},
\]

则：

\[
\mathbf F_1
=
UC\mathbf d,
\qquad
\mathbf F_2=-\mathbf F_1.
\]

### 证明

对：

\[
U
\propto
\exp(-\mathbf d^TC\mathbf d/2)
\]

求导：

\[
\nabla_{\mathbf d}U
=
-UC\mathbf d.
\]

因为：

\[
\mathbf d=\mathbf X_1-\mathbf X_2,
\]

所以：

\[
\mathbf F_1
=
-\nabla_{\mathbf X_1}U
=
UC\mathbf d,
\]

\[
\mathbf F_2
=
-\nabla_{\mathbf X_2}U
=
-\mathbf F_1.
\]

证毕。

---

## T5：旋转不变性与角动量账本

### 命题

若：

\[
U(R\mathbf d,\theta_1+\varphi,\theta_2+\varphi)
=
U(\mathbf d,\theta_1,\theta_2),
\]

则：

\[
\mathbf d\times\mathbf F_1
+
\tau_1+\tau_2
=
0.
\]

### 证明

对共同旋转参数 \(\varphi\)在零点求导：

\[
0
=
\frac{dU}{d\varphi}
=
\nabla_{\mathbf d}U
\cdot
(\mathbf e_z\times\mathbf d)
+
\frac{\partial U}{\partial\theta_1}
+
\frac{\partial U}{\partial\theta_2}.
\]

利用：

\[
\nabla_{\mathbf d}U=-\mathbf F_1,
\]

\[
\tau_i=-\frac{\partial U}{\partial\theta_i},
\]

得到结论。证毕。

---

## T6：pair stress与内部转矩

### 命题

定义：

\[
\Sigma^{\rm pair}
=
-\frac1{V_c}
\mathbf d\otimes\mathbf F_1.
\]

则二维中：

\[
V_c
(
\Sigma_{xy}^{\rm pair}
-
\Sigma_{yx}^{\rm pair}
)
=
\tau_1+\tau_2.
\]

### 证明

左侧：

\[
V_c(\Sigma_{xy}-\Sigma_{yx})
=
-(d_xF_y-d_yF_x)
=
-\mathbf d\times\mathbf F_1.
\]

由T5：

\[
-\mathbf d\times\mathbf F_1
=
\tau_1+\tau_2.
\]

证毕。

---

## T7：Hamilton碰撞守恒

### 命题

对：

\[
H
=
\sum_i
\left[
\frac{|\mathbf p_i|^2}{2m_i}
+
\frac{L_i^2}{2I_i}
\right]
+
U,
\]

若 \(U\)满足共同平移和共同旋转不变性，则：

\[
\dot H=0,
\]

\[
\dot{\mathbf P}=0,
\]

\[
\dot J=0.
\]

### 证明

时间平移不变性给出能量守恒；空间平移不变性给出线动量守恒；共同旋转不变性给出轨道角动量与内部角动量之和守恒。也可将T4和T5代入Hamilton方程直接验证。证毕。
