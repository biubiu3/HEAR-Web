# OpenX-Sound: Audio-Augmented Robot Trajectories

> OpenX-Sound is a pretraining dataset for Vision-Sound-Language-Action learning. Selected Open X-Embodiment episodes retain their original multi-view RGB video, language instructions, proprioception and expert actions, and are augmented with temporally aligned audio tracks. It exists because the large cross-embodiment datasets that enabled VLA progress contain no synchronised microphone recordings, and collecting robot audio at comparable scale would require hardware standardisation no laboratory has achieved.

Source: https://hear.irmv.top/openx-sound/ · Language: en

## What is in it

Every episode preserves the original multi-view RGB, the language instruction, the proprioceptive state and the expert action sequence, with an added audio track aligned to the video. 98.7% of augmented clips were verified within a 100 ms synchronisation tolerance. Episodes with semantically inconsistent audio, implausible event timing or obvious synchronisation errors were corrected or removed during review.

## How it should and should not be used

The authors are explicit about the scope. Because the base omni-modal backbone already has broad multimodal pretraining on general audio-video data, OpenX-Sound is used as a robotics-specific audio-visual-action temporal-alignment stage — not as generic multimodal pretraining, and not as a replacement for native robot audio. Skipping this stage entirely costs 0.81 to 0.69 on HEAR-Bench, which the paper reads as evidence that the gain is about robotic audio-visual-action coupling rather than scale.

The acknowledged limitation is the synthetic-to-real gap: video-to-audio generation can omit subtle contact cues, shift event timing, or produce sounds without a physical source. For a task as timing-sensitive as sound-causal manipulation, that caps what purely offline pretraining can achieve, which is why fine-tuning on real recordings remains necessary.

## License and access

The dataset is released on Hugging Face. Base trajectories derive from Open X-Embodiment; consult that project's licensing for the underlying episodes.

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.