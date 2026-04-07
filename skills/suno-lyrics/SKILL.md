---
name: suno-lyrics
description: >
  Generates song titles and lyrics in both Czech and Slovak for Suno AI.
  Use this skill whenever the user wants to write a song, create lyrics, come up with
  a song title, or generate music content in Czech or Slovak — even if they just mention
  a theme, mood, story, or feeling they want to turn into a song. Trigger for requests
  like "write me a song about...", "make lyrics for...", "song o...", "text písně...",
  "napíš mi pieseň o...", or any variation suggesting they want musical content created.
---

# Suno Lyrics Generator (Czech + Slovak)

## Workflow — three steps, always

This skill works in three steps. Do not skip any of them.

### Step 0 — Language, then artist/band selection

**First, ask which language:**

```
V akom jazyku má byť pieseň?

1. Čeština
2. Slovenčina
```

Wait for the answer. Then ask about the artist/band.

**Then, read all `.md` files in the `bands/` directory** (located next to this SKILL.md). List the saved artists/bands and ask the user which one to use — or whether to proceed without one.

**Format (in the user's language):**
```
Pro koho tvoříme píseň?

1. [Band name] — [one-line description]
2. [Band name] — [one-line description]
…
0. Žádný — volný výběr stylu

Vyber číslo nebo napiš název.
```

If the user picks an artist, read their full profile from `bands/<filename>.md`. Everything that follows — the style menu, the lyrics tone, the Suno prompt — must stay within that artist's sound identity. The style menu in Step 1 should offer variations *within* that artist's world, not completely different genres.

If no artist is selected (option 0 or no bands saved yet), proceed freely as before.

### Step 1 — Propose styles first

Before writing any lyrics, propose **4–5 style options** that would suit the user's theme. Each option should feel like a distinct musical direction — not just genre names, but a short evocative description of the vibe, energy, and sound.

**Format:**
```
Jaký styl ti sedí nejlépe? Nabízím několik směrů:

1. **Worship rock** — silný, emotivní, elektrická kytara a piano, vokály plné vášně
2. **Akustická balada** — klidná, intimní, jen kytara a hlas, jako modlitba šeptem
3. **Gospel/soul** — rytmický, radostný, sbor v refrénech, oslavný náboj
4. **Folk worship** — organické zvuky, banjo nebo mandolína, příběhový text
5. **Ambient worship** — prostorné, pomalé, syntetizátory a smyčce, meditativní

Řekni mi číslo nebo popiš co tě táhne — nebo kombinuj více stylů dohromady.
```

Always write the style menu in the same language the user wrote in (Czech or Slovak). Make the options genuinely varied — don't offer 5 slight variations of the same thing. Think about what would actually feel different to sing and to hear.

**Two styles must always be included in every menu, no exceptions:**
- One option featuring **prominent cello** (e.g. cello-led worship, neoclassical, cinematic strings with cello as the lead voice)
- One option featuring **fingerstyle guitar** (e.g. solo acoustic fingerpicking, intimate and close-miked, no band — just voice and fingers on strings)

Wait for the user's response before proceeding to step 2. Do not generate lyrics yet.

### Step 2 — Generate titles and lyrics

Once the user picks a style (or describes what they want), generate output **in the one language selected in Step 0 only**. Never generate both languages in the same response.

- 3 title options in the selected language
- Full lyrics in the selected language
- All formatted for direct use in Suno AI
- If an artist was selected in Step 0, the Suno style prompt must always include the artist's base Suno prompt string from their profile.

The user should feel like they got a real, professional song — not a template with blanks filled in.

## Generating the titles

Offer 3 title options per language (Czech + Slovak). Titles should feel catchy and authentic — like something you'd actually see on a streaming platform. Vary the tone: one can be poetic, one direct/punchy, one slightly unexpected or metaphorical.

**Format:**
```
## Názvy / Názvy

**Česky:**
1. Název A
2. Název B
3. Název C

**Slovensky:**
1. Názov A
2. Názov B
3. Názov C
```

## Writing the lyrics

### Song length

Target **2:30–4:30 minutes** of music. A short song in Suno runs about 1:15 — that's not enough. To hit the target length, use a fuller structure:

**Required structure for 2:30–4:30 min:**
- `[Intro]` — 4 lines (sung or instrumental cue)
- `[Verse 1]` — **8–10 lines**
- `[Pre-Chorus]` — 4 lines
- `[Chorus]` — **6–8 lines**
- `[Verse 2]` — **8–10 lines**
- `[Pre-Chorus]` — 4 lines
- `[Chorus]` — 6–8 lines
- `[Verse 3]` — **6–8 lines** (emotional peak or new perspective)
- `[Chorus]` — 6–8 lines
- `[Bridge]` — **6–8 lines**
- `[Chorus]` — 6–8 lines
- `[Chorus]` — repeated with variation (last 2 lines changed)
- `[Outro]` — **6–8 lines**, fades into silence

**Line count matters.** Suno generates roughly 15–20 seconds per section. A 4-line verse = ~1:15 song. An 8-line verse = ~2:30+. Always hit the minimum line counts above.

Never write a verse with fewer than 8 lines. Never write a chorus with fewer than 6 lines. If in doubt, add more — a longer song is always better than a short one.

### What goes in the lyrics block — strict rule

**Only singable text belongs in the lyrics block.** Everything else must be in square brackets.

- `[Verse 1]`, `[Chorus]`, `[Bridge]` — structural tags ✓
- `[Instrumental break]`, `[Guitar solo]`, `[Loop builds]` — production instructions ✓
- Any plain text outside brackets **will be sung by Suno** — never write production notes, descriptions, or stage directions as plain text

**Wrong:**
```
Loop přichází tiše — druhý hlas jako ozvěna
```
*(Suno will sing this)*

**Correct:**
```
[Loop builds — second voice enters as echo]
```
or simply remove it and let the style prompt handle it.

Vary the structure based on genre if the user mentions one. If no genre is specified, choose freely based on the theme — match the emotional tone.

Write the Czech and Slovak versions as genuine separate translations, not word-for-word mirrors. Slovak and Czech are close but distinct — respect that. The Slovak version should feel natural to a native Slovak speaker, not like a Google Translate of the Czech.

### Slovak pronunciation — Suno AI pitfall

Suno AI may confuse Slovak with Czech and **mispronounce adjectives/adverbs ending in `-ne`** — reading the `n` as soft (like Czech `-ně`), which sounds wrong in Slovak.

**Affected words to avoid in Slovak lyrics:**
- správne, múdre, čisté, jasne, ticho (as adverb)... any adjective/adverb ending in `-ne`, `-dre`, `-stre` etc.

**Rule:** In Slovak lyrics, always replace these forms with a synonym or rephrase the line so the problematic word disappears entirely.

| Avoid | Use instead |
|---|---|
| správne slová | dobré slová / tie pravé slová |
| nie je za správne správanie | nie je za dobré správanie |
| urobil si to správne | urobil si to dobre / mal si pravdu |
| čisté srdce | srdce bez škvŕn / úprimné srdce |
| múdre rozhodnutie | dobré rozhodnutie / pravé rozhodnutie |

When in doubt, read the Slovak line aloud in your head — if the `-ne` ending could be misread as Czech soft `-ně`, rewrite the line.

**Try to make every song feel different.** Vary:
- Rhyme schemes (ABAB, AABB, free, half-rhymes…)
- Rhythm and syllable density
- Imagery and metaphors
- Emotional tone (melancholic, energetic, hopeful, raw…)

## Suno AI formatting

Suno reads structural tags to understand song layout. Always wrap sections in tags:

```
[Verse 1]
...lyrics...

[Chorus]
...lyrics...

[Verse 2]
...lyrics...

[Chorus]
...lyrics...

[Bridge]
...lyrics...

[Chorus]
```

Optional Suno tags you can use when appropriate:
- `[Intro]` — instrumental or spoken intro
- `[Outro]` — closing section
- `[Pre-Chorus]` — build-up before chorus
- `[Instrumental Break]` — for solo or break sections

**Do not** add genre tags, BPM, or style metadata in the lyrics block — Suno handles those separately.

## Output structure

Present the full output like this:

---

## Názvy / Názvy

**Česky:**
1. ...
2. ...
3. ...

**Slovensky:**
1. ...
2. ...
3. ...

---

## Česky — [chosen or first title]

[Verse 1]
...

[Chorus]
...

[Verse 2]
...

[Chorus]
...

[Bridge]
...

[Chorus]
...

---

## Slovensky — [chosen or first title]

[Verse 1]
...

[Chorus]
...

[Verse 2]
...

[Chorus]
...

[Bridge]
...

[Chorus]
...

---

## Suno style prompt

After the lyrics, always suggest a Suno AI style prompt — the text the user pastes into Suno's "Style of Music" field. This should capture:
- **Genre** (e.g. worship, folk, rock, pop, ambient…)
- **Mood/energy** (e.g. passionate, melancholic, uplifting, raw, gentle…)
- **Vocal style** (e.g. powerful female vocals, male choir, soft tenor, raspy voice…)
- **Instrumentation hints** (e.g. acoustic guitar, piano, strings, electric guitar, synth pads…)
- **Tempo feel** (e.g. slow ballad, mid-tempo, driving, anthemic…)

Keep the prompt short — Suno works best with 10–20 words. Write it in English (Suno understands English style prompts best regardless of lyric language).

**For Slovak lyrics always append:** `Slovak language, hard consonants` — this helps Suno use Slovak phonetics instead of defaulting to Czech softening. Combined with avoiding `-ne` adjective endings (see below), this gives the best pronunciation results.

**For Czech lyrics always append:** `Czech language` — prevents Suno from defaulting to Slovak or Polish phonetics. Czech-specific sounds to watch out for:
- `ř` — unique Czech sound, Suno often mispronounces it as plain `r`. Where possible replace with a synonym that avoids `ř` (e.g. `říkám` → `povídám`, `přijdu` → `půjdu`, `řeka` → `voda`). If `ř` is unavoidable, keep it — the language tag helps.
- `ě` — soft vowel, generally handled well but can be mispronounced after `d/t/n`. If a line sounds wrong, rephrase to avoid `dě/tě/ně` clusters.
- Long vowels `á/é/í/ů` — Suno sometimes shortens them; prefer syllabically simpler words in the chorus hook where clean pronunciation matters most.

**Phonetic respelling — last resort only**

If a word cannot be replaced by a synonym and mispronunciation is likely, you may write it phonetically (e.g. `správneh` instead of `správne`). However, **always provide both versions** when doing this:

```
**Verzia pre Suno (fonetická):**
Urobil si to správneh

**Verzia na čítanie (pravopisná):**
Urobil si to správne
```

The user can then decide which to use. Never silently replace spelling without showing the original.

**Format:**
```
## Suno Style Prompt

`passionate worship rock, powerful female vocals, electric guitar, piano, anthemic`
```

Suggest one primary prompt, then offer 1–2 variations for different interpretations of the same song.

---

### Step 3 — Submit to Suno (optional)

After presenting the lyrics and style prompt, ask the user if they want to generate the song directly:

```
Chceš píseň rovnou vygenerovat přes Suno API?
Stačí říct které titulky a jaký jazyk.
```

If the user confirms, use the `mcp__suno__generate_music` tool with:
- `custom_mode = True`
- `instrumental = False` (or `True` if user wants no vocals)
- `model = "V4"` (default; offer V4_5 or V5 if user wants longer/higher quality)
- `prompt` = the full lyrics block (with section tags)
- `style` = the suggested Suno style prompt (English, max 200 chars for V4)
- `title` = the chosen title (max 80 chars for V4)
- `callback_url = "https://httpbin.org/post"` (placeholder — we poll manually)

After submitting, poll once with `mcp__suno__get_task_status` using the returned `taskId`.

**Status progression:** `PENDING` → `TEXT_SUCCESS` → `FIRST_SUCCESS` → `SUCCESS`

**Share stream URLs as soon as they appear** — they are available from `TEXT_SUCCESS` onward, before the download is ready. Present them immediately so the user can listen without waiting:

```
Generuje se... Streamy jsou už dostupné:

**[Title] — verze 1** (stream)
🎵 [sourceStreamAudioUrl]

**[Title] — verze 2** (stream)
🎵 [sourceStreamAudioUrl]

Chceš počkat na finální stažitelné soubory? (ještě ~1–2 min)
```

Do NOT sleep or auto-poll in a loop. After each poll, report the status and ask the user if they want to poll again. When `SUCCESS`, present the final download URLs:

```
Hotovo! Finální verze ke stažení:

**[Title] — verze 1** (X:XX min)
🎵 [sourceAudioUrl]

**[Title] — verze 2** (X:XX min)
🎵 [sourceAudioUrl]
```

Use `sourceAudioUrl` for download links and `sourceStreamAudioUrl` for stream links (direct Suno CDN URLs).

If generation fails (`CREATE_TASK_FAILED`, `GENERATE_AUDIO_FAILED`, `SENSITIVE_WORD_ERROR`), report the `errorMessage` and offer to retry with adjusted parameters.

**Before submitting**, check credits with `mcp__suno__get_credits` — each generation costs credits. Warn the user if balance is low (under 10).

---

## Tips for quality

- Czech and Slovak lyrics work best with natural speech rhythm — lyrics that feel singable, not forced
- Use colloquialisms where appropriate — real songs don't always use formal grammar
- Repetition in choruses is intentional; the hook should be memorable
- The bridge should shift something — emotionally, lyrically, or rhythmically
- Avoid clichés unless used ironically or purposefully
- The Suno style prompt should feel like a natural extension of the lyrics — if the song is raw and intimate, the prompt shouldn't say "epic orchestral"
