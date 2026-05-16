# Illness Tracker

**Current Version: v0.44**

Live deployments: [itsavibecode.github.io/sick](https://itsavibecode.github.io/sick/) (primary) and [dev.rizzo.cc/sick](https://dev.rizzo.cc/sick/) (mirror).

Track · Analyze · Prevent — A personal illness tracking app with pattern analysis, medicine/vitals logging, Google Calendar sync, and Firebase cloud storage.

## Files

| File | Description |
|------|-------------|
| `index.html` | Current release — single-file app, served by GitHub Pages |
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
