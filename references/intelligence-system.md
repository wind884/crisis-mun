# Intelligence system

## 采集到判断

维护 request_id、question、tasking_authority、collection_channel、capacity、start、collection_due、analysis_due、delivery_due、recipient、report_id。只有所处年代和国家合理拥有的能力才能使用；不能在历史场景凭空使用现代网络/卫星技术。

先后独立判断：有没有采集到信号 → 能否辨识主体 → 有哪些可能意图 → 来源是否可信 → 分析何时送达。采集失败、部分结果、过时/错误信息和欺骗都允许；不为制造悬念任意反转。

`known_information` 是收过的报告，不是真实性保证；`suspected_information` 是推测；`misinformation` 的错误属性不得自动暴露给该角色。

```text
INTELLIGENCE BRIEF · I-RUS-003
CLASSIFICATION: SECRET
Simulation time: 24 MAR 1999 · 21:20 UTC+01:00
Source: allied liaison report
Reliability: B
Confidence: MEDIUM
Observed: increased activity reported at an unspecified staging facility.
Assessment: mobilisation is possible; scale and intent remain uncertain.
Limitations: second-hand reporting; no independent confirmation.
```

上例为格式示例，不是既定事件。Reliability A–F 为本会约定：A 一贯可靠、B 通常可靠、C 有时可靠、D 通常不可靠、E 不可靠、F 无法评估。Confidence 是该判断证据强度，二者不能混用。

玩家索取现有情报：按已送达记录回答，不推进时间。新情报请求：检查权限和采集资源，登记预计时窗；返回“请求已登记”而非立即交付对方完整战略。分享情报需独立投递，限定报告版本、收件人和保密条件。

新闻匿名引述不等于该来源真实身份；不能把安全机构的秘密身份写入玩家未知报告。报告出错后用新报告纠正，保留原报告与旧时间；角色此前基于错误信息作出的行为不自动撤销。
