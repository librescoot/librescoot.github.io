---
lang: de
title: "Librescoot 1.0: das erste stabile Release"
date: 2026-05-01
permalink: /news/librescoot-1-0/
summary: "Offline-Navigation, automatisches Lenkschloss, Bewegungsalarm und Updates über die Luft. Freie Open-Source-Firmware für den unu Scooter Pro, mit einem Installer für Linux, macOS und Windows."
image: /images/handbook/cluster-anzeigen-alle.png
image_alt: "Die Tachoanzeige mit allen Anzeigeelementen"
---

Librescoot 1.0 ist da. Das erste stabile Release: freie Open-Source-Firmware
für den unu Scooter Pro, ein Installer für Linux, macOS und Windows und ein
Handbuch dazu.

## Was drin ist

Offline-Navigation mit Karte und Abbiegehinweisen auf dem Display im Lenker.
Die Kartendaten liegen auf dem Roller selbst, es braucht also weder ein Handy
am Lenker noch eine Datenverbindung.

![Karte mit aktiver Route auf dem Display](/images/handbook/map-nav-day.png)

Das Lenkschloss arbeitet automatisch. Wer den Lenker bei entriegeltem Roller
bewegt, löst es damit; nach dem Abstellen verriegelt es kurz darauf wieder. Ein
Bewegungsalarm überwacht den Roller unabhängig davon.

Nichts davon setzt eine SIM-Karte voraus. Karten, Navigation, Alarm und Updates
über USB funktionieren ohne Datenverbindung. Eine SIM bringt Fernzugriff und
Updates über das Netz, für das Fahren selbst spielt sie keine Rolle.

Das Display gibt es in Hell und Dunkel und lässt sich konfigurieren. Wer den
hinteren Akkuschacht nachgerüstet hat, sieht beide Akkus in der Statusleiste.
Updates kommen als Delta über die Luft, auf drei Kanälen: stable, testing,
nightly. Dazu Keycard-Verwaltung, ein WireGuard-VPN und das
Kommandozeilenwerkzeug `lsc` für alles Weitere.

## Installation

Installer herunterladen, USB-Kabel an den Roller, dem Assistenten folgen. Er
lädt Firmware und Kartendaten für den gewählten Kanal, zeigt die erkannte
Hardware an, damit klar ist, dass es der richtige Roller ist, schreibt das MDB
und flasht anschließend das Display vom Roller aus. Danach richtet er
Offline-Karten, Bluetooth und die Keycard ein.

![Das einzige Kabel, das die Installation braucht, am MDB](/images/install/lsi-mdb_usb_connected.jpg)

Nötig sind ein USB-Kabel, ein Schraubendreher für den Fußraum und rund zwanzig
Minuten.

Die Builds erscheinen für alle drei Plattformen gemeinsam. Am gründlichsten
getestet ist der Weg unter Linux, macOS und Windows funktionieren, haben aber
deutlich weniger Roller gesehen. Im README steht weiterhin *Beta software*, und
das ist ernst gemeint. Wenn eine Installation abbricht, meldet sie bitte.

## Das Handbuch

Elf Seiten zu allem, was nach der Installation kommt: Schnellstart und erste
Schritte, das Display mit allen Anzeigen und den Bremshebel-Gesten, Fahren,
Zustände und Akku, Navigation, Updates, Fehlerbehebung und was sich gegenüber
scooterOS geändert hat. Durchgehend mit Screenshots, damit sich das Gelesene
mit dem Bildschirm abgleichen lässt. Alles im [Handbuch](/handbook/).

- [Downloads](https://downloads.librescoot.org/)
- [v1.0.0 auf GitHub](https://github.com/librescoot/librescoot/releases/tag/v1.0.0)
- [Discord](https://discord.gg/BmY2P2T9j3)
