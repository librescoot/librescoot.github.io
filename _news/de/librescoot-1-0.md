---
lang: de
title: "Librescoot 1.0: Das erste stabile Release"
date: 2026-05-01
permalink: /news/librescoot-1-0/
summary: "Offline-Navigation, automatisches Lenkschloss, Bewegungsalarm und Online-Updates: freie Open-Source-Firmware für den unu Scooter Pro, mit einem Installer für Linux, macOS und Windows."
image: /images/handbook/cluster-anzeigen-alle.png
image_alt: "Die Tachoanzeige mit allen Anzeigeelementen"
---

Librescoot 1.0 ist da! Damit veröffentlichen wir das erste stabile Release der
freien Open-Source-Firmware für den unu Scooter Pro. Dazu gehören ein Installer
für Linux, macOS und Windows sowie ein Handbuch für Einrichtung und Nutzung.

## Navigation und Alltag

Die Offline-Navigation bringt Karten und Abbiegehinweise auf das Display des
Rollers. Die Kartendaten liegen auf dem Fahrzeug, sodass die Navigation weder
ein Handy am Lenker noch eine Mobilfunkverbindung braucht.

![Karte mit aktiver Route auf dem Display](/images/handbook/map-nav-day.png)

Das Lenkschloss kann automatisch arbeiten: Wird der Lenker am entriegelten
Roller bewegt, löst sich das Schloss. Kurz nach dem Ausschalten verriegelt es
wieder. Ein Bewegungsalarm kann den abgestellten Roller zusätzlich überwachen.

Diese Funktionen benötigen keine SIM-Karte. Karten, Navigation, Alarm und
Updates über USB funktionieren vollständig offline. Mit einer SIM kommen
Fernzugriff und Updates über das Mobilfunknetz dazu; zum Fahren ist sie nicht
nötig.

Das Display bietet anpassbare helle und dunkle Ansichten. Bei einem
nachgerüsteten hinteren Akkuschacht erscheinen beide Akkus in der Statusleiste.
Librescoot bringt außerdem eine Keycard-Verwaltung, ein WireGuard-VPN und das
Kommandozeilenwerkzeug `lsc` für erweiterte Einstellungen und Diagnose mit.

Updates stehen auf den drei Kanälen **stable**, **testing** und **nightly**
bereit. Wo möglich, werden nur die Änderungen als kleineres Delta übertragen.

## Librescoot installieren

Der Installer führt durch die Einrichtung. Er lädt Firmware und Karten für den
gewählten Kanal, zeigt die erkannte Hardware zur Bestätigung an, installiert
Librescoot auf beiden Boards und richtet anschließend Offline-Karten, Bluetooth
und die Keycard ein.

![Der USB-Anschluss für die Installation](/images/install/lsi-mdb_usb_connected.jpg)

Die Installation dauert etwa zwanzig Minuten. Benötigt werden ein USB-Kabel und
ein Schraubendreher, um den Fußraum zu öffnen.

Die Builds für Linux, macOS und Windows erscheinen gemeinsam. Unter Linux wurde
der Installer bisher auf den meisten Rollern erprobt. macOS und Windows
funktionieren ebenfalls, haben aber noch weniger Praxistests gesehen. Der
Installer ist weiterhin als Beta-Software gekennzeichnet. Berichte von allen
drei Plattformen sind willkommen, besonders wenn etwas nicht wie erwartet
funktioniert.

## Das Handbuch

Das [Librescoot-Handbuch](/handbook/) erklärt die ersten Schritte nach der
Installation, Display und Bremshebel-Bedienung, Fahren, Akkus und
Fahrzeugzustände, Navigation, Updates und Fehlerbehebung. Für Umsteiger werden
außerdem die wichtigsten Unterschiede zu scooterOS beschrieben.

Vielen Dank an alle, die Code beigetragen, frühe Versionen getestet, Fehler
gemeldet und an der Dokumentation mitgearbeitet haben.

- [Downloads](https://downloads.librescoot.org/)
- [Librescoot v1.0.0 auf GitHub](https://github.com/librescoot/librescoot/releases/tag/v1.0.0)
- [Discord](https://discord.gg/BmY2P2T9j3)
