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


H4: Korelacija med mesecem izdaje in oceno filma: 


0.02, P-value: 0.5120


Ni statistično pomembne korelacije med mesecem izdaje in oceno filma.
![BudRev](https://github.com/Ninodj123/prog1-projektna/assets/109914375/7d0208bf-a49b-4ecb-a127-7d885861f898)


![DolzinaOcena](https://github.com/Ninodj123/prog1-projektna/assets/109914375/f8e37734-d5f3-4fa4-9ea0-1eb05db37773)


![ZanrOcena](https://github.com/Ninodj123/prog1-projektna/assets/109914375/d924a98b-2d0d-44f8-a6c1-27d6f5467a96)


![MesecOcena](https://github.com/Ninodj123/prog1-projektna/assets/109914375/f6633258-a1f6-46db-b8d1-455898a05844)

## **Viri:**

- [TheMovieDB](https://www.themoviedb.org/)

- Uporaba Chatgtp pri izdelavi kode.

## **Avtor:**
Nino Djordjević
