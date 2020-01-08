import pandas as pd
import xlrd


teryt_code_list = pd.read_excel('terytki.xls',header=0,converters={'TERYT':str})

teryt = teryt_code_list['TERYT'][0]
teryt_to_url = teryt[0:2] + '0000'
powiat = teryt_code_list['Powiat'][0]



url = r'https://wybory2011.pkw.gov.pl/wyn/' + teryt_to_url + r'/pl/' + teryt + r'.html'
tables = pd.read_html(url) # Returns list of all tables on page
n_tables = len(tables)
gmina_name = tables[0][0][0]
year = 2011
elections_name = "sejm"
sejm_list = []
# pierwsza tabelka -  wybory do sejmu
for lista in range(2,n_tables-2):
    political_party = tables[lista].iloc[0,0]
    n_of_votes = tables[lista].iloc[-1,2]
    votes_percentage = tables[lista].iloc[-1,3][:-1]
    print(political_party)
    print(votes_percentage)
    print(n_of_votes)
    df_row = {
        'year': year,
        'elections': elections_name,
        'teryt_code': teryt,
        'powiat': powiat,
        'gmina': gmina_name,
        'political_party': political_party,
        'n_votes': n_of_votes,
        'percentage': votes_percentage
    }
    print(df_row)
    sejm_list.append(df_row)



# druga tabelka - frekwencja
turnout_list = []
turnout_row = {
    'year': year,
    'elections': elections_name,
    'teryt_code': teryt,
    'powiat': powiat,
    'gmina': gmina_name,
    'population': tables[0][1][2],
    'eligible_to_vote': tables[0][1][5],
    'turnout_%': tables[1].iloc[-1,6][:-1],
    'turnout_ppl': tables[1].iloc[-1,7]
}
turnout_list.append(turnout_row)

# trzecia tabelka - senat
senat_list = []
for index, candidate in tables[-1][2:].iterrows():
    candidate_ = candidate[1].split()[0]
senat_row = {
'year': year,
    'elections': elections_name,
    'teryt_code': teryt,
    'powiat': powiat,
    'gmina': gmina_name
}
# print(tables[-1].to_string())
