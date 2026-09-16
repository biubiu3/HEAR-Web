# HEAR-Bench: Sound-Causal Manipulation Benchmark

> HEAR-Bench is a simulation benchmark for sound-centric manipulation, built on the dual-arm RoboTwin 2.0 platform. It supplies a streaming microphone channel and enforces a sound-causal success rule: a trial counts as successful only if the robot completes the physical goal after the required acoustic condition has occurred. Reaching the goal early — which standard benchmarks would score as success — is recorded as a failure.

Source: https://hear.irmv.top/benchmark/ · Language: en

## Why a timing-aware benchmark is necessary

Standard manipulation benchmarks evaluate whether the final geometric state was reached. On a sound-gated task, that metric cannot tell the difference between a policy that waited for the cue and a policy that ignored sound entirely and moved on a visual heuristic. HEAR-Bench closes that gap by making the acoustic precondition part of the success predicate. This is the property that makes it possible to measure whether a policy is genuinely sound-causal.

## Task suite

Seven simulation tasks cover four categories of decision-critical acoustic cue. Cue timings and initial visual states are randomised so that policies cannot memorise a fixed schedule, and each task is evaluated over 100 independent trials.

## Four categories of cue

Event-triggered alarms test waiting and transient capture: Alarm Clock requires suppressing a visually tempting early press until a ring begins, and Microwave requires capturing a brief completion beep that can fall entirely inside an execution gap.

Human speech tests timing and prosody: Check Yes uses identical text with different intonation to defeat pure ASR, and Interrupt places a spoken override at a random moment to test safe mode switching mid-motion.

Continuous process sounds test long-horizon monitoring: Pour Water and Boil Water require tracking gradual acoustic evolution while vision is weak or static.

Physical interaction feedback tests contact acoustics: Check Materials uses visually similar objects so that impact timbre is the only discriminative signal.

## How it is used

All evaluated methods share the same observation interface and the same two-stage training recipe (pretraining on OpenX-Sound, then task-specific fine-tuning), so differences reflect architecture rather than data volume. Under this protocol HEAR reaches 81% average sound-causal success, against 61% for the strongest waveform-as-image VLA baseline, 35% for the strongest ASR baseline and 14% for the strongest vision-only backbone.

## Reproducing it

The HEAR-Bench implementation is part of the code release, built on top of RoboTwin 2.0, and the task audio assets ship with it. See OpenX-Sound for the pretraining half of the pipeline.

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.