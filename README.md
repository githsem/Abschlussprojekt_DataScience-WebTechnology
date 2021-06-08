# Abschlussprojekt_DataScience-WebTechnology

Hannover Hochschule Refugeeks IT Data Science und Web Technologien Abschluss Projekt

### Prozess 1: Web Scraping

Aufgabe: Beziehen von Rezensionen von den Seiten Klinikbewertungen.de & Google Maps
Umfang: Rezensionen von mindestens 15 Kliniken beziehen (Liste der verfügbaren Kliniken auf Moodle, Dokument: Klinikliste)
Rahmen Google: 
-	Pflicht: Name der Klinik, Textuelle Bewertung, Sternebewertung, Datum der Bewertung, Likes
-	Optional: Antwort, Datum der Antwort, Nutzerinformationen (Local Guide, Rezensionsanzahl)
-	Nicht: Nutzername  Bezug möglich, aber nicht auf Webseite anzeigen
Rahmen Klinikbewertungen:
-	Pflicht: Name der Klinik, Titel, Datum der Bewertung, Fachbereich, Sternebewertung (Gesamtzufriedenheit, Qualität der Beratung, Mediz. Behandlung, Verwaltung und Abläufe, Ausstattung und Gestaltung), Erfahrungsbericht
-	Optional: Behandlungsjahr, Berichtender, Daumen hoch/runter, Textuelle Sternebewertungen, Pro, Kontra, Krankheitsbild, Privatpatient, Kommentare
-	Nicht: Nutzername  Bezug möglich, aber nicht auf Webseite anzeigen
-	Hinweis: Bei Klinikbewertungen gibt es Bewertungen, die nicht in die Gesamtbewertungen mit einfließen (auf der Webseite und innerhalb des HTML-Dokumentes gekennzeichnet). Entscheidet selbst, ob ihr diese Bewertungen mit einbeziehen wollt
Ziel: Zwei Dateien mit den jeweiligen Bewertungen von Google Maps & Klinikbewertungen zur Weiterverarbeitung


Prozess 2: Data Science/ Machine Learning
Aufgabe: Bezogene & bereinigte Daten mittels einer Machine Learning Methode verarbeiten
Umfang: Mindestens eine Methode auf mindestens einen Datensatz (Google oder Klinikbewertungen) anwenden
Das Modell muss selbst erstellt werden, das Verwenden einer Bibliothek wie TextBlob ist zusätzlich möglich, ist aber als ML-Modell nicht ausreichend
Google Maps & Klinikbewertung:
•	Stimmt die gegebene Sternebewertung mit der Textbewertung überein?
o	Mittels Sentimentsanalyse Stimmung ermitteln
o	Mittels Klassifikation oder Regression genaue Sterne ermitteln
•	Sentimentsanalyse der Bewertungstexte
•	Allgemeiner Score für die Klinik ermitteln
Klinikbewertung:
•	Korrelation der Teilsternebewertungen & der Gesamtsternbewertung
Ziel: Eine funktionierende Machine Learning Methode, auf die die bezogene Daten angewendet werden können 

Prozess 3: Web Technology
Aufgabe: Webseite/Webapp erstellen, um bezogene Daten und Ergebnisse des Machine Learnings darzustellen 
Umfang: Interaktivität in der Webanwendung muss gegeben sein (beispielsweise Filtermöglichkeiten)
Rahmen: Eine Website pro Gruppe auf den bei der HTML/CSS-Veranstaltung verwendeten WebSpaces
Ziel: Frei gestaltete Website, auf denen alle Daten übersichtlich abgebildet sind

Mögliche Herausforderungen (falls Zeit übrig ist):
-	Mittels Flask Machine Learning Model in die Website einbinden
-	ML-Modell auf beide Webseiten anwenden, Ergebnisse vergleichen & einordnen
-	Beziehen von Rezensionen von Facebook




Mögliche Kunden
Kunde 1 – Krankenhausbesucher
Anliegen des Kunden:
Dieser Kunde möchte sich über die Krankenhäuser in Niedersachen informieren. Der Kunde kennt keine Krankenhäuser, er möchte ein allgemeiner Überblick über alle Krankenhäuser gewinnen.
Fragen:
•	Welche Krankenhäuser gibt es?
•	Ggf. Wo sind diese Krankenhäuser genau?
•	Wie sind die Krankenhäuser allgemein bewertet?
•	Was sind die Faktoren, die in die Bewertung einfließen? 
•	Kann ich ein Meinungsbild über die einzelnen Krankenhäuser erkennen?

Kunde 2 – Qualitätsmanager
Anliegen des Kunden:
Dieser Kunde kennt die Krankenhäuser bereits und möchte die Bewertungen genauer analysieren. Er möchte einzelne Krankenhäuser genauer analysieren.
Fragen:
•	Kann ich die Krankenhäuser suchen?
•	Kann ich die einzelnen Bewertungen in sortierter Form abrufen?
•	Kann ich die Unterschiede der Bewertungen erkennen? 
•	Gibt es bestimmte Wörter, die auf eine negative oder positive Bewertung schließen lassen?
•	Kann ich Faktoren der Bewertungen analysieren? 

![image](https://user-images.githubusercontent.com/57366322/121185325-3bc64100-c866-11eb-9ad8-6a4106ff741b.png)
