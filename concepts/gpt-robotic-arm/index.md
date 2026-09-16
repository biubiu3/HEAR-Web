# GPT and Large Models for Robotic Arms

> “GPT robotic arm” describes a robot arm controlled by a large pretrained model. That happens at two levels: a language model can plan and sequence a task in words, and a vision-language-action (VLA) model — a multimodal backbone fine-tuned to emit actions — can drive the arm directly. Both work. Neither automatically solves the problem of acting correctly on brief physical events.

Source: https://hear.irmv.top/concepts/gpt-robotic-arm/ · Language: en

## Level one: planning

A language model can decompose “make coffee” into steps, choose tools, and recover from some failures, because that reasoning is largely symbolic. It has no access to joint angles and does not need them. This level is well established and mostly a software-integration problem.

## Level two: direct action

A VLA model takes images, an instruction and proprioception as input and outputs continuous actions. It works because the backbone's pretraining has already produced representations in which visual scenes and language are aligned, and a comparatively small amount of robot data suffices to attach an action head. This is where most current capability lives, and where the interesting failure modes are.

## The timing problem large models bring with them

A model that can plan beautifully is still far too slow to run at control frequency. The standard workaround — predict a chunk of actions and execute it open-loop — means the arm is following instructions that cannot be revised for a second or more. Anything the robot needs to notice inside that window is invisible to it.

For visual tasks this is usually tolerable, because what the camera saw a second ago is mostly still true. For events it is not: a click, a beep, a rattle or a spoken interruption can begin and end inside the window and leave no trace in any later observation.

## What is needed beyond a bigger model

Scale does not fix this, because the problem is not representational capacity but interface design. What helps is a sensory interface that accumulates rather than samples: a causal memory of what was heard, maintained across the execution gap, so that the next decision can act on an event that is no longer audible. The HEAR framework is one implementation of that idea, together with an evaluation protocol that refuses to score a visually plausible but acoustically premature action as a success.

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.