# EP-R0.5：可形变相场边界、压缩记忆与融合判据

版本：`V0.1`

状态：

\[
\boxed{
[\mathrm{DERIVED\ IN\ THE\ CANONICAL\ LOG\text{-}SHAPE\ MODEL}]
+
[EXPLORATORY NUMERICAL — ALL FROZEN GATES PASSED]
+
[\mathrm{IDENTITY\ RECONSTRUCTION\ OPEN}]
}
\]

## 核心链条

\[
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
\text{平动—形变—自旋交换}.
\]

无标签几何诊断：

\[
\chi_U=1-(1-\chi_1)(1-\chi_2).
\]

冻结阈值下，本次事件得到：

\[
2\rightarrow1\rightarrow2,
\]

即临时几何融合后标记散射。

## 重要限制

连通阈值和记忆阈值经过探索性校准后冻结，所以这是可重复探索性基准，不是独立确认性检验。动力学仍保留两个对象身份，不能证明真实身份重构。

## 文件

- `docs/EP-R0.5-DEFORMABLE-BOUNDARY-COMPRESSION-FUSION.zh-CN.md`
- `docs/THEOREMS-AND-PROOFS.zh-CN.md`
- `docs/EP-R0.5-DEFORMABLE-BOUNDARY-COMPRESSION-FUSION.md`
- `code/run_r0_5_benchmark.py`
- `results/benchmark_results.json`
- `results/deformable_collision_timeseries.csv`
- `figures/`
- `PROTOCOL_FREEZE.json`
- `STATUS.md`

## 运行

```bash
python code/run_r0_5_benchmark.py
```

建议Git提交：

```text
theory: add EP-R0.5 deformable boundary and fusion diagnostics
```
