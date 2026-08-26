---
lang: en
title: "Librescoot 1.0: the first stable release"
date: 2026-05-01
permalink: /news/librescoot-1-0/
summary: "Offline navigation, an automatic steering lock, a motion alarm, and over-the-air updates. Free and open-source firmware for the unu Scooter Pro, with an installer for Linux, macOS and Windows."
image: /images/screenshot-cluster.png
image_alt: "The cluster while riding, 46 km/h on Gitschiner Strasse"
---

Librescoot 1.0 is here. This is the first stable release: free and open-source
firmware for the unu Scooter Pro, an installer that runs on Linux, macOS and
Windows, and a handbook to go with it.

## What it does

Offline navigation, with maps and turn-by-turn on the handlebar display. The
map tiles live on the scooter, so there is no phone in a handlebar mount and no
data connection involved.

![Turn-by-turn on the scooter display](/images/screenshot-nav-day.png)

The steering lock is automatic. Turn the bars while the scooter is unlocked and
it releases on its own; switch off and walk away and it locks again a moment
later. A motion alarm runs alongside it.

None of this needs a SIM. Maps, navigation, the alarm and updates over USB all
work without a data connection. A SIM adds remote access and updates over the
network, and nothing about riding depends on it.

The dashboard comes in light and dark and is configurable. If you have wired up
the rear battery slot, both packs appear in the status bar. Updates arrive over
the air as deltas, on three channels: stable, testing, nightly. There is
keycard management, a WireGuard VPN, and the `lsc` command line for everything
else.

## Installing it

Download the installer, plug a USB cable into the scooter, follow the wizard.
It fetches the firmware and map tiles for the channel you pick, shows you the
hardware it found so you can confirm it is the right scooter, writes the MDB,
and then flashes the dashboard from the scooter itself. Afterwards it sets up
offline maps, Bluetooth and the keycard.

![The one cable the install needs, plugged into the MDB](/images/install/lsi-mdb_usb_connected.jpg)

You need a USB cable, a screwdriver for the footwell, and about twenty minutes.

Builds go out for all three platforms together. Linux is the best travelled of
the three; macOS and Windows work but have seen far fewer scooters. The README
still says *beta software* at the top, and means it. If an install breaks,
please tell us.

## The handbook

Eleven pages covering what happens after the installer finishes: quick start
and first steps, the display with every indicator and the brake lever gestures,
riding, states and the battery, navigation, updates, troubleshooting, and what
changed coming from scooterOS. Screenshots throughout, so you can match what
you are reading against what is on the screen. Read it in the
[handbook](/handbook/).

- [Downloads](https://downloads.librescoot.org/en/)
- [v1.0.0 on GitHub](https://github.com/librescoot/librescoot/releases/tag/v1.0.0)
- [Discord](https://discord.gg/BmY2P2T9j3)
