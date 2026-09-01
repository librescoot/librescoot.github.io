---
lang: en
title: "Installer 2.0: The scooter finishes the installation itself"
date: 2026-09-01
permalink: /news/installer-2-0/
summary: "The new installer prepares firmware, maps and both boards up front. The scooter then finishes without the laptop – faster, more robust and with much less manual work."
image: /images/install/lsi-mdb_usb_connected.jpg
image_alt: "The MDB in the scooter footwell, connected over USB"
---

**Installer 2.0 is here!** The new stable release does the preparation up front:
it checks the MDB and DBC, downloads firmware and map data, and transfers
everything the scooter needs for the remaining steps. Once the USB cable is back
on the dashboard, the installation continues without the laptop. The scooter
installs the dashboard, maps and routing data, restarts its components, and
unlocks itself when finished.

The whole process is faster, more robust and easier to follow. Installer 2.0 is
available for Linux, macOS and Windows.

## Prepare first, then finish unattended

The old installer required the USB cable to be moved several times during an
installation. Installer 2.0 groups the work involving the laptop at the start.
Firmware, maps and routing data are downloaded, checked and transferred before
the scooter takes over.

The dashboard and turn signals show progress from there. The laptop is no
longer needed for this part and does not have to be reconnected later. Power and
the scooter's cables remain connected until the dashboard reports that the
installation is complete.

## A faster process

Downloads and transfers run in parallel where possible. Files already present
are reused rather than downloaded or transferred again. Compressed routing data
makes a particularly large difference to download and transfer times for bigger
map regions.

The flashing tools and USB-device handling have also been updated across Linux,
macOS and Windows. The installer handles the required permissions, network
configuration and, on Windows, the USB driver itself.

## More robust after interruptions

Installation state is recorded on the scooter. After an interruption, the
installer recognises which steps have already finished and explains how to
continue. Files already transferred do not have to be sent to the scooter again.

Longer steps now show their current phase, usual duration and elapsed time.
Transfers running in the background remain visible too. If something fails, the
error and installation log can be copied directly.

## Upgrade without reinstalling

Installer 2.0 can upgrade an existing Librescoot system. Settings, paired
keycards and offline maps are kept. MDB and DBC can each be updated, freshly
installed or left unchanged. The installer warns before a downgrade to an older
release.

A full installation remains available for a stock scooter or when recovering a
system.

## Download and installation

You need a USB cable, a screwdriver and about twenty minutes. Flashing normally
completes without trouble on a scooter that has been running reliably. Still,
do not start in a hurry: leave enough time to follow the steps carefully and to
ask for help or recover the scooter if needed.

- [Download the installer](https://downloads.librescoot.org/en/)
- [Installation guide](https://librescoot.org/en/docs/install.html)
- [Installer 2.0 release notes](https://github.com/librescoot/installer/releases/tag/v2.0.0)
- [Discord](https://discord.gg/BmY2P2T9j3) for questions and feedback
