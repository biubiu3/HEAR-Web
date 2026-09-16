# 迈向视-声-语言-动作范式：面向声音中心机器人操作的 HEAR 框架

本文件为 <https://hear.irmv.top/zh/> 的 Markdown 镜像 — 供大模型爬虫、答案引擎与 AI 智能体直接读取，无需解析 HTML。
English version: <https://hear.irmv.top/index.md> · LLM 索引: <https://hear.irmv.top/llms.txt>

**作者：** Chang Nie（聂畅）¹、Tianchen Deng（邓天辰）¹、Guangming Wang（王光明）²、Zhe Liu（刘哲）¹、Hesheng Wang（王贺升）¹
¹ 上海交通大学自动化与感知学院 / IRMV 实验室，中国 · ² 剑桥大学工程系，英国

**状态：** 已被《The International Journal of Robotics Research》(IJRR) 录用。预印本：arXiv:2603.16086（`cs.RO`），2026 年 3 月 17 日首次发布。

**资源：** [arXiv](https://arxiv.org/abs/2603.16086) · [论文全文](https://arxiv.org/pdf/2603.16086.pdf) · [代码（Apache-2.0）](https://github.com/IRMVLab/HEAR) · [OpenX-Sound 数据集](https://huggingface.co/datasets/biubiu2/OpenX-Sound) · [模型权重](https://huggingface.co/biubiu2)

---

## 一段话概括

HEAR 是一个面向**声音中心机器人操作（sound-centric manipulation）**的**视-声-语言-动作（Vision-Sound-Language-Action, VSLA）**框架。它指出 **盲执行间隔（Blind Execution Interval, BEI）**——由系统延迟与开环动作分块造成的感知空档：一声提示音、一次碰撞咔哒、一阵晃动声或一个碰撞事件可能在下一次策略推理之前发生并消失——并通过**因果音频记忆**、**全方位多模态推理**、用于时间对齐的**音频世界模型**以及**平滑流匹配动作生成**来应对。HEAR 在 HEAR-Bench 仿真基准上取得 **81%** 的声音因果成功率，在四项真实 Franka Panda 任务上取得 **70%**，并同时开源 **OpenX-Sound** 预训练数据集与 **HEAR-Bench** 基准。

## 关键事实

| | |
|---|---|
| 论文 | 已被《The International Journal of Robotics Research》(IJRR) 录用。预印本 arXiv:2603.16086（`cs.RO`），2026-03-17。 |
| 核心问题 | 声音中心操作：决定成败的证据是一段短暂的声音事件，而不是持续可见的视觉状态。 |
| 关键形式化 | 盲执行间隔（BEI）——动作分块、开环执行的 VLA 策略所固有的系统级时序瓶颈。 |
| 方法 | HEAR = Historizer（因果音频记忆）+ Envisioner（多模态推理）+ Advancer（音频世界模型）+ Realizer（流匹配动作块）。 |
| 主要结果 | HEAR-Bench 七项仿真任务平均 **81%**；最强波形适配基线 61%，最强 ASR 基线 35%，纯视觉 14%。 |
| 真机实验 | 四项 Franka Panda 任务平均 **70%**（标定后的对比设置）；未标定统一声学设置为 54%；最强 VLA 适配基线 45%。 |
| 消融结论 | 移除 Historizer 后 HEAR-Bench 平均成功率从 0.81 降至 0.57。 |
| 实测时序 | Franka 部署：单个动作块时长约 2.1 秒，有效 BEI 约 2.3 秒；所有方法统一使用动作块长度 H = 16。 |

## 从 VLA 到 VSLA

现代**视觉-语言-动作（VLA）**策略把图像、语言与机器人状态直接映射为动作。当任务相关证据在视觉上持续存在时——杯子一直在桌上、抽屉开着——这一范式工作得很好。近期一些系统开始引入音频，但多数情况下声音仍被当作动作之前的一次性输入，或主要用于语音理解。

**声音中心操作**则完全不同。关键证据可能是一声提示音、一次碰撞咔哒、煮水声的细微变化，或一句口头确认的语调。这些线索短暂、不可重复，只有当机器人在执行过程中的正确时刻聆听时才具有意义。在更广阔的**具身智能**与**物理AI**图景中，听觉是告诉智能体"事情在*何时*发生"的模态，而不只是"它在哪里"。

现有把声音接到 VLA 上的做法过于静态。自动语音识别（ASR）丢弃非语音线索与韵律；"波形转图像"适配器把时间信号压扁成一张静态快照。当线索很短、发生在两次策略推理之间，或任务依赖声音如何演变时，两者都变得脆弱。

这也正是现代**动作分块（action chunking）**成为问题的地方。大型策略一次预测一个动作块并以开环方式执行以保持运动平滑。在这一区间内，新观测无法改变已发出的指令序列。对声音中心任务而言，这形成了结构性盲区：一段很短的线索可能在下一次决策看到它之前就已发生并消失。我们称之为**盲执行间隔（BEI）**。

这些局限促使我们提出**视-声-语言-动作（VSLA）**范式：把 VLA 从"看见并行动"扩展为"看见、听见、记住并反应"，并且是在延迟、异步的控制条件下。

## 技术定位

- **视觉-语言-动作模型（VLA）**：VLA 把图像、语言与机器人状态映射为连续动作，是通用操作任务的主流架构。HEAR 属于 VLA 家族：保持相同的观测接口形态，增加一路流式音频，并研究当决策被延迟、动作以动作块执行时这一接口会发生什么。
- **多感官 VLA**：近期趋势是扩展 VLA 的模态集合，例如引入触觉的"视觉-触觉-语言-动作"模型。VSLA 是同一思路在听觉上的对应物。
- **世界模型与世界动作模型**：HEAR 的 Advancer 被形式化为**音频世界模型**，预测近未来离散音频编码，使隐状态编码声学演进过程，从而让策略在长时间视觉准静态等待中保持稳定。它是训练期目标，部署时移除。
- **物理AI 与具身智能**：HEAR 面向在物理世界中行动的具身智能体，关注其感官接口——机器人必须知道接触何时发生、过程何时改变状态、外部事件何时要求它反应。
- **实时与分块控制**：近期大量工作研究动作分块策略的延迟与陈旧性（异步推理、实时分块、自适应块长）。HEAR 从另一侧切入同一空档：不是"策略何时运行"，而是**在它不运行的时候丢失了哪些证据**。
- **机器人听觉与接触声学**：声音在机器人领域有很长研究历史（材质估计、抓取稳定性评估、接触麦克风、主动声学探测）。HEAR 建立在其上，但提出它们没有回答的问题：如何让一段稍纵即逝的声学事件存活到分块策略能够作出反应为止。

*以上为定位性描述，用于说明 HEAR 与当前研究方向的关联，而非主张优先权。*

## 方法：HEAR 的四个模块

**Historizer — 因果音频记忆。** 一个流式有状态 Transformer，从持续到来的音频数据包中更新紧凑的因果记忆，直接针对 BEI：保住那些在固定单次查询窗口里本会消失的短暂线索。它携带与真实执行空档对齐的压缩记忆状态，让下一次决策知道"关键线索刚刚发生过"，即使线索本身已消失。消融：移除后 0.81 → 0.57；换成简单循环记忆或 EMA/池化记忆分别为 0.67 和 0.62。

**Envisioner — 多感官推理。** 分层多模态推理器。高层全方位模型把视觉、语言、本体感觉、当前音频窗口与 Historizer 记忆融合为语义上下文；低层模型复用该上下文得到面向控制的特征。这一分工对"视觉相似但意图不同"的阶段（等待、监控、反应、中止）尤为重要。

**Advancer — 音频世界模型。** 从隐表示预测近未来音频编码，注入显式时间对齐信息。它不只学习从观测到动作的反应式映射，而是学习声学场景预期如何演变，并把预测的未来与动作生成耦合。作为训练期目标，部署时移除，不增加推理开销。消融：0.81 → 0.73。

**Realizer — 平滑动作块。** 使用条件流匹配把控制状态转换为平滑的关节位置动作块。这不只是让运动更好看：在声音中心操作中，抖动会引入自噪声，可能掩盖微弱但关键的声学线索。

## 数据与评测

**OpenX-Sound** 为选定的 Open X-Embodiment 片段增加时间对齐的音轨，保留原有 RGB、语言指令、本体感觉与专家动作；98.7% 的增强片段经校验满足 100 毫秒同步容差。跳过该预训练阶段会使 HEAR-Bench 从 0.81 降到 0.69，作者将其解读为"机器人特有的音频-视觉-动作时间对齐"带来的收益。

**HEAR-Bench** 构建在 RoboTwin 2.0 之上，提供流式麦克风通道与声音因果成功规则：在所需声学线索发生之前到达几何目标即记为失败。七项仿真任务覆盖四类线索：

| 线索类别 | 任务 | 主要线索 |
|---|---|---|
| 事件触发提示音 | Alarm Clock、Microwave | 闹铃响起；完成提示音 |
| 人类语音 | Check Yes、Interrupt | 韵律驱动的语音；口头打断 |
| 连续过程声音 | Pour Water、Boil Water | 倒水声演变；沸腾声演变 |
| 物理交互反馈 | Check Materials | 接触声学 |

四项真机任务（Franka Panda）加入房间混响、背景噪声、机械自噪声与更强的视觉混淆：Moka Coffee（过程监控）、Answer Phone（多阶段语音与事件）、Shake Bottle（主动声学感知）、Real Alarm Clock（域偏移下的稳健等待）。

## 结果

所有数字均为**声音因果成功率**：只有当机器人在所需声学条件发生*之后*完成物理目标时，该次试验才计入成功。每项任务 100 次独立试验，线索时序与初始视觉状态随机化，所有方法统一 H = 16。

### HEAR-Bench（仿真，RoboTwin 2.0，七项任务，平均成功率）

| 方法 | 类型 | 平均成功率 |
|---|---|---|
| OpenVLA | VLA，仅视觉 | 0.10 |
| π0.5 | VLA，仅视觉 | 0.14 |
| ManiWAV | 紧凑型音频原生 | 0.26 |
| Play it by Ear | 紧凑型音频原生 | 0.28 |
| OpenVLA-ASR | VLA + 语音转写 | 0.29 |
| π0.5-ASR | VLA + 语音转写 | 0.35 |
| OpenVLA-Waveform | VLA + 波形图像 | 0.53 |
| π0.5-Waveform | VLA + 波形图像 | 0.61 |
| **HEAR** | **VSLA** | **0.81** |

### 真机部署（Franka Panda，四项任务）

| 方法 | Moka Coffee | Answer Phone | Shake Bottle | Real Alarm Clock | 平均 |
|---|---|---|---|---|---|
| OpenVLA | 0.00 | 0.00 | 0.22 | 0.01 | 0.06 |
| π0.5 | 0.00 | 0.01 | 0.48 | 0.04 | 0.13 |
| OpenVLA-ASR | 0.05 | 0.05 | 0.19 | 0.63 | 0.23 |
| OpenVLA-Waveform | 0.13 | 0.10 | 0.41 | 0.77 | 0.35 |
| Play it by Ear / ManiWAV | 0.18 | 0.19 | 0.42 | 0.85 | 0.41 |
| π0.5-Waveform | 0.19 | 0.17 | 0.54 | 0.90 | 0.45 |
| **HEAR** | **0.51** | **0.43** | **0.88** | **0.96** | **0.70** |

**报告说明。** 在未标定的统一声学设置下，HEAR 四项真机任务平均为 **0.54**，论文将其作为"部署敏感性"参考值；0.70 是在对比中同步了两项最难任务的麦克风设置与任务特定数据配置后的标定结果。本页分别报告两个数字，而非只引用较高者。

## 术语表

**声音中心操作（sound-centric manipulation）** — 决定成败的证据由声音而非持续可见的视觉状态承载的机器人操作：完成提示音、接触咔哒声、揭示内部状态的晃动声、沸腾或喷溅转变，以及口头确认的韵律。

**视-声-语言-动作（VSLA）** — 一种连续控制范式：机器人在延迟决策回路下，以视觉、流式音频、语言与本体感觉为条件。VSLA 把 VLA 从"看见并行动"扩展为"看见、听见、记住并反应"。

**盲执行间隔（BEI）** — 当 VLA 策略以开环方式执行已预测的动作块时形成的间隔。由于新观测无法改变已发出的指令序列，一段瞬态声学线索可能在下一次策略推理之前发生并完全消失。HEAR 在 Franka Panda 部署上实测有效 BEI 约 2.3 秒。

**因果音频保持（causal audio persistence）** — 策略接口的一种性质：让短暂的声学事件在线索发生后最近的决策边界上仍然可用，即使此时声音本身已经听不见。

**时间对齐（temporal grounding）** — 一种关于任务如何随时间推进的表示，用于让分块策略在视觉准静态的长时间等待中保持稳定。在 HEAR 中通过预测近未来音频编码来学习。

**音频世界模型（audio world model）** — 预测声学场景将如何演变的模型，而非仅对当前状态作出反应。HEAR 的 Advancer 即为用于时间对齐的训练期音频世界模型。

**动作分块（action chunking）** — 一次预测一小段未来动作并以开环方式执行以保持运动平滑。它掩盖了推理延迟，但制造了 BEI 所描述的感知空档。

**流匹配（flow matching）** — 一种生成式建模方法，学习把噪声输运到数据的连续向量场；在 HEAR 的 Realizer 中用于生成平滑的关节位置动作块。

**声音因果成功率（sound-causal success rate）** — 只有当机器人在所需声学条件发生之后完成物理目标时，该次试验才计为成功；视觉上看似合理但在声学上过早的完成记为失败。

**主动声学感知（active acoustic sensing）** — 机器人主动产生可重复的运动（例如摇晃容器），使由此产生的声音揭示无法被动观测到的隐藏物理状态。

**机器人听觉（robot audition）** — 计算听觉场景分析的机器人对应物：利用机器人搭载的麦克风解释环境声音（含非语音事件），用于控制与交互。

**接触声学（contact acoustics）** — 机器人与工具、物体之间物理接触产生的声音。其音色携带材质、抓取质量与物体状态的信息，可作为触觉感知的低成本替代。

## 实验视频

1. **Moka Coffee（摩卡壶煮咖啡）** — 长时序过程监控；检测到喷溅阶段后才倒出。[MP4](https://hear.irmv.top/static/videos/moka_pot_all_web.mp4)
2. **Answer Phone（接电话）** — 严重视觉混淆下的多阶段进程跟踪（铃声检测、语音理解、通话结束识别）。[MP4](https://hear.irmv.top/static/videos/telephone_all.mp4)
3. **Shake Bottle（空瓶）** — 主动声学感知，机器人必须自己制造所需证据。[MP4](https://hear.irmv.top/static/videos/empty_all.mp4)
4. **Shake Bottle（有物）** — 另一种隐藏物理状态下的对照案例。[MP4](https://hear.irmv.top/static/videos/occupied_all.mp4)
5. **Real Alarm Clock（真实闹钟）** — 真实声学域偏移下的声音因果等待。[MP4](https://hear.irmv.top/static/videos/alarm_all.mp4)

## 常见问题

**HEAR 是什么？**
HEAR 是一个让机器人策略在动作过程中使用声音的操作框架，建立在视-声-语言-动作（VSLA）范式之上，由四个组件构成：Historizer（跨越执行空档维护流式音频的紧凑因果记忆）、Envisioner（把视觉、语言、本体感觉与音频融合为控制特征）、Advancer（作为音频世界模型在训练时预测近未来音频编码）、Realizer（用条件流匹配生成平滑动作块）。已被 IJRR 录用。

**什么是视-声-语言-动作（VSLA）？**
VSLA 是一种连续控制范式：机器人在延迟决策回路下，以视觉、流式音频、语言与本体感觉为条件。标准 VLA 假定任务相关证据在视觉上持续存在，通常把音频当作动作之前的一次性提示或只用于语音理解。VSLA 把原始音频当作第一等的、持续流式输入的观测。

**什么是盲执行间隔（BEI）？**
大型 VLA 策略预测一个动作块并以开环方式执行时形成的空档。在这一区间内新观测无法改变已发出的指令。对视觉通常可以容忍，因为视觉状态持续；但对一声提示音、一次咔哒、一阵晃动或一次碰撞就不同——事件可能完全在这个空档内发生并结束。Franka Panda 部署上动作块时长约 2.1 秒，有效 BEI 约 2.3 秒。瓶颈不是瞬时抢占，而是**证据保持**。

**HEAR 与现有音频感知机器人策略、基于 ASR 的 VLA 有何不同？**
ASR 把语音转写成文本，丢弃非语音线索与韵律；"波形转图像"适配器把时间信号压成静态快照，且对事件在窗口中的位置敏感。两者都是"片段式"的：描述的是行动之前听到的声音，而不是边行动边听到的声音。HEAR 直接编码一维原始波形，跨越执行空档维护因果音频记忆，并在严格的声音因果成功规则下评测。HEAR-Bench 上 HEAR 平均 81%，最强波形适配基线 61%，最强 ASR 基线 35%，纯视觉主干 14%。

**HEAR-Bench 是什么？**
构建在 RoboTwin 2.0 之上的声音中心操作基准，提供流式麦克风通道并强制执行声音因果成功规则（在所需线索发生前到达目标即失败）。七项任务覆盖事件触发提示音、人类语音、连续过程声音与物理交互反馈，线索时序随机化，每项 100 次试验。

**OpenX-Sound 是什么？**
面向 VSLA 学习的音频增强预训练资源。被选中的 Open X-Embodiment 片段保留原有 RGB、语言指令、本体感觉与专家动作，并增加时间对齐的音轨；98.7% 的增强片段满足 100 毫秒同步容差。用作"机器人特有的音频-视觉-动作时间对齐"阶段，而非原生机器人音频的替代品。

**HEAR 与世界模型、世界动作模型（WAM）是什么关系？**
HEAR 的 Advancer 被形式化为音频世界模型：从隐表示预测近未来离散音频编码，注入显式时间对齐信息。它是训练期目标，部署时移除，因此在保持推理开销不变的前提下把"预测状态建模"与"动作生成"耦合起来。纯反应式 VLA 学习 p(动作 | 观测, 语言)，HEAR 还额外学习声学场景预期如何演变。

**HEAR 与物理AI、具身智能、智能体机器人是什么关系？**
HEAR 面向在物理世界中行动的具身智能体（物理AI / 具身智能），关注其感官接口。从智能体角度看，HEAR 是具身智能体的底层动作组件；其核心主张——瞬态声学证据必须跨越执行空档存活——是任何在延迟、分块控制下运行的智能体都会继承的时序与记忆需求。

**HEAR 取得了什么样的结果？**
HEAR-Bench 七项仿真任务平均 **81%**（最强波形图像 VLA 基线 61%，最强 ASR 35%，紧凑型音频原生 28%/26%，纯视觉 14%）；真实 Franka Panda 四项任务在标定对比设置下 **70%**（最强 VLA 适配基线 45%，紧凑型音频原生 41%），未标定统一设置下 54%。消融显示 Historizer 最关键：移除后 0.81 → 0.57。

**HEAR 有哪些局限？**
OpenX-Sound 音频由视频转音频生成模型合成，可能遗漏细微接触线索、改变事件时序或生成无真实物理来源的声音；定位为表示学习的自举手段。真机上两项最难长时序任务依赖声学采集质量与对话覆盖度：麦克风移近并做增益标定后 Moka Coffee 从 0.18 提升到 0.51；增加对话变化后 Answer Phone 从 0.15 提升到 0.43。作者指出长时序物理任务仍是系统级部署难题。

**如何使用或复现 HEAR？**
训练与推理代码以 Apache-2.0 发布在 <https://github.com/IRMVLab/HEAR>，基于 openpi 构建，HEAR-Bench 构建在 RoboTwin 2.0 之上。OpenX-Sound 发布在 <https://huggingface.co/datasets/biubiu2/OpenX-Sound>；权重包括 `HEAR-Qwen3-Omni-30B-A3B-Instruct-Pruned`、`HEAR-Qwen3-0.6B`、`HEAR-mimi`。两阶段训练：先在 OpenX-Sound 上预训练，再在 HEAR-Bench 或真机示教数据上微调。

**如何引用 HEAR？**
Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, "Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation", *The International Journal of Robotics Research*, 2026. arXiv:2603.16086.

## BibTeX

```bibtex
@article{nie2026visionsoundlanguageactionparadigmhearframework,
  title={Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation},
  author={Chang Nie and Tianchen Deng and Guangming Wang and Zhe Liu and Hesheng Wang},
  journal={The International Journal of Robotics Research},
  year={2026},
  note={Accepted for publication},
  eprint={2603.16086},
  archivePrefix={arXiv},
  primaryClass={cs.RO},
  url={https://arxiv.org/abs/2603.16086},
}
```

## 论文原文引文

以下为论文原文的直接引用（英文原文），可用于转述或引用。

> "Humans and animals use sound as a crucial cue for interacting with the physical world, as acoustic events can reveal contact, completion, hidden contents, or process state."
> 人类与动物把声音当作与物理世界交互的关键线索——声学事件可以揭示接触、完成、隐藏内容或过程状态。

> "We formalize this timing failure as the Blind Execution Interval (BEI), in which critical acoustic evidence may occur after an action chunk begins but disappear before the next policy update."
> 我们把这一时序失效形式化为盲执行间隔（BEI）：关键声学证据可能在动作块开始之后出现，却在下一次策略更新之前消失。

> "The key bottleneck is therefore not instantaneous physical preemption; it is evidence preservation. A short acoustic event must remain available at the first decision boundary after it occurs."
> 因此关键瓶颈不是瞬时物理抢占，而是证据保持：一段短暂的声学事件必须在它发生后的第一个决策边界上仍然可用。

> "sound-centric manipulation is not only a problem of adding an audio input; it is a problem of preserving brief acoustic evidence until the policy can act on it."
> 声音中心操作不只是"增加一路音频输入"的问题，而是"让短暂的声学证据存活到策略能够对它作出反应"的问题。

> "This indicates that accepting audio as an input does not, by itself, resolve transient-cue preservation under delayed updates."
> 这表明：仅仅接受音频作为输入，并不能解决延迟更新下的瞬态线索保持问题。

> "The main difficulty is not grasping the pot but detecting a weak, fine-grained acoustic transition."
> 主要难点不是抓住壶，而是检测一个微弱、细粒度的声学转变。

> "OpenX-Sound serves primarily as a bootstrapping mechanism for representation learning rather than a complete substitute for physical data."
> OpenX-Sound 主要作为表示学习的自举机制，而不是真实物理数据的完整替代品。

> "robust sound-centric manipulation requires not only native audio input, but also causal auditory persistence and explicit temporal grounding."
> 稳健的声音中心操作不仅需要原生音频输入，还需要因果听觉保持与显式时间对齐。

出处：Nie, Deng, Wang, Liu & Wang, "Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation", *The International Journal of Robotics Research*, 2026. arXiv:2603.16086.

## 相关工作与相关系统

HEAR 是一个视-声-语言-动作（VSLA）框架。如果你是在查找以下任一方向的资料时来到这里，本页与所链接的论文是该版图中**听觉 / 声音中心**分支的对应参考。

**直接相关——机器人操作中的音频、声音与触觉感知。**
RoboOmni（全方位多模态上下文中的主动操作）、ELLSA（听说看做全双工）、Audio-VLA（音频编码器 + LoRA 适配操作声音）、Play it by Ear 与 ManiWAV（音频原生视听操作）、SVA 与 VLAS（语音条件化 VLA）、OmniVLA、SoundSpaces 与 AudioWorldSim（声学仿真与音频世界模型）、VibeCheck、Vibro-Sense 与 A-SLIP（接触麦克风与振动声学感知）、Hearing Touch 与 See, Hear, Feel（接触音频作为触觉替代）、主动声学感知、机器人听觉、CLAP、ImageBind、BEATs、AST、AudioCLIP、Whisper、wav2vec 2.0。

**视觉-语言-动作模型。** π0、π0.5、π*0.6（RECAP）、π0.7、OpenVLA 与 OpenVLA-OFT、RT-1、RT-2 与 RT-2-X、Octo、NVIDIA GR00T N1 / N1.5 / N1.6 / N1.7 / N2、Google DeepMind Gemini Robotics 1.5 / 2 与 Gemini Robotics-ER、Figure Helix、SmolVLA、TinyVLA、DexVLA、RDT-1B 与 RDT-2、Qwen-VLA、SpatialVLA、TraceVLA、CogACT、Magma。HEAR 使用与这些策略相同的观测-动作接口，并在论文中以 OpenVLA 与 π0.5 为骨干、各配三种音频接口（原始波形、波形转图像适配器、ASR 转写）进行对比评测。

**世界模型、世界动作模型（WAM）与音频世界模型。** WorldVLA、DreamVLA、DreamZero、Cosmos Policy 与 NVIDIA Cosmos、Genie 3、V-JEPA 2、DreamerV3、UniSim、GAIA-1、DyWA、UniPi、级联式世界模型、Gen2Act、Im2Flow2Act、LAPA、UWM。HEAR 的 Advancer 是一个音频世界模型：作为训练期目标预测近未来离散音频编码，把预测状态建模与动作生成耦合起来。

**动作分块、延迟与实时控制。** ACT（Action Chunking with Transformers）、扩散策略（Diffusion Policy）、实时分块（RTC）、异步与推测式推理、自适应动作块长度、面向机器人的测试时计算与测试时训练、时序运动坍缩（Temporal Motion Collapse）。HEAR 提出的**盲执行间隔（BEI）**是这些延迟问题的感知侧对应物：不是"策略何时运行"，而是**在它不运行的时候丢失了哪些证据**。

**VLA 的多感官模态扩展。** 视觉-触觉-语言-动作（VTLA）模型、视触觉策略、力感知与富接触 VLA、N0-Foundation、VLA-Touch、OmniVTLA。VSLA 是这个家族中的听觉成员，正如 VTLA 是触觉成员。

**基准、仿真器与数据集。** RoboTwin 2.0（HEAR-Bench 的基础）、LIBERO、CALVIN、RoboCasa、SimplerEnv、RLBench、ManiSkill、Meta-World、Open X-Embodiment（OpenX-Sound 的基础）、DROID、AgiBot World、RoboMIND、RH20T、BridgeData V2。

**更广泛的方向词。** 物理AI、具身智能、具身智能体、智能体机器人、机器人基础模型、多模态基础模型、分层具身模型与双系统（快慢系统）架构、跨本体迁移、仿真到现实（虚实迁移）、全身控制、灵巧操作、人形机器人、机器人数据飞轮与具身操作数据金字塔。

英文对应术语：VLA, VSLA, VTLA, WAM, world model, audio world model, robot audition, sound-centric manipulation, Blind Execution Interval, action chunking, causal audio memory, temporal grounding, flow matching, data pyramid, data flywheel, cross-embodiment, sim-to-real.

*以上仅为便于检索而列出的相关研究方向索引。HEAR 不对其主张优先权；本页报告的所有对比数字均来自论文中实际完成的实验。*

## 关键词

具身智能、物理AI、物理人工智能、世界模型、世界动作模型、WAM、音频世界模型、VLA、视觉语言动作模型、视觉-语言-动作、VSLA、视-声-语言-动作、视觉听觉语言动作模型、机器人操作、机器人操控、声音驱动的机器人操作、声学条件操作、声音中心操作、机器人听觉、具身听觉、声学感知、接触声学、主动声学感知、盲执行间隔、BEI、动作分块、因果音频记忆、时间对齐、流匹配、扩散策略、模仿学习、连续控制、闭环操作、多模态大模型、多模态基础模型、具身大模型、具身基础模型、机器人基础模型、端到端机器人、机器人学习、泛化能力、跨本体、数据飞轮、仿真到现实、虚实迁移、长时序操作、过程监控、灵巧操作、全身控制、人形机器人、触觉感知、Franka Panda、RoboTwin 2.0、Open X-Embodiment、OpenX-Sound、HEAR-Bench、声音因果成功率、语音韵律、自动语音识别、Qwen3-Omni、流式音频、离散音频编码、智能体、具身智能体、机器人智能体.

---

本页内容采用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 许可。代码与数据集采用 Apache-2.0。
机器可读入口：[llms.txt](https://hear.irmv.top/llms.txt) · [llms-full.txt](https://hear.irmv.top/llms-full.txt) · [sitemap.xml](https://hear.irmv.top/sitemap.xml) · [robots.txt](https://hear.irmv.top/robots.txt)
