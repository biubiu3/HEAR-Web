# Blind Execution Interval (BEI)

> The Blind Execution Interval (BEI) is the interval created when a robot policy predicts an action chunk and executes it open-loop. Because new sensor observations cannot alter the command sequence already being sent to the robot, a transient event — a beep, a click, a rattle, a collision — can occur and finish entirely inside that interval and never influence a decision.

Source: https://hear.irmv.top/concepts/blind-execution-interval/ · Language: en

## Where the interval comes from

Modern robot policies are large and cannot run at control frequency. The standard solution is action chunking: predict a short sequence of future actions, then execute it without waiting for new sensor updates, which hides inference latency and keeps motion smooth. The interval is not a bug in any particular implementation; it is a structural consequence of the architecture.

On the authors' Franka Panda deployment the executed action-chunk interval is about 2.1 seconds and the effective BEI is about 2.3 seconds — so a quarter of the time, roughly, the robot is acting on an observation it can no longer update.

## Why vision tolerates it and audio does not

Visual and auditory information are distributed over time in opposite ways. Objects persist: a drawer that was open is still open a second later, so a stale image is degraded but not empty. Acoustic events do not persist. A completion beep lasts a fraction of a second; once it has passed, no later observation window contains it. A memoryless audio interface therefore does not receive a stale version of the cue — it receives nothing.

## Why faster re-querying is not the fix

It is tempting to treat the BEI as a latency problem and attack it by querying more often. That helps but cannot close the gap: sensing, preprocessing, inference, communication and actuation latency all remain, and aggressive replanning introduces discontinuities and robot ego-noise — which is counterproductive when the robot is trying to listen. The paper's conclusion is that the bottleneck is evidence preservation: a short acoustic event must remain available at the first decision boundary after it occurs.

## Related problems in the same family

Work on asynchronous inference, real-time chunking, adaptive chunk horizons and speculative execution addresses the same gap from the scheduling side — changing when the policy runs. The BEI frames the complementary question of which evidence is lost while it does not run. Both are real, and fixing one does not fix the other.

## How HEAR addresses it

HEAR's Historizer is a streaming stateful transformer that maintains a compact causal audio memory across execution gaps, so a cue that has already vanished from the audio stream still conditions the next decision. It is the single most important component in ablation: removing it drops HEAR-Bench average success from 0.81 to 0.57.

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.