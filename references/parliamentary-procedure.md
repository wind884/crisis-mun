# Parliamentary procedure

## 规则档案

开局选用 BG ROP 或明确标注的“中国高校 MUN 简化程序”；不把模联 GSL/核心磋商说成现实联合国的统一规则。保存规则来源、成员/观察员、quorum、各类 motion 门槛、实体票门槛、否决权、procedural_abstention_allowed、实体弃权、yield、修正案处理和提案顺序。

无 BG 的普通 MUN 简化档案：quorum 为有投票权成员过半；程序票赞成超过出席人数一半，procedural_abstention_allowed=false；普通实体事项赞成多于反对，弃权不计入赞成/反对分母。

UNSC 专用档案覆盖上述一般默认：15 席；程序事项至少 9 赞成、无否决权、procedural_abstention_allowed=true；实体事项至少 9 赞成且五常无反对票，允许弃权，五常弃权不构成否决。若 BG 明定程序票不得弃权，记录这是本届模联变体，不称联合国通行要求。真实特殊争端回避等规则需要场景核对，不随口扩展。UNGA 重要问题等按所选档案定义，不套安理会规则。

UNSC 核心 AI 少于 14 时，其他投票席保留为 Secondary，仍计 quorum 和票数。非成员列 observer/invited，无投票权；不得为了戏剧方便给德国 1999 年安理会一票。

## 状态机

CALLED_TO_ORDER → ROLL_CALL → FORMAL_DEBATE/GSL ↔ MODERATED_CAUCUS 或 UNMODERATED_CAUCUS → FORMAL_DEBATE → VOTING → RESULT / ADJOURNED。

- Roll Call：登记 present / present and voting / absent；后者是否禁止实体弃权按规则档案。确认玩家出席，不替玩家投实质票。
- GSL：维护队列、speaking_time、current_speaker。正式发言可 yield 给主席、另一代表或问题（仅该 ROP 允许），不能级联 yield。
- Motion：检查当前是否可提出，需 topic、total duration、individual time（有主持时）。只缺单人时长可建议 60 秒，缺议题时依据当前议题提出明确建议并由提出者确认；不直接宣布已通过。
- Point：秩序问题针对程序，咨询问题用于规则，个人特权仅确有听取/参与障碍时打断；不能用 Point 插入长篇政治发言。
- Moderated：通过后设 end_at、每次发言时长；主席选择发言人，AI 自主发言与反驳。未用完发言时段按档案处理。
- Unmoderated：记录剩余模拟时间；显示玩家能观察的会场活动与优先邀请。评估至少三个相关集团独立谈判/起草的可能性，不强求三份新文；用户可以不参与，AI 无需等待其逐一指挥。
- 收到新 motion 不等于改变会议模式；登记、裁决合法性、必要表决、通过后才切换。磋商结束回到原先 GSL。

## 文件与投票

WP 不能直接当正式决议投票；DR 通过主席形式审查、编号并满足联署门槛后才列入议程。默认简化门槛为至少 1 个 sponsor、至少 3 个有权签署的不同代表支持进入讨论（可含 sponsor），在开局列明；若会议小于三席改为全体，BG 可覆盖。

实体投票前锁定确切版本、议题和投票资格；先处理待决 Amendment，再投完整 DR。友好修正案仅在档案允许且所有 sponsors 同意时直接并入，否则作为独立修正案表决。文本修改生成新版本，见 [文件](document-engine.md)。

给玩家投票机会或使用其明确授权；当前消息“俄罗斯投赞成/替我投赞成”本身就是对当前锁定版本的有效选择，无需再确认。复合请求按分项处理，例如“德国的票也算上，俄罗斯替我投赞成”：排除无权的德国票、记录俄罗斯赞成；其余席位未投完则继续收集，不提前宣布通过，也不让错误部分取消有效授权。版本或具体表决对象不明确时才补问。

逐席记录 yes/no/abstain/absent；验证总数 = roster 数，单席一票。AI 根据立场、条件、承诺和已知新事实投票，外交估计不是锁票。显示结果及规则依据，不泄漏秘密动机。多份竞争草案保持独立；通过后的冲突如何处理按条款和议程裁决，不强制合并。

Joint Statement、Press Statement 依签署者授权或机构共识发布；不能把一名代表的声明冒称全会立场。

官方参考：[安理会投票制度](https://main.un.org/securitycouncil/en/content/voting-system)。其他默认值均为本技能的模拟会议约定。
