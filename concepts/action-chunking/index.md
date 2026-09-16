# Action Chunking

> Action chunking is the practice of predicting a short sequence of future actions at once — a “chunk” — and executing it open-loop, without waiting for new sensor observations. It is near-universal in modern robot policies because it hides inference latency and produces smoother motion. Its cost is a perception gap: for the duration of the chunk, the robot cannot react to anything.

Source: https://hear.irmv.top/concepts/action-chunking/ · Language: en

## Why it exists

Large robot policies are expensive to evaluate. Predicting one action at a time and re-running the model before every low-level command is not feasible at control frequency. Chunking amortises a single forward pass across many control steps. It was popularised by transformer-based imitation learning and is now standard in both diffusion-policy and flow-matching action heads.

The side benefit is motion quality. Because the whole chunk is generated jointly, the resulting trajectory is internally consistent rather than a stitched sequence of independent decisions, which reduces jitter.

## The cost

During execution the policy is blind by construction. Observations arriving mid-chunk cannot alter the commands already being sent. For slow, visually persistent tasks this is usually fine. For tasks where the decisive evidence is a short event — a contact, a beep, a spoken interruption, a collision — it means the evidence may be missed entirely.

The HEAR paper names this the Blind Execution Interval. Its point is not that chunking is wrong, but that the interval has a modality-dependent cost: harmless for vision, potentially fatal for audio.

## The standard remedies, and their limits

Shortening the chunk reduces the gap but degrades smoothness and increases compute. Re-querying more often has the same trade-off. More recent approaches — asynchronous inference, real-time chunking, adaptive horizons, speculative execution — restructure when the model runs, and help significantly. None of them eliminates the gap, because the latency chain from sensing to actuation remains.

The complementary fix, and the one HEAR takes, is on the input side: make the observation interface remember. If incoming audio is accumulated into a causal memory rather than sampled per query, a cue that occurred mid-chunk is still available at the next decision boundary even though it is no longer audible.

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.