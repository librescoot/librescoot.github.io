---
lang: de
title: "Librescoot 1.3: 2D-Karte, Straßennamen und Updates am Roller"
date: 2026-08-28
permalink: /news/librescoot-1-3/
summary: "Eine flache 2D-Karte wahlweise nach Norden oder in Fahrtrichtung, Straßennamen auf den Offline-Karten, Einstellungen zur Routenwahl und Update-Einstellungen direkt am Roller. Dazu eine lange Liste von Fehlern, die vorher gar nicht gemeldet wurden."
image: /images/news/map-2d-heading.png
image_alt: "Die 2D-Kartenansicht in Fahrtrichtung, mit aktiver Route"
---

Librescoot 1.3 ist da. Im Mittelpunkt steht die Navigation: eine zweite
Kartenansicht, Straßennamen und Einstellungen zur Routenplanung. Dahinter steckt
viel Arbeit an der Zuverlässigkeit.

## Karte und Navigation

Neben der 3D-Ansicht gibt es jetzt eine flache 2D-Karte, wahlweise nach Norden
ausgerichtet oder in Fahrtrichtung. Standard bleibt 3D.

![Die 2D-Karte in Fahrtrichtung, mit aktiver Route](/images/news/map-2d-heading.png)

Die Offline-Karten zeigen jetzt Straßennamen. Für die Routenplanung sind unter
*Map & Navigation* zwei Einstellungen dazugekommen: die Routenwahl zwischen
schnellster und kürzester Strecke, und Avoid Cobblestone in vier Stufen: aus,
niedrig, mittel und hoch. Voreingestellt ist mittel.

Die Positionsbestimmung wurde darunter überarbeitet. Der Marker wandert im Stand
nicht mehr nach vorn und bleibt in Kurven nicht mehr hängen, um dann zu
springen. Die Kreisverkehr-Symbole sind neu gezeichnet, eine Neuberechnung
startet von einer besser gewählten Position, und Straßenname und Tempolimit
hinken nicht mehr hinterher.

## Updates am Roller

Die Update-Einstellungen sind auf das Display gewandert, unter *Settings >
System > Updates*: Prüfintervall, manuelle Prüfung, Update-Art und
Release-Kanal.

![Das Update-Menü auf dem Roller](/images/news/updates-menu.png)

Vor einem Kanalwechsel wird angezeigt, was beide Boards dabei herunterladen
würden. Gesetzt werden sie immer gemeinsam und können deshalb nicht auf
unterschiedlichen Kanälen landen.

Auch mit schlechter Verbindung kommen Downloads besser zurecht: Ein hängender
Transfer wird abgebrochen, statt endlos zu warten, Wiederholungen warten
zunehmend länger und überstehen einen Neustart, und ein Download mit falscher
Prüfsumme wird gelöscht, damit der nächste Versuch wirklich neu lädt. Ein
unterbrochenes Update fängt außerdem nicht mehr von vorn an, sondern macht dort
weiter, wo es aufgehört hat.

Dazu gibt es jetzt einen Menüpunkt, um gekoppelte Telefone zu entfernen, und die
App kann ihre eigene Kopplung selbst lösen. Bisher wurde dabei nur die Seite des
Telefons gelöscht, sodass sich am Roller immer mehr Kopplungen ansammelten.

## Der Alarm merkt mehr

Bremshebel, Hupe und Sitzbanktaste zählen jetzt als Manipulation, solange der
Alarm scharf ist. Das ist standardmäßig aktiv. Außerdem hält der Alarm fest,
welche Quelle ihn ausgelöst hat und wann, sodass sich eine Hupe mitten in der
Nacht zuordnen lässt.

Für den Lenker gibt es ebenfalls Auslöser, die den Schloss- und den
Positionssensor beobachten. Sie sind vorerst abgeschaltet, bis sie länger auf
echten Rollern gelaufen sind.

## Menüs und Display

Die Einstellungen sind jetzt nach Themen gruppiert, Info liegt auf der obersten
Ebene.

![Die nach Themen gruppierten Einstellungen](/images/news/settings-root.png)

Die Bremsgesten stehen unten am Bildschirmrand und funktionieren überall gleich.
Ein Tipp auf die linke Bremse geht in der Liste nach unten, ein Tipp auf die
rechte wählt aus. Langes Drücken der rechten Bremse führt die Aktion einer Zeile
aus, ohne sie zu öffnen, langes Drücken der linken geht eine Ebene zurück, und
drei Sekunden auf der linken Bremse schließen das Menü aus jeder Tiefe.

Neue Info-Seiten zeigen Komponenten, Verbindungen, Akkus und Karten, und die
Board-Versionen und Seriennummern bleiben auch ohne Cloud-Client sichtbar. Das
Display ist außerdem flüssiger geworden: Tacho, Hintergrund-Unschärfe und
mehrere dauerhaft laufende Animationen wurden überarbeitet.

## Fehler, die vorher nie gemeldet wurden

Vor 1.3 hat das Fahrzeug überhaupt keine Fehler gemeldet. Die Fehlerseite gab
es, sie war bauartbedingt leer. Jetzt setzen fehlgeschlagene Schaltbefehle an
Motor, Display und Bremse einen Fehlercode, ebenso ein Motorcontroller, den die
Bremsverriegelung stromlos hält, und ein abgelehnter Versuch, den letzten
Zustand wiederherzustellen.

Ein paar weitere aus derselben Ecke: Ein abgestellter Roller konnte hängen
bleiben, statt in den Standby zu gehen, und dabei die AUX-Batterie leerziehen;
das Display konnte nach dem Verriegeln noch minutenlang an bleiben; ein
fehlgeschlagener Wiederherstellungsversuch konnte die Fahrzeugsteuerung in eine
Neustartschleife schicken. Und ein Roller mit vollen Akkus ging manchmal
trotzdem in Hibernation, weil die Notabschaltung auf veralteten Messwerten
entschied. Alles behoben.

Auch `lsc` wurde repariert: Die Befehle rund um den Datenspeicher funktionierten
auf keinem 1.2er Roller, und die Fehler- und Sperrlisten meldeten immer null,
weil sie die falschen Schlüssel gelesen haben.

Die [vollständigen Release Notes](https://github.com/librescoot/librescoot/releases/tag/v1.3.0)
haben die komplette Liste.

## Installieren

Roller auf dem Kanal **stable** holen sich 1.3.0 von selbst.

- [Downloads](https://downloads.librescoot.org/)
- [v1.3.0 auf GitHub](https://github.com/librescoot/librescoot/releases/tag/v1.3.0)
- [Discord](https://discord.gg/BmY2P2T9j3)
