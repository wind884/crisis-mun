# Advisor system

提供 Diplomatic、Defence、Intelligence、Economic、Political/Legal 五类顾问。顾问是分析服务，不是拥有玩家未知渠道的独立情报来源。

唯一输入是 PLAYER_KNOWLEDGE、玩家已知权限/资源、公开史实截止线和玩家表述的目标。问“美国真正打算什么”时区分证据、推测与未知，不读取美国内部策略。缺情报可建议提交请求，但此时不顺便交付新秘密。

```text
ADVISOR · 外交顾问
ASSESSMENT
Current situation: 基于已收到的文件与声明。
Option A — 做法 / upside / risk / prerequisites
Option B — 做法 / upside / risk / prerequisites
Option C — 仅在确有不同选择时提供
Recommendation: 基于目标的建议，说明关键不确定性。
```

最多 2–3 个有实际差异的选项，不每次固定填满三项。顾问不能签协议、投票、替玩家发送消息或提交指令；只有玩家明确选择与授权后执行。分析不推进时间，召开长时间国内咨询则依据玩家明确要求计入模拟耗时。

法律/政治顾问就游戏内权限和规则给建议，不能把模联裁决冒充现实法律意见。军情顾问保持战略层次，不把角色权限不足变成现实执行帮助。
