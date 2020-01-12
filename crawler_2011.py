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


year = 2011
sejm_list = []
turnout_list = []
senat_list = []

for ind, code in teryt_code_list.iterrows():
    teryt = code['TERYT']
    teryt_to_url = teryt[0:2] + '0000'
    powiat = code['Powiat']

    url = r'https://wybory2011.pkw.gov.pl/wyn/' + teryt_to_url + r'/pl/' + teryt + r'.html'
    tables = pd.read_html(url)  # Returns list of all tables on page
    n_tables = len(tables)
    gmina_name = tables[0][0][0]

    # pierwsza tabelka -  wybory do sejmu
    for lista in range(2, n_tables - 2):
        political_party = tables[lista].iloc[0, 0]
        n_of_votes = tables[lista].iloc[-1, 2]
        votes_percentage = tables[lista].iloc[-1, 3][:-1]
        df_row = {
            'year': year,
            'elections': "sejm",
            'teryt_code': teryt,
            'powiat': powiat,
            'gmina': gmina_name,
            'political_party': political_party,
            'n_votes': n_of_votes,
            'percentage': votes_percentage
        }
        sejm_list.append(df_row)

    # druga tabelka - frekwencja

    turnout_row = {
        'year': year,
        'teryt_code': teryt,
        'powiat': powiat,
        'gmina': gmina_name,
        'population': tables[0][1][2],
        'eligible_to_vote': tables[0][1][5],
        'turnout_%': tables[1].iloc[-1, 6][:-1],
        'turnout_ppl': tables[1].iloc[-1, 7]
    }
    turnout_list.append(turnout_row)

    # trzecia tabelka - senat

    for index, candidate in tables[-1][2:].iterrows():
        candidate_names_list = candidate[1].split()
        candidate_surname = candidate_names_list[0]
        candidate_names = ' '.join(candidate_names_list[1:])
        votes = candidate[2]
        percentage = candidate[3][:-1]
        senat_row = {
            'year': year,
            'elections': "senat",
            'teryt_code': teryt,
            'powiat': powiat,
            'gmina': gmina_name,
            'surname': candidate_surname,
            'names': candidate_names,
            'n_votes': votes,
            'percentage': percentage
        }
        senat_list.append(senat_row)



sejm_df = pd.DataFrame.from_dict(sejm_list)
turnout_df = pd.DataFrame.from_dict(turnout_list)
senat_df = pd.DataFrame.from_dict(senat_list)

sejm_df.to_csv("wybory_do_sejmu_2011_po_gminach_wyniki.csv", index=False)
turnout_df.to_csv("frekwencja_wybory_2011_po_gminach.csv", index=False)
senat_df.to_csv("wybory_do_senatu_2011_po_gminach_wyniki.csv", index=False)

