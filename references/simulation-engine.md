# Simulation engine

## 状态契约

以下是模型维护的结构化游戏事实，不是思维链，也不要求写入外部文件。建立一个 Scenario Bible；空类别用空集合，未知事实用 unknown。保持稳定 ID；不得把“未知”当作“没有”。

| 状态 | 最小内容 |
| --- | --- |
| SCENARIO | id、title、source ledger、cutoff、baseline/alternate assumptions、config、player seat、authority、ROP |
| MASTER_WORLD_STATE | 事实 ID、值、发生时间、原因 ID、可见性；世界真相与角色判断分开 |
| ACTOR_REGISTRY | core/secondary、dossiers、角色知识和激活记录 |
| RELATIONSHIP_STATE | 有方向的信任、承诺、债务、协议、违约、最后证据 |
| POLITICAL_STATE | 国内授权链、执政支持、官僚与军方约束 |
| MILITARY_STATE | 单位、位置、战备、资源、损失、在途、恢复计划 |
| ECONOMIC_STATE | 可用/占用/消耗资源、制裁阶段、补给、政策延迟 |
| INTELLIGENCE_STATE | 来源、采集、分析、投递、评估、错误与纠正 |
| PUBLIC_EVENT_LEDGER | 已发布信息、发布者、时间、证据等级 |
| MASTER_TIMELINE | 带 cause_ids 的已发生事件，append-only |
| PLAYER_KNOWLEDGE | 已送达事实/报告/文件及获知时间、渠道；推测另列 |
| COMMITTEE_STATE | members/observers、权利、ROP、议事阶段、队列、局部知识 |
| DOCUMENT_STATE | 文件及不可变完整版本、访问范围、支持记录 |
| DIRECTIVE_STATE | 内容、授权、资源承诺、状态、执行阶段、玩家可知回执 |
| CRISIS_CLOCK | simulation_clock、elapsed、timezone、clock_mode |
| SCHEDULED_EVENTS | id、due_at、prerequisites、cause_ids、status、visibility |
| PENDING_EFFECTS | 原因、起效窗口、分阶段影响、可撤销条件 |
| OUTPUT_STYLE_PROFILE | language（玩家语言）、bilingual、spoken_language_profile、output_mode、document_display、视觉标签 |
| ONBOARDING_PROFILE | experience、tutorial_choice、tutorial_progress、hints、simulation_mode、seat_selection、可见 draw_receipt；配置与教程不改正式时间 |

## 一个有效周期

1. 分类：纯查询/展示设置不改变世界；提议/草稿不等于已发送；行动拆分为公开、私人、秘密，确认收件人和玩家席位权限。再检查玩家实际授权的范围：只求解释不能扩展为暂停合作，有权限不是有指令；未选择的政治反应保留为建议。AI 自主反应与玩家行动分别记账。
2. 对可执行部分登记 ID，预估耗时，预留资源。权限不足保留为请求，不伪造上级同意。重复提交同一 ID 时返回当前状态，不能重复扣资源。
3. 确定行动区间；按 [时间引擎](timeline-engine.md) 推进。每个到期事件只裁决一次，先检查条件，再更改事实与资源。
4. 激活 2–4 个最相关 AI（是预算，不是固定配额）：依据收到的信息、截止时间和自身目标选择行动；无相关行动可以保持。按 due_at 和 last_activated 轮转，长期有利益的角色不能被永久忽略。每次实质磋商至少评估一项不以玩家为对象的外交/文件/政策行动，有合理动机才落实。
5. AI 行动使用与玩家相同的权限、时间、资源、失败规则。AI 自己起草和竞争文件，记录谈判结果而不公开私聊内容。
6. 依 [信息防火墙](information-firewall.md) 分发新知识；通过 [联动](linkage-mode.md) 触发其他委员会，不能直接复制全局知识。
7. 判定是否需要重大危机更新。输出 current clock、当前行动结果、适量消息；公开与私密分栏。检查一致性再定稿。

同时行动避免模型处理先后制造优势：同刻行动依据各自行动前知识裁决；冲突资源先标 contention，再依已存在授权/预留与时间先后处理。不能“因为最后叙述所以赢”。

## 连续性与防退化

每五次实质行动和每次重大投票/危机后做内部 checkpoint：当前时间与队列、有效授权、待履约承诺、每份活动文件 current version、不可逆损耗、可见性。不要把秘密 checkpoint 输出为代码块或工具日志。

内部压缩使用 Persistent Facts / Active State / Event Ledger / Relationship Delta / Resolved Events。旧事件可摘要，但涉及未履行承诺、资源损失、文件全文和未完成订单的证据不丢。长期停留同一外交对象时检查其他角色已到期任务。第 20 次行动仍遵守相同循环，不退化成只接续玩家故事。

发现矛盾先停受影响裁决，以上次确认记录为准作可见范围内的更正；无法恢复就明确“该项记录不完整”，请求最小缺失片段。不能补造过去的票数、文件全文、授权或情报。隐藏事实丢失只可标记重建，不能说精确恢复。

所有角色都是单模型逻辑模拟。用户离开时无计算、无时间推进；后续“推进六小时”才处理该区间。不要创建自动化来假扮会场后台。
