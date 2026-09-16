# HEAR project page

Source for [hear.irmv.top](https://hear.irmv.top/), the project page for:

> Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation

Accepted for publication in *The International Journal of Robotics Research* (IJRR).

The site is a static GitHub Pages deployment. It contains no analytics, cookies, third-party embeds, or unpublished manuscript files. Public images and the five selected real-robot demonstrations are served from this repository.

## Local preview

```bash
python3 -m http.server 8000
```

Then open `http://127.0.0.1:8000/`.

## Repository layout

| Path | Purpose |
| --- | --- |
| `index.html` | English project page (canonical URL `/`) |
| `zh/index.html` | Simplified Chinese project page (`/zh/`) |
| `index.md` | Markdown mirror of the English page, for LLM ingestion |
| `zh/index.md` | Markdown mirror of the Chinese page |
| `llms.txt` | [llms.txt](https://llmstxt.org/) index: summary, links, key terms |
| `llms-full.txt` | Complete English + Chinese page text as plain Markdown |
| `robots.txt` | Explicit allow rules for AI crawlers, sitemap reference |
| `sitemap.xml` | XML sitemap with image and video extensions |
| `static/` | CSS, JS, images, posters, captions and videos |

## Machine-readable entry points

The site is deliberately structured so that answer engines, retrieval-augmented assistants and AI agents can read it without parsing HTML:

- `/llms.txt` — concise index with a summary, primary links, definitions of key terms and research context.
- `/llms-full.txt` — the complete page content in both languages as plain Markdown.
- `/index.md`, `/zh/index.md` — per-language Markdown mirrors.
- `/sitemap.xml` — includes `image:image` entries for the figures and `video:video` entries for the five real-robot demonstrations.
- `/robots.txt` — explicitly allows GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, Claude-SearchBot, anthropic-ai, Googlebot, Google-Extended, Bingbot, PerplexityBot, Perplexity-User, Applebot, Applebot-Extended, meta-externalagent, Amazonbot, CCBot and others, with `Content-Signal: search=yes, ai-input=yes, ai-train=yes`.

The English page carries a JSON-LD `@graph` covering `WebSite`, `WebPage`, `ScholarlyArticle`, `Dataset` (OpenX-Sound, HEAR-Bench), `SoftwareSourceCode`, `FAQPage`, `DefinedTermSet`, `Person`, `CollegeOrUniversity`, `Organization`, `BreadcrumbList` and an `ItemList` of `VideoObject` entries.

## Editing notes

- The two language pages cross-reference each other with `hreflang` (`en`, `zh-Hans`, `zh-CN`, `x-default`). Keep the link tags in both `<head>` blocks in sync.
- `index.md` and `zh/index.md` are the source of truth for `llms-full.txt`. After editing either mirror, rebuild the combined file:

  ```bash
  {
    printf '# HEAR — Full page content (English + 中文)\n# Source: https://hear.irmv.top/\n\n'
    printf '# ===== PART 1 / 2 — ENGLISH =====\n\n'
    cat index.md
    printf '\n# ===== PART 2 / 2 — 简体中文 =====\n\n'
    cat zh/index.md
  } > llms-full.txt
  ```
- Update `dateModified` in the JSON-LD blocks and the `<lastmod>` values in `sitemap.xml` when content changes materially.
- When adding or replacing a video, regenerate its poster frame and update both `sitemap.xml` and the `VideoObject` entries:

  ```bash
  ffmpeg -ss 4 -i static/videos/<name>.mp4 -frames:v 1 -vf "scale=960:-2" -q:v 3 static/images/posters/<name>.jpg
  ```

## Acknowledgments and license

The page structure was adapted from the [Academic Project Page Template](https://github.com/eliahuhorwitz/Academic-project-page-template) and Nerfies. Website content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
