---
lang: de
title: 'Librescoot 1.4.0 "Spätsommer"'
permalink: /news/librescoot-1-4/
date: 2026-11-01
published: true
summary: "Mehrstopp-Routen mit Übersicht und Fortsetzung nach einer Pause, eine Uhr, die durch die Hibernation weiterläuft, und ein vielseitigerer Tacho. Dazu kommen Android-Smartphone-Schlüssel mit Librescoot Mobile und ein Fahrtenbuch."
icon: map
image: /images/news/librescoot-1-4.png
image_in_post: false
image_alt: "Librescoot-Schriftzug, v1.4.0 und der Codename Spätsommer neben einer Sonne"
---

Librescoot 1.4.0 "Spätsommer" erweitert die Navigation um Routen mit mehreren Stopps, eine Übersicht über die ganze Tour und die Fortsetzung nach einer Pause. Die Uhr läuft während der Hibernation weiter, das Schnellmenü bekommt mehr Möglichkeiten und der Tacho einheitliche Meldungen, anpassbare Farben und fließende Übergänge. Mit der Librescoot Mobile App kann außerdem ein Android-Smartphone als Schlüssel dienen; ein Fahrtenbuch hält die gefahrenen Strecken fest.

## Routen für die ganze Tour

{% include news-screenshot.html src="/images/news/librescoot-1-4-route-de.png" align="right" alt="Navigationskarte mit drei Zwischenstopps in der Berliner Innenstadt" caption='Routenübersicht mit drei Zwischenstopps und Beispieldaten. Kartendaten © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap-Mitwirkende</a>.' %}

Eine Route kann mehrere Stopps enthalten. Unterwegs lassen sich weitere Ziele ergänzen, die Reihenfolge ändern oder einzelne Stopps überspringen. Die Routenübersicht zeigt die verbleibende Strecke und die kommenden Ziele. Nach Standby oder einem Neustart lässt sich die Tour fortsetzen, ohne alles erneut einzugeben.

Auch die Wiederaufnahme der Navigation ist robuster: Sind GPS oder Routenberechnung beim Start noch nicht bereit, wird die Berechnung erneut versucht, sobald sie verfügbar sind. Ist die Position noch zu ungenau, erklärt eine Meldung die Wartezeit; eine bereits nutzbare Karte bleibt sichtbar.

Häufige Ziele wie Zuhause oder Arbeit, die Routenübersicht und das Überspringen eines Stopps lassen sich ins Schnellmenü aufnehmen. Die wichtigsten Navigationsaktionen sind damit unterwegs direkt erreichbar.

Mehrere Offline-Kartenregionen können gleichzeitig auf dem Roller liegen. Nach einmaliger Einrichtung wählt der Tacho anhand der Position die passende Region. Installation und Aktualisierung erfolgen per USB; Routen über die Grenzen getrennter Regionen sind nicht möglich. Die Karteninformationen sind auf Deutsch und Englisch übersetzt und brechen lange Werte um.

## Die Uhr läuft weiter

Nach dem Aufwachen aus der Hibernation stimmt die Uhrzeit, ohne erst auf GPS zu warten. Die Uhr läuft während des Schlafens weiter. Nach vollständigem Stromverlust, einschließlich der internen Akkus, muss sie neu synchronisiert werden, zum Beispiel über GPS oder Internet.

Hibernation lässt sich direkt aus dem Parkmodus starten. Hibernate for funktioniert auch ohne gestellte Uhr; ein Zeitplan benötigt eine gültige Uhrzeit. Nach einem Alarm kann der Roller wieder einschlafen.

## Mehr Möglichkeiten am Tacho

{% include news-screenshot.html src="/images/news/librescoot-1-4-quick-de.png" align="right" alt="Schnellmenü am Tacho mit ausgewählter Kartenansicht" caption="Das Schnellmenü lässt sich mit häufig genutzten Aktionen belegen." %}

Die Einträge und die Reihenfolge des Schnellmenüs lassen sich selbst zusammenstellen. Neben den Navigationsfunktionen können dort die anderen häufig genutzten Aktionen liegen. Farben von Tacho, Leistungs- und Rekuperationsanzeige sowie Kartenstile sind ebenfalls anpassbar.

Die Startanimation geht fließend in den Tacho über; Startlogo und Animation sind wählbar. Das automatische helle oder dunkle Farbschema berücksichtigt bereits beim Start das Umgebungslicht. Die automatische Helligkeit nutzt einen größeren Regelbereich, auch die festen Helligkeitsstufen wurden neu abgestimmt.

Warnungen, Navigationshinweise und andere Benachrichtigungen verwenden eine gemeinsame Darstellung. Mehrere Meldungen wechseln sich ab, lange Texte scrollen. Wichtige Hinweise bleiben auch bei Verbindungsproblemen und während eines Updates sichtbar. Warnungen bei niedrigem Fahrakkustand oder Ladeproblemen der internen Akkus ergänzen die Ladeinformationen im Info-Menü.

Für Roller mit angeschlossenem Verstärker gibt es außerdem neue Töne für Blinker, Navigation, Meldungen und Fahrzeugaktionen. Bei den meisten Rollern ist der Verstärker nicht angeschlossen; dort sind diese Töne nicht hörbar.

## Das Android-Smartphone als Schlüssel

Mit der Librescoot Mobile App lässt sich ein kompatibles Android-Smartphone als NFC-Schlüssel einrichten und am Roller anlernen. Das entsperrte Telefon funktioniert am Leser anschließend wie eine Schlüsselkarte zum Sperren und Entsperren.

Karten und Smartphones lassen sich direkt am Tacho hinzufügen und entfernen. Namen aus der App erscheinen auch dort, ebenso eine Markierung der zuletzt verwendeten Karte. Vor dem Löschen der letzten Entsperrmöglichkeit erscheint eine Rückfrage.

Auf Wunsch öffnet sich die Sitzbank beim Entsperren automatisch, auch mit einer Schlüsselkarte. Die Option ist standardmäßig ausgeschaltet. Die Alarmanlage wartet vor ihrer ersten Warnung kurz, damit eine aufgelegte Karte oder ein Smartphone noch erkannt werden kann.

## Fahrtenbuch und Verbrauchsübersicht

{% include news-screenshot.html src="/images/news/librescoot-1-4-trip-de.png" align="right" alt="Fahrtdetails mit Beispieldaten und aufgezeichneter Strecke" caption='Fahrtdetails mit Beispieldaten. Start- und Endmarkierung sind ab Dashboard 1.24.1 verfügbar. Kartendaten © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap-Mitwirkende</a>.' %}

Das Fahrtenbuch speichert Strecke, Dauer und GPS-Verlauf auf dem Roller. Unter Fahrtenverlauf lassen sich abgeschlossene Fahrten mit Strecke, Fahrzeit und Durchschnittsgeschwindigkeit direkt am Tacho ansehen. Aufgezeichnete GPS-Spuren können auf der Karte angezeigt werden. Die Aufbewahrung lässt sich nach Alter, Fahrtenzahl oder Speichergröße begrenzen; die automatische Löschung kann auch ausgeschaltet werden. Kurze Strecken unter 100 Metern laut Kilometerzähler werden nicht als abgeschlossene Fahrt gespeichert.

Auch der Tageskilometerzähler bleibt beim Ausschalten erhalten und zählt unabhängig vom Fahrtenbuch. Das Zurücksetzen ist konfigurierbar: nach jeder Fahrt, täglich, beim Akkuwechsel oder nur von Hand.

{% include news-screenshot.html src="/images/news/librescoot-1-4-energy-de.png" align="right" alt="Verbrauchsübersicht am Tacho mit Beispielwerten für Fahrbereitschaft, Parkmodus und Standby" caption="Geschätzter Verbrauch nach Betriebsphasen mit Beispielwerten." %}

Die neue Verbrauchsseite am Tacho schätzt die aus den Fahrakkus entnommene Nettoenergie aus Änderungen ihrer Restkapazität. Sie ordnet die Werte nach Fahrbereitschaft, Parkmodus und Standby. So wird auch der Energiebedarf außerhalb einer Fahrt sichtbar. Die Aufteilung ist eine Schätzung nach Betriebsphasen, keine genaue Bilanz einzelner Verbraucher; Erfassungsbeginn und Unterbrechungen bleiben erkennbar.

Getrennt davon zeigen Tacho und Web-Oberfläche die aus Motorcontroller-Daten geschätzte verbrauchte und durch Rekuperation zurückgewonnene Energie in kWh.

## Nachrichten und mehr Möglichkeiten für Apps

{% include news-screenshot.html src="/images/news/librescoot-1-4-sms-de.png" align="right" alt="SMS-Nachricht mit einem beispielhaften Tarifhinweis" caption="SMS direkt am Tacho lesen. Absender und Nachricht sind Beispiele." %}

Tarifhinweise oder Datenvolumenwarnungen des Mobilfunkanbieters landen oft per SMS auf der Roller-SIM. Diese Nachrichten lassen sich jetzt im Parkmodus am Tacho oder mit kompatiblen Apps lesen und löschen. Unter Info > SMS zeigt die Liste Absender und Textvorschau; Nachrichten lassen sich direkt öffnen und als Klartext lesen. Beim Löschen ist zunächst Abbrechen ausgewählt. Das Postfach bleibt über Neustarts erhalten. Neue Nachrichten können optional im Heimatnetz weitergeleitet werden; die Nummer wird in den erweiterten Einstellungen der Web-Oberfläche eingetragen. Am Tacho lassen sich das Ziel ansehen und die Weiterleitung ausschalten. Die Funktion ist standardmäßig aus und kann Tarifkosten verursachen. Bei Multi-SIM hängt es vom Tarif ab, ob SMS am Roller oder an einem anderen Gerät ankommen.

Passende Apps können außerdem Dateien per Bluetooth übertragen, Diagnoseprotokolle herunterladen und unterbrochene Übertragungen fortsetzen. Sie können das Display und den Servicemodus bedienen, den Tageskilometerzähler zurücksetzen und Mehrstopp-Routen bearbeiten. Über die Bluetooth-Schnittstelle lässt sich auch die Connect-Kontoverbindung starten, abfragen und anhalten. Außerdem können Apps abgeschlossene Fahrten mit Details und aufgezeichneten GPS-Punkten abrufen. Die jeweilige App muss diese Funktionen unterstützen.

## Web-Oberfläche für Einrichtung und Wartung

Für Arbeiten am Roller gibt es eine neue Web-Oberfläche mit Einstellungen, Schlüsselkarten, Navigation, Fahrzeug- und Akkudaten sowie Updates. Dateien lassen sich übertragen und Diagnoseprotokolle herunterladen.

Ein Zugang führt über den USB-Anschluss im Fußraum. Dafür muss die Fußraumabdeckung abgeschraubt und ein Computer angeschlossen werden. Bei eingeschaltetem (entsperrtem) Roller ist die [Web-Oberfläche](http://192.168.7.1:8090) erreichbar.

{% include news-screenshot.html src="/images/news/librescoot-1-4-connect-de.png" align="right" alt="Connect-Kopplung mit QR-Code und Bestätigung im Browser" caption="Connect-Kopplung am Tacho. Der abgebildete Code ist ein nicht gültiges Beispiel." %}

Ein Cloudkonto, zum Beispiel bei Sunshine, lässt sich mit Connect auch direkt am Tacho verbinden. Das Menü Einstellungen > Cloud erscheint, wenn Internet und die Verbindung zum Hauptrechner verfügbar sind. Unter Konto verbinden startet ein kurzer Druck auf die rechte Bremse die Kopplung. Solange ein gültiger Kurzcode vorliegt, zeigt der Tacho einen QR-Code mit diesem Code. Nach dem Scannen trägt das [Connect-Portal](https://connect.librescoot.org/pair) ihn ein und entfernt ihn aus der Browseradresse. Der Kurzcode kann auch von Hand eingegeben werden. Seine Gültigkeitsdauer ist am Tacho sichtbar. Der Roller muss online sein; der Start ist im Parkmodus oder Standby möglich. Die Kontofreigabe muss im Browser ausdrücklich bestätigt werden. Der Tacho zeigt die Schritte Code, Bestätigung und Abschluss, weist auf längeres Warten hin und meldet einen Verbindungsverlust.

Auch die Cloud-Seite der Web-Oberfläche kann die Kopplung starten und zeigt Code, Gültigkeitsdauer und Status. Das Warten lässt sich dort beenden; eine laufende Konfigurationstransaktion wird dabei zunächst abgeschlossen. Alternativ kann die Sunshine-Anbindung weiterhin mit einem Einrichtungstoken oder Online-Installer-Link aus den [Sunshine-Kontoeinstellungen](https://sunshine.rescoot.org/account/security#bootstrap-tokens) eingerichtet werden.

## Verbesserungen im Alltag

Der Tacho zeigt an, wenn vor dem Losfahren noch auf die Akkuaktivierung gewartet wird. Die Rekuperation wird auch beim unmittelbaren Losfahren nach dem Einschalten korrekt aktiviert. Parkansichten schließen sich beim Fahrbeginn, und die Menübedienung lässt das Bremslicht nicht mehr eingeschaltet hängen. Die Blinkersteuerung verarbeitet Schalter- und Softwarebefehle nacheinander; Änderungen der Uhrzeit beeinflussen den Blinktakt nicht.

Nach einem Akkuwechsel wird der eingesetzte Akku neu geprüft. Ein einzelner Akku kann auch in Fahrbereitschaft aktiviert werden; ein zweiter darf dort nicht zugeschaltet werden, auch nicht im Stillstand. Bereits aktivierte Akkus bleiben beim Wechsel in die Fahrbereitschaft aktiv.

Bei der Alarmanlage beendet "Stoppen" einen laufenden Alarm; nach fünf Minuten wird sie wieder scharf. "Entschärfen" hält sie länger ausgeschaltet: bis zur nächsten Benutzung mit anschließendem Sperren, bis zur Hibernation oder höchstens acht Stunden. Danach wird sie automatisch wieder scharf.

Vor einem Update zeigt die Web-Oberfläche das benötigte Datenvolumen, der Tacho informiert über Fortschritt und Fehler. Nach der Installation wartet der automatische Neustart des Tachos, bis der Roller gesperrt ist (Standby). So startet der Tacho nicht während der Benutzung unerwartet neu. Die Wiederherstellung behandelt System- und Boot-Updates getrennt und hält den Tacho bis zum notwendigen Boot-Neustart aktiv. Ein Neustart des Update-Dienstes allein zählt nicht als Neustart des Tachos. Auch der USB-Update-Modus kommt besser mit Abbrüchen zurecht; gibt es nichts zu installieren, ist kein Neustart nötig.

## Für Entwickler und Enthusiasten

Eigene Skripte können auf Fahrzeugzustände, Tastenbetätigungen, Akkuänderungen oder Alarme reagieren. Die Regeln werden mit [`lsc ext`](https://librescoot.org/docs/dev/lsc.html#event-service-regeln) eingerichtet; standardmäßig sind keine aktiv.

Der Kernel bringt außerdem die [für Tailscale nötige Netzwerkunterstützung](https://librescoot.org/docs/dev/hardware.html#netzwerk-topologie) mit. Der Tailscale-Client ist nicht vorinstalliert. Für die Fehlersuche bündelt `lsc doctor` häufige Probleme; die vollständigen Release Notes führen weitere Diagnose- und Verbindungsverbesserungen auf.

Dieses Release ist [Patrick Stewart](https://de.wikipedia.org/wiki/Patrick_Stewart) gewidmet.

Nachtrag: [Librescoot 1.4.1](https://github.com/librescoot/librescoot/releases/tag/v1.4.1) ergänzt Start- und Endmarkierungen im Fahrtenbuch.

[Librescoot 1.4.2](https://github.com/librescoot/librescoot/releases/tag/v1.4.2) passt die Voreinstellungen der Alarmanlage an: Die Hupe ist standardmäßig eingeschaltet, und nach einer ersten Bewegung oder Tastenbetätigung kann ein weiterer Auslöser den Vollalarm früher starten. Gespeicherte Alarm-Einstellungen bleiben erhalten. Optional zeigt eine rot blinkende LED die scharfgeschaltete Alarmanlage an. Unter Info > Doctor hilft eine neue Diagnose bei der Fehlersuche. Außerdem verbessert das Update die Akkuerkennung, die Fahrtenkarten und den geplanten Winterschlaf.
