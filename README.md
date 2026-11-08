# Frances Okeke: personal site

Calm and thoughtful. Static site served by Cloudflare Workers from `public/`. Every commit to `main` redeploys automatically once Cloudflare is connected.

## What's where
- `public/`: everything visitors see. `styles.css` holds the brand tokens at the top; `site.js` runs the menu, filters, reading progress and copy-email button.
- `build.py`: regenerates every page so headers, footers and lists stay consistent. Add a piece to `CONTENT`, then run `python3 build.py`.
- `templates/`: starting points for investigations, teardowns, notes and roundups (not published).
- `HEURISTICS.md`: how the design applies Nielsen's 10 usability heuristics.
- `wrangler.jsonc`: Cloudflare settings. The Worker must be named `frances-okeke-site`.

## Before going public
Search for `todo` in `build.py`. Still to add: your email (`EMAIL_ADDRESS`) and LinkedIn (`LINKEDIN_URL`), CV dates, roles and institutions, a CV PDF (`public/cv.pdf`), the AxeoMove description and the first investigation's content.
