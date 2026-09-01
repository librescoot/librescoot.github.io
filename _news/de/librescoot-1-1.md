---
lang: de
title: "Librescoot 1.1: Bessere Energieverwaltung und neue Ruhemodi"
date: 2026-07-04
permalink: /news/librescoot-1-1/
summary: "Suspend für bis zu zehn Tage, Hibernation für eine gewählte Dauer oder nach Zeitplan und automatischer Schutz für die internen Akkus. Dazu Servicemodus, Entsperren per Keycard in Hop-On und eine manuell regelbare Hintergrundbeleuchtung."
icon: moon
---

Librescoot 1.1 ist da! Im Mittelpunkt dieses Releases steht die
Energieverwaltung. Neue Ruhemodi helfen dabei, einen abgestellten Roller
bereitzuhalten, ohne seine internen Akkus unnötig zu entladen.

## Suspend und Hibernation

Wird der Fahrakku entfernt, kann der Roller jetzt automatisch in Suspend
wechseln und bis zu zehn Tage in diesem sparsamen Zustand bleiben.

Für die Hibernation gibt es zwei neue Möglichkeiten. Mit **Hibernate for** wird
der Roller für eine gewählte Dauer ausgeschaltet. **Scheduled hibernate** folgt
einem wiederkehrenden Zeitplan, sodass der Roller beispielsweise nachts
ausschaltet und morgens wieder aufwacht.

Sinkt der Ladestand der internen Akkus zu weit, wechselt der Roller automatisch
in die Hibernation, statt sie weiter zu entladen. Das Display warnt außerdem
frühzeitig vor einem niedrigen Ladestand; auf dem Debug-Screen werden nun auch
die Temperaturen der internen Akkus angezeigt.

## Weitere neue Funktionen

- Servicemodus für Wartung und andere Arbeiten am stehenden Roller
- Entsperren per Keycard in Hop-On
- Manuelle Regelung der Displaybeleuchtung
- Eine Option, die den Hupknopf bei geöffneter Sitzbank deaktiviert
- Ein eigener Menüpunkt zum Verriegeln des Rollers
- Eine optionale Ladeanzeige für die internen Akkus in der Statusleiste

## Verbesserungen und Fehlerbehebungen

Die Leistungs- und Rekuperationsanzeige wurde überarbeitet und das Hauptmenü neu
geordnet. Automatische Helligkeit und Hell-Dunkel-Wechsel reagieren
zuverlässiger. Auch Adresseingabe, Bewegungserkennung und die Erkennung des
Lenkschlosses wurden verbessert. Der Kaltstart ist schneller, und
Online-Updates prüfen heruntergeladene Daten jetzt vor der Installation.

Mehrere Fehler wurden ebenfalls behoben. Die Hupe bleibt beim Entschärfen der
Alarmanlage nicht mehr eingeschaltet, und die Akkuverwaltung funktioniert auch
mit einem abgenutzten Sitzbankverschluss während der Fahrt zuverlässig. Weitere
Verbesserungen betreffen das Herunterfahren des Displays, die Kommunikation mit
den Steuergeräten, die Darstellung in Navigation und Statusleiste, den
Update-Modus und Firmware-Updates des Bluetooth-Controllers. Gleichzeitig
wurde der Datenverbrauch über die Cloud-Verbindung reduziert.

Vielen Dank an alle, die diese Änderungen getestet und Fehler gemeldet haben.

## Update installieren

Roller auf dem Kanal **stable** erhalten Librescoot 1.1 automatisch.

- [Downloads](https://downloads.librescoot.org/)
- [Librescoot v1.1.0 auf GitHub](https://github.com/librescoot/librescoot/releases/tag/v1.1.0)
