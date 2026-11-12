# Wrapped 2026

An independent music-culture website built with Next.js App Router, TypeScript, Tailwind CSS, Motion, and Lucide. Original SVG/CSS artwork; no Spotify authentication, analytics, wallet connection, or fabricated token metrics.

## Run locally

Requires Node.js 20.9 or newer. On Windows PowerShell, use `npm.cmd` if script execution policy blocks `npm`.

```sh
npm ci
npm run dev
```

Open http://localhost:3000.

## Configure before launch

Edit `src/lib/config.ts`: token name, ticker, network, contract address, X, Telegram, trading and DexScreener URLs, and launch status. Empty URLs intentionally render disabled buttons marked SOON. Only valid HTTPS URLs become external links. Contract copying appears only with a configured address and reports clipboard failures. Verify every address and URL before enabling trading links.

## Checks and deployment

```sh
npm run lint
npm run typecheck
npm run build
```

The build exports a static site to `out/`. For Vercel, import this directory as the project root with the Next.js preset, or deploy `out/` to a static host. No environment variables or backend are needed. `next start` does not serve static exports; use `npx serve out` for a production preview.

## Design and behavior

The supplied AVIF was converted to PNG for inspection. Its yellow (#fff200), raspberry (#df104c), green (#16d264), cobalt (#3d52ef), mint (#98c9ad), and purple (#27104f) inform centralized CSS variables in `src/app/globals.css`. The artwork translates the reference's stepping shapes, starbursts, and oversized typography without reusing its Spotify logo.

The timeline uses native scrolling, a desktop sticky index, and vertically stacked mobile panels. Motion handles progressive reveals and pointer response; CSS handles record rotations, waves, and marquees. Reduced-motion preferences and a header pause control disable continuous effects. Personality cards download as locally rendered PNGs without sending user information anywhere. All recap statistics are explicitly illustrative.

## Historical sources

- https://newsroom.spotify.com/2024-12-04/10-years-spotify-wrapped/ — 2015, 2016, 2019, 2021, 2023, and 2024 milestones.
- https://newsroom.spotify.com/2025-12-03/2025-wrapped-user-experience/ — 2025 interactive experiences and Wrapped Party.
- https://newsroom.spotify.com/spotify-timeline/ — contextual chronology.

The 2026 panel is explicitly forward-looking and does not claim an official release. The project is not affiliated with, sponsored by, or endorsed by Spotify.
