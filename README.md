# Illness Tracker

**Current Version: v0.51**

Live deployments: [itsavibecode.github.io/sick](https://itsavibecode.github.io/sick/) (primary) and [dev.rizzo.cc/sick](https://dev.rizzo.cc/sick/) (mirror).

Track · Analyze · Prevent — A personal illness tracking app with pattern analysis, medicine/vitals logging, Google Calendar sync, and Firebase cloud storage.

## Files

| File | Description |
|------|-------------|
| `index.html` | Current release — single-file app, served by GitHub Pages |
| `privacy.html` | Privacy Policy + Terms of Service + Medical Disclaimer, linked from the footer |
| `og-image.png` | 1200×630 social preview image (Open Graph + Twitter) |
| `site.webmanifest` | PWA manifest — lets visitors install to home screen |
| `favicon.ico` / `favicon-16.png` / `favicon-32.png` / `apple-touch-icon.png` / `icon-192.png` / `icon-512.png` / `icon-maskable.png` | Full icon set used by the favicon + PWA install + Android adaptive icons |
| `.scripts/build-icons.py` | Regenerates the icon set from the brand gradient + 🩺 emoji |
| `README.md` | This file |

## Features

- Log illnesses with symptoms, severity, location, activity, contacts
- Medicine & vitals sub-entries with temperature (°F), SpO2 (%), dose intervals
- Real-time next-dose countdowns with dismissable overdue alerts
- Export individual illness cards as PNG images
- Pattern analysis: risk factors, recurring locations/contacts, seasonal trends
- Google Sign-In with Firestore cloud sync (including dismissed alerts)
- Google Calendar sync via OAuth
- Export to .ics and .json with versioned filenames
- Temperature color coding by severity (normal → low-grade → fever → high fever)
- Custom medicine list that persists per-user

## Setup

1. Deploy `index.html` to GitHub Pages
2. Configure Firebase: Authentication (Google), Firestore Database
3. Lock Firestore rules to authenticated users only (`/users/{uid}` per-user docs)
4. Add your GitHub Pages domain to Firebase Authorized Domains
5. Enable Google Calendar API in Google Cloud Console (same project)

## Version History

- **v0.51** — Added a dedicated `privacy.html` page with three sections: Privacy Policy (what's collected, where it's stored, who can access it, third-party assets, Google Calendar scope, cookies, data export & deletion), Terms of Service ("provided as-is", you own your data, no commercial use, limitation of liability), and Medical Disclaimer (not a medical device, not medical advice, emergency guidance, dose-timer caveats, temperature-color caveats, SpO2 caveats). Style-matched to the main app (dark theme, brand gradient), self-contained with relative URLs so the mirror scrub picks it up cleanly. Footer of the main app now links to it as "Privacy · Terms · Disclaimer".
- **v0.50** — New **📅 Calendar** tab. Month grid view shows each illness as severity-colored bars (mild green / moderate orange / severe red) spanning its date range — start dates have a flat-left bar end, recovery dates a flat-right end, so you can read the duration at a glance. Stats card on top: sick days this month, illness count, % of month. Bars are tappable to open the entry in History. Prev/next month nav + "Jump to today" button when off the current month. Below the grid: list of illnesses overlapping this month, plus the existing Google Calendar sync + .ics export controls. Connect-once Google Calendar sync (via a CF worker storing OAuth refresh tokens, similar to pawprints-worker) is on the roadmap — current session-only OAuth still works.
- **v0.49** — Full backup/restore + nicely formatted PDF report. The old "💾 JSON" button only exported `entries`; the new "💾 Backup" exports everything (entries + customMeds + dismissedDoses + schema metadata + counts) under a `illness-tracker/v1` versioned schema. Import is backward-compatible — bare-array files from older versions still work, and full-backup files restore meds and dismissed-dose state too. New "📄 PDF" button opens a print-to-PDF dialog with a polished report: header with date range, 4-up summary cards, risk factors block, per-illness sections with symptom chips + severity badges + vitals tables, timing insights, and most-used medicines. Rendered via hidden iframe so popup blockers don't interfere; user picks "Save as PDF" from the browser's native print dialog.
- **v0.48** — Smoother stat-panel reveal. v0.47 used `max-height: 0 → 3000px` which transitioned to a 3000px ceiling regardless of how short the actual content was — so the visible reveal raced past in the first ~20% of the duration. Switched to the modern `grid-template-rows: 0fr → 1fr` trick which transitions to the panel's natural height, so the entire 0.55s duration is spent on the visible motion. Easing changed to material-style `cubic-bezier(.4,0,.2,1)`, opacity fade replaces the unused translateY animation.
- **v0.47** — Two stat-panel animation fixes: (1) the panel was sliding in from the LEFT because it was reusing the `fadeIn` keyframe (which has `translateX(-50%)` baked in for the toast). New dedicated `slideDownFade` keyframe with `translateY` only, so it slides down from the top. (2) The animation was replaying every 30s as the dose-timer auto-refresh re-rendered the dashboard. Moved the animation to a `.entering` class that `toggleStat` adds on open and removes after 400ms, so re-renders don't re-trigger it.
- **v0.46** — Make the stat card + detail panel actually touch, like a real tab + content area. When a stat is expanded: the grid drops its bottom margin (via `.stats-grid:has(+ .stat-detail.open)`) so the panel sits flush against the cards above; the active card flattens its bottom-left/right corners; the panel flattens its top-left/right corners; their matching colored top borders meet, reading as one continuous unit. Removed the now-redundant downward-pointing notch.
- **v0.45** — Stat panel polish: the expanded card and the slide-down panel now read as one connected tab + content unit (matching colored top border + a downward-pointing notch on the card that aligns with the panel below, per-stat color via `[data-stat]` selectors). The Avg Duration panel now shows each illness's start → recovery dates, and the Avg Gap panel shows the dates of both endpoints for each gap.
- **v0.44** — Tappable dashboard stat cards. Tap any of the 4 top stats (Total Illnesses, Avg Duration, Avg Gap, Risk Factors) and a panel slides down below the grid with the data behind that number — full illness list, per-illness duration bars, gap-between-pairs bars, or the risk-factor breakdown. Chevron rotates to signal the expanded state; tap again to collapse; open state persists across re-renders.
- **v0.43** — Add a discreet page footer with a "🎭 Try the demo" link and the app version stamp. Helps visitors who scroll past the empty state (or already have entries) still discover the demo without re-landing.
- **v0.42** — Installable as a PWA. Replaced the inline SVG-data-URI favicons with a real PNG/ICO icon set (16, 32, 48 in `favicon.ico`, 180 `apple-touch-icon`, 192, 512, and a 512 maskable variant with Android safe-zone padding). Added `site.webmanifest` with `display: standalone`, theme color matching the dark UI, the same brand gradient + 🩺 design, and `start_url: /sick/`. Visitors on Android Chrome or iOS Safari get the "Add to Home Screen" prompt, and the launched app opens chrome-less like a native tracker. Icon set is regenerable from `.scripts/build-icons.py`.
- **v0.41** — Lazy-load `firebase-firestore-compat.js` (99KB) so it stays out of the critical path until a user signs in. The eager `<script defer>` was removed; an `ensureFirestore()` helper now injects the script on first need (the auth listener calls it when the user signs in, and `saveDismissed` / `saveCustomMeds` / `saveToFirestore` / `loadFromFirestore` all `await` it). First-paint downloads went from ~150KB of Firebase compat code to ~50KB — only `firebase-app` + `firebase-auth` are eager-deferred. Unauthenticated visitors (the 99% case) never pay the firestore tax.
- **v0.40** — Fix the LCP regression that v0.39 accidentally introduced. v0.39 wrapped the inline boot in `DOMContentLoaded`, which made `render()` wait for the deferred Firebase scripts to finish downloading before painting the dashboard — mobile FCP/LCP went from 3.4s to 4.6/5.1s. v0.40 restores the synchronous inline render and only defers the Firebase auth bootstrap (the part that pulls the auth iframe + getProjectConfig) to `requestIdleCallback` after first paint
- **v0.39** — Performance pass driven by PSI 84 mobile baseline (FCP/LCP both 3.4s, 520ms unused JS): defer the 3 Firebase SDK scripts and wrap the inline boot in DOMContentLoaded so they no longer block the parser; lazy-load html2canvas on first PNG export click instead of loading 50KB eagerly in head; async-load Google Fonts via `media=print onload swap` with a `<noscript>` fallback; add preconnects for fonts.googleapis.com / fonts.gstatic.com / www.gstatic.com / cdnjs.cloudflare.com so the network handshake overlaps with parsing
- **v0.38** — Demo Mode: empty-state "🎭 Try a Demo" button + shareable `?demo=1` URL load 5 in-memory sample illnesses (active illness with live dose timers, severe flu showing fever color progression, food poisoning, allergies, recurring office cold) + 1 custom med, with recurring location/contact patterns so the Analysis tab shows real risk factors. Demo runs entirely in-memory — saveLocal / saveToFirestore / saveDismissed / saveCustomMeds all short-circuit so real data is never touched. Sign-in and Google Calendar sync are hidden in demo. Backup/restore preserves any existing real state across enter/exit.
- **v0.37** — Open Graph + Twitter card meta tags, canonical URL, theme-color, and a 1200×630 OG image (gradient + stethoscope + angled dashboard screenshot) so links unfurl with a real preview on Discord, iMessage, Slack, X, and search engines instead of falling back to plain text
- **v0.36** — PNG export per illness, versioned filenames, dismissed alerts sync to Firestore, dashboard click-to-history, temperature color coding by fever severity, improved editing flow
- **v0.35** — Dose interval tracking, upcoming doses on dashboard, dismissable overdue alerts, version number display
- **v0.34** — Custom medicine dropdown with "Other" option, persistent custom meds
- **v0.33** — Medicine & vitals sub-entries, favicon, Google Calendar API sync
- **v0.32** — Hardcoded Firebase config, Firestore security rules
- **v0.31** — Converted to single-file HTML for GitHub Pages, Firebase Auth + Firestore
- **v0.30** — Initial React artifact with illness logging, pattern analysis, .ics export
