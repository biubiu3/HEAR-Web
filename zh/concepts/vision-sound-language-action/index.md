# 视-声-语言-动作（VSLA）

> 视-声-语言-动作（Vision-Sound-Language-Action, VSLA）是一种连续控制范式：机器人在延迟决策回路下，以视觉、流式音频、语言与本体感觉为条件。它把视觉-语言-动作（VLA）从「看见并行动」扩展为「看见、听见、记住并反应」——把原始音频当作第一等的、持续流式输入的观测，而不是执行前的一次性提示。

Source: https://hear.irmv.top/zh/concepts/vision-sound-language-action/ · Language: zh-Hans

## 为什么“声”需要自己的范式

给 VLA 策略加音频，与加一路相机并不对称。视觉状态是持续的：杯子一直在桌上，跨越许多控制周期，因此稍微陈旧的图像仍然有用。声学证据恰恰相反——它集中在短暂、不可重复的事件里。一声咔哒、一阵晃动、一次完成提示音或沸腾转变可能只持续几百毫秒且永不再现。如果策略像采样图像那样采样这个模态，证据就直接消失了。

VSLA 命名的是认真对待这种不对称性的设定：流式音频是观测接口的一部分，而接口必须把它听到的内容保存到决策能够使用为止。

## VSLA 形式化的时序问题

大型机器人策略无法以控制频率运行，因此它们预测一个动作块并以开环方式执行。在这一区间内，新的观测无法改变已发出的指令。论文称之为盲执行间隔（BEI）。对视觉而言这是可以容忍的；对一段短促的声音而言它可能是致命的。提高查询频率可以缩短空档，但无法消除它，因为感知、预处理、推理、通信与执行延迟始终存在。因此瓶颈是证据保持，而不是瞬时抢占。

## 兄弟范式

VSLA 与视觉-触觉-语言-动作（VTLA）模型属于同一家族，后者为观测栈加入触觉。两者都扩展了 VLA 策略的模态集合而没有抛弃其结构。原则上机器人可以同时具备两者。

## HEAR 的位置

HEAR 是 IJRR 论文中给出的 VSLA 实例。它的四个组件对应范式的各项要求：Historizer 提供跨越 BEI 的因果保持，Envisioner 进行多感官推理，Advancer 以音频世界模型的形式提供时间对齐，Realizer 生成平滑的动作块。

## 常见问题

**VSLA 是什么的缩写？**

Vision-Sound-Language-Action（视-声-语言-动作）。它是视觉-语言-动作（VLA）与视觉-触觉-语言-动作（VTLA）在听觉上的兄弟。

**VSLA 只是“VLA 加音频”吗？**

不是。区别在时间而不在模态。VLA 策略假定任务相关证据在视觉上持续存在、可以低频采样；VSLA 把流式音频当作必须在延迟、分块执行中存活下来的观测——这需要记忆与时序机制，而单纯增加一个输入通道并不提供这些。

**VSLA 是谁提出的？**

该范式在 HEAR 论文中形式化，作者为 Chang Nie、Tianchen Deng、Guangming Wang、Zhe Liu、Hesheng Wang，已被《The International Journal of Robotics Research》录用（2026），arXiv:2603.16086。

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.