# Robot Audition for Manipulation

> Robot audition is the robotics counterpart of computational auditory scene analysis: using microphones mounted on a robot to interpret environmental sound — including non-speech events — for control and interaction. In manipulation, audition is valuable because it reports events rather than states: contact, completion, hidden contents and process transitions are all more directly audible than visible.

Source: https://hear.irmv.top/concepts/robot-audition/ · Language: en

## What sound tells a manipulator that vision cannot

Many state changes in manipulation are expressed most directly through sound. A click reveals contact. A rattle exposes hidden contents. A beep marks completion. A sputtering process signals that an unseen transition has occurred. A traditional Moka pot, for instance, has no electronic sensor and no discrete visual indicator of completion — the only reliable signal that extraction is finished is the change in the sound of the pot.

This makes audition a low-cost proxy for information that would otherwise require tactile sensing, force sensing or instrumentation of the object.

## The main branches

Passive contact acoustics. Listening to the sound produced by contact between tool and object. Timbre carries information about material, grasp quality and object state — earlier work used this to estimate material properties from impact and to assess grasp gentleness.

Contact microphones. Piezoelectric sensors mounted in the gripper or finger provide a much higher signal-to-noise ratio than ambient microphones and behave as a cheap tactile substitute. Prior work has used them for slip detection, contact localisation and material classification.

Active acoustic sensing. Rather than waiting for a sound, the robot deliberately generates one — shaking a container, tapping a surface — and reads the response. This turns an unobservable hidden state into an observable one. HEAR's Shake Bottle task is an instance.

Speech and prosody. Commands and confirmations carry intent not only in their words but in their intonation, which transcription discards.

## Why audition has lagged behind vision

Three reasons. First, hardware: most robots have no microphone, and the large cross-embodiment datasets that powered VLA progress contain no synchronised audio. Second, interfaces: the common way to feed sound to a policy is to transcribe it with ASR, which discards every non-speech cue, or to render the waveform as an image, which flattens a temporal signal into a static snapshot. Third, timing: the events that matter are short and non-repeatable, which interacts badly with the low-frequency, chunked execution of large policies.

## Where HEAR fits

HEAR takes the third problem as its subject. It does not propose a new acoustic sensor; it proposes an interface that can hold a fleeting auditory event long enough for a slow policy to act on it, and a benchmark that checks whether the resulting behaviour is genuinely sound-causal rather than visually plausible.

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.