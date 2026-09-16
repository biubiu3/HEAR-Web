# Audio World Models

> An audio world model is a model that predicts how an acoustic scene will evolve, rather than only classifying or reacting to its present state. In HEAR, the Advancer component is formulated as an audio world model: it predicts near-future discrete audio codes from latent representations, which injects explicit temporal grounding into a robot policy.

Source: https://hear.irmv.top/concepts/audio-world-model/ · Language: en

## From reacting to anticipating

A purely reactive policy learns a mapping from current observation to action. A world model learns the dynamics instead: given the present, what comes next? For robotics this matters because many tasks have visually identical states that imply different correct behaviours, and the only thing distinguishing them is which direction the process is moving.

Cooking is the clearest case. A pot of water being heated looks similar at many moments, but the correct action depends entirely on how far the process has progressed. A model that can only see “water, pot, heat” cannot distinguish “nearly boiling” from “barely warm”. A model that predicts the next few seconds of sound can.

## Why audio specifically

Audio is an unusually good carrier for this kind of progress signal. Continuous processes — boiling, pouring, grinding, sputtering — have characteristic acoustic signatures that evolve in a structured way, and the evolution is audible before it is visually obvious. Acoustic signals also have high temporal resolution relative to camera frames, so the rate of change is directly observable.

## How HEAR uses one

The Advancer predicts near-future discrete audio codes during training. This forces the policy's latent representation to encode not just what is audible now but how it is changing, which is what keeps the policy stable during long waiting phases where vision is quasi-static — a failure mode related to temporal motion collapse in chunked policies.

Crucially, the Advancer is a training-time objective and is removed at deployment. The temporal structure it teaches stays in the latent space, so inference cost is unchanged. Ablating it costs 0.81 to 0.73 on HEAR-Bench.

## Where it sits in the world-model landscape

Most world-model work for robotics predicts future images or future latent states. Predicting in the audio modality is less common, and it complements rather than replaces visual world modelling: vision reports what the scene looks like, audio reports what is happening to it.

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.