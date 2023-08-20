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
-Beautifulsoup4
-Selenium
-Python
-Pandas
-numpy
-scipy
V scrape.py je potrebno spremeniti lokacijo chromedrivera, število želenih niti in število strani za obdelavo (1 stran ~ 20 filmov)
Za pridobitev podatkov zaženemo scrape.py, ki zgenerira datoteko movies.csv.
Nato zaženemo analyse.py, ki nam izpiše korelacije za hipoteze 1 do 4.

## **Rezultati Hipotez:**
1. Kateri žanri filmov so najboljše ocenjeni?
  
2. Ali obstaja povezava med dolžino filma in oceno filma?
    Correlation between Duration and Score: 0.25, P-value: 0.0000
3. Ali obstaja povezava med budgetom in revenuem filma?
   Correlation between Budget and Revenue: 0.73, P-value: 0.0000
4. Ali obstaja povezava med mesecom izdaje filma in oceno filma?
   

## **Viri:**
- [TheMovieDB](https://www.themoviedb.org/)

## **Avtor:**
Nino Djordjević
