# Automātiskās e-pastu izsūtīšanas sistēmas projekts

## Projekta uzdevums

Šī Python projekta mērķis ir automatizēt e-pastu izsūtīšanu, izmantojot iepriekš sagatavotu e-pastu sarakstu un e-pasta saturu. Projekts nodrošina:

- e-pasta adresātu pārvaldību, izmantojot Excel tabulas (`.xlsx` formātā);
- e-pasta satura ievadi no `content/` mapes;
- e-pasta izsūtīšanu, izmantojot tīmekļa pārlūkprogrammu ar Selenium;
- statusa atzīmēšanu Excel failā par to, kuriem adresātiem e-pasts jau ir nosūtīts;
- iespēju pārvaldīt e-pasta sarakstu kā paša definētu datu struktūru – saistīto sarakstu (`LinkedList`).

## Izmantotās Python bibliotēkas un to pielietojums

Projektā tiek izmantotas šādas bibliotēkas:

- **`os`** – failu un direktoriju pārbaude, ceļu apstrāde.
- **`openpyxl`** – darbam ar Excel `.xlsx` failiem: datu lasīšana, rakstīšana un atjaunošana.
- **`datetime`** – datuma pievienošanai pie nosūtītiem e-pastiem.
- **`selenium`** – automatizēta darbība tīmekļa pārlūkprogrammā.
- **`time`** – paužu ievietošana starp darbībām pārlūkā, lai nodrošinātu stabilu darbību.
- **`LinkedList` (pašdefinēta klase)** – e-pasta adresātu saraksta strukturēta glabāšana un apstrāde, nodrošinot iterāciju un manipulācijas ar datiem.
- **`re`** - nodrošina iespēju pārbaudīt, meklēt un apstrādāt teksta virknes pēc noteiktiem rakstu paraugiem.

## Izmantotās datu struktūras

Projektā izmantota paša izveidota saistītā saraksta (linked list) struktūra.
Šīs struktūras izmantošana ļauj efektīvi veikt darbības ar adresātu sarakstu, piemēram, pievienošanu, iterēšanu un pārbaudīšanu.

## Programmatūras izmantošana un metpdes

Lietotājs var darbināt galveno `main.py` failu, kurš sniegs komandrindas tipa saskarni ar šādiem ievades variantiem (komandām):

### Komandas

1. **`print_file`**  
   Izdrukā e-pasta adreses no teksta faila mapē `address_lists/`.  
   - Prasa faila nosaukumu.  
   - Iegūstama pārskatāma adresātu saraksta izdruka.

2. **`update_excel`**  
   Atjauno `excel/mails.xlsx` failu, ielasot jaunas e-pasta adreses no faila `address_lists/`.  
   - Jaunie adresāti tiks pievienoti tikai tad, ja tie jau neeksistē.

3. **`send_email`**  
   Izsūta e-pastus, izmantojot `inbox.lv` kontu.  
   - Prasa faila nosaukumu no mapes `content/`, kas satur e-pasta tekstu.  
   - Pēc veiksmīgas nosūtīšanas adresāti tiek atzīmēti Excel failā ar sūtīšanas datumu.

4. **`exit`**  
   Izeja no programmas.

### Papildu funkcionalitāte

- Sūtīšanas laikā tiek automātiski pieslēgts `inbox.lv` konts un simulēta visu lauku aizpildīšana, tostarp adresāts, tēma, saturs un sūtīšanas klikšķis.
- Programma pārliecinās, ka netiek sūtīts atkārtoti uz adresēm, kurām jau ir norādīts sūtīšanas datums.
### Piezīmes

- e-pastu saraksta failā kas atrodas mapē `address_lists/`, nepieciešamais formāts: katra e-pasta adrese savā rindā, pretēji tiks izvadīts kļūdu ziņojums.
- Mapē `content/` tiek glabāti e-pasta satura faili, katra faila nosaukums attiecīgi ir sūtāmā e-pasta temats, bet faila saturs ir e-pasta teksts.

## Sistēmas prasības

- Python 3.8+
- Google Chrome pārlūkprogramma
- ChromeDriver atbilstošs jūsu pārlūka versijai
- Instalētas šādas Python bibliotēkas:
  ```bash
  pip install openpyxl selenium
  ```
