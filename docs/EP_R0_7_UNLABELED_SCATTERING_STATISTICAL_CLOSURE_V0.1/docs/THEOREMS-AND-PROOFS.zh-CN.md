# EP-R0.7：定义、命题与证明

## T1：无标签散射映射

固定阈值 \(\rho_c\)，对象定义为：

\[
\operatorname{Conn}\{\rho\ge\rho_c\}.
\]

入射和出射集合必须分别除以排列群：

\[
\mathcal I/S_{N_{\rm in}},
\qquad
\mathcal O/S_{N_{\rm out}}.
\]

因此散射映射不能依赖人为编号，只能依赖无序连通分量观测量。

## T2：事件分类的排列不变性

持续融合、融合—分裂、两分量散射和碎裂的定义只使用 \(N_c(t)\)及末态分量数。交换任意对象编号不改变这些量，所以事件类别是排列不变量。

## T3：各向异性梯度应力

对局域各向同性非线性 \(V(|\psi|^2)\)，局域势项只贡献各向同性部分。因此对角差和非对角分量可以用梯度项构造全局各向异性活动指标：

\[
\Sigma_N=\int(|\psi_x|^2-|\psi_y|^2)d^2x,
\]

\[
\Sigma_{xy}=\int\operatorname{Re}(\psi_x^*\psi_y)d^2x.
\]

它们不是完整局域应力，因此只能作为代理量。

## T4：等效事件时间

对非负活动量 \(A(t)\)：

\[
I=\int A(t)dt,
\qquad
A_{\max}=\max_tA(t),
\]

\[
\tau_{\rm eq}=I/A_{\max}.
\]

它等于具有同面积和同峰值的矩形脉冲宽度。

## T5：统一单时间尺度的必要统计条件

若全部事件由同一归一化核 \(K(t/\tau)\)控制，则：

\[
\tau_{{\rm eq},a}=\tau\int K(s)ds
\]

应在事件间近似常数。因此较大的 \(\mathrm{CV}(\tau_{\rm eq})\)反对统一单时间尺度闭合。该条件与较差单指数拟合同时出现时，可拒绝当前冻结的单极点模型。

## T6：类别混合核

若类别 \(\mathcal C\)以概率 \(p_{\mathcal C}\)出现，条件响应为 \(K_{\mathcal C}(t)\)，则全概率分解给出：

\[
K(t)=\sum_{\mathcal C}p_{\mathcal C}K_{\mathcal C}(t).
\]

Fourier变换后：

\[
\widehat K(\omega)=\sum_{\mathcal C}p_{\mathcal C}\widehat K_{\mathcal C}(\omega).
\]

即使每个条件核只有一个极点，不同 \(\tau_{\mathcal C}\)的混合也会产生多时间尺度响应。
