# Actor system

## 身份与粒度

默认 10–15 核心 AI；用户席位另计。Core 完整维护，Secondary 保存身份、归属、可观察立场和最近事实，相关时再提升。核心数量不是投票席位数量：小预算仍须保留完整法定成员表；次要席位投票前激活并形成独立判断。多个委员会中的同一国家不是共享全部知识的单一大脑，按职位/机构建立独立 actor_id 与授权通信。

每个主要角色采用以下字段（缺失标 unknown；场景合成偏好标 simulated，不冒称真实内心）：

```yaml
actor:
  id: CHN-UN
  name: Chinese delegation
  type: national_representative
  country: China
  position: Permanent Representative
  committee: UNSC
  tier: core
  public_position: Respect sovereignty; seek de-escalation
  strategic_objectives: [Preserve diplomatic autonomy]
  short_term_objectives: [Review ceasefire language]
  red_lines: [Automatic use-of-force authorization]
  preferred_outcomes: [Negotiated settlement]
  unacceptable_outcomes: [Uncontrolled escalation]
  allies: []
  rivals: []
  relationship_map: {}
  political_constraints: [National instructions]
  military_constraints: [No direct operational command]
  economic_constraints: [No independent budget allocation]
  known_information: []
  suspected_information: []
  misinformation: []
  current_strategy: Seek a narrowly framed diplomatic text
  negotiation_history: []
  promises_given: []
  promises_received: []
  personality: Reserved and attentive to wording
  diplomatic_style: Principle first, qualified commitments
  risk_tolerance: low
  trust_toward_player: untested
  credibility_assessment: no_evidence_yet
  authority: {can: [negotiate], cannot_directly: [deploy_forces], can_request: [national_authorization]}
  demeanor_state: {trust: neutral, frustration: low, fear: low, confidence: medium, respect: neutral, suspicion: low}
  last_activated: null
  next_review_at: null
```

对象字段记录可维护的结论、承诺与事实，不记录或输出思维链。政治立场来源于 BG/基线；策略与人格是情境化模拟，不把国籍当成固定性格。

## 独立行动

行动输入仅为该角色知识、资源、权限、长期目标和当前义务。具体选择可以拒绝、索价、拖延、有限欺骗、退谈、另组联盟、联署、提出动议、提交指令。欺骗用“角色提出的未证实主张”与世界事实分开维护。

每项承诺记 counterpart、terms、due、conditions、evidence、status。用户违约且对方得知后，调整分享情报、要求担保、条款与投票倾向；不要给玩家机械信任分。反之 AI 违约也要同等承担代价；不是只有玩家会被惩罚。

三种风格应能区分：法律措辞型关注授权和条文；交易型要求对等让步；联盟协调型先争取伙伴。风格不能让角色忽略自身利益，也不要每国每轮都发表一句相同的“呼吁克制”。
