---
name: AI News Feed
description: A personal AI news wire; major-lab releases arrive as red bulletins above routine copy.
colors:
  ground: "#eef0f2"
  raise: "#ffffff"
  ink: "#15161a"
  muted: "#535861"
  rule: "#d4d8de"
  band: "#15161a"
  band-ink: "#eef0f2"
  band-muted: "#a9aeb6"
  band-rule: "#34363d"
  band-red: "#ff6a55"
  bulletin-red: "#c4241a"
  bulletin-red-ink: "#ffffff"
  lab-ochre: "#845500"
  paper-blue: "#2b4d80"
  press-grey: "#565a61"
  repo-green: "#1e6b41"
  bigtech-violet: "#5b3d9e"
  ground-dark: "#111215"
  raise-dark: "#191b1f"
  ink-dark: "#e8e9e5"
  muted-dark: "#a0a5ad"
  rule-dark: "#2a2d33"
  band-dark: "#1c1e23"
  band-ink-dark: "#e8e9e5"
  band-muted-dark: "#9ca1a9"
  band-rule-dark: "#31343b"
  bulletin-red-dark: "#ff5c49"
  bulletin-red-ink-dark: "#170806"
  lab-ochre-dark: "#e6a842"
  paper-blue-dark: "#93b5ec"
  press-grey-dark: "#a0a5ad"
  repo-green-dark: "#6fd39a"
  bigtech-violet-dark: "#b9a3f2"
typography:
  wordmark:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.55rem"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.01em"
    fontVariation: "'wdth' 75"
  headline:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 800
    letterSpacing: "-0.01em"
    fontVariation: "'wdth' 85"
  title:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 600
    lineHeight: 1.35
    fontVariation: "'wdth' 87.5"
  dateline:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 700
    letterSpacing: "0.02em"
    fontVariation: "'wdth' 85"
  body:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.5
  excerpt:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 600
    lineHeight: 1
  data:
    fontFamily: "JetBrains Mono, ui-monospace, Menlo, monospace"
    fontSize: "0.8125rem"
    fontWeight: 400
    fontFeature: "'tnum'"
  code:
    fontFamily: "JetBrains Mono, ui-monospace, Menlo, monospace"
    fontSize: "0.6875rem"
    fontWeight: 600
    lineHeight: 1
rounded:
  code: "3px"
  tab: "4px"
  control: "6px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  row: "14px"
  lg: "16px"
  xl: "24px"
  section: "36px"
  help: "48px"
components:
  button-band:
    backgroundColor: "transparent"
    textColor: "{colors.band-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.control}"
    padding: "0 14px"
    height: "36px"
  button-band-hover:
    backgroundColor: "{colors.band-rule}"
  tab:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.label}"
    rounded: "{rounded.tab}"
    padding: "0 12px"
    height: "30px"
  tab-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ground}"
  input-search:
    backgroundColor: "{colors.raise}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "0 12px 0 36px"
    height: "38px"
  code-bulletin:
    backgroundColor: "{colors.bulletin-red}"
    textColor: "{colors.bulletin-red-ink}"
    typography: "{typography.code}"
    rounded: "{rounded.code}"
    padding: "5px 6px"
  code-lab:
    backgroundColor: "transparent"
    textColor: "{colors.lab-ochre}"
    typography: "{typography.code}"
    rounded: "{rounded.code}"
    padding: "5px 6px"
  code-paper:
    backgroundColor: "transparent"
    textColor: "{colors.paper-blue}"
    typography: "{typography.code}"
    rounded: "{rounded.code}"
    padding: "5px 6px"
  code-press:
    backgroundColor: "transparent"
    textColor: "{colors.press-grey}"
    typography: "{typography.code}"
    rounded: "{rounded.code}"
    padding: "5px 6px"
  code-repo:
    backgroundColor: "transparent"
    textColor: "{colors.repo-green}"
    typography: "{typography.code}"
    rounded: "{rounded.code}"
    padding: "5px 6px"
---

# Design System: AI News Feed

## Overview

**Creative North Star: "The Wire Desk"**

The page is a news-agency wire terminal, not a card gallery. Every item carries a priority code, and major-lab releases come in as MAJOR LAB items that sit above routine copy. The hierarchy comes from the wire's own conventions: an ink header band, ruled rows, datelines and codes. Coloured chips and floating cards play no part in it.

Density is high and calm. Rows are separated by hairline rules on a cool grey-white ground (light) or a carbon ground (dark), and nothing is lifted off the page. Red is the one loud colour, and it means priority: major labs, the bulletin lane, the new-item signal and focus. Ochre, blue and grey code the other categories quietly. Type works as two voices. Semi-condensed Archivo carries everything a person reads, and JetBrains Mono carries everything a machine stamps (times, codes, counts).

The page follows the system light/dark setting. Both modes share every role, and only the values change.

**Key Characteristics:**
- Ink-black header band with a 3px bulletin-red bottom rule.
- Rows ruled by 1px lines, never boxed as cards.
- A four-column wire grid: time | code | source | headline + excerpt.
- Bordered mono priority codes (MAJOR LAB filled red; LAB, BIG TECH, PAPER, PRESS and REPO outlined in their category colour).
- Datelines ruled by a 2px ink line, with a mono item count right-aligned.
- Flat throughout, with no shadows.

## Colors

A cool neutral newsprint with one bulletin red for priority and two muted category inks.

### Primary
- **Bulletin Red** (`bulletin-red` / `bulletin-red-dark`): Reserved for major-lab priority. It fills the MAJOR LAB code, colours major-lab source names, rules the top of the bulletin lane and the bottom of the header band, and marks the new-item dot, focus outlines, text selection, the caret, help links and "more bulletins". In dark mode it brightens to a coral so it still reads on carbon. **Bulletin Red Ink** sits on red fills.

### Secondary
- **Lab Ochre** (`lab-ochre` / `lab-ochre-dark`): Outline and text of the LAB code for non-major labs. It sits second in rank and is never a fill.

### Tertiary
- **Paper Blue** (`paper-blue` / `paper-blue-dark`): Outline and text of the PAPER code (research).
- **Press Grey** (`press-grey` / `press-grey-dark`): Outline and text of the PRESS code. It is deliberately close to Muted, because press is routine copy.
- **Repo Green** (`repo-green` / `repo-green-dark`): Outline and text of the REPO code for GitHub Trending repositories.
- **Big Tech Violet** (`bigtech-violet` / `bigtech-violet-dark`): Outline and text of the BIG TECH code for research from big tech companies other than the four major labs (Microsoft, Apple, Amazon, Salesforce, NVIDIA, IBM).

### Neutral
- **Cool Ground** (`ground`): Page background and the sticky control row. Carbon (`ground-dark`) in dark mode.
- **Raised White** (`raise`): Field and tab-group fill and help code blocks. It is the only surface lighter than the ground.
- **Wire Ink** (`ink`): Headlines, body text, dateline rules, the active tab fill.
- **Muted Slate** (`muted`): Times, excerpts, source names on routine rows, section notes, placeholders.
- **Hairline** (`rule`): Row dividers, the control-row underline, field and tab-group borders.
- **Header Band** (`band`, `band-ink`, `band-muted`, `band-rule`): The ink band holding the wordmark, wire status and Refresh. In dark mode it sits one step above the carbon ground, so it stays a distinct strip.

### Named Rules
**The One Red Rule.** Red always means priority (major lab, bulletin, new, focus). It is never decoration, and no other hue is ever filled.

**The Outlined Rank Rule.** Only MAJOR LAB is a filled code. Every other category code is a 1px outline in its own ink, so rank shows at a glance without a field of coloured chips.

## Typography

**Display Font:** Archivo (variable width 62–125, weight 400–800), with Helvetica Neue and Arial as fallbacks.
**Body Font:** Archivo, at normal width.
**Label/Mono Font:** JetBrains Mono (400, 600), with ui-monospace and Menlo as fallbacks.

**Character:** A semi-condensed grotesque gives headlines a wire-service urgency without shouting. The mono is a stamp, not a voice.

### Hierarchy
- **Wordmark** (800, 1.55rem, line-height 1, width 75%, uppercase): The header band's "AI News Feed" only.
- **Headline** (800, 1.25rem, width 85%): Section heads (Major labs, The wire, the help summary).
- **Title** (600, 1.0625rem, 1.35, width 87.5%): Row headlines, with `text-wrap: pretty`. Major-lab rows step up to 700.
- **Dateline** (700, 0.9375rem, width 85%, uppercase, +0.02em): Day headings over the wire. Only the date is uppercase.
- **Body** (400, 1rem, 1.5): Help prose, capped at 72ch.
- **Excerpt** (400, 0.9375rem, Muted): Clamped to two lines, 72ch max. Hidden in the bulletin lane.
- **Label** (600, 0.875rem, line-height 1): Buttons, tabs, status and section notes.
- **Data** (mono, 0.8125rem, tabular numbers): Times, relative ages, counts, the updated stamp.
- **Code** (mono 600, 0.6875rem): Priority codes only.

### Named Rules
**The Stamp Rule.** Mono is only for machine-stamped data: times, codes, counts and commands. Prose, labels and headlines are never mono.

**The Narrow Voice Rule.** Width tracks importance. The wordmark is set at 75%, heads at 85% and headlines at 87.5%, while body text stays at 100%.

## Layout

The page is a single centred column, max 1000px wide with 24px gutters (16px under 640px). From the top: the header band (min-height 64px; wordmark, then a status line that flexes to fill the middle, then actions on the right), a sticky control row (search, category tabs, source select), the bulletin lane, the dated wire, and the help section in a collapsible block at the foot.

The wire row is a grid of `4.25rem 6.5rem 10rem 1fr` with a 16px column gap and 14px vertical padding. Under 640px the row collapses: time, code and source share one line, and the headline and excerpt span the full width below. Under the same breakpoint the status line drops to its own line in the band, and the tabs and select stretch to fill the control row.

Rhythm: sections open 36px down, each dateline sits 32px above its rows, and help starts 48px down. Inside rows and controls the spacing steps are 4, 8, 12, 16 and 24px.

## Elevation & Depth

The page is flat with no shadows. Depth is tonal and ruled. The ink band is the darkest plane. The sticky control row repeats the ground colour, closed off by a hairline. Fields and the tab group sit on Raised White. Weight comes from rule thickness: a 1px hairline separates rows, a 2px ink line marks a dateline or the help section, and a 3px red line marks the header band's bottom edge and the top of the bulletin lane.

### Named Rules
**The Rule-Weight Rule.** Hierarchy between regions comes from rule thickness (1px, 2px ink, 3px red), never from shadows or boxes.

## Shapes

Corners are nearly square and get smaller as elements get smaller: 6px for controls (buttons, fields, the tab group), 4px for tabs inside the group and inline code, 3px for priority codes. The only round element is the 7px new-item dot. Rows, sections and the band have no corners because they are never boxes. Icons are 16px inline SVG strokes (2px, round caps) drawn in the current text colour.

## Components

### Buttons
Quiet tools that sit on the band or the ground.
- **Shape:** Small corners (6px), 36px tall, 0 14px padding, label type, optional 16px leading icon at an 8px gap.
- **Band button (Refresh):** Transparent with a band-rule border and band-ink text. On hover it fills with band-rule. While busy it shows a wait cursor, muted text and a spinning icon (0.9s linear, removed under reduced motion), and the label reads "Fetching…".
- **Text action:** "+N more from major labs" is a full-width left-aligned red label over a hairline, underlined on hover. "How to run" is a band-muted link that turns band-ink and underlined on hover.
- **Focus:** Global 2px red outline with a 2px offset.

### Chips (category tabs)
- **Style:** A segmented group on Raised White with a hairline border (6px corners, 3px inner padding, 2px gap). Tabs are 30px tall, transparent, with muted label text.
- **State:** Hover changes the text to ink. The pressed tab (`aria-pressed="true"`) is filled ink with ground-colour text, so the active choice is an inverse, not a hue.

### Inputs / Fields
- **Style:** Raised White fill, hairline border, 6px corners, 38px tall, 0.9375rem text. Search has a 16px muted icon inset 12px from the left. The select uses a CSS-drawn chevron (no icon font) and native `appearance: none`.
- **Hover:** The border darkens to muted. **Focus:** the global red outline.

### Navigation
- **Header band:** Ink band with a 3px red bottom rule. The wordmark is on the left. The status line in the middle is band-muted text with band-ink mono figures (updated time, new count, sources reporting, or an "Unavailable: …" alert in place of the sources count). Actions sit on the right.
- **Control row:** Sticky to the top, ground fill, hairline underline.

### Wire Row (signature)
- **Grid:** time | code | source | headline + excerpt, separated from the next row by a hairline. The first row under a dateline or at the top of the bulletin lane drops its top rule.
- **Time:** Muted mono. It shows `HH:MM` (24h) on the wire, a relative age (`11h`, `1d`) in the bulletin lane, `—` when the feed carries only a date, and `est.` when the date is estimated.
- **Major rows:** The source name turns red and the headline steps to 700.
- **New since last visit:** A 7px red dot before the time, plus a one-time arrival wash (14% red mixed into the background, fading over 1.6s on `cubic-bezier(.16, 1, .3, 1)`). The wash is removed under reduced motion.
- **Headline:** Ink, no underline at rest, underlined on hover, opens the source.

### Priority Code (signature)
Mono 600 at 0.6875rem, padded 5px 6px, 3px corners, 1px border in the current colour. MAJOR LAB is filled red with red-ink text. LAB, PAPER and PRESS are outlines in ochre, blue and press grey.

### Bulletin Lane (signature)
A 3px red top rule over up to four major-lab rows from the last seven days, with excerpts hidden and a "+N more from major labs" toggle. The lane hides while any filter is active.

### Dateline
Uppercase semi-condensed day ("Friday, 2 October 2026") on a 2px ink rule, with the day's item count in muted mono on the right.

## Do's and Don'ts

### Do:
- **Do** give every item a priority code, and keep MAJOR LAB the only filled one.
- **Do** separate rows with 1px hairlines, and mark region breaks with 2px ink or 3px red rules.
- **Do** set times, codes and counts in JetBrains Mono with tabular numbers, and everything else in Archivo.
- **Do** narrow Archivo's width as importance rises (75% wordmark, 85% heads, 87.5% headlines).
- **Do** define every colour role in both light and dark, following `prefers-color-scheme`.
- **Do** show estimated or missing times honestly (`est.`, `—`) rather than inventing a clock time.

### Don't:
- **Don't** box items as cards or lift anything with shadows.
- **Don't** use red for anything that isn't priority, newness or focus.
- **Don't** fill LAB, PAPER or PRESS codes, or add new hue-filled chips.
- **Don't** use lab logos or trademarks. The source name in text is the identifier.
- **Don't** set prose or headlines in mono.
