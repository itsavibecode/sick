# Illness Tracker

**Current Version: v0.37**

Track · Analyze · Prevent — A personal illness tracking app with pattern analysis, medicine/vitals logging, Google Calendar sync, and Firebase cloud storage.

## Files

| File | Description |
|------|-------------|
| `index.html` | Current release — single-file app, served by GitHub Pages |
| `og-image.png` | 1200×630 social preview image (Open Graph + Twitter) |
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

- **v0.37** — Open Graph + Twitter card meta tags, canonical URL, theme-color, and a 1200×630 OG image (gradient + stethoscope + angled dashboard screenshot) so links unfurl with a real preview on Discord, iMessage, Slack, X, and search engines instead of falling back to plain text
- **v0.36** — PNG export per illness, versioned filenames, dismissed alerts sync to Firestore, dashboard click-to-history, temperature color coding by fever severity, improved editing flow
- **v0.35** — Dose interval tracking, upcoming doses on dashboard, dismissable overdue alerts, version number display
- **v0.34** — Custom medicine dropdown with "Other" option, persistent custom meds
- **v0.33** — Medicine & vitals sub-entries, favicon, Google Calendar API sync
- **v0.32** — Hardcoded Firebase config, Firestore security rules
- **v0.31** — Converted to single-file HTML for GitHub Pages, Firebase Auth + Firestore
- **v0.30** — Initial React artifact with illness logging, pattern analysis, .ics export
