# EP-R0.6：单一无标签相场的分裂—融合动力学

版本：`V0.1`

状态：

\[
\boxed{
[\mathrm{DERIVED\ IN\ THE\ SINGLE\text{-}FIELD\ CQ\text{-}NLS\ MODEL}]
+
[EXPLORATORY NUMERICAL — ALL FROZEN GATES PASSED]
+
[\mathrm{FINITE\text{-}N\ EP\ ORIGIN\ OPEN}]
}
\]

## 核心进展

动力学不再包含：

\[
S_0^{(1)},\qquad S_0^{(2)}
\]

这样的预设对象标签，而只有：

\[
\psi(\mathbf x,t).
\]

对象由：

\[
\operatorname{Conn}\{|\psi|^2\ge0.20\}
\]

临时提取。

冻结测试得到：

- 同相慢速：\(2\to1\)；
- 相位差 \(\pi/2\)：\(2\to1\to2\)；
- 相位差 \(\pi\)：\(2\to2\)。

线性控制满足严格叠加，说明融合—分裂来自非线性场动力学，而不是所有波相遇都会重组。

## 主要文件

- `docs/EP-R0.6-SINGLE-UNLABELED-FIELD-FUSION-FISSION.zh-CN.md`
- `docs/THEOREMS-AND-PROOFS.zh-CN.md`
- `docs/EP-R0.6-SINGLE-UNLABELED-FIELD-FUSION-FISSION.md`
- `code/run_r0_6_benchmark.py`
- `results/benchmark_results.json`
- `results/component_observables.json`
- `results/fusion_fission_timeseries.csv`
- `figures/`
- `PROTOCOL_FREEZE.json`
- `STATUS.md`

## 运行

```bash
python code/run_r0_6_benchmark.py
```

建议Git提交：

```text
theory: add EP-R0.6 single-field fusion-fission dynamics
```
