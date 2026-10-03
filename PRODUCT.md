# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS/JS (`index.html`) rendering `items.json`; Python stdlib fetcher (`fetch.py`) and local server (`serve.py`, started by `launch.command`); optional GitHub Pages + hourly GitHub Actions. No frameworks, no build step.

## Users

One person (the owner), using it as a personal daily AI briefing on their own Mac.

## Product Purpose

Collect the latest AI research and release news from many sources into one page, so the owner can see in seconds what is new, especially from the major labs, without visiting each site.

## Positioning

A personal, self-run aggregator: the owner picks the sources (`sources.json`), including small labs that general news sites miss (TypeSafe/Jev, Nous Research/Hermes), with no accounts, ads, or AI summaries.

## Operating Context

Opened once or twice a day for a quick scan. Refresh button re-fetches live when run through `serve.py`. Items: title, source, category (Lab / Research / Press), date, short excerpt from the source, link out.

## Capabilities and Constraints

- Search, filter by source, filter by category, live refresh, built-in "How to run this site" help.
- 19 sources, ~230 items, 60-day window; arXiv capped at 30 per category.
- Excerpts come only from the sources' own feeds; never copy full articles.
- Some dates are estimated (TypeSafe, Nous Research blogs).

## Brand Commitments

- Must follow the system light/dark setting (dark mode kept).
- Major labs (OpenAI, Anthropic, Google DeepMind, TypeSafe/Jev, Nous Research/Hermes) must stand out from press and papers.
- English UI. Current name "AI News Feed" (no other name chosen).

## Evidence on Hand

Real live data in `items.json`. No logos or brand assets; do not use lab logos or trademarks.

## Product Principles

1. Scan first: what's new from the big labs is visible in seconds.
2. Signal over volume: papers and press are present but never drown lab releases.
3. Honest data: show the source's own words, mark estimated dates, show failed sources.
4. Zero setup: one command runs it; no dependencies.
