# Physical AI and Embodied Intelligence

> Physical AI and embodied intelligence are the terms now used for AI systems that perceive and act in the physical world through sensors and actuators, rather than producing text or images. For robot manipulation, the interesting content behind the labels is a set of concrete engineering problems: how a policy's sensory interface should be shaped, how it behaves when decisions are delayed, and where the training data comes from.

Source: https://hear.irmv.top/concepts/physical-ai/ · Language: en

## The label and the substance

Physical AI is the industry framing; embodied intelligence is the more academic one. Both point at the same shift: a language model predicts the next token, whereas a physical agent must predict the consequences of its own actions on a world that pushes back. That difference is not cosmetic — it changes what a model needs to represent. Mass, friction, inertia and contact are not in the training distribution of text.

## What is genuinely hard

Data. Internet text and video are abundant and third-person. A robot needs first-person data: “what does the world become after I do this?” That data is expensive to collect, and the largest cross-embodiment datasets still contain no synchronised audio, force or touch.

Sensory interfaces. Most work assumes vision is sufficient. It is not: contact, force and hidden internal state are invisible to cameras, and the modalities that do report them each have their own temporal structure that a policy must be built to handle.

Timing. Physical agents run under latency, and their most capable policies run slowly. Anything that must be noticed between two decisions — which includes every short event — falls into the gap.

Evaluation. Reaching a goal is not the same as behaving correctly. A policy that ignores an auditory precondition and moves on a visual heuristic can look successful on a geometric metric while being wrong in the way that matters.

## Where HEAR fits

HEAR is a physical-AI system in the narrow sense that it is a closed-loop controller for a real robot arm, and in a more specific sense that it works on the sensory-interface problem. Its claim is that for agents acting under delayed, chunked control, preserving transient evidence is a requirement rather than an optional refinement — and that audition is the modality where its absence is most visible.

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.