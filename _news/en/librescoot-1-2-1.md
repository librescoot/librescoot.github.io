---
lang: en
title: "Librescoot 1.2.1: A new system base, SMS and Bluetooth updates"
date: 2026-08-03
permalink: /news/librescoot-1-2-1/
summary: "A current long-term-support system base with Linux 6.12, plus SMS, support for mechanical hazard switches, firmware updates over Bluetooth and reliability improvements throughout."
image: /images/screenshot-cluster-nav.png
image_alt: "The cluster with a navigation instruction"
---

Librescoot 1.2.1 is here! This release moves the system to a current
long-term-support base with Linux 6.12. It also brings SMS support, mechanical
hazard switches, firmware updates over Bluetooth and a range of reliability
improvements.

## A newer foundation

The system underneath the Librescoot services now uses Linux 6.12, replacing
the previous 5.4 kernel. The change is mostly behind the scenes, but gives the
project a current, maintained foundation for future development.

The scooter can now send and receive SMS messages. Retrofitted mechanical
hazard switches are supported as well. Thank you to Jonas for contributing to
this work.

## Updates over Bluetooth

Firmware updates can now be transferred over Bluetooth, alongside the existing
USB and mobile-network options. On Android this works with **stasis for unu**
from the Play Store. iOS users can ask for the TestFlight link on Discord.

## Improvements and fixes

GPS and mobile connectivity are more reliable. A temporary problem reaching a
network service no longer causes an unnecessary modem restart, and an outdated
GPS position can no longer change the system clock.

The turn signals now remain visible while the dashboard is waiting for a GPS
position. We have also improved the update process, communication with the
scooter's controllers and detection of map data that is already installed.

Librescoot 1.2.0 was withdrawn and replaced by this release.

Thank you to everyone who tested the release and helped track down these issues.

## Installing the update

Scooters on the **stable** channel receive Librescoot 1.2.1 automatically.

- [Downloads](https://downloads.librescoot.org/en/)
- [Librescoot v1.2.1 on GitHub](https://github.com/librescoot/librescoot/releases/tag/v1.2.1)
- [Discord](https://discord.gg/BmY2P2T9j3)
