---
lang: en
title: "Librescoot 1.1: sleep states and power management"
date: 2026-07-04
permalink: /news/librescoot-1-1/
summary: "Power management is the whole story this time: suspend for up to ten days, hibernation on a timer or on a schedule, and a scooter that puts itself to sleep before its internal batteries go flat. Plus service mode, keycard unlock in Hop-On, and manual backlight."
icon: moon
---

Librescoot 1.1 is out, and power management is most of it.

A parked scooter is still awake. The electronics tick over doing nothing in
particular, and over a couple of weeks they drink the internal batteries dry.
Come back from a holiday and the vehicle needs reviving before it will go
anywhere.

## Sleep

Suspend: take the drive battery out and the scooter now drops into suspend by
itself, and it can hold that state for up to ten days.

Hibernation gets two new entry points. "Hibernate for" takes a duration: tell it
nine days and it wakes up in nine days. "Scheduled hibernate" takes a repeating
schedule instead, every night for instance, and brings the scooter back on its
own in the morning.

If the internal batteries get low anyway, the scooter now hibernates rather than
keep pulling on them. A battery that goes properly flat and stays flat often
does not come all the way back.

Alongside that: warnings when the internal batteries run low, and battery
temperatures on the debug screen.

## Also new

- Service mode, for everything that happens to a scooter standing still.
- Keycard unlock in Hop-On mode.
- Manual control of the display backlight.
- A setting that disables the horn button while the seatbox is open.
- Locking the scooter has its own menu entry now.
- An optional charge indicator for the internal batteries in the status bar.

## Fixed

The regen and power display was reworked and the main menu restructured.
Automatic backlight and the automatic light/dark switch both behave better, and
so do address entry, motion detection and handlebar lock detection. Online
updates verify what they downloaded. Cold start is shorter. The horn no longer
stays stuck on when the alarm is disarmed. Battery handling holds up on a worn
seatbox catch while riding. Beyond that: rendering fixes in the status bar and
in navigation, a cleaner dashboard shutdown, better ECU connectivity, less data
over the cloud connection, and work on Update Mode and the nRF firmware update
path.

## Installing it

Scooters on the **stable** channel pick it up on their own.

- [Downloads](https://downloads.librescoot.org/en/)
- [v1.1.0 on GitHub](https://github.com/librescoot/librescoot/releases/tag/v1.1.0)
