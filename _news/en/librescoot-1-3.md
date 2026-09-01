---
lang: en
title: "Librescoot 1.3: Better maps, a faster interface and improvements throughout"
date: 2026-09-01
permalink: /news/librescoot-1-3/
summary: "A much-improved dashboard with street names, a new 2D view, more routing choices and a refined interface, plus fixes and smaller improvements throughout the system."
image: /images/news/map-2d-heading.png
image_alt: "The 2D map view, heading-up, with an active route"
---

Librescoot 1.3 is here! Most of the attention went into the dashboard: alongside
the 3D map there is now a 2D view, maps are more detailed and include street
names, and routes can favour the fastest or shortest journey while avoiding
cobblestones. The interface is faster, the menus have grown and become more
polished, and plenty of work on reliability and stability happened in the
background.

## Dashboard, menus and controls

The dashboard starts faster and responds more smoothly. Settings are now grouped
by topic, while new Info pages show details about components, connectivity,
batteries and maps. Software versions and component serial numbers are available
there as well.

![The new Info menu with component, connectivity, battery and map details](/images/news/info-menu.png)

Menu controls have been standardised, and their labels now make the available
options clear at a glance. A short press of the left brake scrolls down, while a
long press goes back one level. The right brake selects menu entries and
confirms actions. Some entries also gained extra shortcuts, for example to start
navigation more quickly. Holding the left brake for three seconds closes the
menu directly.

![Settings grouped by topic](/images/news/settings-root.png)

The clock can optionally show the date, either alongside the time or alternating
with it. Automatic brightness responds faster while switching more calmly, and
the regenerative-power display now shows more precisely when regeneration is
active.

## Maps and navigation

A 2D map now sits alongside the existing 3D view, oriented either north-up or
heading-up. Map rendering is faster in both views.

![The new 2D map, heading-up, with an active route](/images/news/map-2d-heading.png)

The latest offline maps now display street names and more detail, including
green spaces, lakes and bridges. Routes can favour the fastest or shortest
journey, with four levels of cobblestone avoidance when compatible routing data
is installed: off, low, medium and high.

![Map view, route choice and map updates in Settings](/images/news/settings-map-navigation.png)

The map behaves better on the road too. The position marker now remains steady
while the scooter is stopped, rerouting starts from a better-chosen position,
and road names and speed limits are found and updated more quickly. Roundabout
guidance has also been rebuilt, with completely new, dynamically drawn icons for
the individual exits.

![The new dynamic rendering for roundabouts](/images/news/map-roundabout.png)

## Updates from the scooter

Software and map updates can now be configured directly on the scooter. Under
*Settings > System > Updates* you can set the check schedule, run a manual check,
choose the update type and switch release channel.

![The Updates menu on the scooter](/images/news/updates-menu.png)

Connected scooters can switch release channel directly, with a confirmation
showing the expected data volume. On an offline scooter, a release from another
channel can simply be installed through Update Mode.

Automatic updates for map and navigation data can be configured under *Map &
Navigation > Map Updates*. Librescoot can either show a notification when new
maps are available or immediately download and install them. Active map
downloads now appear in the status bar. Update Mode also supports compressed
routing data, making transfers considerably faster and using less data.

Downloads cope better with poor connections. Stalled downloads no longer block
indefinitely, retries are spaced further apart, and data already downloaded is
kept for the next attempt. One failed attempt also no longer blocks every later
update check.

## Bluetooth

Bluetooth responds faster, and pairing a phone is quicker and more reliable.
Duplicate pairing prompts and stale notifications have been fixed. The BLE
update path also recovers better from stalled or interrupted transfers, so a
new attempt can begin without rebooting the scooter.

All Bluetooth connections stored on the scooter can now be cleared from the
menu. This is especially useful for a second-hand scooter, but can also help
resolve some connection problems.

## Alarm system

While the alarm is armed, either brake lever, the horn button or the seatbox
button now counts as tampering. The source and time of an alarm are kept for
later diagnosis. The handlebar lock and handlebar position can also be
configured as triggers. All of these options can be adjusted individually.

## Stability improvements and bug fixes

More failures are now detected and logged precisely. These include problems
switching on the motor, dashboard and regenerative braking, failed or
interrupted vehicle-state restores, and faults during Bluetooth initialisation
and updates. These problems now also appear in the fault log.

Finally, many smaller faults have been fixed and stability improved throughout
the system. Services are more robust, and communication between components is
more reliable. The speed display appears more consistently, E20 occurs less
often and only for genuine problems, and the odometer is stored and restored
across deep sleep.

The [full release notes](https://github.com/librescoot/librescoot/releases/tag/v1.3.0)
have the complete list of changes.

Scooters on the **stable** channel receive Librescoot 1.3 automatically.

- [Downloads](https://downloads.librescoot.org/en/)
- [v1.3.0 on GitHub](https://github.com/librescoot/librescoot/releases/tag/v1.3.0)
- [Discord](https://discord.gg/BmY2P2T9j3)
