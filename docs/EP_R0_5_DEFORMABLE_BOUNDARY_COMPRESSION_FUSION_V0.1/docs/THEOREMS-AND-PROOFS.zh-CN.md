# EP-R0.5：定理与证明

## T1：正半轴定理

若：

\[
a=a_0e^{\beta_a},
\qquad
b=b_0e^{\beta_b},
\]

且 \(a_0,b_0>0\)，则对任意有限实数 \(\beta_a,\beta_b\)：

\[
a>0,\qquad b>0.
\]

所以：

\[
A=R\operatorname{diag}(a^{-2},b^{-2})R^T
\]

始终正定。

---

## T2：形态—自旋Hamilton耦合

若：

\[
I(\beta)=m(a^2+b^2),
\qquad
T_R=\frac{L^2}{2I},
\]

则：

\[
-\frac{\partial T_R}{\partial\beta_a}
=
\frac{L^2ma^2}{I^2},
\]

\[
-\frac{\partial T_R}{\partial\beta_b}
=
\frac{L^2mb^2}{I^2}.
\]

所以形态变化和自旋能之间的交换来自同一Hamilton量，而不是附加经验阻尼。

---

## T3：总守恒

完整Hamilton量：

\[
H
=
T_{\rm trans}
+
T_{\rm spin}
+
T_{\rm shape}
+
V_{\rm shape}
+
U_{\rm overlap}
\]

不显含时间，所以：

\[
\dot H=0.
\]

若 \(U_{\rm overlap}\)只依赖质心差以及共同旋转不变量，则空间平移和共同旋转分别给出：

\[
\dot{\mathbf P}=0,
\qquad
\dot J=0.
\]

形态变量通过转动惯量和内部势能参与能量交换，但不增加独立的外部线动量。

---

## T4：可逆压缩记忆

碰撞退出后若：

\[
U_{\rm overlap}\approx0
\]

但：

\[
(\beta,\pi_\beta)\ne(0,0),
\]

则：

\[
E_\beta
=
\frac{|\pi_\beta|^2}{2M_\beta}
+
V_s(\beta)
>0.
\]

因此碰撞历史继续保存在形态子系统中。由于总系统可逆，这种记忆表现为振荡而非基本耗散。

---

## T5：无标签并集场

对：

\[
0\le\chi_1,\chi_2\le1,
\]

定义：

\[
\chi_U=1-(1-\chi_1)(1-\chi_2).
\]

则：

\[
0\le\chi_U\le1,
\]

并且：

\[
\chi_U(\chi_1,\chi_2)
=
\chi_U(\chi_2,\chi_1).
\]

因此该几何诊断不依赖对象编号顺序。

---

## T6：临时几何融合判据

固定阈值 \(\chi_c\)，令：

\[
N_c(t)
=
\#\operatorname{Conn}
\{\mathbf x:\chi_U(\mathbf x,t)\ge\chi_c\}.
\]

若：

\[
N_c(0)=2,
\]

某一有限区间：

\[
N_c(t)=1,
\]

而末态：

\[
N_c(t_f)=2,
\]

则定义为“临时几何融合后散开”。

该定义不等价于对象身份已经消失，因为动力学仍可能保留两套规范变量。

---

## T7：快速靠近的结论边界

当前模型中的峰值排斥力和形态储能依赖入射速度。若某一冻结参数窗口中：

\[
F_{\max}(v_2)>F_{\max}(v_1),
\qquad
v_2>v_1,
\]

只能记为该窗口的数值结果。

它不是从对称性推出的普遍单调性定理，改变形态刚度、惯性或重叠势后可能改变趋势。
