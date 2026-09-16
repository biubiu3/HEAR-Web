# Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation

> This is the publication record for the HEAR paper: a Vision-Sound-Language-Action (VSLA) framework for sound-centric robot manipulation, accepted for publication in The International Journal of Robotics Research (IJRR). The paper formalizes the Blind Execution Interval (BEI) — the timing gap created by system latency and open-loop action chunking in which a transient acoustic cue can appear and vanish between two policy queries — and introduces the four-module HEAR architecture that preserves acoustic evidence across that gap.

Source: https://hear.irmv.top/paper/ · Language: en

## Authors and affiliation

Chang Nie, Tianchen Deng, Zhe Liu and Hesheng Wang are with the School of Automation and Intelligent Sensing at Shanghai Jiao Tong University and the Shanghai Key Laboratory of Navigation and Location Based Services, China. Guangming Wang is with the Department of Engineering at the University of Cambridge, UK. The corresponding author is Hesheng Wang.

## Publication status

The article is accepted for publication in The International Journal of Robotics Research (ISSN 0278-3649), published by SAGE Publications. The archival DOI has not yet been assigned. The preprint is permanently available on arXiv as arXiv:2603.16086 (cs.RO), first posted 17 March 2026.

## Abstract

Humans and animals use sound as a crucial cue for interacting with the physical world, as acoustic events can reveal contact, completion, hidden contents, or process state. Embodied agents should similarly benefit from auditory awareness during manipulation, yet existing Vision-Language-Action (VLA) policies typically rely on persistent visual observations, while audio-aware variants often treat audio as speech, waveform renderings, or fixed pre-execution context. Such interfaces can miss transient sounds, such as beeps, clicks, rattles, or collision cues, especially under system latency and open-loop action chunking.

We formalize this timing failure as the Blind Execution Interval (BEI), in which critical acoustic evidence may occur after an action chunk begins but disappear before the next policy update. To address this challenge, we introduce Vision-Sound-Language-Action (VSLA), a continuous control paradigm conditioned on vision, streaming audio, language, and proprioception under delayed decision loops. We further present HEAR, a VSLA framework that preserves causal auditory context across execution gaps, performs multimodal reasoning, models near-future audio dynamics during training, and generates smooth action chunks for closed-loop manipulation.

To support learning and evaluation, we introduce OpenX-Sound for robotics-specific audio-visual-action pretraining and HEAR-Bench, a benchmark for sound-centric manipulation with strict causal timing constraints. On HEAR-Bench, HEAR achieves an 81% success rate, outperforming waveform, ASR, and compact audio-native baselines, and reaches 70% sound-causal success across four real-world Franka tasks. These results show that robust sound-centric manipulation requires not only native audio input, but also causal auditory persistence and explicit temporal grounding.

## How to cite

A ready-to-fetch BibTeX file is served at /cite.bib. The long key is {bibtex_key} and the short key is {bibtex_key_short}. A plain-text citation is: Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.

## Companion artifacts

The paper is released together with four artifacts: the code release (Apache-2.0), the OpenX-Sound pretraining dataset, three pretrained checkpoints, and the HEAR-Bench benchmark built on RoboTwin 2.0. See the dataset page and the benchmark page.

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.