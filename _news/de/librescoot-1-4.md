---
lang: de
title: 'Librescoot 1.4.0 „Spätsommer“'
date: 2026-10-12
permalink: /news/librescoot-1-4/
published: false
summary: Web-Oberfläche, Routen mit mehreren Stopps, regionale Offline-Karten und koordinierter Winterschlaf.
icon: map
---

Librescoot 1.4.0 „Spätsommer“ bringt die Verwaltung in den Browser und erweitert die Navigation um mehrere Stopps und regionale Offline-Karten. Dieser Beitrag ist ein Entwurf für die Veröffentlichung; ein Stable-Image ist noch nicht veröffentlicht.

## Im Browser verwalten

Die [Web-Oberfläche lsd](/handbook/lsd.html) läuft direkt auf dem Roller. Über USB verwaltest du Einstellungen, Schlüsselkarten, Navigationsziele, Dateien, Updates und Log-Pakete. Sunshine bleibt optional. Für die Einrichtung erzeugst du einen Installer-Zugang in den Sunshine-Kontoeinstellungen und fügst dessen Token oder Online-Installer-Link im Cloud-Bereich ein.

## Unterwegs mit mehreren Stopps

Plane Stopps, ändere ihre Reihenfolge oder überspringe einen. Der Plan bleibt nach einem Neustart erhalten. Am Zwischenstopp läuft ein Countdown von 30 Sekunden nur im Fahrmodus. Die Bremsen bedienen diese Meldung nicht; bei geschlossenem Schnellmenü pausiert ein Druck auf den Sitzbankschalter die Route. Beim Verlassen des Fahrmodus endet der Countdown. Nach einem erreichten Zwischenstopp geht es beim nächsten Wechsel in den Fahrmodus zum nächsten Stopp.

Mehrere benannte Karten- und Routing-Pakete lassen sich per USB installieren. Mit aktuellem GPS-Fix wählt der Tacho die passende Region. Routen über Regionsgrenzen sind nicht unterstützt. Vorhandene Einzelregionen bleiben nutzbar; eine reguläre Routing-Datei muss für den Wechsel auf regionale Pakete ausdrücklich umgestellt werden. Mehr dazu im [Navigationshandbuch](/handbook/navigation.html).

## Im Alltag

- **Fahrtenzähler und Verlauf:** Der Zähler bleibt über Neustarts erhalten. Du bestimmst, ob er nach jeder Fahrt, täglich, beim Akkuwechsel oder nur manuell zurückgesetzt wird.
- **Schlüsselkarten:** Am Tacho anlernen und entfernen. Neue Entsperrkarten werden erst mit „Fertig“ gespeichert.
- **Töne und Meldungen:** Der Tacho spielt Töne für Fahrzeug, Navigation und Meldungen, wenn ein Verstärker angeschlossen ist (bei den meisten Rollern nicht angeschlossen); gleich wichtige Hinweise wechseln sich ab.
- **Winterschlaf:** Ein ausdrücklicher Befehl aus dem Parkmodus koordiniert zunächst das Herunterfahren. Ein relativer Zeitraum braucht keine synchronisierte Uhr, ein wiederkehrender Zeitplan dagegen schon.
- **Updates:** Vorschau der geplanten Downloadgröße. Ein USB-Update ohne anwendbare Dateien endet ohne Neustart.
- **Bluetooth:** nRF-Firmware 2.14.0-ls und Dateitransfer für passende Apps. Log-Pakete herunterladen oder Dateien in einen Eingangsordner übertragen; das installiert keine Firmware und aktiviert keine Karten.

Die Beschreibung richtet sich nach dem [veröffentlichten Quellstand für 1.4](https://github.com/librescoot/librescoot/blob/2847f3606bdc6e7c67a1e44bd14619bef9f369ff/stable.env). Sunshine wird separat bereitgestellt.
