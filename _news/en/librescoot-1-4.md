---
lang: en
title: 'Librescoot 1.4.0 “Spätsommer”'
date: 2026-10-12
permalink: /news/librescoot-1-4/
published: false
summary: A web interface, multi-stop routes, regional offline maps and coordinated hibernation.
icon: map
---

Librescoot 1.4.0 “Spätsommer” brings scooter management to the browser and adds multi-stop navigation and regional offline maps. This post is a publication draft; no stable image has been published yet.

## Manage it in the browser

The [lsd web interface](/handbook/lsd.html) runs directly on the scooter. Over USB, manage settings, keycards, navigation destinations, files, updates and log bundles. Sunshine remains optional. To set it up, generate an installer credential in Sunshine Account settings and paste its token or online installer link into the Cloud page.

## Routes with several stops

Plan stops, change their order or skip one. The plan survives a restart. At an intermediate stop, a 30-second countdown runs only in drive mode. Brake gestures do not control this prompt; with the shortcut menu closed, pressing the seatbox switch pauses the plan. Leaving drive mode cancels the countdown. After a reached intermediate stop, entering drive mode again advances to the next stop.

USB Update Mode can install several named map and routing packs. With a recent GPS fix, the dashboard selects the matching region. Routes cannot cross region boundaries. Existing single-region installations remain supported; an existing regular routing archive needs an explicit migration before regional switching can work. See the [navigation handbook](/handbook/navigation.html).

## Everyday use

- **Trip counter and history:** The counter survives restarts. Choose whether it resets each ride, daily, on battery swap or only manually.
- **Keycards:** Enroll and remove cards on the dashboard. New unlock cards are saved only when you choose Done.
- **Sounds and notifications:** The dashboard plays cues for vehicle events, navigation and notifications when an amplifier is connected (disconnected on most scooters); messages with the same priority take turns.
- **Hibernation:** An explicit request from parked first coordinates vehicle shutdown. A relative duration needs no synchronized clock; a recurring schedule does.
- **Updates:** Preview the planned download size. A USB update with no applicable files finishes without rebooting.
- **Bluetooth:** nRF firmware 2.14.0-ls and file transfer for compatible apps. Download log bundles or upload files to an inbox; transfer neither installs firmware nor activates maps.

This description follows the [published source pins for 1.4](https://github.com/librescoot/librescoot/blob/2847f3606bdc6e7c67a1e44bd14619bef9f369ff/stable.env). Sunshine is deployed separately.
