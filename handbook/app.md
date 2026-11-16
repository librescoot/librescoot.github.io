---
layout: docs
lang: en
permalink: /handbook/app.html
title: Librescoot App for unu
description: "Guide to the Librescoot app: setup, controls, navigation, keycards, settings and help."
---
<div class="app-guide" markdown="1">
# Librescoot App for unu: User Guide

This guide covers the Librescoot App for unu for the unu Scooter Pro. The app connects to your scooter over Bluetooth, shows its status and lets you control it. Many features require Librescoot on the scooter. The settings available also depend on your scooter's software and your phone.

The illustrations show a development version of the app in a Flutter test with demo data and no system status bar. They do not show a real scooter. The appearance and available features may differ on your device.

Markers such as <span class="release-pill" title="Available since Librescoot 1.4">1.4+</span> refer to the Librescoot version **on the scooter**, not the app version. The installed app must also support the feature.

## Contents

1. [Preparation and first connection](#preparation-and-first-connection)
2. [Home screen and scooter controls](#home-screen-and-scooter-controls)
3. [Managing scooters](#managing-scooters)
4. [Batteries, range and trips](#batteries-range-and-trips)
5. [Navigation](#navigation)
6. [Keycards and Android phone keys](#keycards-and-android-phone-keys)
7. [Scooter settings](#scooter-settings)
8. [Firmware and system information](#firmware-and-system-information)
9. [App settings and privacy](#app-settings-and-privacy)
10. [Widgets and Tasker](#widgets-and-tasker)
11. [Troubleshooting](#troubleshooting)

## Preparation and first connection

### What you need

- An unu Scooter Pro that is switched on and within Bluetooth range.
- An Android phone or iPhone with the Librescoot App for unu installed and Bluetooth enabled. The Android app is available on [Google Play](https://play.google.com/store/apps/details?id=org.librescoot.mobile.unu); iOS test versions are distributed through TestFlight.
- Access to the scooter display for the initial pairing code.
- Up-to-date, supported Librescoot firmware on the scooter for some features.

Basic Bluetooth control does not need a cloud account. Downloads, online place search and external help pages require an internet connection on your phone.

### Permissions

The app guides you through permissions on first launch. Allow Bluetooth or the "Nearby devices" permission so the app can find and connect to your scooter. On older Android versions, Bluetooth scanning may also require location permission.

On current devices, location and notifications are generally optional. Location is used, for example, for the last known connection location and distances to workshops. Notifications are especially useful for Android background connections. You can change permissions later in your phone's system settings.

The app also asks about **Online Location Services**. When enabled, place search uses external services. You can change your choice later under **Settings > App > Online Location Services**.

### Pair the scooter

1. Open the app, choose **Begin setup** and follow the steps for permissions and Online Location Services.
2. Stand next to the switched-on scooter with your phone and start the scan.
3. Select your scooter from the list, which shows information including signal strength and pairing status.
4. Confirm the phone's pairing request. The code appears on the scooter display. If several requests appear, confirm the ones for your scooter.
5. Give the scooter a name and choose a colour. It then appears on the home screen.

If the app cannot find the scooter, check Bluetooth, permissions, power and distance. Other apps connecting to the same scooter in the background can interfere.

## Home screen and scooter controls

{% include news-screenshot.html src="/images/app-guide/en/start.png" alt="App home screen with a demo scooter, status, battery levels and controls" caption="App home screen with a demo scooter, status, battery levels and controls" %}

The home screen shows the scooter's name and reported state. Depending on the scooter and firmware, it may also show the trip counter, odometer, battery levels and estimated range. Tap an indicator for more information. The arrow next to the scooter name opens the scooter list.

The main actions are at the bottom:

- Unlock or lock: press and hold the centre button. The scooter state changes after a successful request. Unlocking also releases the handlebar lock and enables riding.
- Open seat: press and hold the button to open the seatbox.
- Controls: open additional actions such as wake, hibernate, restart and indicators.
- Navigation: swipe up from the bottom of the screen.

Check the displayed scooter state after an action. If the seatbox is open, the app may offer an additional confirmation when locking; the scooter may still wait for the seatbox to close. The handlebar lock is a separate mechanism and its status is displayed separately. If it does not engage or release as expected, follow the app's instructions and move the handlebars as directed.

### More controls

{% include news-screenshot.html src="/images/app-guide/en/steuerung.png" alt="Controls menu with indicators, scooter state and ride statistics" caption="Controls menu with indicators, scooter state and ride statistics" %}

Under **Controls**, depending on the scooter state and firmware, you can wake the scooter, put it into hibernation, restart it and operate the indicators or hazard lights. A hard restart interrupts power to the affected systems. Use it only when the scooter is safely parked and ready. <span class="release-pill" title="Available since Librescoot 1.1">1.1+</span> A wake-up timer for hibernation is available from Librescoot 1.1.

## Managing scooters

Tap the scooter name on the home screen. In the list, you can select and manage saved scooters using their action menus:

- Connect or disconnect.
- Rename a scooter and change its appearance or colour.
- Turn auto-connect on or off for an individual scooter.
- Remove a scooter from the app or add another one.

The scooter name and appearance are app settings. A saved scooter can be selected and renamed without an active connection. Scooter commands and settings require a connection. If you remove a scooter, you must set it up again to use it later; on supported Librescoot firmware the phone pairing is also removed from the scooter.

## Batteries, range and trips

### Batteries and range

{% include news-screenshot.html src="/images/app-guide/en/akkus.png" alt="Battery screen with example charge levels and estimated range" caption="Battery screen with example charge levels and estimated range" %}

Tap the battery or range indicator on the home screen. The app shows available information about the main and internal batteries. The scooter's equipment and reported values determine what appears. Range is an estimate, not a promise of how far you can travel.

Depending on your phone, you can also read a battery over NFC: choose the corresponding action on the battery screen and hold the phone against the label on the bottom of the battery. NFC antenna positions vary between phones; move the phone slowly over the label if needed.

### Trip counter and trip history

<span class="release-pill" title="Available since Librescoot 1.4">1.4+</span> On compatible Librescoot firmware, tapping the trip indicator opens **Ride stats**. It shows the distance, riding time and average speed for the current counter. You can reset the counter manually or, if supported, choose a reset policy. Resetting the counter does not delete trip history.

<span class="release-pill" title="Available since Librescoot 1.4">1.4+</span> **Trip history** is available from Ride stats and shows supported recorded trips. Under **Settings > Ride stats**, you can change the history retention policy if the scooter supports it. Check deletion and retention options carefully before confirming.

### Battery registration

The app can offer guidance on identifying a battery. Shared registration and email confirmation are available once the associated service is enabled. Reading a serial number alone does not mean a battery has been registered.

## Navigation

Swipe up on the home screen to open **Navigation**. <span class="release-pill" title="Available since Librescoot 1.0">1.0+</span> With Librescoot on the scooter, you can choose destinations and send them to the scooter.

{% include news-screenshot.html src="/images/app-guide/en/navigation.png" alt="Navigation with a search field and saved example destinations" caption="Navigation with a search field and saved example destinations" %}

### Search for a destination and start

1. If necessary, enable online search under **Settings > App > Online Location Services**.
2. Open **Navigation** and enter an address or place in the search field.
3. Select a result. You can save it or choose **Navigate**.
4. Follow the navigation instructions on the scooter display. Use **Stop** to end active navigation.

If you are not connected, the app can queue a destination for later navigation. The app shows that navigation is pending and sends the destination when it connects. Saved destinations may also be marked **Offline**. When Online Location Services are enabled, place names and search queries are sent to the named providers.

### Saved destinations and routes

You can rename or delete saved destinations using their menus. <span class="release-pill" title="Available since Librescoot 1.4">1.4+</span> If your scooter supports route plans, the route icon opens the **Route plan**. There you can add, reorder, skip or remove stops and clear the route. The app warns you when reordering will restart the route from the first stop.

You can also share a place from another app. Choose the Librescoot app in the share menu and check the detected destination before navigating.

### Last location

The location screen shows the last place where the app was connected to the scooter. It is not live tracking or theft protection. The app needs the phone's location permission to record a location.

## Keycards and Android phone keys

{% include news-screenshot.html src="/images/app-guide/en/keycards.png" alt="Keycard management with example cards in demo mode" caption="Keycard management with example cards in demo mode" %}

<span class="release-pill" title="Available since Librescoot 1.0">1.0+</span> With a Librescoot scooter connected, open **Settings > Access & parking > Keycards**. The app reads the list from the scooter. Use a card's menu to rename it, change its appearance or remove it.

### Add a keycard

1. Enable NFC on your phone and open **Keycards**.
2. Tap **+** and hold the compatible card against your phone's NFC antenna.
3. Hold the same card against the phone again to confirm.
4. Wait for confirmation that the card has been added to the scooter.

The app needs a scooter connection to add a card. If the phone cannot detect it, check NFC and move the card slowly over the back of the phone. Keep a working card as a spare before removing keys.

### Android phone as an NFC key

<span class="release-pill" title="Available since Librescoot 1.4">1.4+</span> A compatible Android phone with NFC card emulation enabled and a scooter with the corresponding Librescoot support can use a phone key. Set it up under **Keycards**:

1. Choose **Set up or show phone key** and enable the NFC phone key in the app.
2. Hold the master card against the scooter reader to start learning mode.
3. Hold the unlocked phone against the reader, then hold the master card against it again to save the key.
4. For later use, NFC must be enabled and the phone unlocked.

On supported firmware, the app shows registered phones and can remove them. Do not remove the last working key without another way to access the scooter.

## Scooter settings

{% include news-screenshot.html src="/images/app-guide/en/einstellungen.png" alt="Beginning of Settings with access, keycards and power options in demo mode" caption="Beginning of Settings with access, keycards and power options in demo mode" %}

Open the gear icon on the home screen. Scooter functions shown in grey cannot be used without a connection or firmware support.

### Access and parking

- Auto-unlock unlocks the scooter as the phone approaches when the app's conditions are met. Distance is estimated from Bluetooth signal strength and is not exact. Test it first in a safe place.
- Opening the seatbox on unlock and flashing lights when locking or unlocking are additional options for the selected scooter.
- Under **Keycards**, manage supported cards and phone keys.

When parking, check that the scooter is actually locked. Auto-unlock and an active background connection can cause the scooter to unlock again when you walk past.

### Power and alarm

Under **Power**, depending on firmware, you can set the times for **Auto-standby** and **Auto-hibernation**. Auto-standby applies to inactivity while parked; auto-hibernation applies to inactivity in standby. <span class="release-pill" title="Available since Librescoot 1.1">1.1+</span> Supported **Scheduled hibernation** uses the scooter's clock and runs only when the displayed conditions are met. The scooter clock must be synchronised.

**Keep main battery awake** keeps the main battery active while the seatbox is open. Under **Alarm**, you can adjust supported alarm and horn options. <span class="release-pill" title="Available since Librescoot 1.4">1.4+</span> On supported firmware, the alarm can be temporarily disarmed without permanently changing **Enable on lock**.

### Cellular APN

<span class="release-pill" title="Available since Librescoot 1.0">1.0+</span> With Librescoot on the scooter, you can set the APN through the app.

{% include news-screenshot.html src="/images/app-guide/en/mobilfunk-apn.png" alt="Connectivity settings with Cellular APN in demo mode" caption="Connectivity settings with Cellular APN in demo mode" %}

1. Connect to the Librescoot scooter.
2. Open **Settings > Connectivity > Cellular APN**.
3. Enter the APN provided by the scooter SIM's mobile operator and tap **Save**.
4. If a custom APN is set, use **Clear** to remove it. The scooter then uses the SIM operator's default again.

The APN controls the scooter's mobile connection, not the phone's. It is available only on supported firmware. If unsure, ask the SIM provider for the correct value.

### Messages and service mode

<span class="release-pill" title="Available since Librescoot 1.4">1.4+</span> On supported scooters, **Connectivity > Messages** opens the SMS inbox and an option to forward new messages. Forwarding may incur mobile charges; the app describes the applicable limits on that screen.

<span class="release-pill" title="Available since Librescoot 1.4">1.4+</span> **Service mode** keeps the scooter awake and USB active. The alarm and automatic locking are disabled while it is active. Turn it off after maintenance.

<span class="release-pill" title="Available since Librescoot 1.0">1.0+</span> Use **Update mode** only for its intended USB file transfers and safely eject the USB drive from the computer before leaving the mode.

## Firmware and system information

Under **Settings > System information**, the app shows available main board, dashboard and Bluetooth system versions. Use **Reload version info** to read them again. Information displayed offline may be cached.

### Update firmware over Bluetooth

<span class="release-pill" title="Available since Librescoot 1.2">1.2+</span> Bluetooth firmware updates require Librescoot 1.2 or newer on the scooter.

1. Park the scooter safely and connect the phone over Bluetooth. Keep the phone nearby and the app open during the transfer.
2. Open **System information > Bluetooth firmware updates** or the update entry under **Updates & service**.
3. Let the app check for updates and read the information about the channel, size and selected board.
4. Start an offered step with **Install** and wait for the transfer and installation status. The app then plans the next step again.
5. Installation can continue on the scooter after the transfer. If the app asks, reconnect to confirm installation. An installed step may wait for the scooter to be locked and restarted.

A full image and a channel change can take a long time over Bluetooth. Follow the app's instructions and do not deliberately interrupt an ongoing installation. If the Bluetooth update service is unavailable, the app explains this; another update method may be needed.

<span class="release-pill" title="Available since Librescoot 1.2">1.2+</span> On supported scooters, **Update from file** also accepts files on your phone. The app shows whether files are uploaded first or installed immediately. Use only appropriate firmware files from trusted sources.

## App settings and privacy

In the **App** section of Settings, you can change the language and theme and control **App lock** and **Online Location Services**. App lock uses the biometric authentication configured on your phone, if available.

**Demo mode** shows example data without changing your saved scooters. Disconnect a connected scooter before enabling it. Turn Demo mode off in Settings to leave it.

The Android **background connection** is marked beta. It can use more phone battery and may require pairing again if problems occur. Read the notice when enabling it. **Ignore battery optimisation** may help background features; its effect depends on the phone.

The local **Activity log** records supported actions on this device. You can stop saving new entries or clear the log in its screen. Details about data processing and online services are in the linked privacy policy.

## Widgets and Tasker

On supported Android and iOS devices, you can add a Librescoot widget to the home screen using the operating system's widget picker. It shows available scooter information and offers actions depending on the platform. Current data requires a connection or the relevant background feature.

On Android, Tasker can trigger supported actions such as locking, unlocking and opening the seatbox. Open and save the Tasker action if the app asks for authorisation. Automations must suit the intended scooter and its surroundings. Check the scooter's actual state after an action.

## Troubleshooting

### Connection fails

- Check that the scooter is switched on and nearby and that Bluetooth is enabled on the phone.
- Check Nearby devices permissions or, on older Android versions, location permission.
- If the scooter has just started, wait for Bluetooth to become available and scan again.
- If necessary, disable the background connection of other scooter apps.
- If pairing is lost, setup may need to be repeated. Keep a working keycard available.

### A setting is missing or greyed out

Connect the right scooter and wait for the app to read its supported features. Some entries need Librescoot or a specific firmware capability. A greyed-out setting cannot be changed until the necessary connection or support is available.

### Place search is missing

Check **Settings > App > Online Location Services**. When online search is disabled, the app shows a notice instead of the search field. The phone must also be online to search.

### Send an error report

If the app crashes or another problem occurs, send an error report. Restart the app first if it has crashed.

1. Open the question mark on the home screen and choose **Send debug logs** under **Help & about**.
2. Read the notice and choose **Continue**. Your email app opens a prepared report.
3. Above the separator, describe what you wanted to do, what happened and how to reproduce it.
4. Check the email and attachment for information you do not want to share, then send the message yourself.

The report can include app and device information, settings, recent diagnostic logs and available Android crash information. The app does not send the email automatically. **Help & about** also links to the handbook, troubleshooting, community and workshop directory.

</div>
