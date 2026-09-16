# OpenX-Sound：音频增强的机器人轨迹

> OpenX-Sound 是面向视-声-语言-动作学习的预训练数据集。选定的 Open X-Embodiment 片段保留原有的多视角 RGB 视频、语言指令、本体感觉与专家动作，并增加时间对齐的音轨。它之所以存在，是因为当初推动 VLA 进展的大规模跨本体数据集中不含同步麦克风录音，而在可比规模上采集机器人音频需要硬件标准化，目前没有任何实验室做到。

Source: https://hear.irmv.top/zh/openx-sound/ · Language: zh-Hans

## 包含什么

每个片段保留原有的多视角 RGB、语言指令、本体感觉状态与专家动作序列，并增加与视频对齐的音轨。98.7% 的增强片段经校验满足 100 毫秒同步容差。审核过程中，语义不一致、事件时序不合理或存在明显同步错误的片段被修正或移除。

## 应当如何使用、不应当如何使用

作者对适用范围有明确说明。由于基础全方位骨干已具备广泛的通用音频-视频多模态预训练，OpenX-Sound 被用作机器人特有的音频-视觉-动作时间对齐阶段——不是通用多模态预训练，也不是原生机器人音频的替代品。完全跳过这一阶段会使 HEAR-Bench 从 0.81 降到 0.69，作者将其解读为“收益来自机器人音频-视觉-动作耦合”而非规模。

已声明的局限是合成到真实的差距：视频转音频生成可能遗漏细微的接触线索、改变事件时序，或产生没有物理来源的声音。对于像声音因果操作这样时序敏感的任务，这限制了纯离线预训练能达到的上限，因此在真实录音上微调仍然必要。

## 许可与获取

数据集发布于 Hugging Face。基础轨迹来自 Open X-Embodiment，底层片段的许可请参阅该项目。

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.