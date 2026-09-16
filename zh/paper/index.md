# 迈向视-声-语言-动作范式：面向声音中心机器人操作的 HEAR 框架

> 本页是 HEAR 论文的正式著录页。论文提出面向声音中心机器人操作的视-声-语言-动作（VSLA）框架，已被《The International Journal of Robotics Research》(IJRR) 录用。论文形式化了盲执行间隔（BEI）——由系统延迟与开环动作分块造成的时序空档，一段瞬态声学线索可能在两次策略推理之间发生并消失——并给出四模块的 HEAR 架构来解决它。

Source: https://hear.irmv.top/zh/paper/ · Language: zh-Hans

## 作者与单位

Chang Nie（聂畅）、Tianchen Deng（邓天辰）、Zhe Liu（刘哲）、Hesheng Wang（王贺升）来自上海交通大学自动化与感知学院、上海市导航与定位服务重点实验室；Guangming Wang（王光明）来自英国剑桥大学工程系。通讯作者为王贺升。

## 发表状态

论文已被《The International Journal of Robotics Research》（ISSN 0278-3649，SAGE Publications 出版）录用，正式 DOI 尚未分配。预印本永久发布于 arXiv：arXiv:2603.16086（cs.RO），2026 年 3 月 17 日首次发布。

## 摘要

人类与动物把声音当作与物理世界交互的关键线索——声学事件可以揭示接触、完成、隐藏内容或过程状态。具身智能体同样应当从操作过程中的听觉感知中获益，但现有的视觉-语言-动作（VLA）策略通常依赖持续可见的视觉观测，而音频相关变体往往把音频当作语音、波形图像或固定的执行前上下文。这类接口会遗漏瞬态声音，例如提示音、咔哒声、晃动声或碰撞线索，在系统延迟与开环动作分块下尤其如此。

我们把这一时序失效形式化为盲执行间隔（BEI）：关键声学证据可能在动作块开始之后出现，却在下一次策略更新之前消失。为解决这一问题，我们提出视-声-语言-动作（VSLA）——一种在延迟决策回路下以视觉、流式音频、语言与本体感觉为条件的连续控制范式。作为实例，我们提出 HEAR 框架：它跨越执行空档保持因果听觉上下文，进行多模态推理，在训练时建模近未来音频动态，并生成平滑的动作块。

为支撑学习与评测，我们构建了面向机器人音频-视觉-动作预训练的 OpenX-Sound，以及带严格因果时序约束的声音中心操作基准 HEAR-Bench。在 HEAR-Bench 上 HEAR 取得 81% 的成功率，优于波形、ASR 与紧凑型音频原生基线；在四项真实 Franka 任务上取得 70% 的声音因果成功率。结果表明，稳健的声音中心操作不仅需要原生音频输入，还需要因果听觉保持与显式时间对齐。

## 如何引用

可直接抓取的 BibTeX 文件位于 /cite.bib。长键为 {bibtex_key}，短键为 {bibtex_key_short}。纯文本引用格式：Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.

## 配套产出

论文同时发布四项产出：代码（Apache-2.0）、OpenX-Sound 预训练数据集、三个预训练权重，以及构建在 RoboTwin 2.0 之上的 HEAR-Bench 基准。详见数据集页面与基准页面。

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.