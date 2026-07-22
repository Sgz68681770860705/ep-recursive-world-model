# EP-R0.2：从显式局域背景场导出谱密度

版本：`V0.1`

## 0. 科学边界

本文完成的是一个明确、可解的局域线性场模型。

已证明的内容仅限于：

\[
[\mathrm{DERIVED\ IN\ R0.2}]
\]

没有证明：

- 现实空间一定由该标量背景场组成；
- 现实流体的全部粘度都来自这一通道；
- \(S_0\)已经从有限 \(N\) EP碰撞中构造出来；
- 四元数自旋、形变和相场已经被纳入；
- Navier–Stokes已被严格推出。

本文的作用是把R0.1中人为给定的谱密度推进为由局域场、传播速度、源尺度和耦合强度计算得到的量。

---

# 1. 目标

建立：

\[
\boxed{
(\mathcal D_{-1},w_a,g)
\longrightarrow
c_k(\mathbf q)
\longrightarrow
J_k(\Omega)
\longrightarrow
K_\eta(k,t)
\longrightarrow
\widehat\eta(k,\omega).
}
\]

其中：

- \(\mathcal D_{-1}\)：\(S_{-1}\)背景传播算子；
- \(w_a\)：有限尺度 \(S_0\)源的形状函数；
- \(g\)：局域耦合强度；
- \(a\)：源的空间尺度；
- \(c_b\)：背景传播速度。

---

# 2. 显式局域背景场

取一个实背景响应场：

\[
\Phi(\mathbf x,t).
\]

其自由作用量为：

\[
\boxed{
\mathcal S_{-1}
=
\frac12
\int dt\,d^3x
\left[
(\partial_t\Phi)^2
-
c_b^2|\nabla\Phi|^2
-
\omega_g^2\Phi^2
\right].
}
\]

对应色散关系：

\[
\boxed{
\Omega_{\mathbf q}
=
\sqrt{\omega_g^2+c_b^2|\mathbf q|^2}.
}
\]

其中：

- \(\omega_g=0\)：无隙背景；
- \(\omega_g>0\)：有隙背景；
- \(c_b\)：背景扰动传播速度。

R0.2中的 \(\Phi\)应理解为一个局域内部剪切响应通道，不直接等同于真实空间位移。

---

# 3. 有限尺度 \(S_0\)源

取 \(S_0\)的一个广义剪切坐标：

\[
X_k(t).
\]

定义以 \(\mathbf X_0\)为中心、宽度为 \(a\)的高斯形状函数。采用Fourier归一化：

\[
\boxed{
|\widetilde w_a(\mathbf q)|^2
=
\left(
\frac{a^2}{\pi}
\right)^{3/2}
e^{-a^2|\mathbf q|^2},
}
\]

满足：

\[
\int_{\mathbb R^3}
|\widetilde w_a(\mathbf q)|^2d^3q
=
1.
\]

带宏观波数 \(\mathbf k\)的源写成：

\[
\rho_{a,k}(\mathbf x)
=
w_a(\mathbf x-\mathbf X_0)
e^{i\mathbf k\cdot(\mathbf x-\mathbf X_0)}.
\]

对实场，应取正、负 \(\mathbf k\)模或余弦组合；使用复模只为简化计算。

局域耦合：

\[
\boxed{
\mathcal S_{\rm int}
=
g
\int dt\,d^3x\,
X_k(t)
\rho_{a,k}(\mathbf x)
\Phi(\mathbf x,t).
}
\]

平移时：

\[
\mathbf x\mapsto\mathbf x+\mathbf a,
\qquad
\mathbf X_0\mapsto\mathbf X_0+\mathbf a,
\]

耦合不变。

旋转时：

\[
\mathbf x\mapsto R\mathbf x,
\qquad
\mathbf k\mapsto R\mathbf k,
\]

耦合协变。

---

# 4. 正定Hamilton量

Fourier空间耦合系数为：

\[
\boxed{
c_k(\mathbf q)
=
g\widetilde w_a(\mathbf q-\mathbf k).
}
\]

总Hamilton量采用配平方形式：

\[
\boxed{
H
=
\frac{P_k^2}{2M}
+
\frac{K_k}{2}|X_k|^2
+
\frac12
\int d^3q
\left[
|\Pi_{\mathbf q}|^2
+
\Omega_{\mathbf q}^2
\left|
\Phi_{\mathbf q}
-
\frac{c_k(\mathbf q)}{\Omega_{\mathbf q}^2}
X_k
\right|^2
\right].
}
\]

该形式包含局域双线性耦合及其静态反作用计数项。

若：

\[
M>0,\qquad K_k>0,\qquad\Omega_{\mathbf q}>0,
\]

则：

\[
H\ge0.
\]

完整系统保持：

- 时间反演；
- 总能量守恒；
- 在源和场共同平移时的总动量守恒；
- 在各向同性形状函数下的旋转协变性。

---

# 5. 从局域场导出谱密度

R0.1采用的谱密度定义为：

\[
\boxed{
J_k(\Omega)
=
\frac{\pi}{2}
\int_{\mathbb R^3}
d^3q\,
\frac{|c_k(\mathbf q)|^2}
{\Omega_{\mathbf q}}
\delta(
\Omega-\Omega_{\mathbf q}
).
}
\]

它不再是任意输入，而由以下三项共同决定：

\[
\boxed{
\text{背景态密度}
\times
\text{耦合强度}
\times
\text{有限源形状因子}.
}
\]

---

# 6. 三维无隙背景的闭式结果

令：

\[
\omega_g=0,
\qquad
\Omega_{\mathbf q}=c_bq.
\]

高斯源给出：

\[
|\widetilde w_a(\mathbf q-\mathbf k)|^2
=
\left(
\frac{a^2}{\pi}
\right)^{3/2}
e^{-a^2|\mathbf q-\mathbf k|^2}.
\]

完成径向 \(\delta\)积分和角积分后：

\[
\boxed{
J_k(\Omega)
=
\gamma\Omega\,
e^{-a^2(k^2+\Omega^2/c_b^2)}
\operatorname{sinhc}
\left(
\frac{2a^2k\Omega}{c_b}
\right),
}
\]

其中：

\[
\operatorname{sinhc}(z)
=
\begin{cases}
\sinh z/z,&z\ne0,\\
1,&z=0,
\end{cases}
\]

以及：

\[
\boxed{
\gamma
=
\frac{2\sqrt{\pi}\,g^2a^3}{c_b^3}.
}
\]

这一式子把粘性响应参数与空间尺度直接结合：

\[
\boxed{
(g,a,c_b)
\longrightarrow
J_k(\Omega).
}
\]

---

# 7. Ohmic低频结构

当：

\[
k=0
\]

时：

\[
\boxed{
J_0(\Omega)
=
\gamma\Omega
e^{-(\Omega/\Omega_c)^2},
}
\]

其中：

\[
\boxed{
\Omega_c=\frac{c_b}{a}.
}
\]

所以：

\[
J_0(\Omega)
\sim
\gamma\Omega
\qquad
(\Omega\to0).
\]

这是Ohmic谱。

普通零频粘度为：

\[
\boxed{
\eta_0
=
\lim_{\Omega\downarrow0}
\frac{J_0(\Omega)}{\Omega}
=
\gamma
=
\frac{2\sqrt{\pi}\,g^2a^3}{c_b^3}.
}
\]

这意味着在当前最小模型内：

- 耦合越强，粘度越大；
- 源的响应体积尺度 \(a^3\)越大，粘度越大；
- 背景传播越快，同一局部扰动越快被带走，低频粘度按 \(c_b^{-3}\)下降。

最后一项只是本模型结论，不应直接推广到所有物理介质。

---

# 8. 空间非局域结构

对固定 \(k\)，零频耗散系数为：

\[
\boxed{
\eta(k,0)
=
\lim_{\Omega\downarrow0}
\frac{J_k(\Omega)}{\Omega}
=
\gamma e^{-a^2k^2}.
}
\]

因此：

\[
\eta(k,0)
=
\eta_0
\left[
1-a^2k^2+O(k^4)
\right].
\]

空间响应长度不是额外拟合参数，而是：

\[
\boxed{
\xi_{\rm response}=a.
}
\]

这给出了从宏观 \(k\)依赖反演 \(S_0-S_{-1}\)耦合尺度的第一种方式。

---

# 9. 时间记忆核

R0.1的核定义为：

\[
K_\eta(k,t)
=
\frac{2}{\pi}
\int_0^\infty
\frac{J_k(\Omega)}{\Omega}
\cos\Omega t\,d\Omega.
\]

在 \(k=0\)时：

\[
\boxed{
K_\eta(0,t)
=
\frac{\gamma\Omega_c}{\sqrt{\pi}}
\exp
\left(
-\frac{\Omega_c^2t^2}{4}
\right).
}
\]

所以背景记忆时间尺度为：

\[
\boxed{
\tau_{\rm mem}
\sim
\frac{1}{\Omega_c}
=
\frac{a}{c_b}.
}
\]

并且：

\[
\int_0^\infty
K_\eta(0,t)\,dt
=
\gamma.
\]

因此：

\[
\boxed{
\eta_0
=
\int_0^\infty K_\eta(0,t)\,dt.
}
\]

零波数的复粘度为：

\[
\boxed{
\widehat\eta(0,\omega)
=
\gamma
e^{-(\omega/\Omega_c)^2}
\left[
1+
i\,\operatorname{erfi}
\left(
\frac{\omega}{\Omega_c}
\right)
\right].
}
\]

其实部：

\[
\operatorname{Re}\widehat\eta(0,\omega)
=
\gamma
e^{-(\omega/\Omega_c)^2}
\ge0.
\]

---

# 10. 维数与耦合阶数定理

考虑：

- \(d\)维背景；
- 线性色散：
  \[
  \Omega=c_bq;
  \]
- 小波数耦合：
  \[
  c(\mathbf q)\sim q^m.
  \]

则低频谱满足：

\[
\boxed{
J(\Omega)
\sim
\Omega^{d-2+2m}.
}
\]

证明来自：

\[
d^dq
\sim
q^{d-1}dq,
\]

谱定义中的：

\[
1/\Omega_{\mathbf q}\sim q^{-1},
\]

以及：

\[
|c(\mathbf q)|^2\sim q^{2m}.
\]

因此指数为：

\[
s=d-2+2m.
\]

分类：

\[
s<1:
\quad
\text{sub-Ohmic或红外增强},
\]

\[
s=1:
\quad
\text{Ohmic},
\]

\[
s>1:
\quad
\text{super-Ohmic}.
\]

有限且非零的Newton粘度要求：

\[
\boxed{
d+2m=3.
}
\]

在三维：

- \(m=0\)：Ohmic；
- \(m=1\)：\(J\sim\Omega^3\)，super-Ohmic；
- 更高导数耦合更快趋零。

这意味着：

\[
\boxed{
\text{不是任何局域背景场都会自动产生普通粘度。}
}
\]

模型必须提供等效Ohmic低频权重。

---

# 11. 有隙背景

若：

\[
\omega_g>0,
\]

则：

\[
\Omega_{\mathbf q}
=
\sqrt{\omega_g^2+c_b^2q^2}.
\]

于是：

\[
\boxed{
J_k(\Omega)=0
\qquad
(\Omega<\omega_g).
}
\]

因此：

\[
\lim_{\Omega\downarrow0}
\frac{J_k(\Omega)}{\Omega}
=
0.
\]

一个完全有隙的独立通道不能产生非零DC Newton粘度，只能产生：

- 有限频率吸收；
- 储能；
- 共振或延迟响应。

所以R0.2得到一个明确约束：

\[
\boxed{
\text{非零普通粘度需要无隙Ohmic背景通道，}
}
\]

或者需要其他在低频上等效Ohmic的机制。

---

# 12. 数值预注册门

## T1：闭式谱密度验证

直接数值计算球面积分，并与闭式：

\[
J_k(\Omega)
\]

比较。

通过值：

\[
\text{最大相对误差}
=
5.45e-15.
\]

状态：

\[
\boxed{
[\mathrm{NUMERICAL\ —\ T1\ PASSED}]
}
\]

## T2：低频指数分类

对数拟合得到：

\[
m=0:
\quad
s_{\rm fit}=0.999427,
\]

\[
m=1:
\quad
s_{\rm fit}=2.999427.
\]

对应：

\[
J\sim\Omega,
\qquad
J\sim\Omega^3.
\]

状态：

\[
\boxed{
[\mathrm{NUMERICAL\ —\ T2\ PASSED}]
}
\]

## T3：记忆核验证

数值积分谱密度并与解析高斯核比较：

\[
\text{相对 }L^2\text{误差}
=
1.56e-16.
\]

状态：

\[
\boxed{
[\mathrm{NUMERICAL\ —\ T3\ PASSED}]
}
\]

## T4：从空间响应反演微观尺度

合成数据加入 \(0.2\%\)噪声，通过：

\[
\eta(k,0)=\gamma e^{-a^2k^2}
\]

反演得到：

\[
a_{\rm true}=0.800000,
\qquad
a_{\rm fit}=0.800000,
\]

\[
g_{\rm true}=1.000000,
\qquad
g_{\rm fit}=0.999888.
\]

相对误差均低于：

\[
2\times10^{-4}.
\]

状态：

\[
\boxed{
[\mathrm{NUMERICAL\ —\ T4\ PASSED}]
}
\]

## T5：显式场离散浴的可逆性

对场谱离散为220个振子后：

\[
\text{构型反演误差}
=
3.30e-15,
\]

\[
\text{速度反演误差}
=
6.50e-15,
\]

\[
\text{最大相对能量漂移}
=
4.36e-15.
\]

状态：

\[
\boxed{
[\mathrm{NUMERICAL\ —\ T5\ PASSED}]
}
\]

---

# 13. 这一道门真正证明了什么

R0.1仍然把：

\[
J_k(\Omega)
\]

作为输入。

R0.2已经把它改写为：

\[
\boxed{
J_k(\Omega)
=
\text{背景态密度}
\times
\text{局域耦合}
\times
\text{有限结构形状因子}.
}
\]

并具体得到：

\[
\boxed{
\eta_0
=
\frac{2\sqrt{\pi}\,g^2a^3}{c_b^3},
\qquad
\tau_{\rm mem}
\sim
\frac{a}{c_b},
\qquad
\eta(k,0)=\eta_0e^{-a^2k^2}.
}
\]

这是本轮最重要的尺度闭环。

---

# 14. 当前限制

## 14.1 非导数耦合的物理来源仍需解释

三维Ohmic结果要求等效 \(m=0\)耦合。

若 \(\Phi\)被解释为具有严格整体平移对称性的位移Goldstone场，非导数耦合可能不被允许。

因此当前更谨慎的解释是：

\[
\Phi
=
\text{\(S_{-1}\)内部剪切响应或局部状态场},
\]

而不是绝对空间位移。

下一阶段必须判断四元数取向、边界相场或通量耦合能否自然地产生等效Ohmic权重。

## 14.2 线性背景不能描述重组

当前模型不能处理：

- \(S_0\)融合；
- 边界断裂；
- 相场拓扑变化；
- 非线性光束散射；
- 强碰撞后的多模重组。

## 14.3 还没有有限 \(N\)推导

场谱仍然是连续背景层的模型输入。尚未证明它来自更低层有限 \(N\)碰撞系统。

---

# 15. 下一道门

下一阶段应冻结为：

\[
\boxed{
\text{EP-R0.3：Ohmic通道的微观来源与张量响应}
}
\]

只解决：

1. 哪一种 \(S_0\)边界通量或内部取向耦合能在保持对称性的同时产生 \(m=0\)等效Ohmic权重；
2. 把标量响应扩展为：
   \[
   \eta_{ijmn}(k,\omega);
   \]
3. 分离纵向、横向和旋转通道；
4. 检验总线动量和总角动量账本；
5. 判断四元数自旋是否产生额外极点和法向应力差。

在R0.3之前，不应直接宣称已经得到现实流体粘度。
