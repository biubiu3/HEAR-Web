"""English page content for the HEAR site.

Consumed by seo/build.py. Numbers and identifiers must NOT be written here —
they are pulled from seo/facts.yaml at build time so every page quotes the
same figure. This module holds prose only.

Page shape:
    slug        URL path (no leading/trailing slash); "" is the site root
    title       <title> text
    description <meta name="description">
    h1          visible H1
    lede        answer-first paragraph, must stand alone when quoted
    sections    list of (heading, [paragraphs])
    faq         optional list of (question, answer)
    keywords    meta keywords for this page
    schema      optional extra JSON-LD node types
"""

# --------------------------------------------------------------------------
# /paper/  — Google Scholar landing page
# --------------------------------------------------------------------------
PAPER = {
    "slug": "paper",
    "title": "HEAR (IJRR 2026) — Paper, Abstract and Citation | Vision-Sound-Language-Action",
    "description": "The HEAR paper: \"Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation\", accepted at The International Journal of Robotics Research. Abstract, authors, BibTeX and links to code, dataset and benchmark.",
    "h1": "Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation",
    "lede": (
        "This is the publication record for the HEAR paper: a Vision-Sound-Language-Action (VSLA) framework for "
        "sound-centric robot manipulation, accepted for publication in <i>The International Journal of Robotics "
        "Research</i> (IJRR). The paper formalizes the Blind Execution Interval (BEI) — the timing gap created by "
        "system latency and open-loop action chunking in which a transient acoustic cue can appear and vanish "
        "between two policy queries — and introduces the four-module HEAR architecture that preserves acoustic "
        "evidence across that gap."
    ),
    "sections": [
        ("Authors and affiliation", [
            "Chang Nie, Tianchen Deng, Zhe Liu and Hesheng Wang are with the School of Automation and Intelligent "
            "Sensing at Shanghai Jiao Tong University and the Shanghai Key Laboratory of Navigation and Location "
            "Based Services, China. Guangming Wang is with the Department of Engineering at the University of "
            "Cambridge, UK. The corresponding author is Hesheng Wang.",
        ]),
        ("Publication status", [
            "The article is accepted for publication in <i>The International Journal of Robotics Research</i> "
            "(ISSN 0278-3649), published by SAGE Publications. The archival DOI has not yet been assigned. "
            "The preprint is permanently available on arXiv as <code>arXiv:2603.16086</code> (cs.RO), first posted "
            "17 March 2026.",
        ]),
        ("Abstract", [
            "Humans and animals use sound as a crucial cue for interacting with the physical world, as acoustic "
            "events can reveal contact, completion, hidden contents, or process state. Embodied agents should "
            "similarly benefit from auditory awareness during manipulation, yet existing Vision-Language-Action "
            "(VLA) policies typically rely on persistent visual observations, while audio-aware variants often "
            "treat audio as speech, waveform renderings, or fixed pre-execution context. Such interfaces can miss "
            "transient sounds, such as beeps, clicks, rattles, or collision cues, especially under system latency "
            "and open-loop action chunking.",
            "We formalize this timing failure as the Blind Execution Interval (BEI), in which critical acoustic "
            "evidence may occur after an action chunk begins but disappear before the next policy update. To "
            "address this challenge, we introduce Vision-Sound-Language-Action (VSLA), a continuous control "
            "paradigm conditioned on vision, streaming audio, language, and proprioception under delayed decision "
            "loops. We further present HEAR, a VSLA framework that preserves causal auditory context across "
            "execution gaps, performs multimodal reasoning, models near-future audio dynamics during training, and "
            "generates smooth action chunks for closed-loop manipulation.",
            "To support learning and evaluation, we introduce OpenX-Sound for robotics-specific audio-visual-action "
            "pretraining and HEAR-Bench, a benchmark for sound-centric manipulation with strict causal timing "
            "constraints. On HEAR-Bench, HEAR achieves an 81% success rate, outperforming waveform, ASR, and compact "
            "audio-native baselines, and reaches 70% sound-causal success across four real-world Franka tasks. "
            "These results show that robust sound-centric manipulation requires not only native audio input, but "
            "also causal auditory persistence and explicit temporal grounding.",
        ]),
        ("How to cite", [
            "A ready-to-fetch BibTeX file is served at <a href=\"/cite.bib\">/cite.bib</a>. The long key is "
            "<code>{bibtex_key}</code> and the short key is <code>{bibtex_key_short}</code>. "
            "A plain-text citation is: Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, "
            "“Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric "
            "Manipulation”, <i>The International Journal of Robotics Research</i>, 2026. arXiv:2603.16086.",
        ]),
        ("Companion artifacts", [
            "The paper is released together with four artifacts: the code release (Apache-2.0), the OpenX-Sound "
            "pretraining dataset, three pretrained checkpoints, and the HEAR-Bench benchmark built on RoboTwin 2.0. "
            "See the <a href=\"/openx-sound/\">dataset page</a> and the <a href=\"/benchmark/\">benchmark page</a>.",
        ]),
    ],
    "keywords": "HEAR paper, HEAR IJRR, Vision-Sound-Language-Action paper, VSLA paper, sound-centric manipulation paper, arXiv 2603.16086, Nie Deng Wang Liu Wang, robot manipulation paper 2026, Google Scholar, BibTeX",
    "schema": ["ScholarlyArticle"],
}

# --------------------------------------------------------------------------
# /research-context/
# --------------------------------------------------------------------------
RESEARCH_CONTEXT = {
    "slug": "research-context",
    "title": "Research Context: Where HEAR Sits in VLA, World Models and Embodied AI",
    "description": "How the HEAR sound-centric manipulation framework relates to Vision-Language-Action models, world models and World Action Models (WAM), physical AI, embodied intelligence, agentic robotics, robot audition and action-chunking research.",
    "h1": "Research Context: Where HEAR Sits",
    "lede": (
        "HEAR is a Vision-Sound-Language-Action (VSLA) framework for sound-centric robot manipulation. It extends "
        "the Vision-Language-Action (VLA) family by adding streaming audio as a first-class observation, and it "
        "connects to world-model research through its Advancer component, which is formulated as an audio world "
        "model. This page states plainly where the work stands in each of the neighbouring research directions."
    ),
    "sections": [
        ("Vision-Language-Action (VLA)", [
            "VLA models map images, language and robot state to continuous actions and are the dominant architecture "
            "for general-purpose manipulation. HEAR is a VLA-family policy: it keeps the same observation-interface "
            "shape, adds a streaming audio channel, and studies what happens to that interface when decisions are "
            "delayed and actions are executed in open-loop chunks. HEAR is evaluated against OpenVLA and π0.5 "
            "backbones, each equipped with three audio interfaces (raw 1D waveform, waveform-as-image adapter, and "
            "ASR transcript) so that the comparison isolates the interface rather than the backbone.",
        ]),
        ("Multi-sensory VLAs", [
            "A clear recent trend is extending the modality set of VLA policies. Vision-tactile-language-action "
            "(VTLA) models add touch to the observation stack; force-aware and contact-rich policies do the same for "
            "force. VSLA is the same move for hearing: sound becomes a continuously streaming observation rather "
            "than a pre-execution instruction or an after-the-fact check. VSLA and VTLA are siblings, not "
            "competitors — a robot could carry both.",
        ]),
        ("World models and World Action Models (WAM)", [
            "World-model-based policies learn how a scene evolves, not only how to react to it. HEAR's Advancer is "
            "formulated as an <b>audio world model</b>: it predicts near-future discrete audio codes from latent "
            "representations, so the latent state encodes acoustic progression rather than only current loudness. "
            "This is what keeps the policy stable through long, visually quasi-static waiting phases. Because the "
            "Advancer is a training-time objective that is removed at deployment, HEAR couples predictive state "
            "modelling with action generation without adding inference cost.",
        ]),
        ("Physical AI and embodied intelligence", [
            "HEAR targets embodied agents acting in the physical world — the setting usually described as physical AI "
            "or embodied intelligence. Its subject is the agent's <i>sensory interface</i>: a robot that must know "
            "when contact occurred, when a process changed state, or when an external event demands a response. "
            "Auditory perception complements vision as a practical sensing modality for physical interaction, "
            "because many state changes are expressed most directly through sound.",
        ]),
        ("Real-time, asynchronous and chunked control", [
            "A large body of recent work attacks the latency and staleness of action-chunked policies: asynchronous "
            "inference, real-time chunking, adaptive chunk lengths, speculative execution. HEAR studies the same "
            "execution gap from the other side. The question is not <i>when</i> the policy runs, but <b>which "
            "evidence is lost while it is not running</b>. The Blind Execution Interval is a sensory problem, not "
            "only a compute problem — re-querying faster shortens the gap but cannot eliminate it, because sensing, "
            "preprocessing, inference, communication and actuation latency all remain.",
        ]),
        ("Robot audition and contact acoustics", [
            "Sound has a long history in robotics, largely separate from the VLA wave: material estimation from "
            "impact acoustics, grasp-stability assessment from contact sound, contact microphones as a cheap proxy "
            "for tactile sensing, and active acoustic probing in which the robot deliberately generates a sound to "
            "interrogate an object. HEAR builds on that literature and asks a question those systems do not: how to "
            "keep a fleeting acoustic event alive until a slow, chunked policy can act on it.",
        ]),
    ],
    "faq": [
        ("Is HEAR a VLA model?",
         "HEAR is a VLA-family policy with an extended observation interface. It keeps the vision-language-action "
         "mapping and adds streaming audio and proprioception, which is why the paper names the resulting setting "
         "Vision-Sound-Language-Action (VSLA) rather than claiming to replace VLA."),
        ("Is HEAR a world model?",
         "HEAR contains a world-model component but is not itself a pure world model. The Advancer predicts "
         "near-future audio codes during training, which couples predictive state modelling to action generation. "
         "It is removed at deployment, so the shipped policy is a reactive VLA-style controller whose latent space "
         "encodes acoustic dynamics."),
        ("How is HEAR different from audio-language models?",
         "Audio-language models reason about audio offline. HEAR is a closed-loop controller under delayed, chunked "
         "execution, and its evaluation rejects actions that reach the goal before the required sound has occurred."),
    ],
    "keywords": "HEAR research context, VSLA vs VLA, VLA robot manipulation, world model robotics, world action model WAM, audio world model, physical AI, embodied intelligence, embodied agent, agentic robotics, robot audition, action chunking, asynchronous inference, multisensory VLA, VTLA",
}

# --------------------------------------------------------------------------
# /research-landscape/
# --------------------------------------------------------------------------
RESEARCH_LANDSCAPE = {
    "slug": "research-landscape",
    "title": "Robot Manipulation Research Landscape: VLA, World Models, Multi-Sensory Policies",
    "description": "A map of the current robot manipulation research landscape — Vision-Language-Action models, world models and World Action Models, multi-sensory policy families, action chunking and real-time control — and where sound-centric manipulation and HEAR fit.",
    "h1": "Robot Manipulation Research Landscape",
    "lede": (
        "Robot manipulation research currently organises around a few large ideas: Vision-Language-Action (VLA) "
        "policies that map perception and language directly to continuous actions; world models that predict how a "
        "scene will evolve; multi-sensory extensions that add touch, force or sound to the observation stack; and a "
        "family of techniques for making large policies run under real-time constraints. This page is a map of "
        "those directions and of the slice HEAR works in."
    ),
    "sections": [
        ("1. Vision-Language-Action policies", [
            "The dominant architecture for general-purpose manipulation. A large pretrained multimodal backbone is "
            "conditioned on camera images, a language instruction and proprioception, and predicts actions directly. "
            "The field's shared engineering problem is that these models are expensive, so they cannot run at "
            "control frequency — which leads directly to the next two sections.",
        ]),
        ("2. Action generation and chunking", [
            "To hide inference latency and keep motion smooth, policies predict a short sequence of future actions "
            "(“a chunk”) and execute it open-loop. Diffusion policy and flow matching are the two dominant "
            "generative recipes for producing those chunks, with flow matching now the more common default because "
            "it needs fewer integration steps. Chunking solves the smoothness problem and creates a perception "
            "problem: during the chunk, new sensor readings cannot change the commands already being sent.",
        ]),
        ("3. World models and World Action Models", [
            "World-model-based approaches learn the dynamics of a scene, often by predicting future observations in "
            "pixel space, latent space or token space. When the same model also emits actions, the resulting system "
            "is increasingly called a World Action Model (WAM): it targets the joint distribution of future state "
            "and action rather than the reactive mapping from current observation to action. The practical appeal is "
            "generalisation; the practical difficulty is that predicted futures must be physically consistent, and "
            "errors compound over long horizons.",
        ]),
        ("4. Multi-sensory policy families", [
            "Vision alone cannot observe contact, force or hidden internal state. A growing family of policies adds "
            "modalities: vision-tactile-language-action (VTLA) for touch, force-aware policies for contact-rich "
            "tasks, and — the branch HEAR works in — audio. Sound is unusual among these modalities because it is "
            "temporally sparse: it carries little information during quiet periods and concentrates it into very "
            "short events.",
        ]),
        ("5. Real-time and asynchronous control", [
            "Work on asynchronous inference, real-time chunking, adaptive chunk horizons and speculative execution "
            "all targets the same issue: a chunked policy's decisions are stale by construction. These methods "
            "change <i>when</i> the policy runs. HEAR addresses the complementary question of what sensory evidence "
            "is destroyed in the meantime, and shows that for transient acoustic events the answer is "
            "“all of it” unless the interface is changed.",
        ]),
        ("6. Data, benchmarks and evaluation", [
            "Progress in this field tracks the availability of large cross-embodiment datasets and of benchmarks "
            "that measure the right thing. Standard manipulation benchmarks evaluate final geometric success, which "
            "cannot distinguish a policy that listened from one that happened to move correctly. Sound-centric "
            "manipulation needs timing-aware success rules: HEAR-Bench marks a trial as failed if the robot reaches "
            "the goal before the required acoustic cue has occurred.",
        ]),
        ("Where sound-centric manipulation fits", [
            "Sound-centric manipulation is a narrow but well-defined slice: tasks whose correctness depends on "
            "<i>when</i> a sound occurred. It matters because audition is the modality that reports events rather "
            "than states — contact, completion, transitions, hidden contents — and because those events are exactly "
            "what a chunked, delayed policy tends to miss.",
        ]),
    ],
    "keywords": "robot manipulation research, VLA landscape, robot learning survey, world model robotics, WAM world action model, action chunking, flow matching, diffusion policy, multisensory robot policies, VTLA vision tactile language action, robot audition, robotic manipulation benchmarks, embodied AI research directions",
}

# --------------------------------------------------------------------------
# /benchmark/  — HEAR-Bench
# --------------------------------------------------------------------------
BENCHMARK = {
    "slug": "benchmark",
    "title": "HEAR-Bench: A Sound-Centric Manipulation Benchmark with Causal Timing Rules",
    "description": "HEAR-Bench is a sound-enabled robot manipulation benchmark built on RoboTwin 2.0. It streams task-relevant audio and marks a trial as failed if the robot reaches the goal before the required acoustic cue has occurred. Seven tasks across four cue categories, 100 trials each.",
    "h1": "HEAR-Bench: Sound-Causal Manipulation Benchmark",
    "lede": (
        "HEAR-Bench is a simulation benchmark for sound-centric manipulation, built on the dual-arm RoboTwin 2.0 "
        "platform. It supplies a streaming microphone channel and enforces a <b>sound-causal success rule</b>: a "
        "trial counts as successful only if the robot completes the physical goal <i>after</i> the required acoustic "
        "condition has occurred. Reaching the goal early — which standard benchmarks would score as success — is "
        "recorded as a failure."
    ),
    "sections": [
        ("Why a timing-aware benchmark is necessary", [
            "Standard manipulation benchmarks evaluate whether the final geometric state was reached. On a "
            "sound-gated task, that metric cannot tell the difference between a policy that waited for the cue and a "
            "policy that ignored sound entirely and moved on a visual heuristic. HEAR-Bench closes that gap by making "
            "the acoustic precondition part of the success predicate. This is the property that makes it possible to "
            "measure whether a policy is genuinely sound-causal.",
        ]),
        ("Task suite", [
            "Seven simulation tasks cover four categories of decision-critical acoustic cue. Cue timings and initial "
            "visual states are randomised so that policies cannot memorise a fixed schedule, and each task is "
            "evaluated over 100 independent trials.",
        ]),
        ("Four categories of cue", [
            "<b>Event-triggered alarms</b> test waiting and transient capture: <i>Alarm Clock</i> requires suppressing "
            "a visually tempting early press until a ring begins, and <i>Microwave</i> requires capturing a brief "
            "completion beep that can fall entirely inside an execution gap.",
            "<b>Human speech</b> tests timing and prosody: <i>Check Yes</i> uses identical text with different "
            "intonation to defeat pure ASR, and <i>Interrupt</i> places a spoken override at a random moment to test "
            "safe mode switching mid-motion.",
            "<b>Continuous process sounds</b> test long-horizon monitoring: <i>Pour Water</i> and <i>Boil Water</i> "
            "require tracking gradual acoustic evolution while vision is weak or static.",
            "<b>Physical interaction feedback</b> tests contact acoustics: <i>Check Materials</i> uses visually "
            "similar objects so that impact timbre is the only discriminative signal.",
        ]),
        ("How it is used", [
            "All evaluated methods share the same observation interface and the same two-stage training recipe "
            "(pretraining on OpenX-Sound, then task-specific fine-tuning), so differences reflect architecture rather "
            "than data volume. Under this protocol HEAR reaches 81% average sound-causal success, against 61% for the "
            "strongest waveform-as-image VLA baseline, 35% for the strongest ASR baseline and 14% for the strongest "
            "vision-only backbone.",
        ]),
        ("Reproducing it", [
            "The HEAR-Bench implementation is part of the code release, built on top of RoboTwin 2.0, and the "
            "task audio assets ship with it. See <a href=\"/openx-sound/\">OpenX-Sound</a> for the pretraining half "
            "of the pipeline.",
        ]),
    ],
    "keywords": "HEAR-Bench, sound-centric manipulation benchmark, RoboTwin 2.0 benchmark, sound-causal evaluation, robot manipulation benchmark, audio robot benchmark, VLA benchmark, timing-aware evaluation, contact acoustics benchmark, robot audition evaluation",
}

# --------------------------------------------------------------------------
# /openx-sound/
# --------------------------------------------------------------------------
OPENX_SOUND = {
    "slug": "openx-sound",
    "title": "OpenX-Sound: Audio-Augmented Open X-Embodiment for VSLA Pretraining",
    "description": "OpenX-Sound is an audio-augmented robot pretraining dataset. Selected Open X-Embodiment episodes keep their original multi-view RGB, language, proprioception and expert actions, and gain a temporally aligned audio track. 98.7% of augmented clips verified within a 100 ms sync tolerance.",
    "h1": "OpenX-Sound: Audio-Augmented Robot Trajectories",
    "lede": (
        "OpenX-Sound is a pretraining dataset for Vision-Sound-Language-Action learning. Selected Open X-Embodiment "
        "episodes retain their original multi-view RGB video, language instructions, proprioception and expert "
        "actions, and are augmented with temporally aligned audio tracks. It exists because the large "
        "cross-embodiment datasets that enabled VLA progress contain no synchronised microphone recordings, and "
        "collecting robot audio at comparable scale would require hardware standardisation no laboratory has "
        "achieved."
    ),
    "sections": [
        ("What is in it", [
            "Every episode preserves the original multi-view RGB, the language instruction, the proprioceptive state "
            "and the expert action sequence, with an added audio track aligned to the video. 98.7% of augmented clips "
            "were verified within a 100 ms synchronisation tolerance. Episodes with semantically inconsistent audio, "
            "implausible event timing or obvious synchronisation errors were corrected or removed during review.",
        ]),
        ("How it should and should not be used", [
            "The authors are explicit about the scope. Because the base omni-modal backbone already has broad "
            "multimodal pretraining on general audio-video data, OpenX-Sound is used as a <b>robotics-specific "
            "audio-visual-action temporal-alignment stage</b> — not as generic multimodal pretraining, and not as a "
            "replacement for native robot audio. Skipping this stage entirely costs 0.81 to 0.69 on HEAR-Bench, "
            "which the paper reads as evidence that the gain is about robotic audio-visual-action coupling rather "
            "than scale.",
            "The acknowledged limitation is the synthetic-to-real gap: video-to-audio generation can omit subtle "
            "contact cues, shift event timing, or produce sounds without a physical source. For a task as "
            "timing-sensitive as sound-causal manipulation, that caps what purely offline pretraining can achieve, "
            "which is why fine-tuning on real recordings remains necessary.",
        ]),
        ("License and access", [
            "The dataset is released on Hugging Face. Base trajectories derive from Open X-Embodiment; consult that "
            "project's licensing for the underlying episodes.",
        ]),
    ],
    "keywords": "OpenX-Sound, audio augmented robot dataset, Open X-Embodiment audio, robot pretraining dataset, audio-visual-action pretraining, VSLA dataset, robot manipulation dataset, embodied AI dataset, sound dataset robotics, 具身智能数据集",
}

# --------------------------------------------------------------------------
# Concept pages
# --------------------------------------------------------------------------
CONCEPTS = [
    {
        "slug": "vision-sound-language-action",
        "title": "Vision-Sound-Language-Action (VSLA): Extending VLA Robots with Continuous Hearing",
        "description": "Vision-Sound-Language-Action (VSLA) is a robot control paradigm conditioned on vision, streaming audio, language and proprioception under delayed decision loops. It extends VLA from 'see and act' to 'see, hear, remember and react'.",
        "h1": "Vision-Sound-Language-Action (VSLA)",
        "lede": (
            "Vision-Sound-Language-Action (VSLA) is a continuous control paradigm in which a robot policy is "
            "conditioned on vision, streaming audio, language and proprioception under delayed decision loops. It "
            "extends Vision-Language-Action (VLA) from “see and act” to “see, hear, remember and "
            "react” by treating raw audio as a first-class, continuously streaming observation rather than a "
            "pre-execution prompt."
        ),
        "sections": [
            ("Why the “S” needs its own paradigm", [
                "Adding audio to a VLA policy is not symmetric with adding another camera. Visual state persists: a "
                "cup stays on the table across many control cycles, so a slightly stale image is still useful. "
                "Acoustic evidence is the opposite — it is concentrated into short, non-repeatable events. A click, a "
                "rattle, a completion beep or a boiling transition may last a few hundred milliseconds and never "
                "recur. If the policy samples that modality the way it samples images, the evidence is simply gone.",
                "VSLA names the setting in which that asymmetry is taken seriously: streaming audio is part of the "
                "observation interface, and the interface must preserve what it hears until a decision can use it.",
            ]),
            ("The timing problem VSLA formalizes", [
                "Large robot policies cannot run at control frequency, so they predict an action chunk and execute it "
                "open-loop. During that interval new observations cannot change the outgoing commands. The paper "
                "calls this the <b>Blind Execution Interval</b> (BEI). For vision it is tolerable; for a short sound "
                "it can be fatal. Re-querying faster shortens the gap but cannot remove it, because sensing, "
                "preprocessing, inference, communication and actuation latency all remain. The bottleneck is "
                "therefore evidence preservation, not instantaneous preemption.",
            ]),
            ("Sibling paradigms", [
                "VSLA belongs to the same family as vision-tactile-language-action (VTLA) models, which add touch to "
                "the observation stack. Both extend the modality set of a VLA policy without abandoning its "
                "structure. A robot could in principle carry both.",
            ]),
            ("Where HEAR fits", [
                "HEAR is the instantiation of VSLA presented in the IJRR paper. Its four components map onto the "
                "paradigm's requirements: the Historizer provides causal persistence across the BEI, the Envisioner "
                "performs multi-sensory reasoning, the Advancer supplies temporal grounding as an audio world model, "
                "and the Realizer generates smooth action chunks.",
            ]),
        ],
        "faq": [
            ("What does VSLA stand for?",
             "Vision-Sound-Language-Action. It is the auditory sibling of Vision-Language-Action (VLA) and "
             "Vision-Tactile-Language-Action (VTLA)."),
            ("Is VSLA just VLA with audio?",
             "No. The difference is temporal, not modal. VLA policies assume task-relevant evidence is visually "
             "persistent and can be sampled at low frequency. VSLA treats streaming audio as an observation that "
             "must survive delayed, chunked execution — which requires memory and timing mechanisms that a plain "
             "extra input channel does not provide."),
            ("Who introduced VSLA?",
             "The paradigm is formalized in the HEAR paper by Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and "
             "Hesheng Wang, accepted for publication in The International Journal of Robotics Research (2026), "
             "arXiv:2603.16086."),
        ],
        "keywords": "VSLA, Vision-Sound-Language-Action, audio VLA, VLA with sound, robot vision language audio action, multimodal VLA, sound-centric manipulation, continuous hearing robot, audio robot manipulation, VLA sound, 视声语言动作, 听觉语言动作模型",
        "related": ["blind-execution-interval", "robot-audition", "multisensory-robotics"],
    },
    {
        "slug": "blind-execution-interval",
        "title": "Blind Execution Interval: The Perception Gap in Action-Chunked Robot Policies",
        "description": "The Blind Execution Interval (BEI) is the gap created when a VLA policy executes an action chunk open-loop: new observations cannot change the outgoing commands, so a transient acoustic cue can occur and vanish before the next policy query.",
        "h1": "Blind Execution Interval (BEI)",
        "lede": (
            "The Blind Execution Interval (BEI) is the interval created when a robot policy predicts an action chunk "
            "and executes it open-loop. Because new sensor observations cannot alter the command sequence already "
            "being sent to the robot, a transient event — a beep, a click, a rattle, a collision — can occur and "
            "finish entirely inside that interval and never influence a decision."
        ),
        "sections": [
            ("Where the interval comes from", [
                "Modern robot policies are large and cannot run at control frequency. The standard solution is action "
                "chunking: predict a short sequence of future actions, then execute it without waiting for new sensor "
                "updates, which hides inference latency and keeps motion smooth. The interval is not a bug in any "
                "particular implementation; it is a structural consequence of the architecture.",
                "On the authors' Franka Panda deployment the executed action-chunk interval is about 2.1 seconds and "
                "the effective BEI is about 2.3 seconds — so a quarter of the time, roughly, the robot is acting on "
                "an observation it can no longer update.",
            ]),
            ("Why vision tolerates it and audio does not", [
                "Visual and auditory information are distributed over time in opposite ways. Objects persist: a "
                "drawer that was open is still open a second later, so a stale image is degraded but not empty. "
                "Acoustic events do not persist. A completion beep lasts a fraction of a second; once it has passed, "
                "no later observation window contains it. A memoryless audio interface therefore does not receive a "
                "stale version of the cue — it receives nothing.",
            ]),
            ("Why faster re-querying is not the fix", [
                "It is tempting to treat the BEI as a latency problem and attack it by querying more often. That helps "
                "but cannot close the gap: sensing, preprocessing, inference, communication and actuation latency all "
                "remain, and aggressive replanning introduces discontinuities and robot ego-noise — which is "
                "counterproductive when the robot is trying to listen. The paper's conclusion is that the bottleneck "
                "is <i>evidence preservation</i>: a short acoustic event must remain available at the first decision "
                "boundary after it occurs.",
            ]),
            ("Related problems in the same family", [
                "Work on asynchronous inference, real-time chunking, adaptive chunk horizons and speculative "
                "execution addresses the same gap from the scheduling side — changing <i>when</i> the policy runs. "
                "The BEI frames the complementary question of which evidence is lost while it does not run. Both are "
                "real, and fixing one does not fix the other.",
            ]),
            ("How HEAR addresses it", [
                "HEAR's Historizer is a streaming stateful transformer that maintains a compact causal audio memory "
                "across execution gaps, so a cue that has already vanished from the audio stream still conditions the "
                "next decision. It is the single most important component in ablation: removing it drops HEAR-Bench "
                "average success from 0.81 to 0.57.",
            ]),
        ],
        "keywords": "Blind Execution Interval, BEI, action chunking latency, robot policy delay, asynchronous robot inference, stale observations robot, VLA action chunk latency, real-time robot policy, open-loop execution robot, robot perception gap, 盲执行间隔, 动作分块延迟",
        "related": ["action-chunking", "vision-sound-language-action"],
    },
    {
        "slug": "robot-audition",
        "title": "Robot Audition for Manipulation: From Sound Recognition to Sound-Causal Control",
        "description": "Robot audition is the use of microphones on a robot to interpret environmental sound for control and interaction. In manipulation it spans material estimation from impact, grasp-stability assessment, contact microphones as a tactile proxy, and active acoustic probing.",
        "h1": "Robot Audition for Manipulation",
        "lede": (
            "Robot audition is the robotics counterpart of computational auditory scene analysis: using microphones "
            "mounted on a robot to interpret environmental sound — including non-speech events — for control and "
            "interaction. In manipulation, audition is valuable because it reports <i>events</i> rather than states: "
            "contact, completion, hidden contents and process transitions are all more directly audible than visible."
        ),
        "sections": [
            ("What sound tells a manipulator that vision cannot", [
                "Many state changes in manipulation are expressed most directly through sound. A click reveals "
                "contact. A rattle exposes hidden contents. A beep marks completion. A sputtering process signals that "
                "an unseen transition has occurred. A traditional Moka pot, for instance, has no electronic sensor and "
                "no discrete visual indicator of completion — the only reliable signal that extraction is finished is "
                "the change in the sound of the pot.",
                "This makes audition a low-cost proxy for information that would otherwise require tactile sensing, "
                "force sensing or instrumentation of the object.",
            ]),
            ("The main branches", [
                "<b>Passive contact acoustics.</b> Listening to the sound produced by contact between tool and object. "
                "Timbre carries information about material, grasp quality and object state — earlier work used this "
                "to estimate material properties from impact and to assess grasp gentleness.",
                "<b>Contact microphones.</b> Piezoelectric sensors mounted in the gripper or finger provide a much "
                "higher signal-to-noise ratio than ambient microphones and behave as a cheap tactile substitute. "
                "Prior work has used them for slip detection, contact localisation and material classification.",
                "<b>Active acoustic sensing.</b> Rather than waiting for a sound, the robot deliberately generates "
                "one — shaking a container, tapping a surface — and reads the response. This turns an unobservable "
                "hidden state into an observable one. HEAR's Shake Bottle task is an instance.",
                "<b>Speech and prosody.</b> Commands and confirmations carry intent not only in their words but in "
                "their intonation, which transcription discards.",
            ]),
            ("Why audition has lagged behind vision", [
                "Three reasons. First, hardware: most robots have no microphone, and the large cross-embodiment "
                "datasets that powered VLA progress contain no synchronised audio. Second, interfaces: the common way "
                "to feed sound to a policy is to transcribe it with ASR, which discards every non-speech cue, or to "
                "render the waveform as an image, which flattens a temporal signal into a static snapshot. Third, "
                "timing: the events that matter are short and non-repeatable, which interacts badly with the "
                "low-frequency, chunked execution of large policies.",
            ]),
            ("Where HEAR fits", [
                "HEAR takes the third problem as its subject. It does not propose a new acoustic sensor; it proposes "
                "an interface that can hold a fleeting auditory event long enough for a slow policy to act on it, and "
                "a benchmark that checks whether the resulting behaviour is genuinely sound-causal rather than "
                "visually plausible.",
            ]),
        ],
        "keywords": "robot audition, robot hearing, audio robot manipulation, acoustic sensing robot, robot sound perception, auditory robotics, contact acoustics, contact microphone robot, active acoustic sensing, vibro-acoustic manipulation, material estimation impact sound, 机器人听觉, 具身听觉, 声学感知",
        "related": ["vision-sound-language-action", "audio-world-model"],
    },
    {
        "slug": "audio-world-model",
        "title": "Audio World Models: Predicting How a Scene Will Sound",
        "description": "An audio world model predicts how an acoustic scene will evolve rather than only reacting to its current state. HEAR's Advancer is an audio world model used as a training-time objective for temporal grounding in a robot policy.",
        "h1": "Audio World Models",
        "lede": (
            "An audio world model is a model that predicts how an acoustic scene will evolve, rather than only "
            "classifying or reacting to its present state. In HEAR, the Advancer component is formulated as an audio "
            "world model: it predicts near-future discrete audio codes from latent representations, which injects "
            "explicit temporal grounding into a robot policy."
        ),
        "sections": [
            ("From reacting to anticipating", [
                "A purely reactive policy learns a mapping from current observation to action. A world model learns "
                "the dynamics instead: given the present, what comes next? For robotics this matters because many "
                "tasks have visually identical states that imply different correct behaviours, and the only thing "
                "distinguishing them is which direction the process is moving.",
                "Cooking is the clearest case. A pot of water being heated looks similar at many moments, but the "
                "correct action depends entirely on how far the process has progressed. A model that can only see "
                "“water, pot, heat” cannot distinguish “nearly boiling” from “barely warm”. "
                "A model that predicts the next few seconds of sound can.",
            ]),
            ("Why audio specifically", [
                "Audio is an unusually good carrier for this kind of progress signal. Continuous processes — boiling, "
                "pouring, grinding, sputtering — have characteristic acoustic signatures that evolve in a structured "
                "way, and the evolution is audible before it is visually obvious. Acoustic signals also have high "
                "temporal resolution relative to camera frames, so the rate of change is directly observable.",
            ]),
            ("How HEAR uses one", [
                "The Advancer predicts near-future discrete audio codes during training. This forces the policy's "
                "latent representation to encode not just what is audible now but how it is changing, which is what "
                "keeps the policy stable during long waiting phases where vision is quasi-static — a failure mode "
                "related to temporal motion collapse in chunked policies.",
                "Crucially, the Advancer is a <b>training-time objective and is removed at deployment</b>. The "
                "temporal structure it teaches stays in the latent space, so inference cost is unchanged. Ablating it "
                "costs 0.81 to 0.73 on HEAR-Bench.",
            ]),
            ("Where it sits in the world-model landscape", [
                "Most world-model work for robotics predicts future images or future latent states. Predicting in the "
                "audio modality is less common, and it complements rather than replaces visual world modelling: "
                "vision reports what the scene looks like, audio reports what is happening to it.",
            ]),
        ],
        "keywords": "audio world model, world model robotics, world action model WAM, future audio prediction, temporal grounding robot, latent dynamics model, audio token prediction, predictive audio dynamics, robot world model, 音频世界模型, 世界模型, 世界动作模型",
        "related": ["robot-audition", "research-context"],
    },
    {
        "slug": "action-chunking",
        "title": "Action Chunking in Robot Policies: Why Policies Act Open-Loop, and What It Costs",
        "description": "Action chunking means predicting a short sequence of future actions and executing them open-loop. It hides inference latency and keeps motion smooth, but creates a perception gap in which new observations cannot affect the robot.",
        "h1": "Action Chunking",
        "lede": (
            "Action chunking is the practice of predicting a short sequence of future actions at once — a "
            "“chunk” — and executing it open-loop, without waiting for new sensor observations. It is "
            "near-universal in modern robot policies because it hides inference latency and produces smoother "
            "motion. Its cost is a perception gap: for the duration of the chunk, the robot cannot react to anything."
        ),
        "sections": [
            ("Why it exists", [
                "Large robot policies are expensive to evaluate. Predicting one action at a time and re-running the "
                "model before every low-level command is not feasible at control frequency. Chunking amortises a "
                "single forward pass across many control steps. It was popularised by transformer-based imitation "
                "learning and is now standard in both diffusion-policy and flow-matching action heads.",
                "The side benefit is motion quality. Because the whole chunk is generated jointly, the resulting "
                "trajectory is internally consistent rather than a stitched sequence of independent decisions, which "
                "reduces jitter.",
            ]),
            ("The cost", [
                "During execution the policy is blind by construction. Observations arriving mid-chunk cannot alter "
                "the commands already being sent. For slow, visually persistent tasks this is usually fine. For tasks "
                "where the decisive evidence is a short event — a contact, a beep, a spoken interruption, a collision "
                "— it means the evidence may be missed entirely.",
                "The HEAR paper names this the <b>Blind Execution Interval</b>. Its point is not that chunking is "
                "wrong, but that the interval has a modality-dependent cost: harmless for vision, potentially fatal "
                "for audio.",
            ]),
            ("The standard remedies, and their limits", [
                "Shortening the chunk reduces the gap but degrades smoothness and increases compute. Re-querying more "
                "often has the same trade-off. More recent approaches — asynchronous inference, real-time chunking, "
                "adaptive horizons, speculative execution — restructure when the model runs, and help significantly. "
                "None of them eliminates the gap, because the latency chain from sensing to actuation remains.",
                "The complementary fix, and the one HEAR takes, is on the input side: make the observation interface "
                "remember. If incoming audio is accumulated into a causal memory rather than sampled per query, a "
                "cue that occurred mid-chunk is still available at the next decision boundary even though it is no "
                "longer audible.",
            ]),
        ],
        "keywords": "action chunking, action chunk robot policy, open-loop execution, chunked VLA policy, real-time chunking RTC, asynchronous inference robot, action chunk horizon, temporal motion collapse, robot policy latency, flow matching action head, 动作分块, 动作块",
        "related": ["blind-execution-interval", "robot-foundation-models"],
    },
    {
        "slug": "physical-ai",
        "title": "Physical AI and Embodied Intelligence: What the Terms Mean for Robot Manipulation",
        "description": "Physical AI and embodied intelligence describe AI systems that act in the physical world through sensors and actuators. For robot manipulation, the open problems are sensory interfaces, timing under delayed control, and data.",
        "h1": "Physical AI and Embodied Intelligence",
        "lede": (
            "Physical AI and embodied intelligence are the terms now used for AI systems that perceive and act in "
            "the physical world through sensors and actuators, rather than producing text or images. For robot "
            "manipulation, the interesting content behind the labels is a set of concrete engineering problems: how "
            "a policy's sensory interface should be shaped, how it behaves when decisions are delayed, and where the "
            "training data comes from."
        ),
        "sections": [
            ("The label and the substance", [
                "Physical AI is the industry framing; embodied intelligence is the more academic one. Both point at "
                "the same shift: a language model predicts the next token, whereas a physical agent must predict the "
                "consequences of its own actions on a world that pushes back. That difference is not cosmetic — it "
                "changes what a model needs to represent. Mass, friction, inertia and contact are not in the training "
                "distribution of text.",
            ]),
            ("What is genuinely hard", [
                "<b>Data.</b> Internet text and video are abundant and third-person. A robot needs first-person data: "
                "“what does the world become after <i>I</i> do this?” That data is expensive to collect, "
                "and the largest cross-embodiment datasets still contain no synchronised audio, force or touch.",
                "<b>Sensory interfaces.</b> Most work assumes vision is sufficient. It is not: contact, force and "
                "hidden internal state are invisible to cameras, and the modalities that do report them each have "
                "their own temporal structure that a policy must be built to handle.",
                "<b>Timing.</b> Physical agents run under latency, and their most capable policies run slowly. "
                "Anything that must be noticed between two decisions — which includes every short event — falls into "
                "the gap.",
                "<b>Evaluation.</b> Reaching a goal is not the same as behaving correctly. A policy that ignores an "
                "auditory precondition and moves on a visual heuristic can look successful on a geometric metric "
                "while being wrong in the way that matters.",
            ]),
            ("Where HEAR fits", [
                "HEAR is a physical-AI system in the narrow sense that it is a closed-loop controller for a real "
                "robot arm, and in a more specific sense that it works on the sensory-interface problem. Its claim is "
                "that for agents acting under delayed, chunked control, preserving transient evidence is a "
                "requirement rather than an optional refinement — and that audition is the modality where its absence "
                "is most visible.",
            ]),
        ],
        "keywords": "physical AI, embodied AI, embodied intelligence, embodied agent, physical artificial intelligence, robot manipulation, sensors actuators AI, first-person robot data, robot learning, 物理AI, 物理人工智能, 具身智能, 具身智能体",
        "related": ["robot-foundation-models", "research-context"],
    },
    {
        "slug": "ai-agent-robotics",
        "title": "AI Agent Robotics: How LLM Agents and Robot Policies Fit Together",
        "description": "AI agent robotics combines high-level reasoning agents with low-level robot policies. The emerging pattern is hierarchical: an LLM agent plans and selects skills, while a vision-language-action policy executes them in real time.",
        "h1": "AI Agent Robotics",
        "lede": (
            "AI agent robotics is the combination of a reasoning agent — typically an LLM that plans, calls tools "
            "and tracks state — with the low-level policies that actually move a robot. The pattern that has "
            "emerged is hierarchical: the agent decides <i>what</i> to do and the robot policy handles <i>how</i>, "
            "because a language model cannot produce joint torques and a manipulation policy cannot reason about a "
            "multi-minute task."
        ),
        "sections": [
            ("Why the split exists", [
                "The two layers have incompatible requirements. A planning agent benefits from a long context, slow "
                "deliberation and access to tools and memory. A manipulation policy must run in a control loop at "
                "tens of hertz and cannot afford that deliberation. Trying to make one model do both produces "
                "something that is either too slow to control or too shallow to plan.",
                "The layered answer also matches how the fields have specialised: high-level work in language and "
                "reasoning, low-level work in imitation learning and action generation.",
            ]),
            ("Skills as tools", [
                "A productive framing is that a robot policy <i>is</i> a tool: the agent registers manipulation skills "
                "alongside search, code execution and other capabilities, and invokes them by intent. This makes "
                "robot capability composable and inspectable, and lets the agent's planning be evaluated separately "
                "from the policy's dexterity. Its known weakness is the handoff — deciding when a skill has finished "
                "and what to do when one fails.",
            ]),
            ("What the agent layer cannot see", [
                "A high-level agent observes the world through whatever its tools report. If the low-level policy's "
                "sensory interface discards something, the agent's world model is missing it too. A robot that cannot "
                "tell when a process actually finished — as opposed to appearing to be finished — cannot report "
                "progress accurately, and an agent planning on that report will plan wrongly.",
                "This is where the low-level interface becomes an agent-level concern. Transient evidence that is "
                "lost inside an execution gap is not just a control problem; it is missing information in the agent's "
                "model of the world.",
            ]),
            ("Where HEAR fits", [
                "HEAR is a low-level action component: a policy that converts streaming perception into joint "
                "commands under real-time constraints. Its contribution to the agentic stack is ensuring that the "
                "acoustic portion of the world state is not silently dropped between decisions.",
            ]),
        ],
        "keywords": "AI agent robotics, robot agent, agentic robotics, embodied agent, LLM robot agent, robot skills as tools, hierarchical robot policy, MCP robotics, tool-using agent robot, physical agent, 智能体机器人, 具身智能体, AI智能体",
        "related": ["physical-ai", "research-context"],
    },
    {
        "slug": "gpt-robotic-arm",
        "title": "GPT and Large Models for Robotic Arms: What They Can and Cannot Do",
        "description": "Large language and multimodal models can drive robotic arms at the planning level and, through vision-language-action training, at the action level. What they cannot do without extra machinery is notice short-lived events under delayed control.",
        "h1": "GPT and Large Models for Robotic Arms",
        "lede": (
            "“GPT robotic arm” describes a robot arm controlled by a large pretrained model. That happens "
            "at two levels: a language model can plan and sequence a task in words, and a vision-language-action "
            "(VLA) model — a multimodal backbone fine-tuned to emit actions — can drive the arm directly. Both work. "
            "Neither automatically solves the problem of acting correctly on brief physical events."
        ),
        "sections": [
            ("Level one: planning", [
                "A language model can decompose “make coffee” into steps, choose tools, and recover from "
                "some failures, because that reasoning is largely symbolic. It has no access to joint angles and does "
                "not need them. This level is well established and mostly a software-integration problem.",
            ]),
            ("Level two: direct action", [
                "A VLA model takes images, an instruction and proprioception as input and outputs continuous actions. "
                "It works because the backbone's pretraining has already produced representations in which visual "
                "scenes and language are aligned, and a comparatively small amount of robot data suffices to attach "
                "an action head. This is where most current capability lives, and where the interesting failure modes "
                "are.",
            ]),
            ("The timing problem large models bring with them", [
                "A model that can plan beautifully is still far too slow to run at control frequency. The standard "
                "workaround — predict a chunk of actions and execute it open-loop — means the arm is following "
                "instructions that cannot be revised for a second or more. Anything the robot needs to notice inside "
                "that window is invisible to it.",
                "For visual tasks this is usually tolerable, because what the camera saw a second ago is mostly still "
                "true. For events it is not: a click, a beep, a rattle or a spoken interruption can begin and end "
                "inside the window and leave no trace in any later observation.",
            ]),
            ("What is needed beyond a bigger model", [
                "Scale does not fix this, because the problem is not representational capacity but interface design. "
                "What helps is a sensory interface that accumulates rather than samples: a causal memory of what was "
                "heard, maintained across the execution gap, so that the next decision can act on an event that is no "
                "longer audible. The HEAR framework is one implementation of that idea, together with an evaluation "
                "protocol that refuses to score a visually plausible but acoustically premature action as a success.",
            ]),
        ],
        "keywords": "GPT robotic arm, LLM robot control, large model robot arm, VLA model, vision language action model, robot foundation model, AI robot arm, ChatGPT robot, large language model robotics, 大模型机械臂, GPT机械臂, 机械臂大模型",
        "related": ["robot-foundation-models", "action-chunking"],
    },
    {
        "slug": "robot-foundation-models",
        "title": "Robot Foundation Models: Pretraining, Cross-Embodiment Transfer and Data",
        "description": "Robot foundation models are large models pretrained on broad robot data and fine-tuned per task. The main open problems are cross-embodiment transfer, action chunking under real-time constraints, and the shortage of sensory data beyond vision.",
        "h1": "Robot Foundation Models",
        "lede": (
            "A robot foundation model is a large model pretrained on data from many robots and tasks, then "
            "fine-tuned — or prompted — for a specific one. The pattern is borrowed from language and vision, and it "
            "works for the same reason: broad pretraining produces representations that transfer, so downstream "
            "learning needs far less data."
        ),
        "sections": [
            ("The pretraining recipe", [
                "A large multimodal backbone, usually a vision-language model, is adapted to emit actions. Training "
                "proceeds in stages: broad multimodal pretraining, then robot-specific pretraining on a "
                "cross-embodiment corpus, then task-specific fine-tuning. The first stage provides general "
                "perception and language grounding; the second provides the coupling between perception and physical "
                "action that no amount of internet data supplies.",
                "Cross-embodiment corpora — Open X-Embodiment and its successors — are what make the second stage "
                "possible. They aggregate trajectories from many robot platforms and tasks under a shared format.",
            ]),
            ("What the corpora do not contain", [
                "Vision, language, proprioception and actions. Not force. Not touch. Not audio. This is not an "
                "oversight so much as a hardware problem: collecting synchronised microphone, tactile or force data "
                "at the scale of a cross-embodiment corpus would require standardisation across every contributing "
                "laboratory.",
                "The consequence is that foundation models inherit a vision-centric world view, and every additional "
                "modality has to solve its own data problem before it can be trained on. HEAR's OpenX-Sound is one "
                "such solution for audio: rather than standardising hardware, it augments existing episodes with "
                "temporally aligned synthesised audio, and is explicit that this is a bootstrapping stage rather than "
                "a substitute for real recordings.",
            ]),
            ("Real-time constraints", [
                "Foundation models are large, robot control is fast, and the gap is bridged by action chunking. That "
                "makes the Blind Execution Interval a property of the whole class, not of any one model: any policy "
                "big enough to need chunking also has an interval in which it cannot react.",
            ]),
            ("Where HEAR fits", [
                "HEAR is a foundation-model-style policy whose pretraining stage adds the audio modality. Its "
                "contribution to the class is showing that the interface, not just the backbone, determines whether "
                "transient sensory events survive long enough to matter.",
            ]),
        ],
        "keywords": "robot foundation model, robot pretraining, cross-embodiment, Open X-Embodiment, robot policy pretraining, VLA backbone, robot manipulation foundation model, embodied foundation model, robot data scaling, robot generalist policy, 机器人基础模型, 具身基础模型, 跨本体",
        "related": ["action-chunking", "gpt-robotic-arm", "openx-sound"],
    },
    {
        "slug": "multisensory-robotics",
        "title": "Multi-Sensory Robot Policies: Adding Touch, Force and Sound to VLA Models",
        "description": "Multi-sensory robot policies extend vision-language-action models with additional modalities. The vision-tactile-language-action (VTLA) family adds touch; VSLA adds streaming audio. Each modality has its own temporal structure, and the interface must match it.",
        "h1": "Multi-Sensory Robot Policies",
        "lede": (
            "Multi-sensory robot policies extend a vision-language-action model with modalities beyond vision — "
            "typically touch, force or sound. The motivation is straightforward: cameras cannot observe contact, "
            "force or hidden internal state, so tasks that depend on them need another channel. The engineering "
            "lesson is less obvious: each modality has its own temporal structure, and an interface that suits "
            "vision does not automatically suit the others."
        ),
        "sections": [
            ("The families", [
                "<b>Vision-tactile-language-action (VTLA).</b> Adds tactile sensing, usually from fingertip sensors or "
                "a tactile skin, to the observation stack. Tactile data is high-dimensional, local and fast-changing, "
                "which makes it informative for contact-rich manipulation and awkward to feed to a model built for "
                "camera frames.",
                "<b>Force and torque.</b> Wrist or joint force sensing gives a lower-dimensional but very direct "
                "measure of contact. Often added as an additional input vector rather than an image-like modality.",
                "<b>Audio — VSLA.</b> Adds streaming sound. Unlike touch and force, audio carries information about "
                "events that are not happening at the robot's own end-effector: an appliance finishing, a phone "
                "ringing, a liquid reaching a boil.",
            ]),
            ("Why the temporal structure matters more than the modality", [
                "The standard VLA assumption is that observations can be sampled at low frequency because the world "
                "changes slowly. That assumption is reasonable for cameras and disastrous for modalities whose "
                "information arrives in short bursts.",
                "Tactile and force signals are dense but strongly correlated with the robot's own motion, so a policy "
                "generally knows when to expect them. Audio is different: task-relevant acoustic events are sparse, "
                "asynchronous, and often generated by something other than the robot. They can occur at any moment, "
                "including during an open-loop execution chunk, and they do not repeat.",
            ]),
            ("The design consequence", [
                "Adding a modality is not the same as adding an input channel. A modality whose evidence is transient "
                "requires the interface to have memory: something that accumulates what arrived and keeps it "
                "available until a decision can use it. Without that, the additional modality is present in the API "
                "and absent in effect.",
            ]),
            ("Where HEAR fits", [
                "HEAR is the auditory member of this family. It pairs a streaming audio interface with causal memory "
                "(the Historizer), a reasoning module that fuses it with vision, language and proprioception (the "
                "Envisioner), and an evaluation protocol that rejects actions completed before the required sound "
                "occurred. It is designed to be combined with, not to replace, tactile and force sensing.",
            ]),
        ],
        "keywords": "multisensory robot policy, VTLA, vision tactile language action, tactile VLA, force-aware robot policy, audio VLA, multimodal robot manipulation, sensor fusion robot learning, visuotactile, robot sensing modalities, 多感官机器人, 视触觉, 多模态机器人",
        "related": ["vision-sound-language-action", "robot-audition"],
    },
]
