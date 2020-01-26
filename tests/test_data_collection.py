from crawler_2011 import crawl_2011
from crawler_2007 import crawl_2007
import pandas as pd
import pathlib


terytki_path = pathlib.Path(__file__).parents[1] / 'terytki.xls'
sample_size = 10

teryt_code_list = pd.read_excel(terytki_path, header=0, converters={'TERYT': str})
sejm_df, turnout_df, senat_df = crawl_2011(teryt_code_list[0:sample_size])
sejm_df_2007, turnout_df_2007 = crawl_2007(teryt_code_list[0:sample_size])


def test_imported_teryt_list():
    assert teryt_code_list.columns[1] == 'TERYT'
    assert teryt_code_list.columns[2] == 'Gmina'
    assert teryt_code_list.columns[3] == 'Powiat'
    assert teryt_code_list['TERYT'].dtypes == object # wazne jest aby teryt wczytac jako string


def test_2011_datacrawl():
    assert turnout_df.shape == (sample_size,8)
    assert sejm_df.shape[1] == 8
    assert senat_df.shape[1] == 9


def test_2007_datacrawl():
    assert turnout_df_2007.shape == (sample_size,8)
    assert sejm_df_2007.shape[1] == 8


test_imported_teryt_list()
test_2011_datacrawl()
test_2007_datacrawl()
