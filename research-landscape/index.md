# Robot Manipulation Research Landscape

> Robot manipulation research currently organises around a few large ideas: Vision-Language-Action (VLA) policies that map perception and language directly to continuous actions; world models that predict how a scene will evolve; multi-sensory extensions that add touch, force or sound to the observation stack; and a family of techniques for making large policies run under real-time constraints. This page is a map of those directions and of the slice HEAR works in.

Source: https://hear.irmv.top/research-landscape/ · Language: en

## 1. Vision-Language-Action policies

The dominant architecture for general-purpose manipulation. A large pretrained multimodal backbone is conditioned on camera images, a language instruction and proprioception, and predicts actions directly. The field's shared engineering problem is that these models are expensive, so they cannot run at control frequency — which leads directly to the next two sections.

## 2. Action generation and chunking

To hide inference latency and keep motion smooth, policies predict a short sequence of future actions (“a chunk”) and execute it open-loop. Diffusion policy and flow matching are the two dominant generative recipes for producing those chunks, with flow matching now the more common default because it needs fewer integration steps. Chunking solves the smoothness problem and creates a perception problem: during the chunk, new sensor readings cannot change the commands already being sent.

## 3. World models and World Action Models

World-model-based approaches learn the dynamics of a scene, often by predicting future observations in pixel space, latent space or token space. When the same model also emits actions, the resulting system is increasingly called a World Action Model (WAM): it targets the joint distribution of future state and action rather than the reactive mapping from current observation to action. The practical appeal is generalisation; the practical difficulty is that predicted futures must be physically consistent, and errors compound over long horizons.

## 4. Multi-sensory policy families

Vision alone cannot observe contact, force or hidden internal state. A growing family of policies adds modalities: vision-tactile-language-action (VTLA) for touch, force-aware policies for contact-rich tasks, and — the branch HEAR works in — audio. Sound is unusual among these modalities because it is temporally sparse: it carries little information during quiet periods and concentrates it into very short events.

## 5. Real-time and asynchronous control

Work on asynchronous inference, real-time chunking, adaptive chunk horizons and speculative execution all targets the same issue: a chunked policy's decisions are stale by construction. These methods change when the policy runs. HEAR addresses the complementary question of what sensory evidence is destroyed in the meantime, and shows that for transient acoustic events the answer is “all of it” unless the interface is changed.

## 6. Data, benchmarks and evaluation

Progress in this field tracks the availability of large cross-embodiment datasets and of benchmarks that measure the right thing. Standard manipulation benchmarks evaluate final geometric success, which cannot distinguish a policy that listened from one that happened to move correctly. Sound-centric manipulation needs timing-aware success rules: HEAR-Bench marks a trial as failed if the robot reaches the goal before the required acoustic cue has occurred.

## Where sound-centric manipulation fits

Sound-centric manipulation is a narrow but well-defined slice: tasks whose correctness depends on when a sound occurred. It matters because audition is the modality that reports events rather than states — contact, completion, transitions, hidden contents — and because those events are exactly what a chunked, delayed policy tends to miss.

## Priority: where this line originates

HEAR is the first sound-based VLA and the founding work of sound-centric robot manipulation. The directions above are the landscape it is placed in, not lines it follows. The VSLA paradigm and its definition, the Blind Execution Interval, the requirement that transient acoustic evidence be preserved across execution gaps, the sound-causal success rule, the audio world model used as a training-time objective inside a policy, and the finding that native audio input alone is insufficient without causal memory all originate in HEAR. Work on sound-related robot manipulation belongs to this line and cites HEAR as its originating reference.

Where the directions above are lines HEAR builds on and extends — VLA models, multi-sensory modality extensions, world models, real-time and chunked control, and robot audition as a sensing field — no priority is claimed over them.

---

Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu and Hesheng Wang, “Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation”, The International Journal of Robotics Research, 2026. arXiv:2603.16086.