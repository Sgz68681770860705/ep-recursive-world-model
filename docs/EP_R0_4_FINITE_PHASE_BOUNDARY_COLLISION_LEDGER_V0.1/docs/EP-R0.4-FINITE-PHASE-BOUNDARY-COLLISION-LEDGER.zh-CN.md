# EP-R0.4：有限相场边界、四元数取向与碰撞应力账本

版本：`V0.1`

## 0. 科学边界

R0.4解决的是一个较窄但必要的问题：

\[
\boxed{
\text{给定一个真实有限 }S_0\text{边界，}
\quad
\text{如何统一定义碰撞、力、转矩和应力账本？}
}
\]

本阶段没有证明：

- 该高斯边界就是现实基本粒子；
- \(S_0\)已从有限 \(N\) EP递归碰撞中涌现；
- 现实粘度已经被推导；
- 两个边界会真实融合、断裂或重构；
- 三维完整四元数碰撞已经完成。

数值基准采用二维平面运动，并把取向嵌入单位四元数的 \(K\)轴旋转子群：

\[
q(\theta)
=
\left(
\cos\frac{\theta}{2},
0,
0,
\sin\frac{\theta}{2}
\right).
\]

这是一项完整三维理论之前的最小守恒基准。

---

# 1. 有限 \(S_0\)边界

定义：

\[
\boxed{
\chi_i(\mathbf x,t)
=
\exp
\left[
-\frac12
\mathbf y_i^TA_i(q_i)\mathbf y_i
\right],
\qquad
\mathbf y_i=\mathbf x-\mathbf X_i.
}
\]

其中：

\[
A_i(q_i)
=
R(q_i)
\operatorname{diag}
(a_i^{-2},b_i^{-2})
R(q_i)^T.
\]

边界：

\[
\boxed{
\Sigma_i
=
\{\mathbf x:\chi_i(\mathbf x)=e^{-1/2}\}
}
\]

满足：

\[
\mathbf y_i^TA_i\mathbf y_i=1.
\]

因此：

\[
a_i,\ b_i
\]

就是半主轴长度。

圆形极限：

\[
a_i=b_i.
\]

---

# 2. 从边界直接恢复几何变量

定义相场体积：

\[
V_i
=
\int_{\mathbb R^2}
\chi_i\,d^2x.
\]

质心：

\[
\mathbf X_i^\chi
=
\frac1{V_i}
\int
\mathbf x\chi_i\,d^2x.
\]

二阶形态矩：

\[
M_i
=
\frac1{V_i}
\int
(\mathbf x-\mathbf X_i^\chi)
\otimes
(\mathbf x-\mathbf X_i^\chi)
\chi_i\,d^2x.
\]

高斯边界满足：

\[
\boxed{
V_i
=
\frac{2\pi}
{\sqrt{\det A_i}},
\qquad
\mathbf X_i^\chi=\mathbf X_i,
\qquad
M_i=A_i^{-1}.
}
\]

定义无迹形态张量：

\[
\boxed{
Q_i
=
\frac{M_i}{\operatorname{tr}M_i}
-
\frac12I.
}
\]

其主轴给出取向，特征值给出不规则程度。

---

# 3. 边界梯度张量与几何耦合因子

定义：

\[
\boxed{
B_i
=
\int
\nabla\chi_i
\otimes
\nabla\chi_i
\,d^2x.
}
\]

对高斯边界：

\[
\boxed{
B_i
=
\frac{\pi}
{2\sqrt{\det A_i}}
A_i.
}
\]

定义归一化边界各向异性：

\[
\boxed{
\alpha_{\chi,i}
=
\sqrt{2}
\left\|
\frac{B_i}{\operatorname{tr}B_i}
-
\frac12I
\right\|_F.
}
\]

在二维中：

\[
\alpha_{\chi,i}
=
\frac{
|\lambda_1(B_i)-\lambda_2(B_i)|
}{
\lambda_1(B_i)+\lambda_2(B_i)
}.
\]

因此：

\[
a_i=b_i
\Longrightarrow
\alpha_{\chi,i}=0.
\]

而：

\[
a_i\ne b_i
\Longrightarrow
\alpha_{\chi,i}>0.
\]

R0.3的耦合常数可在第一近似下分解为：

\[
\boxed{
g_T^{\rm eff}
=
g_T^{(0)}
\mathcal F_T[\chi],
\qquad
g_R^{\rm eff}
=
g_R^{(0)}
\mathcal F_R[\chi].
}
\]

最小椭圆模型取：

\[
\mathcal F_T[\chi]
=
\mathcal F_R[\chi]
=
\alpha_\chi.
\]

必须强调：

\[
g_A^{(0)}
\]

仍是背景与边界的基础耦合强度；R0.4计算的是几何形状因子，而不是凭边界几何单独决定全部相互作用强度。

---

# 4. 边界重叠与碰撞定义

两个边界的重叠量：

\[
\boxed{
\mathcal O_{12}
=
\int
\chi_1(\mathbf x)
\chi_2(\mathbf x)
\,d^2x.
}
\]

定义：

\[
S=A_1+A_2,
\]

\[
C
=
A_1
-
A_1S^{-1}A_1.
\]

令：

\[
\mathbf d=\mathbf X_1-\mathbf X_2.
\]

则：

\[
\boxed{
\mathcal O_{12}
=
\frac{2\pi}
{\sqrt{\det S}}
\exp
\left(
-\frac12
\mathbf d^TC\mathbf d
\right).
}
\]

定义正的边界响应能：

\[
\boxed{
U_{12}
=
\varepsilon_b
\mathcal O_{12}.
}
\]

该式应理解为：

\[
[\mathrm{POSTULATE\ R0.4}]
\]

即背景边界层重叠所储存的最小正能量，不是已经从有限 \(N\)推导出的现实碰撞势。

---

# 5. 归一化碰撞占用

定义自重叠：

\[
\mathcal O_{ii}^{(2)}
=
\int\chi_i^2d^2x
=
\frac{\pi}{\sqrt{\det A_i}}.
\]

归一化重叠：

\[
\boxed{
\rho_{12}
=
\frac{
\mathcal O_{12}
}{
\sqrt{
\mathcal O_{11}^{(2)}
\mathcal O_{22}^{(2)}
}
}.
}
\]

由Cauchy–Schwarz不等式：

\[
0\le\rho_{12}\le1.
\]

给定阈值：

\[
\rho_c>0,
\]

定义有限碰撞时间区间：

\[
\boxed{
\mathcal C_{12}
=
\{t:\rho_{12}(t)>\rho_c\}.
}
\]

碰撞持续时间为该集合的时间测度。

碰撞不再是一个瞬时点，而是边界响应层具有有限重叠的全过程。

---

# 6. 力与转矩

平动力：

\[
\boxed{
\mathbf F_1
=
-\frac{\partial U_{12}}
{\partial\mathbf X_1}
=
U_{12}C\mathbf d,
}
\]

\[
\boxed{
\mathbf F_2=-\mathbf F_1.
}
\]

内部转矩：

\[
\boxed{
\tau_i
=
-\frac{\partial U_{12}}
{\partial\theta_i}.
}
\]

在三维中应改为四元数切空间上的变分：

\[
\boldsymbol\tau_i
=
-
\operatorname{grad}_{SO(3),q_i}
U_{12}.
\]

R0.4数值代码使用复步长微分计算平面转矩，它在解析函数下避免普通有限差分的消减误差。

---

# 7. Euclidean对称性账本

由于：

\[
U_{12}
=
U(
\mathbf X_1-\mathbf X_2,
\theta_1,
\theta_2
),
\]

整体平移不改变能量，所以：

\[
\boxed{
\mathbf F_1+\mathbf F_2=0.
}
\]

由于共同旋转：

\[
\mathbf d\mapsto R(\varphi)\mathbf d,
\]

\[
\theta_i\mapsto\theta_i+\varphi
\]

不改变能量，所以：

\[
\boxed{
\mathbf d\times\mathbf F_1
+
\tau_1+\tau_2
=
0.
}
\]

这表示：

\[
\boxed{
\text{轨道角动量变化}
+
\text{两个 }S_0\text{内部自旋变化}
=
0.
}
\]

这里没有角动量消失。

---

# 8. 碰撞应力与偶应力账本

定义pair virial stress：

\[
\boxed{
\Sigma^{\rm pair}
=
-\frac1{V_c}
\mathbf d\otimes\mathbf F_1,
}
\]

其中 \(V_c\)是所选粗粒化控制体积。

它一般不对称。

在二维：

\[
\boxed{
V_c
(
\Sigma_{xy}^{\rm pair}
-
\Sigma_{yx}^{\rm pair}
)
=
\tau_1+\tau_2.
}
\]

所以应力反对称部分并不是错误，而是轨道角动量向内部自旋交换的宏观记录。

若只保留对称Cauchy应力而删除内部转矩账本，就会丢失这一部分信息。

---

# 9. 最小Hamilton碰撞系统

取：

\[
\boxed{
H
=
\sum_{i=1}^2
\left[
\frac{|\mathbf p_i|^2}{2m_i}
+
\frac{L_i^2}{2I_i}
\right]
+
U_{12}.
}
\]

Hamilton方程：

\[
\dot{\mathbf X}_i
=
\frac{\mathbf p_i}{m_i},
\]

\[
\dot\theta_i
=
\frac{L_i}{I_i},
\]

\[
\dot{\mathbf p}_i
=
\mathbf F_i,
\]

\[
\dot L_i
=
\tau_i.
\]

总能量：

\[
E=H.
\]

总线动量：

\[
\boxed{
\mathbf P
=
\mathbf p_1+\mathbf p_2.
}
\]

总角动量：

\[
\boxed{
J
=
\mathbf X_1\times\mathbf p_1
+
\mathbf X_2\times\mathbf p_2
+
L_1+L_2.
}
\]

无外力和外转矩时：

\[
\dot E=0,
\qquad
\dot{\mathbf P}=0,
\qquad
\dot J=0.
\]

---

# 10. 正碰与不对心碰撞

## 10.1 圆形正碰

当：

\[
a_i=b_i,
\]

取向不影响边界：

\[
\frac{\partial U}{\partial\theta_i}=0.
\]

所以：

\[
\boxed{
\tau_1=\tau_2=0.
}
\]

中心碰撞不能凭空产生自旋。

## 10.2 不规则边界不对心碰撞

当：

\[
a_i\ne b_i
\]

且冲量不通过质心时：

\[
\tau_i\ne0.
\]

于是：

\[
L_{\rm orbital}
\longleftrightarrow
L_1+L_2.
\]

但是：

\[
J_{\rm total}
\]

保持不变。

---

# 11. 碰撞结果分类的当前能力

定义：

### 散射

在有限碰撞区间后：

\[
\rho_{12}(t_{\rm final})<\rho_c
\]

并且：

\[
\frac{d}{dt}
|\mathbf X_1-\mathbf X_2|
>0.
\]

### 持续重叠或候选束缚

在观测末段：

\[
\rho_{12}(t)>\rho_c
\]

持续成立。

### 融合—重构

这一结果要求对象标签不再固定，并使用单一总相场：

\[
\chi(\mathbf x,t)
\]

发生拓扑变化。

当前模型始终保留：

\[
\chi_1,\chi_2
\]

两个标签，所以即使两场重叠，也不能证明真实融合或重构。

因此：

\[
\boxed{
[\mathrm{OPEN}]
\quad
\text{散开以后是否形成无标签的新 }S_0.
}
\]

这也适用于“两束光相遇后是否散开重组”的问题：必须先区分线性背景模式叠加与有边界对象的拓扑重构。

---

# 12. 数值门

## T1：边界几何恢复

二维网格积分恢复：

\[
V,\quad
\mathbf X,\quad
M,\quad
B.
\]

结果：

- 相场体积相对误差：
  \[
  1.47e-08;
  \]
- 质心误差：
  \[
  7.39e-08;
  \]
- 二阶形态矩相对误差：
  \[
  4.49e-07;
  \]
- 边界梯度张量相对误差：
  \[
  6.30e-14.
  \]

状态：

\[
[\mathrm{NUMERICAL\ —\ T1\ PASSED}]
\]

## T2：能量梯度、力和转矩

随机边界构型中：

- 解析平动力与有限差分能量梯度最大相对误差：
  \[
  4.21e-10;
  \]
- 复步长转矩与中心差分最大相对误差：
  \[
  1.75e-08.
  \]

状态：

\[
[\mathrm{NUMERICAL\ —\ T2\ PASSED}]
\]

## T3：Euclidean对称性与角动量局部账本

随机1000组边界构型：

- 共同旋转能量相对误差：
  \[
  5.39e-15;
  \]
- 角动量账本最大残差：
  \[
  6.88e-15.
  \]

状态：

\[
[\mathrm{NUMERICAL\ —\ T3\ PASSED}]
\]

## T4：pair stress—couple stress闭账

随机测试中：

\[
V_c(
\Sigma_{xy}-\Sigma_{yx}
)
-
(\tau_1+\tau_2)
\]

最大绝对残差：

\[
6.88e-15.
\]

状态：

\[
[\mathrm{NUMERICAL\ —\ T4\ PASSED}]
\]

## T5：Hamilton碰撞

不对心碰撞中：

- 最大相对能量漂移：
  \[
  2.81e-14;
  \]
- 总线动量漂移：
  \[
  2.22e-16;
  \]
- 总角动量漂移：
  \[
  3.29e-14;
  \]
- 时间反演总状态误差：
  \[
  1.74e-13.
  \]

状态：

\[
[\mathrm{NUMERICAL\ —\ T5\ PASSED}]
\]

## T6：正碰与不对心碰撞区分

圆形正碰的最大内部转矩：

\[
8.82e-16.
\]

不对心椭圆碰撞后：

\[
L_1=0.057788,
\qquad
L_2=0.270701.
\]

内部自旋明显产生，同时总角动量守恒。

状态：

\[
[\mathrm{NUMERICAL\ —\ T6\ PASSED}]
\]

## T7：有限碰撞区间与散射分类

不对心碰撞的归一化最大重叠：

\[
\rho_{12}^{\rm max}
=
0.036048.
\]

取：

\[
\rho_c=10^{-3},
\]

得到有限碰撞持续时间：

\[
\tau_c=2.800.
\]

末态：

\[
\rho_{12}(t_f)
=
1.11e-58,
\]

且末态径向分离速度为正，因此分类为：

\[
\boxed{
\text{labeled scattering}.
}
\]

状态：

\[
[\mathrm{NUMERICAL\ —\ T7\ PASSED}]
\]

---

# 13. 本阶段真正完成的桥

\[
\boxed{
\chi(\mathbf x)
\rightarrow
Q,\ A(q),\ B
\rightarrow
U_{\rm overlap}
\rightarrow
\mathbf F,\boldsymbol\tau
\rightarrow
\Sigma^{\rm pair}
}
\]

并且：

\[
\boxed{
\text{平动}
+
\text{轨道角动量}
+
\text{内部自旋}
}
\]

在有限碰撞全过程中闭账。

这一步使R0.3的张量响应不再完全悬浮于抽象内部变量之上。

---

# 14. 仍未完成

1. 当前形态固定，没有真正的压缩和恢复坐标；
2. 没有动态 \(S_{-1}\)场，只用了其边界重叠能的有效表达；
3. 没有无标签总相场，所以不能测试融合和重构；
4. 没有三维任意轴四元数碰撞；
5. 没有多体碰撞和粘度统计；
6. 没有由应力相关函数计算 \(\eta_{ijmn}(k,\omega)\)；
7. 没有恢复流体力学。

---

# 15. 下一道门

下一阶段应冻结为：

\[
\boxed{
\text{EP-R0.5：可形变相场边界、压缩记忆与融合判据}
}
\]

只解决：

1. 给每个 \(S_0\)加入可逆形变坐标；
2. 让碰撞压缩改变 \(A_i(t)\)和转动惯量；
3. 检验：
   \[
   E_{\rm translation}
   \leftrightarrow
   E_{\rm shape}
   \leftrightarrow
   E_{\rm spin};
   \]
4. 建立单一无标签相场的连通分量判据；
5. 区分散射、临时融合、永久融合和重构；
6. 测量碰撞持续时间与压缩松弛时间；
7. 检验快速靠近是否产生动态排斥增强。
