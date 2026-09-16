# Robot Foundation Models

> A robot foundation model is a large model pretrained on data from many robots and tasks, then fine-tuned — or prompted — for a specific one. The pattern is borrowed from language and vision, and it works for the same reason: broad pretraining produces representations that transfer, so downstream learning needs far less data.

Source: https://hear.irmv.top/concepts/robot-foundation-models/ · Language: en

## The pretraining recipe

A large multimodal backbone, usually a vision-language model, is adapted to emit actions. Training proceeds in stages: broad multimodal pretraining, then robot-specific pretraining on a cross-embodiment corpus, then task-specific fine-tuning. The first stage provides general perception and language grounding; the second provides the coupling between perception and physical action that no amount of internet data supplies.

Cross-embodiment corpora — Open X-Embodiment and its successors — are what make the second stage possible. They aggregate trajectories from many robot platforms and tasks under a shared format.

## What the corpora do not contain

Vision, language, proprioception and actions. Not force. Not touch. Not audio. This is not an oversight so much as a hardware problem: collecting synchronised microphone, tactile or force data at the scale of a cross-embodiment corpus would require standardisation across every contributing laboratory.

The consequence is that foundation models inherit a vision-centric world view, and every additional modality has to solve its own data problem before it can be trained on. HEAR's OpenX-Sound is one such solution for audio: rather than standardising hardware, it augments existing episodes with temporally aligned synthesised audio, and is explicit that this is a bootstrapping stage rather than a substitute for real recordings.

## Real-time constraints

Foundation models are large, robot control is fast, and the gap is bridged by action chunking. That makes the Blind Execution Interval a property of the whole class, not of any one model: any policy big enough to need chunking also has an interval in which it cannot react.

## Where HEAR fits

HEAR is a foundation-model-style policy whose pretraining stage adds the audio modality. Its contribution to the class is showing that the interface, not just the backbone, determines whether transient sensory events survive long enough to matter.

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.