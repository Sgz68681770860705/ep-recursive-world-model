# EP-R0.7：单场无标签散射映射与统计闭合

版本：`V0.1`

## 0. 科学状态

\[
\boxed{
[\mathrm{DERIVED\ DEFINITIONS\ FOR\ AN\ UNLABELED\ SCATTERING\ MAP}]
+
[EXPLORATORY NUMERICAL — SCATTERING MAP PASSED; UNIVERSAL SINGLE-POLE CLOSURE FAILED]
+
[\mathrm{OHMIC\ VISCOSITY\ CLOSURE\ OPEN}]
}
\]

本阶段不再只挑选少数代表性碰撞，而是在冻结参数网格上系统扫描单场事件，并回答两个问题：

1. 单场连通结构能否形成稳定、可重复的无标签散射相图；
2. 全部事件能否被一个统一的单松弛时间记忆核描述。

结论是：

\[
\boxed{
\text{散射映射门通过，统一单极点闭合门失败。}
}
\]

这个负结果是重要进展：它说明从R0.6的单场碰撞返回R0.1的广义粘性时，不能把全部拓扑分支压缩成同一个常数 \(\tau\)。

---

# 1. 无标签入射—出射散射映射

固定密度阈值：

\[
\rho_c=0.20.
\]

对象定义为超水平集的连通分量：

\[
C_a(t)\in\operatorname{Conn}\{\rho(\mathbf x,t)\ge\rho_c\}.
\]

每个分量提取：

\[
\mathcal Z_a
=
(N_a,\mathbf X_a,\mathbf P_a,Q_a,\bar\varphi_a),
\]

其中：

\[
N_a=\int_{C_a}\rho\,d^2x,
\qquad
\mathbf X_a=\frac1{N_a}\int_{C_a}\mathbf x\rho\,d^2x,
\]

\[
\mathbf P_a
=
\int_{C_a}\operatorname{Im}(\psi^*\nabla\psi)d^2x.
\]

二阶矩给出形态和取向，分量平均相位定义为：

\[
\bar\varphi_a
=
\arg\int_{C_a}\psi\rho\,d^2x.
\]

入射和出射状态都必须视为无序多重集：

\[
\mathcal I=\{\mathcal Z_a^{\rm in}\}/S_{N_{\rm in}},
\qquad
\mathcal O=\{\mathcal Z_b^{\rm out}\}/S_{N_{\rm out}}.
\]

因此散射映射定义为：

\[
\boxed{
\mathfrak S_T:
\mathcal I
\longrightarrow
(\mathcal O,\mathcal C,\tau_{\rm act},I_\Sigma).
}
\]

这里 \(\mathcal C\) 是事件类别；\(\tau_{\rm act}\) 是应力活动持续时间；\(I_\Sigma\) 是应力活动脉冲。

---

# 2. 冻结扫描

扫描参数为：

\[
v\in\{0.35,0.55,0.75,0.95,1.15\},
\]

\[
\Delta\varphi/\pi
\in
\left\{0,\frac16,\frac13,\frac12,\frac23,\frac56,1\right\},
\]

\[
b\in\{0,0.8,1.6\}.
\]

总案例数：

\[
\boxed{N_{\rm scan}=105.}
\]

得到四个主要分支：

- 持续融合候选：`33`例；
- 融合—分裂散射：`40`例；
- 两分量散射或相位阻断：`22`例；
- 末态碎裂：`10`例。

事件分类只使用连通分量数 \(N_c(t)\)：

\[
N_c(0)=2,\quad N_c(t_f)=1
\]

定义为持续融合候选；

\[
\min_tN_c(t)=1,\quad N_c(t_f)=2
\]

定义为融合—分裂散射；

若整个观测序列保持两个分量，则归为两分量散射；若末态有三个或更多分量，则归为碎裂。

---

# 3. 分辨率稳健性

选取8个代表点，覆盖持续融合、融合—分裂、两分量散射、碎裂以及不同冲量参数。

粗网格与更高分辨率的分类一致率：

\[
\boxed{R_{\rm resolution}=1.000.}
\]

冻结门槛为：

\[
R_{\rm resolution}\ge0.875.
\]

因此代表点稳健性门通过。

这并不等于整个相图边界已经收敛。真正的临界线仍需要在类别变化附近自适应加密。

---

# 4. 守恒和时间反演

高分辨率代表案例使用：

\[
N=192,\quad L=50,\quad \Delta t=0.003,
\quad t_f=15.
\]

数值结果：

\[
\frac{\Delta N}{N}=2.251e-12,
\]

\[
\frac{\Delta H}{|H(0)|}=2.366e-05,
\]

\[
\Delta|\mathbf P|=3.815e-05,
\]

时间反演相对误差：

\[
\boxed{\varepsilon_{\rm rev}=4.441e-12.}
\]

所以统计相图来自同一可逆、近守恒的单场动力学，而不是人为改写碰撞结果。

---

# 5. 各向异性应力活动指标

定义全局梯度应力的对角差和剪切分量：

\[
\Sigma_N(t)
=
\int
\left(|\partial_x\psi|^2-|\partial_y\psi|^2\right)d^2x,
\]

\[
\Sigma_{xy}(t)
=
\int
\operatorname{Re}(\partial_x\psi^*\partial_y\psi)d^2x.
\]

减去入射基线后，定义：

\[
\boxed{
A_\Sigma(t)
=
\sqrt{[\Delta\Sigma_N(t)]^2+4[\Delta\Sigma_{xy}(t)]^2}.
}
\]

这个量是全局各向异性Noether应力活动指标。它不是完整局域Cauchy应力，也不是现实流体中已经测得的压力。

进一步定义：

\[
\tau_{\rm act}
=
\int\mathbf1_{A_\Sigma>0.1A_{\max}}dt,
\]

\[
I_\Sigma=\int A_\Sigma(t)dt,
\]

\[
\boxed{
\tau_{\rm eq}=\frac{I_\Sigma}{A_{\max}}.
}
\]

\(\tau_{\rm eq}\) 等于具有相同面积和峰值的矩形脉冲宽度，因此不依赖额外持续时间阈值。

---

# 6. 不同拓扑类别具有不同时间尺度

全部事件：

\[
\langle\tau_{\rm eq}\rangle=4.303256,
\]

\[
\sigma_\tau=1.679899,
\]

\[
\boxed{\mathrm{CV}(\tau_{\rm eq})=0.390379.}
\]

分类平均值：

- 碎裂：`6.635528`；
- 融合—分裂：`4.899143`；
- 持续融合候选：`3.482321`；
- 两分量散射：`3.391103`。

因此：

\[
\boxed{
\tau_c=\tau_c(v,\Delta\varphi,b,\mathcal C),
}
\]

不能在当前事件族中直接压缩成一个与事件类别无关的常数。

---

# 7. 从事件构造经验记忆包络

对每个事件，把应力活动峰值时刻对齐为 \(t=0\)，并归一化：

\[
k_a(t)
=
\frac{A_{\Sigma,a}(t_a^*+t)}{A_{\Sigma,a}^{\max}}.
\]

定义经验包络：

\[
\boxed{
K_{\rm env}(t)=\langle k_a(t)\rangle_a.
}
\]

其冻结时间窗内的零频面积为：

\[
\int K_{\rm env}(t)dt=4.018815.
\]

这建立了第一条从单场碰撞统计返回记忆响应的链：

\[
\boxed{
\text{单场事件}
\rightarrow
A_{\Sigma,a}(t)
\rightarrow
K_{\rm env}(t).
}
\]

但必须保持边界：\(K_{\rm env}\) 是峰值对齐的正活动包络，不是平衡态Green–Kubo相关函数，不能直接称为粘度核。

---

# 8. 统一单极点闭合失败

检验：

\[
K_1(t)=Ae^{-t/\tau_1}.
\]

拟合结果：

\[
A=1.010600,
\qquad
\tau_1=10.721967,
\]

\[
\boxed{R^2=0.812753.}
\]

冻结门槛：

\[
R^2\ge0.90,
\qquad
\mathrm{CV}(\tau_{\rm eq})\le0.30.
\]

实际结果没有同时满足，因此：

\[
\boxed{
[\mathrm{FAILED\ AS\ A\ UNIVERSAL\ SINGLE\text{-}POLE\ CLOSURE}].
}
\]

这说明R0.1中的单慢模表达式：

\[
\widehat\eta
=
\eta_\infty+
\frac{\Delta\eta}{1+\xi^2k^2-i\omega\tau}
\]

可以作为单类事件或单慢模的基准，但不能直接承载R0.7全部散射分支。

---

# 9. 正确的新闭合方向

最小修正是类别条件混合：

\[
\boxed{
K(t)=\sum_{\mathcal C}p_{\mathcal C}K_{\mathcal C}(t).
}
\]

其中：

\[
p_{\mathcal C}=P(\mathcal C|v,\Delta\varphi,b).
\]

更一般地：

\[
K(t)
=
\int d\tau\,dI\,
P(\tau,I,\mathcal C)
K(t|\tau,I,\mathcal C).
\]

因此宏观响应中的多极点或连续谱，可能来自：

\[
\boxed{
\text{不同碰撞拓扑}
+
\text{不同持续时间}
+
\text{不同应力脉冲}
}
\]

的统计混合，而不只是一个内部振子。

---

# 10. 本阶段完成的桥

\[
\boxed{
(v,\Delta\varphi,b)
\rightarrow
\mathcal C
\rightarrow
(\tau_{\rm act},I_\Sigma,\tau_{\rm eq})
\rightarrow
K_{\rm env}(t).
}
\]

这是第一次从R0.6的单场融合—分裂事件，向R0.1—R0.3的记忆响应方向返回。

同时得到明确否定：

\[
\boxed{
\text{全部事件}
\not\rightarrow
\text{一个统一单松弛时间}.
}
\]

---

# 11. 当前限制

1. 扫描是探索性冻结，不是独立确认；
2. 相图临界边界尚未自适应加密；
3. 应力活动量是全局各向异性代理，不是完整局域应力；
4. 经验包络不是Green–Kubo核；
5. 没有稳态事件发生率，因此不能给出绝对粘度；
6. 没有波数 \(k\) 分辨的应力相关；
7. 没有多事件平衡浴；
8. 没有有限 \(N\) EP来源和Navier–Stokes极限。

---

# 12. 下一道门

下一阶段冻结为：

\[
\boxed{
\text{EP-R0.8：类别条件记忆核与稳态多事件响应}
}
\]

任务：

1. 按事件类别分别计算 \(K_{\mathcal C}(t)\)；
2. 在冻结分布下生成连续多事件序列；
3. 构造平稳应力时间序列；
4. 计算Green–Kubo型相关 \(C_\Sigma(t)\)；
5. 得到频率响应 \(\widehat\eta(\omega)\)；
6. 检验类别混合是否产生多极点或连续谱；
7. 判断低频极限是否为有限、正的Ohmic响应。
