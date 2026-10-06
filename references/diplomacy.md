# Diplomacy

“找中国私聊”建立仅双方可见的 PRIVATE CHANNEL。明确与哪个职位联系；同国常驻代表不自动代表总统授权。首次接触可直接模拟对方回应；玩家未给政治底线时不要替其许诺。

把每次接触分成“玩家已选择的表达/动作”和“对方自行反应”。玩家只问为何违约，便传达问题并记录回答；即使暂停支持在玩家职位权限内，也不能代发暂停通知、施压威胁、让步或重新谈判条件。可在回复后列可选反应，等待其选择。仅当已有协议条款明确设定自动后果时，依条款触发并指出依据，不把自主政策选择伪装成自动惩罚。

每次磋商记录 `id, participants, channel, started_at, ended_at, proposal, conditions, commitments, documents_shared, disclosure_scope`。长谈分段，允许玩家决策时其他已有计划继续沿模拟时钟推进。

谈判回复依该 actor 的已知信息、利益、红线、信任和现有协议；可以不同意、索要代价、暂缓、转向另一集团或要求书面保障。“愿意讨论”不记作支持；“签字让文件进入讨论”不记作赞成条款。

AI-to-AI 同样能提案、联署、竞争文件、妥协、威胁、秘密交易和违约。运行引擎按相关性激活；不把会谈内容自动写给玩家。自发文件先按作者访问范围流转，玩家拿到才可打开全文。

## 协议强度与履约

verbal commitment → political understanding / informal agreement → written agreement → signed agreement → ratified agreement，不自动升级。条约是否需要批准依据该国制度/场景授权；无法确认时记录待批准。

每项 agreement 保存：parties、level、terms、conditions、signatures、authority、entry_into_force、deadlines、monitoring、dispute_clause、termination、public/private、status。不同意生效条件的主体不能被“成交”强行绑定。

违约按条款判断，不按玩家情绪判断。事实违约与对方何时得知分开；发现后可要求解释、暂停共享、索赔、转向盟友、撤回支持、公开指责。执行制裁仍需权限、资源与时间。保留违约证据，不让下轮角色忘记。

玩家帮助起草时，措辞和格式可代劳；停火监督机构、边界、让步、威慑等实质选择给 2–3 个方案或追问关键偏好，不擅自作政治决定。
