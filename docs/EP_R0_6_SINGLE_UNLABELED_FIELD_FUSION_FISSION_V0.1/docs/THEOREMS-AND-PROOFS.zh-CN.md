# EP-R0.6：定理与证明

## T1：Hamilton场方程

作用量：

\[
\mathcal S
=
\int dt\,d^2x
\left[
\frac{i}{2}
(\psi^*\psi_t-\psi\psi_t^*)
-
\frac12|\nabla\psi|^2
+
\frac g2|\psi|^4
-
\frac h3|\psi|^6
\right]
\]

对 \(\psi^*\)变分，得到：

\[
i\psi_t
=
-\frac12\nabla^2\psi
-g|\psi|^2\psi
+h|\psi|^4\psi.
\]

---

## T2：范数守恒

定义：

\[
N=\int|\psi|^2d^2x.
\]

由场方程及其共轭式：

\[
\partial_t|\psi|^2
+
\nabla\cdot
\operatorname{Im}(\psi^*\nabla\psi)
=
0.
\]

在周期边界或无穷远衰减条件下：

\[
\dot N=0.
\]

---

## T3：能量、动量和角动量

时间平移不变性给出：

\[
H
=
\int
\left[
\frac12|\nabla\psi|^2
-\frac g2|\psi|^4
+\frac h3|\psi|^6
\right]d^2x
\]

守恒。

空间平移不变性给出：

\[
\mathbf P
=
\int
\operatorname{Im}
(\psi^*\nabla\psi)d^2x
\]

守恒。

连续旋转不变性给出：

\[
L_z
=
\int
\operatorname{Im}
\left[
\psi^*(x\partial_y-y\partial_x)\psi
\right]d^2x
\]

守恒。

---

## T4：时间反演

若 \(\psi(\mathbf x,t)\)是解，则：

\[
\widetilde\psi(\mathbf x,t)
=
\psi^*(\mathbf x,-t)
\]

也满足同一方程。

这是因为Laplacian和非线性系数均为实数，并且非线性只依赖 \(|\psi|^2\)。

---

## T5：连通分量标签的中断

给定阈值 \(\rho_c\)，对象定义为：

\[
\operatorname{Conn}
\{\rho\ge\rho_c\}.
\]

若入射时有两个连通分量，而某一时间区间只有一个连通分量，则基于连通分量的两条对象标签不能在该区间内保持一一连续延拓。

若随后重新出现两个分量，可以重新编号，但编号并非由连通拓扑唯一决定。

该命题不意味着完整场状态的信息被删除。

---

## T6：线性叠加

当：

\[
g=h=0,
\]

演化算子为：

\[
U(t)=e^{i t\nabla^2/2}.
\]

它是线性算子，所以：

\[
U(t)(\psi_1+\psi_2)
=
U(t)\psi_1+U(t)\psi_2.
\]

因此线性场相遇不产生真正的非线性散射映射。

---

## T7：五次项的高密度作用

局域势能密度：

\[
V(\rho)
=
-\frac g2\rho^2+\frac h3\rho^3.
\]

当 \(h>0\)且密度足够高时，六次项为正并增长更快，提供高密度能量惩罚。

这可以抑制纯聚焦三次项的无限压缩倾向，但不自动保证所有初值的全局正则性；完整适定性需要独立证明。
