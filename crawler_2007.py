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
# -- nie przyda mi sie to wiec na razie
sejm_list = []
teryt = teryt_code_list['TERYT'][0]
powiat = teryt_code_list['Powiat'][0]
gmina_name = teryt_code_list['Gmina'][0]
url = "https://wybory2007.pkw.gov.pl/SJM/PL/WYN/W/" + teryt + ".htm"
print(url)

url_data = pd.read_html(url)

# for table in test:
#     print(table.to_string())

# w tabelce z indeksem 5 sa wyniki glosowania na listy -- rozna liczba list -- trzeba bedzie iterowac od zerowego wiersza az uzyskamy symbol sumy
# w tabelce z indeksem cztery - frekwencja
print(url_data[5].to_string())
for index, row in url_data[5].iterrows():
    if row[0] != 'Σ':
        df_row = {
            'year': year,
            'elections': "sejm",
            'teryt_code': teryt,
            'powiat': powiat,
            'gmina': gmina_name,
            'political_party': row[3],
            'n_votes': row[4],
            'percentage': row[5]
        }
        sejm_list.append(df_row)

print(sejm_list)
print(pd.DataFrame.from_dict(sejm_list).to_string())
