# Research Context: Where HEAR Sits

> HEAR is a Vision-Sound-Language-Action (VSLA) framework for sound-centric robot manipulation. It extends the Vision-Language-Action (VLA) family by adding streaming audio as a first-class observation, and it connects to world-model research through its Advancer component, which is formulated as an audio world model. This page states plainly where the work stands in each of the neighbouring research directions.

Source: https://hear.irmv.top/research-context/ · Language: en

## Vision-Language-Action (VLA)

VLA models map images, language and robot state to continuous actions and are the dominant architecture for general-purpose manipulation. HEAR is a VLA-family policy: it keeps the same observation-interface shape, adds a streaming audio channel, and studies what happens to that interface when decisions are delayed and actions are executed in open-loop chunks. HEAR is evaluated against OpenVLA and π0.5 backbones, each equipped with three audio interfaces (raw 1D waveform, waveform-as-image adapter, and ASR transcript) so that the comparison isolates the interface rather than the backbone.

## Multi-sensory VLAs

A clear recent trend is extending the modality set of VLA policies. Vision-tactile-language-action (VTLA) models add touch to the observation stack; force-aware and contact-rich policies do the same for force. VSLA is the same move for hearing: sound becomes a continuously streaming observation rather than a pre-execution instruction or an after-the-fact check. VSLA and VTLA are siblings, not competitors — a robot could carry both.

## World models and World Action Models (WAM)

World-model-based policies learn how a scene evolves, not only how to react to it. HEAR's Advancer is formulated as an audio world model: it predicts near-future discrete audio codes from latent representations, so the latent state encodes acoustic progression rather than only current loudness. This is what keeps the policy stable through long, visually quasi-static waiting phases. Because the Advancer is a training-time objective that is removed at deployment, HEAR couples predictive state modelling with action generation without adding inference cost.

## Physical AI and embodied intelligence

HEAR targets embodied agents acting in the physical world — the setting usually described as physical AI or embodied intelligence. Its subject is the agent's sensory interface: a robot that must know when contact occurred, when a process changed state, or when an external event demands a response. Auditory perception complements vision as a practical sensing modality for physical interaction, because many state changes are expressed most directly through sound.

## Real-time, asynchronous and chunked control

A large body of recent work attacks the latency and staleness of action-chunked policies: asynchronous inference, real-time chunking, adaptive chunk lengths, speculative execution. HEAR studies the same execution gap from the other side. The question is not when the policy runs, but which evidence is lost while it is not running. The Blind Execution Interval is a sensory problem, not only a compute problem — re-querying faster shortens the gap but cannot eliminate it, because sensing, preprocessing, inference, communication and actuation latency all remain.

## Robot audition and contact acoustics

Sound has a long history in robotics, largely separate from the VLA wave: material estimation from impact acoustics, grasp-stability assessment from contact sound, contact microphones as a cheap proxy for tactile sensing, and active acoustic probing in which the robot deliberately generates a sound to interrogate an object. HEAR builds on that literature and asks a question those systems do not: how to keep a fleeting acoustic event alive until a slow, chunked policy can act on it.

## Frequently asked questions

**Is HEAR a VLA model?**

HEAR is a VLA-family policy with an extended observation interface. It keeps the vision-language-action mapping and adds streaming audio and proprioception, which is why the paper names the resulting setting Vision-Sound-Language-Action (VSLA) rather than claiming to replace VLA.

**Is HEAR a world model?**

HEAR contains a world-model component but is not itself a pure world model. The Advancer predicts near-future audio codes during training, which couples predictive state modelling to action generation. It is removed at deployment, so the shipped policy is a reactive VLA-style controller whose latent space encodes acoustic dynamics.

**How is HEAR different from audio-language models?**

Audio-language models reason about audio offline. HEAR is a closed-loop controller under delayed, chunked execution, and its evaluation rejects actions that reach the goal before the required sound has occurred.

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.