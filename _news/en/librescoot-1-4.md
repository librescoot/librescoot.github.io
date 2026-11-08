---
lang: en
title: 'Librescoot 1.4 "Spätsommer"'
permalink: /news/librescoot-1-4/
date: 2026-11-01
published: true
summary: "Multi-stop routes with an overview and the option to resume after a break, a clock that keeps running through Hibernation, and a more versatile dashboard. Android phone keys with Librescoot Mobile and a trip log add to the everyday improvements."
icon: map
image: /images/news/librescoot-1-4.png
image_in_post: false
image_alt: "Librescoot wordmark, v1.4.0 and the codename Spätsommer beside a sun"
---

Librescoot 1.4.0 "Spätsommer" expands navigation with multi-stop routes, an overview of the whole tour and the option to resume after a break. The clock keeps running through Hibernation, the shortcut menu gains more options, and the dashboard gets unified notifications, customizable colors and smooth transitions. With the Librescoot Mobile app, an Android phone can also serve as a key, while a trip log records your rides.

## Routes for the whole tour

{% include news-screenshot.html src="/images/news/librescoot-1-4-route-en.png" align="right" alt="Navigation map with three stops in central Berlin" caption='Route overview with three stops and example data. Map data © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>.' %}

A route can include several stops. Add destinations along the way, change their order or skip individual stops. The route overview shows the remaining route and upcoming destinations. After standby or a restart, the tour can be resumed without entering everything again.

Resuming navigation is more robust too. If GPS or routing is not ready at startup, route calculation is retried once they are available. When the position is not yet accurate enough, a message explains the wait and a usable map stays visible.

Frequent destinations such as home or work, the route overview and the option to skip a stop can all be added to the shortcut menu, keeping the main navigation actions within easy reach.

Several offline map regions can be stored on the scooter at once. After a one-time setup, the dashboard selects the appropriate region for the current position. Installation and updates use USB; routes cannot cross between separate regions. Map information labels are translated into German and English, and long values wrap.

## The clock keeps running

After waking from Hibernation, the clock shows the correct time without waiting for GPS. It keeps running while the scooter sleeps. After a complete loss of power, including the internal batteries, it needs to synchronize again, for example through GPS or the internet.

Hibernation can be started directly from parked. Hibernate for also works without a set clock; scheduled hibernation requires a valid time. A scooter woken by an alarm can go back to sleep afterwards.

## A more versatile dashboard

{% include news-screenshot.html src="/images/news/librescoot-1-4-quick-en.png" align="right" alt="Dashboard shortcut menu with map view selected" caption="The shortcut menu can be configured with frequently used actions." %}

Choose the shortcut menu's actions and their order. Alongside navigation controls, it can hold the other actions you use most often. Speedometer, power and recuperation colors, as well as map styles, are customizable too.

The startup animation fades into the dashboard, and the startup logo and animation are selectable. Automatic light or dark theme selection takes ambient light into account during startup. Automatic brightness uses a wider adjustment range, and the fixed brightness presets have also been revised.

Warnings, navigation instructions and other notifications now share a common presentation. Multiple messages take turns, and long text scrolls. Important notices remain visible during connection problems and updates. Low main-battery charge and internal-battery charging warnings complement the charging information in the Info menu.

Scooters with a connected amplifier also get new sounds for blinkers, navigation, notifications and vehicle actions. The amplifier is disconnected on most scooters, so these sounds will not be audible there.

## Use an Android phone as a key

The Librescoot Mobile app can set up a compatible Android phone as an NFC key and enroll it on the scooter. The unlocked phone then works at the reader like a keycard for locking and unlocking.

This works only with the Librescoot Mobile app, where the phone key must be explicitly enabled. Without it, the scooter does not recognize the phone as a phone key and treats it like an ordinary card. Android phones then often present a different, random ID on every tap, so they are not recognized later and do not unlock the scooter.

Cards and phone keys can be added and removed directly on the dashboard. Names assigned in the app appear there too, along with a mark identifying the last-used card. Removing the last way to unlock the scooter requires confirmation.

An optional setting can open the seatbox automatically when the scooter is unlocked, including with a keycard. It is off by default. The alarm briefly delays its initial warning to give a keycard or phone tap time to finish.

## Trip log and energy overview

<div class="news-screenshot-grid">
{% include news-screenshot.html src="/images/news/librescoot-1-4-trip-en.png" alt="Trip details with example data and a recorded route" caption='Trip details with example data. Start and end markers are available from dashboard 1.24.1. Map data © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>.' %}
{% include news-screenshot.html src="/images/news/librescoot-1-4-energy-en.png" alt="Dashboard consumption overview with example values for riding, parked and standby" caption="Estimated consumption by operating state, shown with example values." %}
</div>

The trip log saves distance, duration and GPS tracks on the scooter. Under Trip history, you can view completed rides with distance, riding time and average speed directly on the dashboard. Recorded GPS tracks can be shown on the map. Retention can be limited by age, number of trips or storage size, or automatic deletion can be turned off. Short distances below 100 metres on the odometer are not saved as completed trips.

The trip counter also keeps its distance when the scooter is switched off and counts independently of trip history. Choose whether it resets after each ride, daily, on a battery swap or only manually.

The new dashboard consumption page estimates net energy drawn from the traction batteries from changes in their remaining capacity. Values are grouped by ready-to-drive, parked and standby, making energy use outside a ride visible too. This is an estimate by operating phase, not an exact breakdown by electrical load; the recording start and gaps remain visible.

Separately, the dashboard and web interface show energy consumed and recovered through regenerative braking in kWh, estimated from motor-controller data.

## Messages and more options for apps

{% include news-screenshot.html src="/images/news/librescoot-1-4-sms-en.png" align="right" alt="SMS message with an example mobile plan notice" caption="Read SMS directly on the dashboard. Sender and message are examples." %}

Mobile carriers often send plan notices and data allowance warnings by SMS to the scooter's SIM card. These messages can now be read and deleted on the dashboard while parked or through compatible apps. Under Info > SMS, the list shows the sender and a message preview; messages open directly as plain text. Cancel is selected first when deleting. The inbox survives restarts. New messages can optionally be forwarded on the home network; set the number in the web interface's advanced settings. The dashboard shows the destination and can turn forwarding off. Forwarding is off by default and carrier charges may apply. With multi-SIM, the mobile plan determines whether SMS reach the scooter or another device.

Compatible apps can also transfer files over Bluetooth, download diagnostic logs and resume interrupted transfers. They can control dashboard power and Service Mode, reset the trip counter and edit multi-stop routes. The Bluetooth interface also supports starting, checking and stopping Connect account pairing. Apps can also retrieve completed trips with details and recorded GPS points. Each app needs to support these functions.

## A web interface for setup and maintenance

The new web interface provides access to settings, keycards, navigation, vehicle and battery status, and updates when working on the scooter. It also supports file transfers and diagnostic log downloads.

One way to connect is through the USB port in the footwell. This requires unscrewing the footwell cover and connecting a computer. With the scooter switched on (unlocked), open the [web interface](http://192.168.7.1:8090).

{% include news-screenshot.html src="/images/news/librescoot-1-4-connect-en.png" align="right" alt="Connect pairing with a QR code and browser approval" caption="Connect pairing on the dashboard. The code shown is an invalid example." %}

A cloud account, such as Sunshine, can also be connected directly on the dashboard with Connect. Settings > Cloud appears when internet and main-controller connections are available. Under Connect account, briefly press the right brake to start pairing. While a valid short code is available, the dashboard displays a QR code containing it. After scanning, the [Connect portal](https://connect.librescoot.org/pair) fills in the code and removes it from the browser address. The short code can also be entered manually. The dashboard shows how long the code remains valid. The scooter must be online; starting is allowed in parked or standby. Account approval still requires explicit confirmation in the browser. The dashboard shows the code, confirmation and completion steps, explains longer waits and reports a lost connection.

The web interface's Cloud page can also start pairing, show the code, expiry and status, and stop waiting. A configuration transaction already in progress finishes before stopping. Alternatively, the Sunshine connection can still be configured using a setup token or online installer link from your [Sunshine account settings](https://sunshine.rescoot.org/account/security#bootstrap-tokens).

## Everyday improvements

The dashboard indicates when battery activation is still in progress before riding starts. Regenerative braking is activated correctly even when riding off immediately after switching on. Parked-only screens close when riding starts, and using the menu no longer leaves the brake light stuck on. Indicator control processes switch and software requests one at a time; clock corrections no longer affect the blink cadence.

A replacement battery is checked before activation. A single battery can be activated in ready-to-drive, but a second battery cannot be added there, even while stationary. Already-active batteries remain active when entering ready-to-drive.

For the alarm, Stop ends a sounding alarm, which re-arms after five minutes. Disarm keeps it off until the scooter is used and locked again, Hibernation begins or eight hours have passed. It then re-arms automatically.

Before an update, the web interface shows the required download size, while the dashboard reports progress and errors. After installation, the dashboard's automatic restart waits until the scooter is locked in standby. This prevents an unexpected dashboard restart while the scooter is in use. Recovery handles system and boot updates separately and keeps the dashboard active until the required boot-update restart. Restarting the update service alone does not count as a dashboard reboot. USB Update Mode also handles interruptions more reliably; if there is nothing to install, no restart is needed.

## For developers and enthusiasts

Custom scripts can react to vehicle states, button presses, battery changes or alarms. Rules are configured through [`lsc ext`](https://librescoot.org/en/docs/dev/lsc.html#event-service-rules); none are active by default.

The kernel also includes the [networking support needed by Tailscale](https://librescoot.org/en/docs/dev/hardware.html#network-topology). The Tailscale client is not preinstalled. For troubleshooting, `lsc doctor` brings common problems together in one report; the full release notes cover further diagnostic and connectivity improvements.

This release is dedicated to [Patrick Stewart](https://en.wikipedia.org/wiki/Patrick_Stewart).

<hr>

[Librescoot 1.4.1](https://github.com/librescoot/librescoot/releases/tag/v1.4.1) adds start and end markers to the trip log.

[Librescoot 1.4.2](https://github.com/librescoot/librescoot/releases/tag/v1.4.2) changes the alarm defaults: the horn is enabled by default, and after an initial motion or button press, a further trigger can start the full alarm sooner. Saved alarm settings are preserved. An optional blinking red LED indicates that the alarm is armed. A new diagnostic tool under Info > Doctor helps with troubleshooting. The update also improves battery detection, trip maps and scheduled hibernation.
