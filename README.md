# **Analiza Filmov z Spletne Strani TheMovieDB**

## **Opis**
V tej projektni nalogi se osredotočamo na pridobivanje podatkov iz spletne strani [TheMovieDB](https://www.themoviedb.org/) z uporabo knjižnic `BeautifulSoup 4.8.0` in `Selenium`. Zbrane podatke bomo uporabili za analizo različnih hipotez, povezanih s filmi.

## **Zbrane Lastnosti Filmov:**
- Dolžina filma
- Naslov filma
- Ocena filma
- Budget filma
- Revenue filma
- Žanr filma
- Datum izdaje filma

## **Hipoteze:**
1. Kakšena je korelacija med žanrom filma in oceno?
2. Ali obstaja povezava med dolžino filma in oceno filma?
3. Ali obstaja povezava med budgetom in revenuem filma?
4. Ali obstaja povezava med mesecom izdaje filma in oceno filma?

## **Navodila za Uporabo:**
Potrebni moduli: 
- `Beautifulsoup4` 
- Selenium 
- Python
- Pandas
- numpy
- scipy
- matplotlib
- pip install pandas

  
Te naložimo tako, da v CMD ali Vscode terminal vpišemo naslednje ukaze:
- pip install numpy
- pip install scipy
- pip install matplotlib
- pip install selenium
- pip install beautifulsoup4

  
V scrape.py je potrebno spremeniti lokacijo chromedrivera, število želenih niti in število strani za obdelavo (1 stran ~ 20 filmov)
Za pridobitev podatkov zaženemo scrape.py, ki zgenerira datoteko movies.csv.
Nato zaženemo analyse.py, ki nam izpiše korelacije za hipoteze 1 do 4.

## **Rezultati Hipotez:**


H1: Korelacija med žanrom in oceno: 

1.35, P-value: 0.1476


Ni statistično pomembne korelacije med žanrom in oceno.


H2: Korelacija med dožino filma in oceno: 

0.11, P-value: 0.0002


Je statistično pomembna korelacija med dolžino in oceno.


H3: Korelacija med proračunom in prihodkom: 

0.77, P-value: 0.0000


Je statistično pomembna korelacija med proračunom in prihodkom.


H4: Korelacija med mesecem izdaje in oceno filma: 0.02, P-value: 0.5120


Ni statistično pomembne korelacije med mesecem izdaje in oceno filma.


   

## **Viri:**
- [TheMovieDB](https://www.themoviedb.org/)

## **Avtor:**
Nino Djordjević
