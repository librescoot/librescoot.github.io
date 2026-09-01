---
lang: en
title: "Librescoot 1.1: Better power management and new sleep options"
date: 2026-07-04
permalink: /news/librescoot-1-1/
summary: "Suspend for up to ten days, Hibernation for a chosen duration or on a schedule, and automatic protection for the internal batteries. Plus Service mode, keycard unlock in Hop-On and manual backlight control."
icon: moon
---

Librescoot 1.1 is here! This release focuses on power management, with new ways
to keep a parked scooter ready without unnecessarily draining its internal
batteries.

## Suspend and Hibernation

When the drive battery is removed, the scooter can now enter Suspend
automatically and remain there for up to ten days.

Hibernation has two new options. **Hibernate for** switches the scooter off for
a chosen length of time, while **Scheduled hibernate** follows a recurring
schedule, such as switching off overnight and waking again in the morning.

If the internal batteries run low, the scooter now enters Hibernation rather
than continuing to discharge them. The dashboard also warns when these
batteries are getting low, and the debug screen can show their temperatures.

## More new features

- Service mode for maintenance and other work on a stationary scooter
- Keycard unlocking in Hop-On
- Manual control of the display backlight
- An option to disable the horn button while the seatbox is open
- A dedicated menu entry for locking the scooter
- An optional internal-battery indicator in the status bar

## Improvements and fixes

The power and regenerative-braking display has been revised, and the main menu
has been reorganised. Automatic brightness and the light/dark switch respond
more reliably, as do address entry, motion detection and steering-lock
detection. Cold starts are faster, and online updates now verify downloaded
data before installation.

Several faults have also been fixed. The horn no longer remains active when the
alarm is disarmed, and battery handling remains reliable with a worn seatbox
catch while riding. This release also improves dashboard shutdown, ECU
communication, navigation and status-bar rendering, Update Mode and firmware
updates for the Bluetooth controller, while reducing data use over the cloud
connection.

Thank you to everyone who tested these changes and reported problems.

## Installing the update

Scooters on the **stable** channel receive Librescoot 1.1 automatically.

- [Downloads](https://downloads.librescoot.org/en/)
- [Librescoot v1.1.0 on GitHub](https://github.com/librescoot/librescoot/releases/tag/v1.1.0)
