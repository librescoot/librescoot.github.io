---
lang: en
title: "Librescoot 1.3: 2D maps, street names and updates on the scooter"
date: 2026-08-28
permalink: /news/librescoot-1-3/
summary: "A flat 2D map with north-up or heading-up, street names on offline maps, route preferences, and update settings you can reach from the scooter. Plus a long list of faults that were previously never reported at all."
image: /images/news/map-2d-heading.png
image_alt: "The 2D map view, heading-up, with an active route"
---

Librescoot 1.3 is out. The headline is navigation: a second map view, street
names, and settings for how routes are planned. Behind it sits a lot of
reliability work.

## Maps and navigation

There is now a flat 2D map view alongside the 3D one, with a north-up or
heading-up toggle. The default stays 3D.

![The 2D map, heading-up, with an active route](/images/news/map-2d-heading.png)

Offline maps now show street names. Route planning gained two settings under
*Map & Navigation*: a route preference of fastest or shortest, and Avoid
Cobblestone at off, low, medium or high, defaulting to medium.

Position tracking was reworked underneath. The marker no longer creeps forward
while you are stopped, and no longer freezes and then jumps as you pass a
corner. Roundabout icons are redrawn, reroutes start from a better-chosen
position, and the road name and speed limit keep up.

## Updates from the scooter

Update settings moved onto the dashboard, under *Settings > System > Updates*:
check frequency, a manual check, update type, and release channel.

![The Updates menu on the scooter](/images/news/updates-menu.png)

Switching channel asks both boards what the switch would download and shows you
that before it applies anything, and both boards are always written together so
they cannot end up on different channels.

Downloads also cope much better with a bad connection: a stalled transfer is
abandoned rather than left hanging, retries back off and survive a reboot, and a
download that fails its checksum is deleted so the retry actually re-fetches it.
An update interrupted partway through now picks up where it left off instead of
starting over.

There is a Clear Paired Phones entry now as well, and the companion app can drop
its own pairing. Forgetting a scooter used to clear only the phone's side of it,
which left bonds piling up on the scooter.

## The alarm notices more

A brake lever, the horn or the seatbox button now count as tampering while the
alarm is armed. This is on by default. The alarm also records which source set
it off and when, so a horn in the night can be traced rather than guessed at.

Handlebar triggers exist as well, watching the lock and position sensors, but
ship disabled pending more testing on real vehicles.

## Menus and the dashboard

Settings are grouped by topic now, with Info at the top level.

![The Settings menu grouped by topic](/images/news/settings-root.png)

The brake gestures are named along the bottom of the screen and behave the same
way everywhere. Tap the left brake to move down a list and the right to select.
A long press of the right brake runs a row's action without opening it, a long
press of the left goes back a level, and holding the left brake for three
seconds closes the menu from any depth.

New Info pages cover components, connectivity, batteries and maps, and the board
versions and serials no longer read blank on a scooter without a cloud client.
The dashboard is faster, too: the speedometer, the background blur and several
always-on animations were all reworked.

## Faults that were never reported

Before 1.3 the vehicle reported no faults at all. The fault screen existed and
was empty by construction. Failed power and brake commands, a motor controller
held unpowered by the brake interlock, and a state restore the vehicle refused
now all raise a code.

A few others in the same vein: a parked scooter could fail to suspend and drain
the AUX battery, the dashboard could stay lit for minutes after locking, and a
failed state restore could send the scooter's control software into a restart
loop. A scooter with plenty of charge could also go into hibernation anyway,
because the power guard was deciding on readings that had gone stale. All fixed.

`lsc` got the same treatment. Its datastore commands had been broken on every 1.2
scooter, and its fault and inhibitor listings always reported zero because they
read the wrong keys.

The [full release notes](https://github.com/librescoot/librescoot/releases/tag/v1.3.0)
have the complete list.

## Installing it

Scooters on the **stable** channel pick up 1.3.0 by themselves.

- [Downloads](https://downloads.librescoot.org/en/)
- [v1.3.0 on GitHub](https://github.com/librescoot/librescoot/releases/tag/v1.3.0)
- [Discord](https://discord.gg/BmY2P2T9j3)
