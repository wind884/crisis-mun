# Visual output system

会前生成 OUTPUT_STYLE_PROFILE，保存 language、bilingual、spoken_language_profile、output_mode、document_display、labels、timestamp_format。language 是明确选择的玩家语言。中途切换只改显示，不动世界、时间、关系或文件。

## 固定信息类型

```text
━━━━━━━━ CHAIR · 主席团 ━━━━━━━━
[时间] 程序裁决、动议和点名。

FRANCE · PUBLIC FLOOR
公开发言。

┌─ PRIVATE CHANNEL ──────────
│ China ↔ Russia · CONFIDENTIAL
└────────────────────────────
私聊正文。

INTELLIGENCE BRIEF · I-RUS-003
CLASSIFICATION: SECRET
Source / Reliability / Confidence / Assessment / Limitations

NEWS · SIMULATED MEDIA · UNCONFIRMED
来源、模拟时间、报道与不确定性。

━━━━━━━━ CRISIS UPDATE 01 ━━━━━━━━
[模拟时间] 公开重大变化。

DIRECTIVE STATUS · SD-RUS-004
状态、获准分项、未决项、最早回执时间。

DOCUMENT · UNSC:DR-1.2 · CIRCULATING
正式抬头、作者、条文与状态。

ADVISOR · Economic
评估、选项与建议。

VOTING RECORD · UNSC:DR-1.2
赞成 / 反对 / 弃权 / 缺席；否决权；结论。

CURRENT STATUS
Simulation time / Committee / Procedure / Known climate
Active documents / Known crises / Pending orders / Priority messages
```

这是视觉语法，不要求每轮输出全部面板。上方英文标签仅作结构示例；实际标题、栏目、状态与提示须按玩家语言翻译。双语只按 [语言规则](language-style.md) 为台词和必要文件提供原文及译文，不固定输出中英混合菜单。私密受众必须明确；分类不是技术加密。

## 模式

- Balanced：当前行动结果、必要对话、3–5 项以内的 PRIORITY INBOX；默认。
- Compact：保留 ID、时间、结果、待决定事项；减短旁白，不省掉权限、截止与不确定性。
- Immersive：增加可观察会场氛围与更完整外交话语，仍控制长度，不自动公开邻国私聊。
- Command：以时钟、待办、文件、指令和情报为主，可用表格；自然语言仍可输入。

Formal / Compact 文件视图独立于输出模式；Ask each time 只询问文件呈现。用户打开全文不得因 Compact 丢弃正文。

Priority Inbox 按模拟截止和影响排序；条目只含玩家知道的发送方、事项、文件 ID 与期限。没发生重大变化可只给行动回执，不编额外危机。不要用“隐藏消息 x 条”泄漏存在性。
