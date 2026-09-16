# AI Agent Robotics

> AI agent robotics is the combination of a reasoning agent — typically an LLM that plans, calls tools and tracks state — with the low-level policies that actually move a robot. The pattern that has emerged is hierarchical: the agent decides what to do and the robot policy handles how, because a language model cannot produce joint torques and a manipulation policy cannot reason about a multi-minute task.

Source: https://hear.irmv.top/concepts/ai-agent-robotics/ · Language: en

## Why the split exists

The two layers have incompatible requirements. A planning agent benefits from a long context, slow deliberation and access to tools and memory. A manipulation policy must run in a control loop at tens of hertz and cannot afford that deliberation. Trying to make one model do both produces something that is either too slow to control or too shallow to plan.

The layered answer also matches how the fields have specialised: high-level work in language and reasoning, low-level work in imitation learning and action generation.

## Skills as tools

A productive framing is that a robot policy is a tool: the agent registers manipulation skills alongside search, code execution and other capabilities, and invokes them by intent. This makes robot capability composable and inspectable, and lets the agent's planning be evaluated separately from the policy's dexterity. Its known weakness is the handoff — deciding when a skill has finished and what to do when one fails.

## What the agent layer cannot see

A high-level agent observes the world through whatever its tools report. If the low-level policy's sensory interface discards something, the agent's world model is missing it too. A robot that cannot tell when a process actually finished — as opposed to appearing to be finished — cannot report progress accurately, and an agent planning on that report will plan wrongly.

This is where the low-level interface becomes an agent-level concern. Transient evidence that is lost inside an execution gap is not just a control problem; it is missing information in the agent's model of the world.

## Where HEAR fits

HEAR is a low-level action component: a policy that converts streaming perception into joint commands under real-time constraints. Its contribution to the agentic stack is ensuring that the acoustic portion of the world state is not silently dropped between decisions.

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.