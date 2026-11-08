# Frances Okeke — personal site

Plain HTML/CSS site, hosted on Cloudflare Workers (static assets), deployed from GitHub.

## Folder layout

- `public/` — everything visitors see
  - `index.html` — homepage
  - `about.html` — bio and contact
  - `research/`, `projects/`, `notes/`, `roundup/` — one folder per section, each with an `index.html` list page and a template
  - `styles.css` — all styling (colours at the top)
- `wrangler.jsonc` — tells Cloudflare to serve the `public/` folder

## Go live

1. Create a GitHub repository (e.g. `frances-okeke-site`) and upload **everything in this folder**, keeping the structure (`wrangler.jsonc` at the top level, next to `public/`).
2. In Cloudflare: **Workers & Pages → Create application → GitHub**, sign in, choose the repository.
3. Name the Worker `frances-okeke-site` (it must match `"name"` in `wrangler.jsonc`), then **Save and Deploy**.
4. Check the site at the `*.workers.dev` address Cloudflare gives you.
5. Add your domain in the Worker's **Domains** settings. The domain's nameservers must be managed by Cloudflare.

Every change you commit to GitHub after that redeploys automatically.

## Before publishing

Search for `class="todo"`: the highlighted placeholders still need your words (AxeoMove one-liner, email, LinkedIn, article content).

## Adding a new piece

1. Copy the template in the right folder (e.g. `research/article-template.html`) and rename it, e.g. `research/exit-friction.html`.
2. Write the content and remove the yellow `todo` markers.
3. Add a link to it in that folder's `index.html` (and on the homepage under "Latest").
