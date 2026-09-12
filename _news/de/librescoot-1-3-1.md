---
lang: de
title: "Librescoot 1.3.1 „Guten Morgen“: Zuverlässiges Aufwachen und schnelleres Display"
date: 2026-09-07
permalink: /news/librescoot-1-3-1/
summary: "Zeitgesteuertes Aufwachen aus der Hibernation funktioniert wieder zuverlässig. Dazu kommen ein schnellerer Displaystart ohne weißes Aufblitzen, mehr Akkuinformationen, neue Anzeigeoptionen und robustere Updates."
image: /images/news/librescoot-1-3-1.png
image_alt: "Librescoot-Schriftzug, v1.3.1 und der Codename Guten Morgen über einem Wecker"
---

**Librescoot 1.3.1 „Guten Morgen“ ist da!** Dieses Wartungsrelease behebt einen
Fehler beim zeitgesteuerten Aufwachen aus der Hibernation. Außerdem startet
der Tacho schneller und zeigt Fahrzeugdaten früher an; Updates und Verbindungen
sind robuster.

Die [Ankündigung zu Librescoot 1.3](/news/librescoot-1-3/) beschreibt die mit
Version 1.3.0 eingeführten Änderungen.

## Zuverlässig aus der Hibernation aufwachen

Das zeitgesteuerte Aufwachen aus der Hibernation funktioniert wieder
zuverlässig. Ein Fehler in 1.3.0 konnte verhindern, dass der Roller nach einer
festgelegten Dauer oder zu einem geplanten Zeitpunkt von selbst aufwacht. Das
ist in 1.3.1 behoben.

Wird ein Wechsel in Suspend abgebrochen, schaltet sich nun auch das Modem
wieder ein. Der Roller bleibt danach nicht mehr versehentlich offline.

## Schnelleres und informativeres Display

Das Display startet schneller und zeigt die Fahrzeugdaten früher an. Beim
Ein- und Ausschalten bleibt das kurze weiße Aufblitzen aus, das in 1.3.0 zu
sehen war. Auch die Suche nach Hausnummern ist deutlich schneller geworden,
und Navigationshinweise nutzen die verfügbare Bildschirmbreite besser aus.

Die Akku-Infoseiten zeigen nun die Kapazität des Fahrakkus an und weisen auf
einen niedrigen Ladestand hin. Für die Anzeige der aktuell befahrenen Straße
lässt sich wählen, ob sie immer, nur in der Kartenansicht, nur während der
Navigation oder gar nicht erscheint. Für das Tempolimit gibt es dieselben
Optionen. Es kann zusätzlich als reine Warnung erscheinen, sobald der Roller
das angezeigte Limit überschreitet. Die Tachometerskala und ihre Warnschwellen
lassen sich über `settings.toml` oder `lsc` anpassen.

## Robustere Updates und USB-Wartung

Der Versuch, eine bereits installierte Version per Online- oder
Bluetooth-Update erneut einzuspielen, wird jetzt gleich zu Beginn abgelehnt –
statt erst nach der vollständigen Übertragung und einem ganzen
Installationslauf. Solange der Roller im Update-Modus als USB-Speicher
bereitsteht, bleibt die Alarmanlage aus. Reparierbare Dateisystemfehler behebt
der Update-Modus nun selbst. Nach dem Verlassen des Update-Modus steht die
USB-Netzwerkverbindung wieder zuverlässig zur Verfügung.

## Verbindungen und Diagnose

GPS-Start, Wechsel der SIM-Karte und SMS-Verarbeitung kommen nun besser mit
Fehlern und Zustandswechseln zurecht. WireGuard versucht den
Verbindungsaufbau erneut, wenn die Aktivierung beim Start fehlschlägt. Auch die
interne Verbindung zwischen Hauptrechner und Display bleibt unter hoher Last
stabiler.

Für die Arbeit auf der Kommandozeile zeigt `lsc` jetzt zusätzlich Kapazität,
Fehlercode und niedrigen Ladestand des Fahrakkus an.

Online-Roller auf dem Kanal **stable** erhalten Librescoot 1.3.1 automatisch.

- [Downloads](https://downloads.librescoot.org/)
- [Vollständige Release Notes zu Librescoot v1.3.1](https://github.com/librescoot/librescoot/releases/tag/v1.3.1)
- [Discord](https://discord.gg/BmY2P2T9j3)
