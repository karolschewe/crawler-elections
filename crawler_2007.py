import pandas as pd
from time import sleep
import requests






def crawl_2007(teryt_code_list: pd.DataFrame):
    '''

        :param teryt_code_list: dataframe containing teryt code list (look example teryt file in repository)
        :return: tuple of dataframes containing:
        sejm_df - sejm 2007 elections outcome
        turnout_df - 2007 elections turnout
    '''
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

        for i in range(3):
            try:
                site = requests.get(url, timeout=5)
                break
            except requests.exceptions.ConnectTimeout:
                print("timeout error")
                sleep(5)

        try:
            url_data = pd.read_html(site.content)
        except ValueError:
            print("nie ma takiej gminy")
            continue

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

    return sejm_df, turnout_df




