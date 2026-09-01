---
lang: de
title: "Librescoot 1.3: Bessere Karten, besseres und schnelleres Interface und viele Verbesserungen"
date: 2026-09-01
permalink: /news/librescoot-1-3/
summary: "Eine stark verbesserte Tacho-Ansicht mit Straßennamen, einer neuen 2D-Ansicht, mehr Routenoptionen und überarbeitetem UI. Außerdem Fehlerbehebungen und viele kleine Verbesserungen."
image: /images/news/map-2d-heading.png
image_alt: "Die 2D-Kartenansicht in Fahrtrichtung, mit aktiver Route"
image_caption: "2D-Karte in Fahrtrichtung mit aktiver Route"
image_in_post: false
---

<div class="news-screenshot-grid news-screenshot-grid-three">
{% include news-screenshot.html src="/images/news/map-2d-heading.png" alt="Die 2D-Karte in Fahrtrichtung mit aktiver Route" caption="2D-Karte in Fahrtrichtung mit aktiver Route" loading="eager" %}
{% include news-screenshot.html src="/images/news/map-2d-north.png" alt="Die 2D-Karte nach Norden ausgerichtet, mit aktiver Route" caption="2D-Karte nach Norden ausgerichtet, mit aktiver Route" loading="eager" %}
{% include news-screenshot.html src="/images/news/map-2d-noroute.png" alt="Die 2D-Karte in Fahrtrichtung ohne aktive Route" caption="2D-Karte in Fahrtrichtung ohne aktive Route" loading="eager" %}
</div>

Librescoot 1.3 ist da! Das Hauptaugenmerk lag auf dem Tacho: Neben der 3D-Karte
gibt es nun auch eine 2D-Ansicht, die Karten sind detaillierter und enthalten
Straßennamen, beim Routing kann jetzt zwischen schnellster und kürzester Route
gewählt und Kopfsteinpflaster vermieden werden. Außerdem wurde die Darstellung
beschleunigt und das Menü erweitert und verfeinert. Im Hintergrund wurde viel an
Zuverlässigkeit und Stabilität gearbeitet.

## Tacho, Menüs und Bedienung

Der Tacho startet schneller und reagiert flüssiger. Außerdem sind die
Einstellungen jetzt nach Themen sortiert und neue Info-Seiten zeigen Details zu
Komponenten, Verbindungen, Akkus und Karten. Auch Software-Versionen und
Seriennummern der Bauteile sind dort zu finden.

{% include news-screenshot.html src="/images/news/info-menu.png" alt="Das Info-Menü auf dem Tacho" caption="Das neue Info-Menü bündelt Details zu Komponenten, Verbindungen, Akkus, Karten und Fehlern." %}

Die Menüsteuerung wurde vereinheitlicht und die Beschriftungen zeigen die
Optionen jetzt klarer und auf einen Blick. Mit der linken Bremse wird bei kurzem
Drücken nach unten gescrollt, mit längerem Drücken springt man eine Ebene
zurück. Die rechte Bremse wählt Menüeinträge aus und bestätigt Aktionen. Manche
Menüeinträge haben darüber hinaus noch weitere Kurzbefehle bekommen, z.B. um
Navigation schneller zu starten. Außerdem kann das Menü direkt geschlossen
werden, indem die linke Bremse drei Sekunden lang gehalten wird.

{% include news-screenshot.html src="/images/news/settings-root.png" alt="Das nach Themen gruppierte Einstellungsmenü" caption="Die Einstellungen sind jetzt nach Themen gruppiert." %}

Die Uhr kann jetzt optional auch das Datum anzeigen, entweder zusammen mit der
Uhrzeit oder abwechselnd. Die automatische Hintergrundbeleuchtung reagiert
schneller und schaltet ruhiger, und die Rekuperationsanzeige zeigt jetzt genauer
an, wann Regeneration aktiviert ist.

## Karte und Navigation

Neben der 3D-Ansicht gibt es jetzt eine 2D-Karte, die wahlweise nach Norden oder
in Fahrtrichtung ausgerichtet ist. Die Kartendarstellung ist in beiden Ansichten
schneller geworden.

Die aktuellsten Offline-Karten zeigen nun Straßennamen und mehr Details wie
Grünflächen, Seen, Brücken usw. Für die Routenplanung kann zwischen der
schnellsten und der kürzesten Strecke gewählt werden. Kopfsteinpflaster lässt
sich mit kompatiblen Routingdaten in vier Stufen vermeiden: aus, niedrig, mittel
und hoch.

{% include news-screenshot.html src="/images/news/settings-map-navigation.png" alt="Die Einstellungen für Karte und Navigation" caption="Kartenansicht, Routenwahl und Kartenupdates lassen sich direkt am Roller einstellen." %}

Auch während der Fahrt verhält sich die Karte besser: Der Marker bleibt im Stand
nun stabil, Routen-Neuberechnungen starten von einer besser gewählten Position,
und Straßennamen und Tempolimit werden schneller gefunden und aktualisiert. Die
Darstellung von Kreisverkehren wurde ebenfalls neu aufgebaut – mit komplett
neuen, dynamisch gezeichneten Symbolen für die einzelnen Ausfahrten.

{% include news-screenshot.html src="/images/news/map-roundabout.png" alt="Eine aktive Route durch einen Kreisverkehr" caption="Kreisverkehrs-Hinweise zeigen Ausfahrt und Streckenverlauf dynamisch." %}

## Updates am Roller

Software- und Kartenupdates lassen sich jetzt direkt am Roller konfigurieren.
Unter *Einstellungen > System > Updates* stehen *Update-Zeitplan*, *Jetzt
prüfen*, *Update-Art ändern* und *Update-Kanal wechseln* zur Verfügung.

{% include news-screenshot.html src="/images/news/updates-menu.png" alt="Das Update-Menü auf dem Roller" caption="Prüfintervall, manuelle Prüfung, Update-Art und Release-Kanal im Update-Menü." %}

Mit dem Internet verbundene Roller können nun auch direkt den Release-Kanal
umstellen, dabei gibt es eine Bestätigung für das erwartete Datenvolumen. Bei
Offline-Rollern können einfach per Update-Modus ein Release eines anderen Kanals
eingespielt werden.

Unter *Karte & Navigation > Kartenupdates* können automatische Updates der
Karten- und Navigationsdaten konfiguriert werden. Bei neuen Karten wird entweder
nur ein Hinweis gezeigt, oder die neuen Daten sofort heruntergeladen und
installiert. Laufende Downloads von Karten sind jetzt auch in der Statuszeile
sichtbar. Außerdem unterstützt der Update-Modus nun komprimierte Routingdaten,
was die Übertragung deutlich schneller und datensparsamer macht.

Downloads kommen nun besser mit schlechten Verbindungen zurecht: Hängende
Downloads blockieren nicht mehr ewig, es wird mit mehr Abstand erneut versucht,
und bereits heruntergeladene Daten bleiben erhalten. Ein fehlgeschlagener
Versuch blockiert außerdem nicht mehr alle späteren Updateprüfungen.

## Bluetooth

Bluetooth reagiert schneller und die Kopplung mit einem Handy geht zügiger und
zuverlässiger. Doppelte Kopplungsabfragen und veraltete Benachrichtigungen
wurden behoben. Auch der Updateweg über BLE erholt sich besser von abgebrochenen
oder hängenden Übertragungen, sodass ein neuer Versuch ohne Neustart möglich
ist.

Im Menü können jetzt auch sämtliche verbundenen Bluetooth-Geräte gelöscht
werden. Das ist vor allem für Roller interessant, die z.B. gebraucht gekauft
wurden, kann aber auch bei manchen Fehlerbildern hilfreich sein.

## Alarmanlage

Bei scharfgeschalteter Alarmanlage zählen jetzt auch Bremshebel, Hupe und
Sitzbanktaste als Manipulation. Auslöser und Zeitpunkt eines Alarms werden für
die spätere Diagnose festgehalten. Auch das Lenkerschloss und die Lenkerposition
können als Auslöser konfiguriert werden. Natürlich ist das alles konfigurierbar.

## Stabilitätsverbesserungen und Fehlerbehebungen

An vielen Stellen werden Fehler jetzt genauer erkannt und protokolliert. Dazu
gehören Probleme beim Einschalten von Motor, Tacho und Rekuperation, fehlerhafte
oder abgebrochene Wiederherstellungen des Fahrzeugzustands, sowie Fehler bei
Bluetooth-Initialisierung und -Updates. Diese Fehler tauchen jetzt auch im
Fehlerspeicher auf.

Schließlich wurden einige kleine Fehler behoben und Stabilitätsverbesserungen
vorgenommen, die Services robuster gemacht, und die Kommunikation zwischen
Komponenten stabiler gemacht. Die Geschwindigkeitsanzeige erscheint
zuverlässiger, Fehler E20 tritt seltener auf und nur bei echten Problemen. Der
Kilometerstand wird außerdem auch über den Tiefschlaf hinweg gespeichert und
wiederhergestellt.

Die [vollständigen Release Notes](https://github.com/librescoot/librescoot/releases/tag/v1.3.0)
enthalten die komplette Liste der Änderungen.

Roller auf dem Kanal **stable** erhalten Librescoot 1.3 automatisch.

- [Downloads](https://downloads.librescoot.org/)
- [v1.3.0 auf GitHub](https://github.com/librescoot/librescoot/releases/tag/v1.3.0)
- [Discord](https://discord.gg/BmY2P2T9j3)
