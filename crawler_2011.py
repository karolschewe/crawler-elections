import pandas as pd
from time import sleep
import requests


def crawl_2011(teryt_code_list: pd.DataFrame):
    '''

    :param teryt_code_list: dataframe containing teryt code list (look example teryt file in repository)
    :return: tuple of dataframes containing:
    sejm_df - sejm 2011 elections outcome
    turnout_df - 2011 elections turnout
    senat_df - 2011 senat elections outcome
    '''



    year = 2011
    sejm_list = []
    turnout_list = []
    senat_list = []

    for ind, code in teryt_code_list.iterrows():
        teryt = code['TERYT']
        teryt_to_url = teryt[0:2] + '0000'
        powiat = code['Powiat']

        url = r'https://wybory2011.pkw.gov.pl/wyn/' + teryt_to_url + r'/pl/' + teryt + r'.html'
        for i in range(3):
            try:
                site = requests.get(url, timeout=5)
                break
            except requests.exceptions.ConnectTimeout:
                print("timeout error")
                sleep(5)

        try:
            tables = pd.read_html(site.content)
        except ValueError:
            print("nie ma takiej gminy")
            continue
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
    return sejm_df, turnout_df, senat_df








