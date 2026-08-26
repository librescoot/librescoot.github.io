---
lang: de
title: "Librescoot 1.2.1: neue Systembasis, SMS und Updates über Bluetooth"
date: 2026-08-03
permalink: /news/librescoot-1-2-1/
summary: "Alles unterhalb der Librescoot-Dienste läuft jetzt auf einer aktuellen LTS-Basis mit Linux 6.12. Dazu SMS, Unterstützung für mechanische Warnblinkschalter und Firmware-Updates über Bluetooth."
image: /images/handbook/cluster-mit-navigation.png
image_alt: "Navigationshinweis in der Tachoanzeige"
---

Librescoot 1.2.1 ist da. Was sich gegenüber 1.1 getan hat:

Die größte Änderung ist vom Sattel aus nicht zu sehen: Alles unterhalb der
Librescoot-Dienste läuft jetzt auf einer aktuellen Long-Term-Support-Basis mit
Linux 6.12. Der alte 5.4er-Kernel ist damit abgelöst.

Der Roller kann SMS senden und empfangen, und nachgerüstete mechanische
Warnblinkschalter werden unterstützt. Danke an Jonas.

Firmware-Updates können über Bluetooth ankommen, neben den Wegen über USB und
Mobilfunk. Vom Telefon aus geht das mit „stasis for unu“ aus dem Play Store;
den TestFlight-Link für iOS gibt es auf Discord.

Dazu die Reparaturen: Eine veraltete GPS-Position zieht die Systemuhr nicht mehr
mit sich, und das Modem wird nicht mehr neu gestartet, bloß weil ein Endpunkt im
Netz gerade nicht erreichbar ist, daher kamen die GPS-Aussetzer. Die Blinker
erscheinen jetzt auch auf dem „Warten auf GPS“-Bildschirm. Updateprozess,
ECU-Kommunikation und das Erkennen bereits installierter Kartendaten sind
stabiler geworden.

Hinweis zu Version 1.2.0: 1.2.0 wurde zurückgezogen.

## Installieren

Roller auf dem Kanal **stable** holen sich 1.2.1 von selbst.

- [Downloads](https://downloads.librescoot.org/)
- [v1.2.1 auf GitHub](https://github.com/librescoot/librescoot/releases/tag/v1.2.1)
