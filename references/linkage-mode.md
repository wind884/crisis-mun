# Crisis linkage mode

多个委员会共享一个 MASTER_WORLD_STATE 和世界时钟；各委员会保存不同 LOCAL_KNOWLEDGE_STATE、成员、权限和议程状态。用户只控制一个席位，国内内阁仍由 AI 独立裁决，不能因“我当俄罗斯”获得所有俄罗斯机构控制权。

委员会结构示例：A UNSC、B NATO North Atlantic Council、C Russian Security Council、D FR Yugoslav Government、E Media Centre。Media Centre 是传播层，可以无投票职能；不必伪造为正式联合国机关。联动关闭则只保留主委员会与必要外部行为，不开多会场视图。

## 每一条边都有机制

```text
link_event:
  id / cause_ids / origin_committee / originating_actor
  world_effect / occurred_at
  channel / source / recipients / earliest_receipt
  confidence / classification / shared_content
  destination_committee / response_event / status
```

传播需要发出者有权限、有理由、具备渠道；接收端收到后依据自己的目标回应。允许拒绝、保留、只分享删节报告、误解或延迟。无渠道则没有联动知识。

条件性案例：俄罗斯内阁授权秘密调动 → 准备完成后出现可观察运输活动 → 美国具备的侦察渠道采集 → 分析报告送达 → 美国选择向北约分享 → 北约讨论并可能公开声明 → 安理会代表获得公开声明 → 媒体引用声明。每个箭头独立事件、时间和接收范围，不能一轮把秘密原文广播世界。

联动影响不局限于消息：一个委员会批准制裁会改变共享经济状态和其他政府可用资源；某内阁拒绝通行会阻断军事执行；公众消息影响安理会谈判。因果效果与其何时被知晓分开。

去重：一个世界事实只创建一次；传播是新 receipt 而非再次执行。对 source_event + destination + report_version 建唯一关联，防止 A→B→A 回声重复扣资源或无穷触发。跨会场相同文件 ID 要加委员会 namespace。

对玩家只展示已知委员会概况，不显示“俄内阁正在秘密开会”除非玩家被告知。联动不是允许用户自由切换扮演所有角色；想换席位应另存可知分支、明确视角重置。
