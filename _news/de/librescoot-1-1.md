---
lang: de
title: "Librescoot 1.1: Schlafzustände und Energieverwaltung"
date: 2026-07-04
permalink: /news/librescoot-1-1/
summary: "Der Fokus liegt auf der Energieverwaltung: Suspend für bis zu zehn Tage, Hibernation per Timer oder nach Zeitplan, und ein Roller, der sich selbst schlafen legt, bevor die internen Akkus leer sind. Dazu Servicemodus, Keycard im Hop-On-Modus und manuell regelbare Hintergrundbeleuchtung."
icon: moon
---

Librescoot 1.1 ist erschienen. Der Fokus liegt auf der Energieverwaltung.

Ein abgestellter Roller ist trotzdem wach: Die Elektronik läuft im Leerlauf
weiter und zieht über die Wochen die internen Akkus leer. Nach zwei Wochen
Urlaub steht ein Fahrzeug da, das erst wieder betriebsbereit gemacht werden
muss.

## Schlafen

Suspend, ein Bereitschaftszustand mit stark reduziertem Verbrauch: Ohne
eingesetzten Fahrakku wechselt der Roller jetzt von selbst in diesen Zustand und
kann bis zu zehn Tage darin bleiben.

In die Hibernation führen zwei zusätzliche Wege. „Hibernate for“ legt eine feste
Dauer fest, nach der der Roller von selbst wieder hochfährt. „Scheduled
hibernate“ arbeitet stattdessen nach einem wiederkehrenden Zeitplan, etwa jede
Nacht, und weckt den Roller morgens wieder auf.

Gehen die internen Akkus dennoch zur Neige, wechselt der Roller selbsttätig in
die Hibernation, statt sie weiter zu belasten. Ein Akku, der einmal vollständig
entladen war und in diesem Zustand geblieben ist, erholt sich davon oft nicht
mehr ganz.

Ergänzend dazu: Warnungen bei niedrigem Ladestand der internen Akkus und die
Akkutemperaturen auf dem Debug-Screen.

## Außerdem neu

- Servicemodus, für alles, was am stehenden Roller passiert.
- Entsperren mit der Keycard im Hop-On-Modus.
- Die Hintergrundbeleuchtung des Displays lässt sich von Hand regeln.
- Eine Einstellung, die den Hupknopf deaktiviert, solange die Sitzbank offen ist.
- Verriegeln hat jetzt einen eigenen Menüpunkt.
- Optional zeigt die Statusleiste den Ladestand der internen Akkus.

## Behoben

Die Rekuperations- und Leistungsanzeige wurde überarbeitet, das Hauptmenü
umstrukturiert. Automatische Hintergrundbeleuchtung und automatischer
Hell-Dunkel-Wechsel arbeiten zuverlässiger, ebenso Adresseingabe,
Bewegungserkennung und Lenkschlosserkennung. Online-Updates prüfen nach, was sie
heruntergeladen haben. Der Kaltstart ist kürzer. Die Hupe bleibt beim
Entschärfen der Alarmanlage nicht mehr hängen. Bei abgenutztem
Sitzbankverschluss bleibt die Akkuverwaltung auch während der Fahrt stabil. Dazu
kommen Darstellungsfehler in der Statusleiste und in der Navigation, ein
sauberer Shutdown des Displays, eine bessere ECU-Anbindung, weniger
Datenverbrauch über die Cloud-Verbindung sowie Arbeit am Updatemodus und am
nRF-Updateprozess.

## Update installieren

Roller auf dem Kanal **stable** holen sich das Update von selbst.

- [Downloads](https://downloads.librescoot.org/)
- [v1.1.0 auf GitHub](https://github.com/librescoot/librescoot/releases/tag/v1.1.0)
