---
lang: en
title: "Librescoot 1.3.1 “Guten Morgen”: Reliable wake-up and a faster dashboard"
date: 2026-09-07
permalink: /news/librescoot-1-3-1/
summary: "Timed wake-up from Hibernation works reliably again. The dashboard starts faster and no longer flashes white, with more useful battery details, new display options and more robust updates."
image: /images/news/librescoot-1-3-1.png
image_alt: "Librescoot wordmark, v1.3.1 and the codename Guten Morgen above an alarm clock"
---

**Librescoot 1.3.1 “Guten Morgen” is here!** This maintenance release fixes a
fault affecting timed wake-up from Hibernation and brings a faster dashboard,
more display options and more robust updates and connections.

The [Librescoot 1.3 announcement](/en/news/librescoot-1-3/) describes the
changes introduced in version 1.3.0.

## Reliable wake-up from Hibernation

Timed wake-up from Hibernation works reliably again. A fault in 1.3.0 could
prevent the scooter from waking on its own after a chosen duration or at the
scheduled time. This has been corrected in 1.3.1.

If a transition into Suspend is cancelled, the modem is now switched back on as
well, so the scooter does not remain offline afterwards.

## A faster and more useful dashboard

The dashboard starts faster and shows vehicle data sooner. The display also
turns on and off without the brief white flash seen in 1.3.0. House-number
searches are considerably faster, and navigation instructions use more of the
available screen width.

The battery Info pages now show the main battery's capacity and indicate a low
charge. The current road can be shown at all times, only in the map view, only
while navigating or not at all. The speed-limit sign has the same choices and
can also be used purely as a warning that appears when the scooter exceeds the
displayed limit. The speedometer scale and its warning thresholds can be
changed through `settings.toml` or `lsc`.

## More robust updates and USB maintenance

An attempt to install the same version through an online or Bluetooth update
is now rejected at the start, rather than after the entire transfer and
installation run. The alarm remains off while the scooter is available as USB
storage in Update Mode. Update Mode can now repair recoverable filesystem
errors itself. USB Ethernet also returns correctly after leaving Update Mode.

## Connectivity and diagnostics

GPS startup, SIM-card changes and SMS handling now cope better with errors and
state changes. WireGuard retries its connection if activation fails during
startup, and communication between the scooter's main computer and dashboard
is more stable under heavy load.

For command-line users, `lsc` now also reports the main battery's capacity,
fault code and low-charge state.

Online scooters on the **stable** channel receive Librescoot 1.3.1
automatically.

- [Downloads](https://downloads.librescoot.org/en/)
- [Full Librescoot v1.3.1 release notes](https://github.com/librescoot/librescoot/releases/tag/v1.3.1)
- [Discord](https://discord.gg/BmY2P2T9j3)
