# CrisisMUN · 危机联动模联

**一个人，也能开一场模联。**

你扮演一个国家代表或内阁职位，其他代表、主席、危机中心和媒体由模型模拟。你可以发言、谈判、起草文件、投票、提交危机指令，也可能遇到反对、拖延或失败。不同委员会会通过消息与行动相互影响。

**Model United Nations, for one player.**

Take a country seat or a cabinet role. The model runs the other delegates, chair, crisis staff and media. Speak, negotiate, draft, vote and submit directives. Other actors have their own interests, and your plans can fail. Linked committees share a world through information and actions.

[中文使用说明](#中文使用说明) · [English guide](#english-guide)

## 下载 / Downloads

| 你想怎么用 / How you want to use it | 下载 / Download |
| --- | --- |
| 直接上传给聊天 AI，不用解压 / Upload to a chat without extracting files | [完整单文件 / All-in-one Markdown](downloads/CrisisMUN.md) |
| 安装为 Skill，或给能解压的 AI / Install as a skill, or use a chat that can extract ZIP | [完整技能包 / Skill ZIP](downloads/crisis-mun-1.1.1.zip) |

MD 和 ZIP 包含同一套游玩规则，选一个即可，不必重复上传。ZIP 不含开发测试、测试报告、缓存或聊天记录。随机分配默认在聊天内完成；附带抽签工具仅供主动要求严格抽签时使用。

The Markdown and ZIP editions contain the same playing rules. Choose one; there is no need to upload both. The ZIP excludes development tests, reports, caches and chat logs. Random assignment happens in the chat by default; the included draw tools are optional for players requesting a strict draw.

## 中文使用说明

### 最快开局

把 `CrisisMUN.md` 上传给 ChatGPT、Claude 或 DeepSeek，再发送：

> 请完整读取这个文件，按 CrisisMUN 规则带我开局。先让我选语言，再问我熟悉程度、是否需要教程和模拟强度。暂时不要替我选国家。

文件太长、上传失败或模型不能读取附件时，打开 MD，将内容分段粘贴到同一聊天，并注明“尚未发完，等我说发完再开始”。需要完整的主入口和运行规则；不要只发 README。普通聊天读取附件不等于永久安装，下次新聊天要重新提供规则和存档。

### 开局会问什么

1. **先选语言。** 中文、English，或双语并选择界面语言。之后的菜单、教程、状态和提示都按所选语言显示。
2. **熟悉程度和教程。** 模联老玩家、普通玩家、新手、从未玩过；再选择跳过、快速说明或逐步教学。老玩家也可以只学系统操作。
3. **模拟强度。** 轻度模拟简化程序并给操作提示；正常学术模拟按会议规则处理动议、文件、授权与投票。两种都保留权限、时间和资源限制。
4. **场景和席位。** 可上传 BG，或选历史、现实、架空场景。国家由你指定，或在合资格国家池内直接随机分配；不是默认让你当大国。
5. **会前简报。** 看清背景、职位权限和眼前任务，确认后开会。

已经明确给出的选择不会再问一遍。随时可以说“解释这个步骤”或“我想跳过教程”。

### 双语怎样显示

双语台词先是代表或主席实际使用的语言，再是你的语言译文。两种语言相同，只显示一次。比如中文界面下，中国代表说中文就不用重复；主席用英语发言，则先英语、再中文。

还可以选“会场工作语言”或“母语沉浸”。前者默认按会议语言发言，联合国模联通常设为英语；后者让代表按角色母语发言，配模拟口译。主席按会场规则使用工作语言，不是任何会场都必须英语。

**双语可能增加 token 消耗，但有助于沉浸感。** 不会把每个菜单和教程都重复翻译。

### 随机选国：在聊天里完成

选择“随机”后，系统直接给你分配一个合资格国家，再进入会前简报。ChatGPT、Claude、DeepSeek 的普通聊天都使用这套流程，不需要打开网页、提供数字或粘贴抽签回执。

有可用代码工具时，系统优先实际抽签；没有工具时，使用模型模拟抽取，结果会简标“随机分配（模拟抽取）”。不会为了方便剧情、照顾新手或匹配玩家语言而优先挑大国或熟悉国家；也不能因第一次抽中小国而偷偷换国。想重抽，直接说“重抽”。

模型模拟抽取提供的是聊天内的随机体验，不能保证数学等概率。只有你主动要求严格抽签时，才使用真实随机工具；聊天无法执行时，可选附带的网页抽签器。普通游玩不用这一步。

### 玩的时候直接说话

“我想私聊法国。” “请求发言。” “准备草案，先别发送。” “打开 DR-1.2。” “向本国内阁请求授权。” “存档。”

草稿不等于提交，联署不等于承诺投赞成，国家代表也不一定有调兵权。顾问可以分析选项，最后由你决定。说“推进三小时”会推进模拟时钟；现实中暂时离开不会自动推进。

### 安装为 Skill

解压 ZIP，保留整个 `crisis-mun` 文件夹。Codex 的用户技能目录为 Windows `%USERPROFILE%\.agents\skills\crisis-mun`，macOS/Linux `~/.agents/skills/crisis-mun`；项目安装可用 `.agents/skills/crisis-mun`。已有同名目录请先备份，避免丢失自定义内容。确认 `crisis-mun/SKILL.md` 没有套两层目录，在新聊天调用 `$crisis-mun`。

其他支持 Agent Skills 的工具使用它们自己的技能安装入口。没有安装入口的聊天版，使用单文件 MD。基本游玩不需要服务器、数据库或 API key；Python 抽签脚本只是有执行工具时的可选辅助。

### 存档

发送“存档”，保存完整的 `CRISISMUN SAVE` JSON。新聊天重新提供规则和存档，说“恢复这局”。语言、双语、教程和强度偏好会保留；旧存档仍可读取。

跨聊天保存的是玩家已知状态。隐藏目标和未发现行动需要重建，后续可能不同。模型也有上下文上限，长局请及时保存；这套规则不提供真正的私有存储或后台运行。

## English guide

### Start a game

Upload `CrisisMUN.md` to ChatGPT, Claude or DeepSeek, then send:

> Read this file in full and run CrisisMUN. Ask me to choose a language first, then my MUN experience, tutorial preference and simulation intensity. Let me choose how my country is assigned.

If the attachment cannot be read, paste the Markdown in numbered parts in the same chat and ask the model to wait until you have sent all parts. Include the rules, not just the README. Uploading a file does not permanently install a skill; a new chat needs the rules and your save again.

### Opening choices

Language comes first: Chinese, English, or bilingual with an interface language. All menus, tutorials and status messages then use that language. Choose your experience level—veteran, regular delegate, beginner or never played—and whether to skip, take a quick introduction or learn step by step.

Choose LIGHT for fewer procedural steps and short hints, or ACADEMIC for formal procedure, documents, authority and voting under the selected rules. Neither removes constraints or guarantees success. Select a BG, historical, current or fictional setting, then choose your own country or request an in-chat random assignment from eligible countries. Review your briefing before the meeting starts.

### Bilingual dialogue

Delegates and the chair speak in their configured spoken language first, followed by a complete translation into your language. If the languages match, the line appears once. Choose the committee's working language or native-language immersion with simulated interpretation. The chair uses the committee's working language, often English in an international MUN setting.

Bilingual dialogue may use more tokens, but can improve immersion. Menus and tutorials remain in your selected interface language.

### Random assignment in a regular chat

Choose random assignment and receive an eligible country directly in the chat, followed by your briefing. The same flow is used in regular ChatGPT, Claude and DeepSeek chats. No website, supplied number or pasted draw receipt is needed.

When a real code tool is available, the system uses it for the draw. Otherwise, it makes one model-simulated selection and labels it “Random assignment (simulated).” It must not favor major powers, familiar countries, your language or a convenient plot, and must not quietly replace an inconvenient result. Ask to redraw if you want another assignment.

Model-simulated selection gives an in-chat random experience, not a guarantee of mathematical uniformity. A strict draw with a real random source is an optional flow that you can request. The included browser draw is a fallback for that optional flow; ordinary play does not require it.

### Playing, installing and saving

Use ordinary language: “Talk privately to France,” “Request the floor,” “Prepare a draft but do not send it,” “Open DR-1.2,” or “Ask my cabinet for authorization.” Drafting is separate from submitting, and a delegate's authority has limits. Simulation time advances through actions or an explicit time request, not while you are away.

For Codex, extract the entire `crisis-mun` folder into `~/.agents/skills/` (Windows: `%USERPROFILE%\.agents\skills\`). Keep a single folder layer and back up an existing installation before replacing it. Start a new chat with `$crisis-mun`. Other Agent Skills hosts have their own installation paths. Regular chat users can use the Markdown edition instead.

Ask to save and keep the complete `CRISISMUN SAVE` JSON. Provide the rules and save in a new chat to resume. Known state and preferences are restored; hidden events must be reconstructed, so the future may differ. Long games remain subject to context limits. There is no background service or private state database.

## 模型建议 / Suggested models

这类模拟需要持续维护角色、文件和因果关系，建议使用 ChatGPT、Claude 或 DeepSeek 中推理能力较强的模型。下面是按任务需要给出的起点，不是三家实测排名。可用型号与额度会变化，以账号界面为准。

This simulation needs sustained reasoning across actors, documents and consequences. Start with a capable reasoning model in ChatGPT, Claude or DeepSeek. These are task-based suggestions, not a tested ranking across providers. Availability and limits depend on your account.

| 平台 / Platform | 建议 / Suggestion |
| --- | --- |
| ChatGPT | GPT-5.6 的 Medium/High 思考档；额度充足可尝试 GPT-6 Pro。Work/Codex 可选 GPT-6.1 Sol，复杂联动可尝试 Astra。 / GPT-5.6 Medium or High; try GPT-6 Pro if available and within your budget. In Work/Codex, consider GPT-6.1 Sol or Astra. [ChatGPT](https://help.openai.com/en/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt) · [Work/Codex](https://learn.chatgpt.com/docs/models) |
| Claude | 可用时优先 Opus 5.5；也可选账户中的 Sonnet 系列，从小规模会议开始。 / Consider Opus 5.5 when available, or a Sonnet model for a smaller meeting. [Claude Opus](https://www.anthropic.com/claude/opus) |
| DeepSeek | 聊天版开启“深度思考”；API 可选 DeepSeek-V4-Pro 的思考模式，较轻场景可尝试 deepseek-flash。 / Enable DeepThink in chat; for API use, consider DeepSeek-V4-Pro in thinking mode, or deepseek-flash for a lighter session. [模型与模式 / Models and modes](https://api-docs.deepseek.com/quick_start/pricing) |

## 文件导航 / Files

[技能入口 / Skill entry](SKILL.md) · [文件目录 / File list](FILE-TREE.md) · [科索沃示例 / Kosovo example](examples/kosovo-1999.md) · [架空场景 / Fictional scenario](examples/fictional-crisis.md) · [存档示例 / Save example](examples/example-save.md)

## 额度提醒 / Usage

请注意您的聊天额度或 API token 消耗。双语、更多代表、长篇文件和更高思考档会增加消耗。建议先用 10–12 个核心代表、单语与简洁输出试一局，再按需要调整。

Please watch your chat allowance or API token usage. Bilingual dialogue, more delegates, full-length documents and higher reasoning settings can increase usage. Start with 10–12 core delegates, one language and concise output, then adjust as needed.
