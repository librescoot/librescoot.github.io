---
lang: en
title: "Librescoot 1.2.1: new system base, SMS and updates over Bluetooth"
date: 2026-08-03
permalink: /news/librescoot-1-2-1/
summary: "Everything below the Librescoot services now runs on a current LTS base with Linux 6.12. Plus SMS, support for mechanical hazard switches, and firmware updates over Bluetooth."
image: /images/screenshot-cluster-nav.png
image_alt: "The cluster with a navigation instruction"
---

Librescoot 1.2.1 is out. What has changed since 1.1:

The largest change is invisible from the saddle: everything below the Librescoot
services now runs on a current long-term-support base with Linux 6.12, replacing
the old 5.4 kernel.

The scooter can send and receive SMS, and retrofitted mechanical hazard
switches are supported. Thanks to Jonas.

Firmware updates can arrive over Bluetooth, alongside USB and cellular. From a
phone that works with "stasis for unu" on the Play Store; ask on Discord for the
TestFlight link on iOS.

Then the fixes. A stale GPS position no longer drags the system clock with it,
and the modem is no longer restarted just because some endpoint on the network
is briefly unreachable, which is where the GPS dropouts came from. The turn
signals now show on the "waiting for GPS" screen too. The update process, ECU
communication and detection of already-installed map data are all steadier.

A note on 1.2.0: it was withdrawn.

## Installing it

Scooters on the **stable** channel pick up 1.2.1 by themselves.

- [Downloads](https://downloads.librescoot.org/en/)
- [v1.2.1 on GitHub](https://github.com/librescoot/librescoot/releases/tag/v1.2.1)
