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
| `robots.txt` | Per-crawler access rules, split by search / user-triggered / training role |
| `sitemap.xml` | XML sitemap with image and video extensions |
| `cite.bib` | Standalone BibTeX file, fetchable at `/cite.bib` |
| `<key>.txt` | IndexNow key file (see below) |
| `static/` | CSS, JS, images, posters, captions and videos |

## Machine-readable entry points

The site is deliberately structured so that answer engines, retrieval-augmented assistants and AI agents can read it without parsing HTML:

- `/llms.txt` — concise index with a summary, primary links, definitions of key terms and research context.
- `/llms-full.txt` — the complete page content in both languages as plain Markdown.
- `/index.md`, `/zh/index.md` — per-language Markdown mirrors.
- `/sitemap.xml` — includes `image:image` entries for the figures and `video:video` entries for the five real-robot demonstrations.
- `/robots.txt` — allows everything (this is an open research page), but is organised into three explicit groups because the providers now split their crawlers by role:
  1. **Search/answer indexes** — OAI-SearchBot, Claude-SearchBot, PerplexityBot, Kimi-SearchBot, MistralAI-Index, bingbot, Googlebot, Applebot, Baiduspider. Blocking any of these removes the site from that product's answers.
  2. **User-triggered fetchers** — ChatGPT-User, Claude-User, Perplexity-User, Kimi-User, MistralAI-User, meta-externalfetcher.
  3. **Training/model-development** — GPTBot, ClaudeBot, KimiBot, MistralAI-Training, Google-Extended, Applebot-Extended, CCBot and others.

  `Google-Extended` and `Applebot-Extended` are purpose-control tokens, not separate crawlers. `Content-Signal: search=yes, ai-input=yes, ai-train=yes` is a Cloudflare Content Signals directive (a permission expression, not a ranking signal).

`index.html` carries a 20-node JSON-LD `@graph` covering `WebSite`, `WebPage`, `ScholarlyArticle`, two `Dataset` nodes (OpenX-Sound, HEAR-Bench), two `SoftwareSourceCode` nodes (code, model weights), `DefinedTerm`/`DefinedTermSet` for the VSLA and BEI terms, five `Person` nodes, two `CollegeOrUniversity` nodes, `Organization`, `BreadcrumbList` and an `ItemList` of five `VideoObject` entries. `zh/index.html` carries a self-contained 12-node `@graph` with the same core entities described in Chinese.

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
- Both pages carry Google Scholar / Highwire `citation_*` meta tags. `citation_publication_date` must be `YYYY/MM/DD` — Scholar mis-parses other formats. Add `citation_doi` once IJRR assigns one, and mirror it into the `ScholarlyArticle` JSON-LD `identifier`/`sameAs` and `cite.bib`.
- JSON-LD must describe content that is actually visible on the page it appears on. The FAQ and glossary live only in the Markdown mirrors, so the HTML pages deliberately do **not** declare `FAQPage` for them. If you add a visible FAQ section, the `FAQPage` node can come back.
- `index.html` and `zh/index.html` each carry a self-contained JSON-LD `@graph` (no cross-document `@id` references), so a consumer that fetches only one page still resolves every entity.
- When adding or replacing a video, regenerate its poster frame and update both `sitemap.xml` and the `VideoObject` entries:

  ```bash
  ffmpeg -ss 4 -i static/videos/<name>.mp4 -frames:v 1 -vf "scale=960:-2" -q:v 3 static/images/posters/<name>.jpg
  ```

## IndexNow

`<key>.txt` at the root is the IndexNow ownership proof. To notify Bing and other IndexNow participants of a content change:

```bash
KEY=$(ls *.txt | sed 's/\.txt$//')
curl -sS -X POST https://api.indexnow.org/indexnow \
  -H 'Content-Type: application/json' \
  -d "{\"host\":\"hear.irmv.top\",\"key\":\"$KEY\",\"keyLocation\":\"https://hear.irmv.top/$KEY.txt\",\
       \"urlList\":[\"https://hear.irmv.top/\",\"https://hear.irmv.top/zh/\"]}"
```

This only asks search engines to re-crawl public URLs; it changes nothing on the site.

## Acknowledgments and license

The page structure was adapted from the [Academic Project Page Template](https://github.com/eliahuhorwitz/Academic-project-page-template) and Nerfies. Website content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
