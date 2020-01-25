import pandas as pd
from time import sleep
import requests
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

turnout_list = []



# WYBORY DO SENATU W TEJ ORDYNACJI WYBORCZEJ POZWALAŁY NA ODDANIE GŁOSU NA DOWOLNĄ LICZBĘ KANDYDATÓW
# -- nie przyda mi sie to wiec na razie
sejm_list = []
for ind, code in teryt_code_list.iterrows():
    teryt = code['TERYT']
    powiat = code['Powiat']
    gmina_name = code['Gmina']
    url = "https://wybory2007.pkw.gov.pl/SJM/PL/WYN/W/" + teryt + ".htm"
    print(url)



    # for table in test:
    #     print(table.to_string())

    # w tabelce z indeksem 5 sa wyniki glosowania na listy -- rozna liczba list -- trzeba bedzie iterowac od zerowego wiersza az uzyskamy symbol sumy
    # w tabelce z indeksem cztery - frekwencja

    for index, row in url_data[5].iterrows():
        if row[0] == 'Σ':
            break
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

    turnout_row = {
        'year': year,
        'teryt_code': teryt,
        'powiat': powiat,
        'gmina': gmina_name,
        'population': url_data[4][1][2],
        'eligible_to_vote': url_data[4][1][6].replace('\xa0', ''),
        'turnout_%': url_data[4][1][12][:-1],
        'turnout_ppl': url_data[4][1][8].replace('\xa0', '')
    }
    turnout_list.append(turnout_row)











sejm_df = pd.DataFrame.from_dict(sejm_list)
turnout_df = pd.DataFrame.from_dict(turnout_list)



sejm_df.to_csv("wybory_do_sejmu_2007_po_gminach_wyniki.csv", index=False, encoding='utf-8-sig')
turnout_df.to_csv("frekwencja_wybory_2007_po_gminach.csv", index=False, encoding='utf-8-sig')

