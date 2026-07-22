# EP-R0.6：单一无标签相场的分裂—融合动力学

版本：`V0.1`

## 0. 科学状态

\[
\boxed{
[\mathrm{DERIVED\ IN\ THE\ SINGLE\text{-}FIELD\ CQ\text{-}NLS\ MODEL}]
+
[EXPLORATORY NUMERICAL — ALL FROZEN GATES PASSED]
+
[\mathrm{FINITE\text{-}N\ EP\ ORIGIN\ OPEN}]
}
\]

这一阶段真正删除了R0.5动力学中的对象标签：

\[
(\chi_1,\chi_2)
\longrightarrow
\psi(\mathbf x,t).
\]

现在只有一个定义在整个空间上的复场。所谓“对象”不再是预先编号的粒子，而是从密度超水平集的连通分量中临时提取出来。

本阶段完成的是：

- 单场Hamilton动力学；
- 连通分量自然融合和分裂；
- 场范数、能量、线动量和角动量账本；
- 时间反演；
- 入射两分量—单分量—出射两分量的无标签过程；
- 线性波叠加与非线性拓扑变化的严格区分。

尚未完成：

- 从有限 \(N\) EP递归碰撞推出该场方程；
- 四元数内部自旋；
- 三维场中的完整边界取向；
- 真实光束、物质粒子或现实流体的参数对应；
- 多体动理学和Navier–Stokes极限。

本包中的参数和密度阈值经过探索性选择后冻结，因此不是独立确认性预注册。

---

# 1. 单一无标签复相场

取：

\[
\boxed{
\psi(\mathbf x,t)\in\mathbb C,
\qquad
\rho(\mathbf x,t)=|\psi|^2.
}
\]

动力学为二维聚焦三次—散焦五次非线性Schrödinger场：

\[
\boxed{
i\partial_t\psi
=
-\frac12\nabla^2\psi
-g|\psi|^2\psi
+h|\psi|^4\psi.
}
\]

本次数值使用：

\[
g=2,
\qquad
h=1.
\]

三次项允许局域聚集，五次项在高密度时提供饱和排斥，避免无限压缩。

它是一个最小的“吸引—高密度排斥”单场模型，但目前只是：

\[
[\mathrm{POSTULATE\ R0.6}],
\]

不是从EP底层碰撞推导出的最终场方程。

---

# 2. 作用量与Hamilton量

作用量：

\[
\boxed{
\mathcal S
=
\int dt\,d^2x
\left[
\frac{i}{2}
(\psi^*\partial_t\psi-\psi\partial_t\psi^*)
-
\frac12|\nabla\psi|^2
+
\frac g2|\psi|^4
-
\frac h3|\psi|^6
\right].
}
\]

Hamilton量：

\[
\boxed{
H
=
\int d^2x
\left[
\frac12|\nabla\psi|^2
-
\frac g2|\psi|^4
+
\frac h3|\psi|^6
\right].
}
\]

完整场方程没有基本粘性项，也没有对象之间的人工碰撞规则。

---

# 3. Noether账本

全局相位对称：

\[
\psi\mapsto e^{i\alpha}\psi
\]

给出范数：

\[
\boxed{
N=\int|\psi|^2d^2x.
}
\]

空间平移给出：

\[
\boxed{
\mathbf P
=
\int
\operatorname{Im}
(\psi^*\nabla\psi)
\,d^2x.
}
\]

平面旋转给出：

\[
\boxed{
L_z
=
\int
\operatorname{Im}
\left[
\psi^*
(x\partial_y-y\partial_x)\psi
\right]
d^2x.
}
\]

时间平移给出 \(H\)守恒。

时间反演：

\[
\boxed{
\psi(\mathbf x,t)
\mapsto
\psi^*(\mathbf x,-t).
}
\]

---

# 4. 数值账本

融合—分裂案例中：

\[
\frac{\Delta N}{N}
=
2.251e-12,
\]

\[
\frac{\Delta H}{|H(0)|}
=
2.366e-05,
\]

\[
\Delta|\mathbf P|
=
3.815e-05.
\]

时间反演相对误差：

\[
\boxed{
\varepsilon_{\rm rev}
=
1.111e-12.
}
\]

在扩大计算区域的非中心入射测试中：

\[
L_z(0)
=
11.920962,
\]

角动量相对漂移：

\[
\boxed{
\frac{\Delta L_z}{|L_z(0)|}
=
2.676e-06.
}
\]

方形周期网格只近似保持连续旋转对称，因此角动量数值精度低于范数和线动量；连续场理论中的角动量守恒来自精确旋转对称性。

---

# 5. 对象不再是动力学标签

固定密度阈值：

\[
\rho_c=0.20.
\]

定义超水平集：

\[
\Omega_{\rho_c}(t)
=
\{\mathbf x:\rho(\mathbf x,t)\ge\rho_c\}.
\]

对象数量定义为：

\[
\boxed{
N_c(t)
=
\#\operatorname{Conn}
\Omega_{\rho_c}(t).
}
\]

每个连通分量 \(C_a(t)\)可以临时提取：

\[
N_a
=
\int_{C_a}\rho\,d^2x,
\]

\[
\mathbf X_a
=
\frac1{N_a}
\int_{C_a}\mathbf x\rho\,d^2x,
\]

\[
\mathbf P_a
=
\int_{C_a}
\operatorname{Im}(\psi^*\nabla\psi)
d^2x,
\]

以及二阶形态矩和主轴方向。

这些量是从场中测量出来的，不是方程预先携带的“粒子编号”。

---

# 6. 三种相遇结果

## 6.1 持续融合候选

同相位、较慢入射：

\[
\Delta\varphi=0,
\qquad
v=0.40.
\]

连通分量序列：

\[
\boxed{
[2, 1].
}
\]

初态：

\[
N_c(0)=2,
\]

末态：

\[
N_c(t_f)=1.
\]

在当前观测窗中，它被分类为：

\[
\boxed{
\text{persistent fusion candidate}.
}
\]

这不等于证明永久稳定，因为更长时间仍可能再次分裂。

## 6.2 融合后分裂

相位差：

\[
\Delta\varphi=\frac{\pi}{2},
\qquad
v=0.80.
\]

连通序列：

\[
\boxed{
[2, 1, 2, 1, 2].
}
\]

该冻结案例的完整序列为：

\[
2\rightarrow1\rightarrow2\rightarrow1\rightarrow2.
\]

其中包含两次单连通阶段，末态回到两个分量。

单连通区间持续：

\[
\boxed{
\tau_{1{\rm comp}}
=
2.200000.
}
\]

这是本阶段第一次由**单一动力学场自身**产生的融合—分裂过程，而不是把两个带标签边界相加后做几何诊断。

## 6.3 相位阻断

相位差：

\[
\Delta\varphi=\pi,
\qquad
v=0.80.
\]

连通序列：

\[
\boxed{
[2].
}
\]

整个观测区间保持两个高密度分量。

因此在当前模型中：

\[
\boxed{
\text{相同密度包的拓扑结果取决于相对相位。}
}
\]

---

# 7. 分裂后的输出结构

融合—分裂案例的两个入射分量进入单一连通分量后，组件编号不再存在。

末态重新出现两个连通分量，其超水平质量比：

\[
\boxed{
R_N
=
3.570581.
}
\]

两个出射分量的动量差：

\[
\boxed{
\Delta P_{\rm out}
=
10.343827.
}
\]

这表明出射结构并不是简单复制两个完全相同的入射超水平分量。

但必须准确区分：

\[
\boxed{
\text{分量标签不能连续延拓}
\neq
\text{完整场信息被删除}.
}
\]

完整复场动力学仍然可逆，信息保存在振幅、相位和辐射尾部中。当前结论只是：

> 在单连通区间内，基于连通分量的“对象1/对象2”标签没有规范唯一的连续延拓。

---

# 8. 线性波叠加控制

令：

\[
g=h=0.
\]

方程变成线性Schrödinger场。

分别演化两个入射包后相加，与直接演化两包之和进行比较，得到：

\[
\boxed{
\varepsilon_{\rm superposition}
=
4.665e-16.
}
\]

这验证：

\[
U(t)(\psi_1+\psi_2)
=
U(t)\psi_1+U(t)\psi_2.
\]

因此：

- 线性波相遇首先是叠加；
- 当前融合—分裂和相位敏感拓扑来自非线性场项；
- 不能把普通线性光束相遇直接解释为强碰撞重构。

---

# 9. 与两束光问题的关系

R0.6给出的严格区分是：

\[
\boxed{
\text{线性传播模式}
\rightarrow
\text{叠加后继续传播},
}
\]

而：

\[
\boxed{
\text{具有足够非线性的局域场结构}
\rightarrow
\text{可能融合、分裂或相位阻断}.
}
\]

所以“两束光相遇会不会散开重组”不能只凭场是连续的就回答“会”。

必须先证明现实光学通道中存在足够强的非线性，并确定其响应尺度。R0.6只说明这种机制在一个单场Hamilton模型中数学上可以发生。

---

# 10. 本阶段完成的桥

\[
\boxed{
(\chi_1,\chi_2)
\longrightarrow
\psi(\mathbf x,t)
\longrightarrow
\rho=|\psi|^2
\longrightarrow
N_c(t).
}
\]

并建立：

\[
\boxed{
2\rightarrow1,
\qquad
2\rightarrow1\rightarrow2,
\qquad
2\rightarrow2
}
\]

三种由相位和速度控制的拓扑分支。

最重要的进展是：

\[
\boxed{
\text{对象由场的连通结构涌现，}
\quad
\text{而不是预先写入动力学。}
}
\]

---

# 11. 当前限制

1. 场方程是最小三次—五次模型，不是EP有限 \(N\)推导结果；
2. 复相位不等于已经推导出的量子相位；
3. 当前只有标量复场，没有四元数内部自旋；
4. 超水平阈值经过探索性选择；
5. “持续融合”只在有限观测时间内成立；
6. 分量标签失效不等于完整场信息消失；
7. 没有三维拓扑、涡线和任意轴取向；
8. 没有多体动理学、粘性谱和流体极限。

---

# 12. 下一道门

下一阶段应冻结为：

\[
\boxed{
\text{EP-R0.7：单场连通结构的散射映射与统计闭合}
}
\]

任务包括：

1. 对速度、相位、冲量参数做冻结扫描；
2. 建立：
   \[
   \text{融合、分裂、穿越、反弹、碎裂}
   \]
   的相图；
3. 从单场自动提取入射和出射分量的质量、动量、形态和相位；
4. 定义无标签散射映射；
5. 统计多次事件得到碰撞持续时间和应力脉冲分布；
6. 判断这些统计是否产生R0.1—R0.3中的记忆核与Ohmic谱；
7. 开始连接：
   \[
   \text{单场碰撞统计}
   \rightarrow
   \widehat\eta(k,\omega).
   \]
