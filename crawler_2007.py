import pandas as pd
'''
Do uruchomienia tego programu potrzebny jest plik z lista kodów TERYT gmin, o których zamierzamy zebrać informacje.
Program korzysta z bibliotek:
- pandas
- urllib3
- html5lib
Repozytorium zawiera plik requirements.txt za pomocą którego w prosty sposób można zainstalować wszystkie wymagane pakiety.
Aby to uczynić należy wykonać komendę pip install: –r requirements.txt
Do programu nie wymagany jest dodatkowy input.
Program zapisuje wyniki wyborów do sejmu, senatu oraz frekwencję na poziomie gminy do trzech odrębnych plików csv.

'''


teryt_code_list = pd.read_excel('terytki.xls',header=0,converters={'TERYT':str})
year = 2007
sejm_list = []
turnout_list = []

# WYBORY DO SENATU W TEJ ORDYNACJI WYBORCZEJ POZWALAŁY NA ODDANIE GŁOSU NA DOWOLNĄ LICZBĘ KANDYDATÓW
# -- PROSZĘ SIE NIE DZIWIĆ ŻE NIE SUMUJE SIĘ DO 100%
senat_list = []
teryt = teryt_code_list['TERYT'][1020]
url = "https://wybory2007.pkw.gov.pl/SJM/PL/WYN/W/" + teryt + ".htm"

test = pd.read_html(url)

# for table in test:
#     print(table.to_string())

# w tabelce z indeksem 5 sa wyniki glosowania na listy -- rozna liczba list -- trzeba bedzie iterowac od zerowego wiersza az uzyskamy symbol sumy
# w tabelce z indeksem cztery - frekwencja
print(test[5].to_string())

