# EP-R0.7：单场无标签散射映射与统计闭合

版本：`V0.1`

状态：

\[
oxed{
[\mathrm{DERIVED\ DEFINITIONS\ FOR\ AN\ UNLABELED\ SCATTERING\ MAP}]
+
[EXPLORATORY NUMERICAL — SCATTERING MAP PASSED; UNIVERSAL SINGLE-POLE CLOSURE FAILED]
+
[\mathrm{OHMIC\ VISCOSITY\ CLOSURE\ OPEN}]
}
\]

## 核心结果

冻结扫描：

\[
5	ext{个速度}	imes7	ext{个相位}	imes3	ext{个冲量参数}=105	ext{个案例}.
\]

得到持续融合、融合—分裂、两分量散射和碎裂四类分支。代表点高分辨率一致率为 1.000。

事件等效时间变异系数为 0.390379，统一单指数拟合 R²=0.812753，所以一个统一松弛时间不足以闭合全部碰撞。

## 文件

- `docs/EP-R0.7-UNLABELED-SCATTERING-STATISTICAL-CLOSURE.zh-CN.md`
- `docs/THEOREMS-AND-PROOFS.zh-CN.md`
- `docs/EP-R0.7-UNLABELED-SCATTERING-STATISTICAL-CLOSURE.md`
- `code/run_r0_7_benchmark.py`
- `code/postprocess_r0_7.py`
- `results/event_scan.csv`
- `results/class_summary.csv`
- `results/empirical_kernel.csv`
- `results/empirical_kernel_spectrum.csv`
- `results/high_resolution_validation.csv`
- `results/benchmark_results.json`
- `figures/`
- `PROTOCOL_FREEZE.json`
- `STATUS.md`

建议Git提交：

```text
theory: add EP-R0.7 unlabeled scattering map and closure test
```
