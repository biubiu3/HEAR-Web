# HEAR-Bench：声音因果操作基准

> HEAR-Bench 是一个面向声音中心操作的仿真基准，构建在双臂 RoboTwin 2.0 平台之上。它提供流式麦克风通道，并强制执行声音因果成功规则：只有当机器人在所需声学条件发生之后完成物理目标时，该次试验才计为成功。提前到达目标——标准基准会判为成功——在这里记为失败。

Source: https://hear.irmv.top/zh/benchmark/ · Language: zh-Hans

## 为什么需要时序敏感的基准

标准操作基准评测最终几何状态是否达成。在声音门控任务上，这一指标无法区分“等待了线索的策略”与“完全忽略声音、靠视觉启发式移动的策略”。HEAR-Bench 通过把声学前提并入成功判据来填补这个缺口。正是这一性质使得“测量策略是否真正声音因果”成为可能。

## 任务套件

七项仿真任务覆盖四类决定成败的声学线索。线索时序与初始视觉状态均随机化，使策略无法记忆固定的时间表；每项任务评测 100 次独立试验。

## 四类线索

事件触发提示音测试等待与瞬态捕捉：Alarm Clock 要求抑制“看起来诱人”的提前按下，直到铃声响起；Microwave 要求捕捉可能在执行空档内完全发生的短暂完成提示音。

人类语音测试时序与韵律：Check Yes 使用相同文本但不同语调，以击败纯 ASR；Interrupt 在随机时刻插入口头打断，测试运动中的安全模式切换。

连续过程声音测试长时序监控：Pour Water 与 Boil Water 要求在视觉薄弱或静止时跟踪渐进的声学演变。

物理交互反馈测试接触声学：Check Materials 使用视觉相似的物体，使撞击音色成为唯一的判别信号。

## 如何使用

所有被评测的方法共享相同的观测接口与相同的两阶段训练配方（先在 OpenX-Sound 上预训练，再做任务特定微调），因此差异反映的是架构而非数据量。在这一协议下，HEAR 取得 81% 的平均声音因果成功率，而最强波形图像 VLA 基线为 61%、最强 ASR 基线为 35%、最强纯视觉骨干为 14%。

## 复现

HEAR-Bench 的实现包含在代码发布中，构建在 RoboTwin 2.0 之上，任务音频资源随代码一同提供。流程的另一半见 OpenX-Sound。

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.