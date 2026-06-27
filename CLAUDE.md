# CLAUDE.md — MiseOS Active Project Context
# Version: 1.0
# This file is the single source of truth for all AI-assisted development.
# Claude Code reads this file automatically at the start of every session.
# Do not delete or rename this file.

---

## Project Identity

**Name:** MiseOS
**Type:** Back-of-House (BOH) kitchen operations platform
**Repo:** https://github.com/bwaters9-maker/MiseOS_App
**Status:** Active development

---

## Tech Stack

- **Frontend:** React 19 + TypeScript
- **Build:** Vite (port 3000, HMR enabled)
- **Styling:** Tailwind CSS v4 (global imports only, zero sub-specifiers)
- **Database:** Firebase Firestore (cloud state replication)
- **Server:** Express (server.ts)
- **Package Manager:** pnpm

---

## What MiseOS Is

A static, chef-managed Back-of-House command center for high-end
culinary operations.

MiseOS replaces reactive kitchen management with disciplined,
chef-controlled data pipelines built around a pre-loaded,
human-verified ingredient library.

**Core Principle — Master Pantry Mandate:**
All ingredient data is static and human-verified. Chefs select
from a pre-loaded library. There is no invoice scanning, no live
syncing, and no unpredictable external data of any kind.

---

## Operational Philosophy

- **Enlightened Hospitality:** The guest is the center of the universe
- **Prep-Heavy, Service-Light:** Excellence is built in back-of-house
- **Chef-Managed Data:** Human verification is the only source of truth
- **Milestone Moments:** Every experience is curated, never reactive
- **Professional Integrity:** Craftsmanship is non-negotiable

---

## Active Features — LOCKED SCOPE

These are the only three features that exist in MiseOS.
Do not add, extend, or suggest features outside this list.

### Brain Dump Module [LOCKED]
Captures raw operational data, kitchen tasks, and intake
information. Organizes systematically to eliminate mental clutter.

### Intelligent Insight Rail [LOCKED]
Persistent UI component surfacing critical operational data,
alerts, and high-priority tasks. Designed to reduce cognitive
load, not add to it.

### Station Matrix [LOCKED]
Digital translation of the physical kitchen line. Organizes
tasks, prep lists, and cross-station workflows for maximum
operational efficiency.

---

## Key Files — Know These Before Touching Anything

| File | Purpose |
|------|---------|
| `src/main.tsx` | App entry point |
| `src/App.tsx` | Root component |
| `src/hooks/useKitchenState.ts` | ALL state mutations go here |
| `src/lib/costEngine.js` | Ingredient
