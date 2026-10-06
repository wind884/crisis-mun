# Document engine

## 对象与不可变版本

每份文件持续维护以下字段，不以聊天摘要替代全文：

```text
document_id（如 UNSC:DR-1） / display_id（DR-1.2） / type / title / committee
created_at / last_modified_at / authors / sponsors / signatories
status / version / parent_document / visibility / recipients
content（完整逐条正文） / amendments / negotiation_history
version_history（每版完整正文、时间、编辑者、变更说明）
support_estimates（各 actor 的已知/未知立场，不默认对玩家可见）
```

ID 规则：`WP-1.1` 是 WP 家族 1 的第 1 版；`DR-1.2` 是 DR 家族 1 第 2 版，不是第二份竞争草案。不同家族为 DR-2.1。委员会有独立 namespace；同 ID 跨会查询时带 `UNSC:`。A-01、JD-02、SD-RUS-04、AG-03 使用单独序列且不复用。

修改创建新版本与逐条 diff，不覆盖旧版。每次分发记具体 version；收过 DR-1.1 的人不自动获得 DR-1.2。既有签署适用于原版；实质改变须再次征求支持，不静默继承。WP 升为 DR 创建新家族，parent_document 指向原 WP；合并保留双方来源，不能删除竞争文本。

## 生命周期与权利

draft → circulating → submitted → accepted_for_debate → voting → adopted / rejected。
draft/circulating/submitted 可 withdrawn；旧版 superseded，历史投票文本 frozen。协议另用 negotiating / signed / pending_ratification / in_force / breached / terminated / expired。指令执行状态见 [指令](directive-system.md)。

玩家可编辑自己的草稿、提交有权作者的新版本；对他国草案提出 Amendment 或另立提案，不能替作者发布修订。不知道全文时先请求获取，禁止回填“原文”。作者/签署者名单的增删必须有其同意或撤回证据。玩家一句“把条款改掉”不改已通过的决议；需新的合法修正程序。

SUPPORTED / LIKELY_SUPPORT / UNDECIDED / LIKELY_OPPOSE / OPPOSE 是内部评估，带证据与时间；玩家只看到其外交获得的估计。Sponsor ≠ signatory ≠ guaranteed yes vote。

## 支持的文件

WP、DR、Amendment；Joint Statement、Communiqué、Press Release、Diplomatic Note；Public/Private/Secret/Joint Directive；Intelligence Request、Policy Order、Military Order、Economic Order；Treaty、Protocol、Memorandum of Understanding、Ceasefire Agreement、Security Guarantee、Secret Protocol、Informal Political Understanding。共享基础字段，各类型添加期限、生效、授权、保密和执行字段，不能只给名词不给对象。

## 展示与操作

Formal：机构与标题、ID/版本/时间、sponsors/signatories、preambulatory clauses、编号 operative clauses、附件、状态。正式外交文书少表情；模拟草案不得伪称真实联合国公文。

Compact：ID、作者/主旨、关键条款、状态；全文仍保留，用户可随时展开。Ask each time 只问新文/打开文时的显示偏好，不改变文件内容。

“打开 DR-1.2”可跟随修改、发给指定国家、请求支持、加/删条款、提修正案、合并、提交、撤回。每次回执包括 exact ID、状态和分发对象。对猜出的未知 ID 不确认其存在；回复当前可访问档案中无该文件。

档案分 WP / DR / Amendment / Agreement / Directive，私密文件只有玩家为合法收件人时列出。知道标题未得全文显示“已知标题，尚未收到全文”；不能通过索引泄漏未知文件。保存与恢复须携带所有已知版本的全文，不能只保留 current_version 编号。
