# Writing news posts

Notes from writing the first set. Most of these exist because the first draft
got them wrong.

## Register

Professional, slightly technical, open-source project. The reader owns the
vehicle and is competent. Not corporate, not chummy, no jokes, no scene-setting.

A release announcement is a good day for the project. Say what shipped and what
it does. Do not open with a history of how bad things used to be.

Being pleased about a release is fine and correct: "Wir freuen uns, die Beta des
neuen Librescoot-Installers 1.3 vorzustellen". Do not stretch that into
marketing.

## Two tests, per sentence

1. **Is this the right voice?**
2. **Does anyone care?**

The second one kills more text than the first. Things that failed it:

- `authopen`, `diskpart`, the RNDIS driver
- `.mender` artifacts, per-board install plans, tiles resolved from a manifest
- the datastore being renamed from Redis to Valkey
- `pm-service` and `vehicle-service` by name
- the MDB's USB port being dual-role, gadget vs host
- a paragraph explaining why the previous paragraph was worth including

**Mechanism is not benefit.** "Firmware goes on as a `.mender` artifact installed
per board" is mechanism. "The installer can now upgrade an existing system, so
you don't have to set everything up again" is the benefit. Write the benefit.

## Each post is written on its date

A post dated 1 May knows nothing about 2 May. This is the rule that broke most
often:

- No "and since then" / "und seitdem" sections listing later point releases.
- No "the version you should install today" - that is a sentence written from
  months later.
- No referencing a later beta in a post dated before it shipped.
- Do not judge a post by how it will read next to a later one. If it was news on
  its date, it is a post. "It would look odd beside the August one" is not a
  reason to skip an April milestone.

The index sorts newest-first. The timeline emerges from the dates; no post needs
to position itself relative to the others.

## Do not invent the before-state

The most damaging error, twice over. Both of these were written confidently and
both were false:

- "Until now, moving a scooter to a newer system meant reinstalling it." Updates
  were always possible over Update Mode, the shell, or the network. What the
  *installer* could not do was update.
- "E20 no longer appears at every power-on." That symptom was introduced and
  fixed between two releases, so no user on the previous stable ever saw it.

Check what was actually true for users at the time. A commit existing is not
evidence that anyone experienced the problem it fixes.

## German

Written as German, not translated from the English. Translating produces:

- **Referents that do not exist.** `Suspend: ... geht der Roller jetzt von selbst
  dorthin` - `dorthin` points at a place, but `Suspend` was a bare label.
  Same class: `Darunter läuft ein Bewegungsalarm`, an `Er` whose only antecedent
  was `die Rollerseite`.
- **Bureaucratic constructions.** `nimmt eine Dauer entgegen`, `deren Erhalt ein
  Upgrade zugesagt hat`, `gibt jeden unterwegs stillgelegten Dienst wieder frei`.
- **Denglisch** where a normal word exists: `ungemergt`, `Turn-by-Turn`,
  `Light- und Dark-Mode`.
- **Headings translated literally.** `## Bekommen` is nobody's German. Use
  `Installieren`, `Update installieren`, `Herunterladen` per context.

Read it aloud as German. Check examples make sense for the vehicle: a scooter is
not left in an airport multi-storey.

Do not explain the obvious back to the reader: "neun Tage eingeben, und nach neun
Tagen ist der Roller wieder da".

## The two languages are separate

- **The English post does not reference German.** Not the translation process,
  not which language pages are written in first, not glosses of German terms.
  The English reader does not care.
- **If nothing changed for one language, do not publish in it.** The handbook
  translation is news in English and not in German.

## Terminology

- Product and UI names stay as they are in both languages: `Hibernate for`,
  `Scheduled hibernate`, `Hop-On`, `Hibernation`, and the channels `stable`,
  `testing`, `nightly`.
- Match the handbook. If the handbook says one thing and a post another, the post
  is wrong.
- Internal names never appear: no `trampoline`, no `Yocto`, no `Wrynose`, no
  `last-ditch hibernate`. Describe the behaviour.
- Do not attribute anything to the OEM. Naming the vehicle is fine: "für den unu
  Scooter Pro".
- Credit contributors plainly in a sentence: "Danke an Jonas."

## Mechanics

- **Every link gets a name.** Not `[/handbook/](/handbook/)`.
- German is the default language, so the handbook publishes at `/handbook/`, not
  `/de/handbook/`.
- **Screenshots must be period-accurate.** A post about an old release must not
  show a screen that did not exist then. Capture sets from current code contain
  screens no shipped release has.
- Show the features. Map and routing are the headline; a cluster shot is not a
  substitute for a map with an active route.
- Language-match the UI text in screenshots to the post language where a capture
  exists in both.
- Do not pin a post to a version number that goes stale ("the download page
  currently links beta.3"). Link the downloads page and the releases list.

## Process

- An agent's report on its own writing is not verification. "German rewritten as
  German" is a claim, not a check. Read the output.
- Cut before adding. Every one of these posts got better and shorter.
