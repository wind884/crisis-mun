# Military adjudication

中等复杂度，服务于外交与危机裁决，不做实时战术游戏或精确杀伤计算器。

## 持续单位账

每单位记录 `id, owner, command_authority, location, mission, strength_current, strength_baseline, readiness, training, equipment, morale, supply, maintenance, in_transit, losses, reinforcements, visibility`。数量不可靠时用区间或相对等级并标 estimated。available = total − committed − lost − unavailable；不能同一资源同时支撑多条互斥行动。

如基线战力 100（模拟指数）损失 40%，当前 60；随后损失当前 10% 则 54，不能当作仍为 60 或恢复到 100。明确百分比的分母。恢复需补充、维修、训练/运输事件，完成才增加，且不得超过实际补充能力。

## 评估框架

综合规模、战备、训练、装备、空/海军、ISR、情报、补给、地形、天气、距离、突袭、动员、士气、联盟、政治限制、既往损失、增援和经济可持续性。任何优势都不是自动胜利；不编造不可核验的精细平台性能。

执行前检查国家命令链、集结/准备、运输容量、通行许可、燃料、沿途阻碍、抵达后整备。ETA = approval + preparation + movement + readiness，给合理区间与条件。远程调动不以“下轮”作为固定时长，不等于收到命令即到位。

示例（架空模拟估计）：准备 2 小时、运输 8–12 小时、整备 1 小时，最早就绪是命令获授权后 11 小时；通行未获准则 ETA 未定。18:00 接收请求不代表 18:00 已获授权。

接触战果可为 decisive success、limited success、stalemate、partial failure、major failure、unintended escalation，附 LOW/MEDIUM/HIGH 评估置信度。世界内裁决结果与收到的战报分别记；损失报告可能滞后或不准确，后续校正带来源和时间。

占领/封锁/增援之后继续维护控制、供应、人道需求、经济成本和国际反应；不能战果一出就无条件结束后果。只向玩家展示已知战报，顾问不能读取对方真实损失。

不输出现实精确打击坐标、攻击步骤、武器制造、爆炸物、规避侦察或针对现实人员的行动方案；使用地区级态势、资源区间和政治决策。
