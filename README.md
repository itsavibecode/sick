# Illness Tracker

**Current Version: v0.36**

Track · Analyze · Prevent — A personal illness tracking app with pattern analysis, medicine/vitals logging, Google Calendar sync, and Firebase cloud storage.

## Files

| File | Description |
|------|-------------|
| `v0.36.html` | Current release — single-file app, deploy to GitHub Pages |
| `firestore.rules` | Firestore security rules — paste into Firebase Console |
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

1. Deploy `v0.36.html` to GitHub Pages
2. Configure Firebase: Authentication (Google), Firestore Database
3. Apply `firestore.rules` in Firebase Console → Firestore → Rules
4. Add your GitHub Pages domain to Firebase Authorized Domains
5. Enable Google Calendar API in Google Cloud Console (same project)

## Version History

- **v0.36** — PNG export per illness, versioned filenames, dismissed alerts sync to Firestore, dashboard click-to-history, temperature color coding by fever severity, improved editing flow
- **v0.35** — Dose interval tracking, upcoming doses on dashboard, dismissable overdue alerts, version number display
- **v0.34** — Custom medicine dropdown with "Other" option, persistent custom meds
- **v0.33** — Medicine & vitals sub-entries, favicon, Google Calendar API sync
- **v0.32** — Hardcoded Firebase config, Firestore security rules
- **v0.31** — Converted to single-file HTML for GitHub Pages, Firebase Auth + Firestore
- **v0.30** — Initial React artifact with illness logging, pattern analysis, .ics export
