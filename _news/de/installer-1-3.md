---
lang: de
title: "Installer 1.3.0: Der Roller bringt die Installation selbst zu Ende"
date: 2026-09-01
permalink: /news/installer-1-3/
summary: "Der neue Installer bereitet Firmware, Karten und Boards im Voraus vor. Danach schließt der Roller die Installation ohne Laptop ab – schneller, robuster und mit deutlich weniger Handarbeit."
image: /images/install/lsi-mdb_usb_connected.jpg
image_alt: "Das per USB angeschlossene MDB im Fußraum des Rollers"
---

**Installer 1.3.0 ist da!** Die neue stabile Version erledigt die Vorbereitung am
Anfang: Sie prüft MDB und DBC, lädt Firmware und Kartendaten herunter und
überträgt alles, was der Roller für die weiteren Schritte braucht. Sobald das
USB-Kabel wieder am Display angeschlossen ist, läuft die Installation ohne
Laptop weiter. Der Roller installiert Display, Karten und Routingdaten, startet
die Komponenten neu und entsperrt sich nach dem Abschluss selbst.

Der gesamte Ablauf ist schneller, robuster und einfacher geworden. Installer
1.3.0 steht für Linux, macOS und Windows zum Download bereit.

## Erst vorbereiten, dann selbständig fertig werden

Beim alten Installer musste das USB-Kabel während der Installation mehrfach
umgesteckt werden. Installer 1.3.0 bündelt die Arbeit am Laptop am Anfang. Firmware,
Karten und Routingdaten werden heruntergeladen, geprüft und übertragen, bevor
der Roller übernimmt.

Display und Blinker zeigen den weiteren Fortschritt an. Der Laptop wird für
diesen Teil nicht mehr gebraucht und muss später auch nicht erneut angeschlossen
werden. Stromversorgung und Kabel am Roller bleiben angeschlossen, bis das
Display den erfolgreichen Abschluss meldet.

## Schneller durch den Ablauf

Downloads und Übertragungen laufen dort parallel, wo es möglich ist. Bereits
vorhandene Dateien werden wiederverwendet, statt noch einmal geladen oder
übertragen zu werden. Komprimierte Routingdaten verkürzen vor allem bei größeren
Kartenregionen Download und Übertragung deutlich.

Auch die Flash-Werkzeuge und die Behandlung von USB-Geräten wurden für Linux,
macOS und Windows aktualisiert. Der Installer kümmert sich selbst um benötigte
Berechtigungen, Netzwerkkonfiguration und unter Windows um den USB-Treiber.

## Robuster bei Unterbrechungen

Der Installationszustand wird auf dem Roller festgehalten. Nach einer
Unterbrechung erkennt der Installer, welche Schritte bereits abgeschlossen
wurden, und erklärt, wie es weitergeht. Schon übertragene Dateien müssen dabei
nicht erneut auf den Roller.

Längere Schritte zeigen jetzt ihre aktuelle Phase, die übliche Dauer und die
bereits vergangene Zeit. Auch Übertragungen im Hintergrund bleiben sichtbar.
Wenn etwas fehlschlägt, lassen sich Fehlermeldung und Installationsprotokoll
direkt kopieren.

## Upgrades ohne Neuinstallation

Installer 1.3.0 kann ein bestehendes Librescoot-System aktualisieren. Einstellungen,
angelernte Schlüsselkarten und Offline-Karten bleiben dabei erhalten. MDB und DBC
lassen sich getrennt aktualisieren, neu installieren oder unverändert lassen.
Vor einem Downgrade auf eine ältere Version warnt der Installer.

Eine vollständige Neuinstallation ist weiterhin möglich, etwa für einen
Serienroller oder zur Wiederherstellung eines Systems.

## Download und Installation

Du brauchst ein USB-Kabel, einen Schraubendreher und ungefähr zwanzig Minuten
Zeit. Auf einem bisher zuverlässig laufenden Roller klappt das Flashen
normalerweise problemlos. Beginne trotzdem nicht in Eile, damit du die Schritte
in Ruhe ausführen kannst und bei Rückfragen oder einer Wiederherstellung genug
Zeit hast.

- [Installer herunterladen](https://downloads.librescoot.org/)
- [Installationsanleitung](https://librescoot.org/docs/install.html)
- [Release Notes zu Installer 1.3.0](https://github.com/librescoot/installer/releases/tag/v1.3.0)
- [Discord](https://discord.gg/BmY2P2T9j3) für Fragen und Rückmeldungen
