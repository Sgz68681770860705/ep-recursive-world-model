# EP-R0.1：可逆背景响应与广义粘性基础

版本：`V0.1`

状态：

\[
\boxed{
[\mathrm{DERIVED\ IN\ THE\ MINIMAL\ LINEAR\ MODEL}]
+
[\mathrm{NUMERICAL\ BENCHMARK\ PASSED}]
+
[\mathrm{MICROSCOPIC\ EP\ ORIGIN\ OPEN}]
}
\]

## 本包解决的问题

本包冻结EP新路线的第一项基础工作：

\[
S_0+S_{-1}\text{可逆总系统}
\rightarrow
\text{消去 }S_{-1}
\rightarrow
\text{因果记忆核}
\rightarrow
\widehat\eta(k,\omega)
\rightarrow
\text{单慢模正向—逆向闭环}.
\]

它没有证明真实流体、引力或基本粒子来自该模型，也没有完成有限 \(N\) EP碰撞到该谱密度的推导。

## 已完成

- T1：最小总Hamilton系统能量有下界、守恒且时间可逆；
- T2：消去背景振子连续谱后，约化运动出现因果记忆核；
- T3：一个Drude型背景谱给出有限、被动、频率—波数依赖的广义粘度；
- T4：在单极点模型类别内，可从合成的 \(\widehat\eta(k,\omega)\) 数据反演慢模参数。

## 核心公式

\[
\widehat\eta(k,\omega)
=
\eta_\infty+
\frac{\Delta\eta}
{1+\xi^2k^2-i\omega\tau}.
\]

其中：

- \(\eta_\infty\)：未解析快速通道的高频背景值；
- \(\Delta\eta\)：当前慢模的低频粘度增量；
- \(\tau\)：慢模松弛时间；
- \(\xi\)：慢模空间相关长度。

普通粘度为：

\[
\eta_0=\widehat\eta(0,0)=\eta_\infty+\Delta\eta.
\]

## 文件

- `docs/EP-R0.1-REVERSIBLE-BACKGROUND-RESPONSE.zh-CN.md`：主理论文档；
- `docs/THEOREMS-AND-PROOFS.zh-CN.md`：T1—T4定理与证明；
- `docs/EP-R0.1-REVERSIBLE-BACKGROUND-RESPONSE.md`：英文摘要；
- `code/run_r0_1_benchmark.py`：可重复数值基准；
- `results/benchmark_results.json`：数值结果；
- `results/inverse_fit.csv`：反演参数；
- `figures/`：核逼近、能量守恒和反演图；
- `PRE_REGISTRATION.json`：预注册门槛；
- `STATUS.md`：结论与开放项。

## 运行

```bash
python code/run_r0_1_benchmark.py
```

建议Git提交说明：

```text
theory: add EP-R0.1 reversible background response and generalized viscosity
```
