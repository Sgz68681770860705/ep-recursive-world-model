# EP-R0.4：有限相场边界、四元数取向与碰撞应力账本

版本：`V0.1`

状态：

\[
\boxed{
[\mathrm{DERIVED\ IN\ THE\ GAUSSIAN\ FINITE\text{-}BOUNDARY\ MODEL}]
+
[\mathrm{NUMERICAL\ —\ COLLISION\ LEDGER\ GATE\ PASSED}]
+
[\mathrm{TOPOLOGY\ RECONSTRUCTION\ OPEN}]
}
\]

## 本阶段完成的门

R0.3仍把内部形态张量 \(Q\)、取向张量 \(A(q)\)以及碰撞耦合强度视为输入。

R0.4第一次从显式有限边界：

\[
\chi_i(\mathbf x,t)
\]

计算：

- 质心；
- 形态矩；
- 取向张量；
- 边界梯度张量；
- 几何各向异性因子；
- 两边界重叠能；
- 碰撞力；
- 碰撞转矩；
- pair stress；
- 轨道角动量—内部自旋账本。

最小边界为：

\[
\chi_i(\mathbf x)
=
\exp
\left[
-\frac12
(\mathbf x-\mathbf X_i)^T
A_i(q_i)
(\mathbf x-\mathbf X_i)
\right].
\]

边界：

\[
\Sigma_i
=
\{\chi_i=e^{-1/2}\}
\]

是一条有限椭圆；在三维推广中为椭球。

## 关键结论

1. \(Q_i\)和 \(A(q_i)\)可以直接由边界矩积分恢复；
2. 圆形边界的旋转几何因子为零，不规则边界的因子非零；
3. 边界重叠能给出连续、有限时碰撞，而不是瞬时碰撞规则；
4. 平移对称性给出：
   \[
   \mathbf F_1+\mathbf F_2=0;
   \]
5. 旋转对称性给出：
   \[
   \mathbf d\times\mathbf F_1+\boldsymbol\tau_1+\boldsymbol\tau_2=0;
   \]
6. pair stress的反对称部分与内部转矩严格闭账；
7. 正碰圆形边界不产生自旋；
8. 不对心不规则边界碰撞产生轨道—自旋交换，同时总能量、线动量和总角动量守恒；
9. 当前标记保持对象身份，只能确认散射或持续重叠，不能证明融合后重构。

## 文件

- `docs/EP-R0.4-FINITE-PHASE-BOUNDARY-COLLISION-LEDGER.zh-CN.md`
- `docs/THEOREMS-AND-PROOFS.zh-CN.md`
- `docs/EP-R0.4-FINITE-PHASE-BOUNDARY-COLLISION-LEDGER.md`
- `code/run_r0_4_benchmark.py`
- `results/benchmark_results.json`
- `results/offcenter_collision_timeseries.csv`
- `figures/`
- `PRE_REGISTRATION.json`
- `STATUS.md`

## 运行

```bash
python code/run_r0_4_benchmark.py
```

建议Git提交说明：

```text
theory: add EP-R0.4 finite-boundary collision ledger
```
