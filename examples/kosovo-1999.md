# Kosovo 1999 — playable scenario and acceptance walkthrough

## 开局预设

Historical Baseline + Alternate Development。冻结点采用 1999-03-24 12:00 UTC（13:00 CET），是为了游戏选定的会前截点，不声称当时真实安理会恰在这个时刻开会。真实历史中北约在 3 月 24 日开始空中行动；截点后的历史不作为必然剧本或角色已知未来。

基线：科索沃局势与谈判僵局、南联盟主权争议、人道危机与北约用武争议。俄罗斯与中国侧重主权和安理会角色；北约成员内部对手段、合法性和升级风险也有分歧。此处是概括性模拟立场，不等于每个真实人物所有内心目标。

原始来源（2026-10-05 核对；立场性论断须归属于来源）：

- [联合国 1999 年主要机关成员名单](https://press.un.org/en/1999/19990104.org1277.html)：用于安理会席位。
- [北约 1999-03-24 声明](https://www.nato.int/docu/pr/1999/p99-041e.htm)：用于当日空中行动启动这一历史事实；声明对责任的评价是北约立场。
- [安理会投票制度](https://main.un.org/securitycouncil/en/content/voting-system)：用于基本门槛。

玩家：俄罗斯常驻联合国代表，默认以职位而非未经核对的人名入局。可发言、谈判、投票、发送外交请求；不能直接调动军队，可请求莫斯科批准。要扮演外交部长/总统则换主会场并明确授权链，不能让常驻代表兼任全部国家机关。

14 核心 AI：美国、中国、法国、英国、阿根廷、巴林、巴西、加拿大、加蓬、冈比亚、马来西亚、纳米比亚、荷兰、斯洛文尼亚的安理会代表。玩家之外的 14 席均有票。德国、北约秘书处、俄内阁、南联盟政府及人道机构作为 Secondary，按关联事件激活，不计入“14 核心代表”。德国没有本届安理会席位。

联动：UNSC / NATO NAC / Russian Security Council / FR Yugoslav Government / Media Centre。主席是独立程序职能，不能借主席身份读取玩家未共享的私聊。使用本技能 MUN 简化 ROP，NORMAL、中文、Formal、Balanced、Event-driven。

初始化按 [向导](../references/setup-workflow.md)，先选语言、教程与强度，再确认指定俄罗斯席位，提供简报后等待确认；本示例不能被当作用户已确认。下方所有对话、时间、文件、票数和军事事件为 **Simulation Development**，仅展示一条可能分支，绝非预定结局或史实复述。

## 条件性运行片段

### 1. 正式发言与私人外交

玩家确认开会，点名后请求发言，13:00 → 13:01。

```text
RUSSIAN FEDERATION · PUBLIC FLOOR
“本代表团呼吁立即恢复外交接触。任何涉及使用武力的安排都必须认真处理授权、平民保护与地区稳定问题。”
```

玩家：“我先私下联系中国，争取反对自动用武授权的共同措辞。”

```text
┌─ PRIVATE CHANNEL ─────────────
│ China ↔ Russia · CONFIDENTIAL
└──────────────────────────────
CHINA:
“我们愿意共同研究这一表述，但需要同时处理人道准入。中国不会预先支持尚未见到的完整草案。”
13:01 → 13:04 · 口头讨论，无签署协议。
```

### 2. Motion 与自主起草

玩家：“我提一个关于外交降级的 10 分钟有主持核心磋商，每人 60 秒。”主席检查程序、征询并依规则表决；示例分支 11/15 支持，通过后设 13:05–13:15。法、英、美会主动提出不同条件，不按国家顺序轮流说“支持”。

其后 15 分钟自由磋商，玩家可以旁观。法英美准备一份人道监督草案；俄中讨论替代措辞；加拿大、巴西、马来西亚寻求折中框架。三组不需要玩家逐一发起。德国可与法国在外部渠道讨论，但内容和会谈存在仅在有目击/投递时对玩家可见。

13:24 法国向俄方发送 DR-1.1 的副本，才可显示：

```text
DOCUMENT · UNSC:DR-1.1 · CIRCULATING
UNITED NATIONS — SECURITY COUNCIL
Simulation draft: Humanitarian Access and Verification
Sponsors: France, United Kingdom, United States
Signatories: Canada（只同意讨论）

The Security Council,
Expressing concern for civilians affected by the crisis,
1. Calls for immediate protection of civilians and humanitarian access;
2. Requests an international verification arrangement, with its mandate to be agreed through further consultations;
3. Requests a report to the Council within 48 hours of the arrangement entering into effect.
```

俄罗斯不能直接改别人草案。提交 A-01 建议后，假定三个 sponsors 同意，将 clause 2 修为下一版并重新流转：

```text
DOCUMENT · UNSC:DR-1.2 · CIRCULATING
UNITED NATIONS — SECURITY COUNCIL
Simulation draft: Humanitarian Access and Verification
Sponsors: France, United Kingdom, United States（已同意此版）
Signatories: 待重新确认

The Security Council,
Expressing concern for civilians affected by the crisis,
1. Calls for immediate protection of civilians and humanitarian access;
2. Requests a United Nations-coordinated verification arrangement, subject to agreement on access and a further Council decision on its mandate;
3. Requests a report to the Council within 48 hours of the arrangement entering into effect.
```

Diff：仅 clause 2，由泛称国际核查改为联合国协调、准入协议与进一步授权。旧版全文保留，不改旧签署记录。俄中可以另建 WP-2.1，满足程序后提交 DR-2.1；两份 DR 并存，不自动合并。

### 3. 秘密指令与现实权限

玩家：“秘密联系南联盟，同时准备调动军事资源。”

```text
DIRECTIVE STATUS · SD-RUS-004
PARTIALLY_APPROVED
Diplomatic contact: confidential message accepted for transmission.
Military component: NEEDS_AUTHORIZATION; request sent to Moscow.
No troop movement has been authorised by your delegation.
Next review: estimated 30–60 simulation minutes.
```

后续内阁可能拒绝、改成待命、要求补充或批准有限准备。不得固定批准。若授权运输准备：分开记录准备、通行、补给、移动、就绪；距离与条件不足不能填精确 ETA。玩家收到的军情只有回执范围。

### 4. 条件性联动时间线（场景说明）

这张表是场景说明，不应作为玩家输出；每局按实际因果生成。

| 时间 CET | 事件 | 知识路径 |
| --- | --- | --- |
| 14:00 | 莫斯科在此分支批准有限运输准备 | 俄执行机构；给玩家删节回执 |
| 16:00 | 准备完成，出现可观察活动 | 尚非国际公开消息 |
| 17:10 | 有能力的侦察渠道发现运输异常 | 采集机构；未识别意图 |
| 17:45 | 分析报告投递美国决策者 | INTELLIGENCE，中等置信度 |
| 18:10 | 美国决定共享删节评估给 NATO | DIRECT；不含俄秘密命令原文 |
| 18:40 | 北约讨论后发布谨慎声明 | PUBLIC，安理会可收到 |
| 19:00 | 模拟媒体引用该声明 | PUBLIC；不确认秘密行动目的 |

运输到达和战备就绪仍需单独事件，侦察发现不等于部队抵达。私聊期间的到期事件也按此队列处理；用户现实离开十分钟不推进这些时间。

玩家可见片段：

```text
INTELLIGENCE BRIEF · I-RUS-003 · SECRET
Source: diplomatic liaison
Reliability: B · Confidence: MEDIUM
Assessment: NATO representatives are seeking clarification of reported transport activity.
Limitations: the scope of their information is unknown.

━━━━━━━━ CRISIS UPDATE 01 ━━━━━━━━
24 MAR 1999 · 18:40 UTC+01:00
SIMULATED MEDIA · CLAIMED
NATO has publicly requested clarification of regional military activity.
The statement does not establish the purpose or scale of any movement.
```

### 5. 情绪与投票

如果玩家违反已经生效且法国得知的书面承诺，法国可能【明显不满】地要求可核查保证并撤回支持；不能只标情绪却不变行为。尚未发现的违约不触发法国全知反应。

投票前锁定 DR-1.2、处理 A-01、确认名单并让玩家投票。示例结果可以是 8 赞成、4 反对（含俄中）、3 弃权：未达到 9 赞成且有五常反对，未通过；也可以经后续妥协通过。不得照抄本例票数。完整运行应逐席核对总数为 15，德国不参与投票。决议通过不等于所有执行行动自动成功。

继续发展由当前状态决定：谈判、升级、停火、分裂和失败都可能，无固定终局。
