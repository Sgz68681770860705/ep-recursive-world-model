# EP-R0.5：可形变相场边界、压缩记忆与融合判据

版本：`V0.1`

## 0. 科学状态

\[
\boxed{
[\mathrm{DERIVED\ IN\ THE\ CANONICAL\ LOG\text{-}SHAPE\ MODEL}]
+
[EXPLORATORY NUMERICAL — ALL FROZEN GATES PASSED]
+
[\mathrm{IDENTITY\ RECONSTRUCTION\ OPEN}]
}
\]

本阶段把R0.4中的固定有限边界推进为具有规范形态坐标的可逆可形变边界，并完成：

\[
\text{平动}
\leftrightarrow
\text{边界重叠}
\leftrightarrow
\text{形变}
\leftrightarrow
\text{自旋}
\]

的Hamilton能量和角动量账本。

本包中的连通阈值和形态记忆阈值经过探索性校准后冻结，因此属于**可重复的探索性基准**，不是独立确认性预注册结果。

它没有证明：

- 真实物质边界一定服从高斯椭圆模型；
- 两个对象的身份会真实消失并重建；
- 形变振荡已经热化为不可逆粘性；
- 三维完整四元数碰撞和多体流体极限已经完成。

---

# 1. 正定形态坐标

对第 \(i\) 个 \(S_0\)，定义：

\[
\boldsymbol\beta_i
=
(\beta_{ia},\beta_{ib}).
\]

半主轴为：

\[
\boxed{
a_i=a_{i0}e^{\beta_{ia}},
\qquad
b_i=b_{i0}e^{\beta_{ib}}.
}
\]

只要初始半轴为正，对任意有限实数 \(\beta\)：

\[
a_i>0,\qquad b_i>0.
\]

因此：

\[
A_i
=
R(q_i)
\operatorname{diag}(a_i^{-2},b_i^{-2})
R(q_i)^T
\]

始终正定。

随机形态测试中的最小半轴为：

\[
\boxed{
a_{\min}^{\rm random}
=
0.347839.
}
\]

碰撞全过程中的最小半轴为：

\[
\boxed{
a_{\min}^{\rm collision}
=
0.534804.
}
\]

所以这套坐标不会数值穿过“负尺寸”。

---

# 2. 可逆形变Hamilton量

形态共轭动量记为：

\[
\boldsymbol\pi_i.
\]

形态能为：

\[
\boxed{
H_{\rm shape}
=
\sum_i
\frac{|\boldsymbol\pi_i|^2}{2M_\beta}
+
\frac{K_s}{2}
\sum_i|\boldsymbol\beta_i|^2
+
\frac{K_A}{2}
\sum_i(\beta_{ia}+\beta_{ib})^2.
}
\]

其中：

- \(M_\beta\)：形态惯性；
- \(K_s\)：主轴恢复刚度；
- \(K_A\)：面积变化惩罚。

瞬时转动惯量由当前边界决定：

\[
\boxed{
I_i(\boldsymbol\beta_i)
=
m_i(a_i^2+b_i^2).
}
\]

完整Hamilton量：

\[
\boxed{
H
=
\sum_i
\left[
\frac{|\mathbf p_i|^2}{2m_i}
+
\frac{L_i^2}{2I_i(\boldsymbol\beta_i)}
+
\frac{|\boldsymbol\pi_i|^2}{2M_\beta}
+
V_s(\boldsymbol\beta_i)
\right]
+
U_{12}.
}
\]

形态方程：

\[
\dot{\boldsymbol\beta}_i
=
\frac{\boldsymbol\pi_i}{M_\beta},
\]

\[
\dot{\boldsymbol\pi}_i
=
-
\frac{\partial H}{\partial\boldsymbol\beta_i}.
\]

右侧同时包含：

- 弹性恢复；
- 边界重叠压缩；
- 转动惯量变化带来的形态—自旋交换。

重叠能对形态坐标的复步长梯度，与中心差分的最大相对误差：

\[
\boxed{
\varepsilon_{\nabla_\beta U}
=
1.594e-10.
}
\]

---

# 3. 形态—自旋耦合

由于：

\[
I=m(a^2+b^2),
\qquad
T_R=\frac{L^2}{2I},
\]

有：

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

所以碰撞期间不是只有：

\[
E_{\rm translation}
\leftrightarrow
E_{\rm shape},
\]

而是：

\[
\boxed{
E_{\rm translation}
\leftrightarrow
E_{\rm overlap}
\leftrightarrow
E_{\rm shape}
\leftrightarrow
E_{\rm spin}.
}
\]

本次数值中：

\[
E_{\rm shape}^{\max}
=
0.138909,
\]

\[
E_{\rm rotation}^{\max}
=
0.366704,
\]

\[
U_{\rm overlap}^{\max}
=
0.594607,
\]

内部自旋交换幅度：

\[
\boxed{
\Delta L_{\max}
=
0.715070.
}
\]

---

# 4. 守恒账本

总线动量：

\[
\mathbf P
=
\mathbf p_1+\mathbf p_2.
\]

总角动量：

\[
J
=
\mathbf X_1\times\mathbf p_1
+
\mathbf X_2\times\mathbf p_2
+
L_1+L_2.
\]

数值结果：

\[
\frac{\Delta E}{E}
=
1.835e-15,
\]

\[
\Delta P
=
0.000e+00,
\]

\[
\Delta J
=
2.010e-14,
\]

时间反演总状态误差：

\[
\boxed{
\varepsilon_{\rm rev}
=
1.340e-13.
}
\]

因此形态自由度没有破坏R0.4已经建立的平移和旋转Noether账本。

---

# 5. 压缩记忆

碰撞归一化重叠阈值取：

\[
\rho_c=10^{-3}.
\]

碰撞区间：

\[
t_{\rm in}
=
0.777857,
\qquad
t_{\rm out}
=
2.680714,
\]

持续时间：

\[
\boxed{
\tau_c
=
1.902857.
}
\]

定义形态能：

\[
E_\beta
=
E_{\beta,\rm kin}
+
E_{\beta,\rm elastic}.
\]

碰撞结束后，平均形态能占峰值：

\[
\boxed{
\frac{\langle E_\beta\rangle_{t>t_{\rm out}}}
{E_\beta^{\max}}
=
0.011883.
}
\]

冻结的记忆阈值为峰值的：

\[
0.5\%.
\]

在碰撞退出后，形态能高于该阈值的持续时间：

\[
\boxed{
\tau_{\rm memory}
=
6.319286.
}
\]

这说明碰撞历史进入了形态自由度。

但当前系统是Hamilton系统，所以这里表现为**可逆形态振荡**，不是不可逆热化。真正的松弛还需要与更低层连续背景耦合并粗粒化。

---

# 6. 快速靠近时的动态排斥增强

对相同圆形边界比较：

\[
v_{\rm slow}=0.65,
\qquad
v_{\rm fast}=1.30.
\]

峰值排斥力：

\[
F_{\rm slow}^{\max}
=
0.883709,
\]

\[
F_{\rm fast}^{\max}
=
2.739766.
\]

比值：

\[
\boxed{
\frac{F_{\rm fast}^{\max}}
{F_{\rm slow}^{\max}}
=
3.100304.
}
\]

峰值形态能：

\[
E_{\beta,\rm slow}^{\max}
=
0.090764,
\]

\[
E_{\beta,\rm fast}^{\max}
=
0.589335.
\]

比值：

\[
\boxed{
\frac{E_{\beta,\rm fast}^{\max}}
{E_{\beta,\rm slow}^{\max}}
=
6.493025.
}
\]

最大总压缩坐标分别为：

\[
C_{\rm slow}
=
0.042188,
\]

\[
C_{\rm fast}
=
0.110283.
\]

所以在当前参数窗口中，快速靠近使边界进入更深的动态压缩状态，产生更强的瞬时排斥和形态储能。

这是一项：

\[
[\mathrm{EXPLORATORY\ NUMERICAL}]
\]

结果，不应直接外推成所有尺度上的普遍力律。

---

# 7. 无标签总相场

为了不依赖“对象1”和“对象2”的命名顺序，定义：

\[
\boxed{
\chi_U
=
1-(1-\chi_1)(1-\chi_2).
}
\]

它满足：

\[
0\le\chi_U\le1
\]

并且交换：

\[
\chi_1\leftrightarrow\chi_2
\]

不改变结果。

冻结超水平阈值：

\[
\chi_c=0.10.
\]

定义：

\[
\Omega_U(t)
=
\{\mathbf x:\chi_U(\mathbf x,t)\ge\chi_c\}.
\]

连通分量数：

\[
N_c(t)
=
\#\operatorname{Conn}\Omega_U(t).
\]

本次数值中：

\[
N_c(0)
=
2,
\]

\[
\min_tN_c(t)
=
1,
\]

\[
N_c(t_f)
=
2.
\]

即：

\[
\boxed{
2\rightarrow1\rightarrow2.
}
\]

单连通阶段持续：

\[
\boxed{
\tau_{\rm geom}
=
1.497857.
}
\]

分类为：

\[
\boxed{
\texttt{temporary_geometric_fusion_then_scattering}.
}
\]

这可以称为“临时几何融合后散开”。

---

# 8. 为什么仍不能称为身份重构

虽然拓扑诊断使用无标签场：

\[
\chi_U,
\]

动力学变量仍然是两套：

\[
(\mathbf X_1,q_1,\beta_1),
\qquad
(\mathbf X_2,q_2,\beta_2).
\]

因此当前证明的是：

\[
\boxed{
\text{两个边界超水平集临时连接为一个连通区域。}
}
\]

它没有证明：

\[
S_0^{(1)}+S_0^{(2)}
\rightarrow
S_0^{(3)}+S_0^{(4)}
\]

中的对象身份消失、新生和重构。

两束光是否“碰撞散开重组”也必须使用同样的纪律：

- 线性背景波相遇可能只是叠加；
- 有边界结构可以发生几何连通；
- 真正重组必须出现无标签场中的新出射连通结构，并且不能再用原标签唯一追踪。

---

# 9. 最终散射

最大归一化重叠：

\[
\rho_{12}^{\max}
=
0.021584.
\]

末态重叠：

\[
\rho_{12}(t_f)
=
1.326e-38.
\]

末态径向分离速度：

\[
v_r(t_f)
=
1.808557>0.
\]

因此标记动力学分类为：

\[
\boxed{
\texttt{labeled_scattering}.
}
\]

也就是说，本次事件经历了：

\[
\boxed{
\text{两个几何分量}
\rightarrow
\text{一个临时连通分量}
\rightarrow
\text{两个分离出射对象}.
}
\]

---

# 10. 本阶段完成的桥

\[
\boxed{
\chi
\rightarrow
\beta
\rightarrow
A(\beta,q)
\rightarrow
I(\beta)
\rightarrow
U_{\rm overlap}
\rightarrow
F,\tau,\dot\pi_\beta.
}
\]

并建立：

\[
\boxed{
\text{边界重叠}
\rightarrow
\text{压缩储能}
\rightarrow
\text{碰撞后形态记忆}.
}
\]

同时建立：

\[
\boxed{
\chi_U
\rightarrow
N_c(t)
\rightarrow
\text{临时几何融合判据}.
}
\]

---

# 11. 当前限制

1. 形态只有两个全局主轴自由度；
2. 不能表示局部凹陷、褶皱和高阶边界波；
3. 形态记忆是可逆振荡，不是热化；
4. 动力学仍保留两个对象身份；
5. 拓扑阈值和记忆阈值是探索性校准后冻结；
6. 没有显式动态 \(S_{-1}\)场；
7. 没有三维任意轴四元数碰撞；
8. 没有多体统计、粘度计算和流体极限。

---

# 12. 下一道门

下一阶段应冻结为：

\[
\boxed{
\text{EP-R0.6：单一无标签相场的分裂—融合动力学}
}
\]

需要完成：

1. 从两套带标签边界改为单一场：
   \[
   \chi(\mathbf x,t);
   \]
2. 给相场加入共轭动量或等效可逆场变量；
3. 允许连通分量自然出生、合并、分裂和消失；
4. 从每个连通分量自动提取质心、形态、取向和自旋；
5. 检验融合前后总能量、线动量和角动量；
6. 区分波叠加、临时融合、持续融合和真正重构；
7. 检验两个入射结构能否产生不能由原标签唯一延拓的新出射结构。
