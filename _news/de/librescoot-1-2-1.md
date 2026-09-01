---
lang: de
title: "Librescoot 1.2.1: Neue Systembasis, SMS und Bluetooth-Updates"
date: 2026-08-03
permalink: /news/librescoot-1-2-1/
summary: "Eine aktuelle, langfristig unterstützte Systembasis mit Linux 6.12, dazu SMS, mechanische Warnblinkschalter, Firmware-Updates über Bluetooth und zahlreiche Verbesserungen an der Zuverlässigkeit."
image: /images/handbook/cluster-mit-navigation.png
image_alt: "Navigationshinweis in der Tachoanzeige"
---

Librescoot 1.2.1 ist da! Dieses Release stellt das System auf eine aktuelle,
langfristig unterstützte Basis mit Linux 6.12 um. Dazu kommen SMS, mechanische
Warnblinkschalter, Firmware-Updates über Bluetooth und zahlreiche
Verbesserungen an der Zuverlässigkeit.

## Eine neue Grundlage

Unter den Librescoot-Diensten läuft jetzt Linux 6.12 anstelle des bisherigen
5.4er-Kernels. Die Umstellung geschieht weitgehend im Hintergrund und schafft
eine aktuelle, langfristig gepflegte Grundlage für die weitere Entwicklung.

Der Roller kann nun SMS senden und empfangen. Auch nachgerüstete mechanische
Warnblinkschalter werden unterstützt. Danke an Jonas für den Beitrag zu dieser
Funktion.

## Updates über Bluetooth

Firmware-Updates können neben USB und Mobilfunk jetzt auch über Bluetooth
übertragen werden. Unter Android funktioniert das mit **stasis for unu** aus
dem Play Store. Für iOS ist der TestFlight-Link auf Nachfrage über Discord
erhältlich.

## Verbesserungen und Fehlerbehebungen

GPS und Mobilfunkverbindung arbeiten zuverlässiger. Ein vorübergehend nicht
erreichbarer Netzwerkdienst führt nicht mehr zu einem unnötigen Neustart des
Modems. Eine veraltete GPS-Position kann außerdem nicht mehr die Systemzeit
verstellen.

Die Blinker bleiben nun auch sichtbar, während das Display auf eine GPS-Position
wartet. Darüber hinaus wurden der Updateprozess, die Kommunikation mit den
Steuergeräten und die Erkennung bereits installierter Kartendaten verbessert.

Librescoot 1.2.0 wurde zurückgezogen und durch dieses Release ersetzt.

Vielen Dank an alle, die das Release getestet und bei der Fehlersuche geholfen
haben.

## Update installieren

Roller auf dem Kanal **stable** erhalten Librescoot 1.2.1 automatisch.

- [Downloads](https://downloads.librescoot.org/)
- [Librescoot v1.2.1 auf GitHub](https://github.com/librescoot/librescoot/releases/tag/v1.2.1)
- [Discord](https://discord.gg/BmY2P2T9j3)
