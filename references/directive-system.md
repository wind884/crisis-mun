# Directive system

## 接收

区分 public / private / secret / joint；子类型 diplomatic、economic、military、intelligence、domestic policy、media。私密仅限指定收件人与执行链，不等于绝不会泄露。Joint 必须列每方授权和资源贡献，不能替未同意的 AI 签名。

“准备一份/我想”默认草稿；“提交/命令/请转交”表示模拟内发送，但仍须检查权限。自然语言足够明确时转换成指令并给回执，不要求用户填表。缺目标、执行方或关键授权时只补必要项。

```text
ID / type / classification / author_actor / committee / submitted_at
objective / action_scope / recipient_authority / executing_actors
authorization_evidence / resources_requested / resources_reserved
start_window / duration_estimate / prerequisites / abort_conditions
report_to / exposure_assessment / status / stages / linked_events
```

## 裁决与状态

逐项检查 Authority、Capability、Resources、Time、Information、Opposition、Exposure Risk、Consequences。玩家可见裁决只含其已知的原因与范围，不暴露未知对手部署来解释失败。

状态：DRAFT → SUBMITTED → REJECTED / NEEDS_AUTHORIZATION / DELAYED / APPROVED / PARTIALLY_APPROVED → EXECUTING → COMPLETED / PARTIAL_FAILURE / FAILED / CANCELLED。

APPROVED 只表示允许执行，不表示成功。被部分批准的每个分项单独记 status、resource reservation、due_at；禁止用一个总成功覆盖被拒部分。相同 ID 重发不创建第二次执行。变更订单用 revision 与新授权，撤销只影响尚未发生阶段；已消耗资源不返还。

回执：

```text
DIRECTIVE STATUS · SD-RUS-004
NEEDS_AUTHORIZATION
Accepted component: private diplomatic contact with Belgrade.
Military component: referred to national authority; no movement ordered.
Next review: estimated 30–60 simulation minutes, subject to response.
Known exposure: diplomatic transmission only; military exposure not yet applicable.
```

这是模拟处理估计，不是史实速度。若玩家仅为常驻代表，不能把其“秘密调兵”自动改成国家已命令调兵；可以在其意图内转交请求，国家是否同意需独立裁决。外交部分可单独进行。

秘密行动与情报发现使用不同事件 ID。玩家不得因发出命令就收到对方真实探测能力、隐蔽反制或未知来源名单。
