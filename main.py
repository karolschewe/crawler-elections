import pandas as pd
from crawler_2011 import crawl_2011
from crawler_2007 import crawl_2007
from crawler2005 import crawl_2005
#author: Karol Schewe
'''
Do uruchomienia tego programu potrzebny jest plik z lista kodów TERYT gmin, o których zamierzamy zebrać informacje.
Program korzysta z bibliotek:
- pandas
- requests
- urllib3
- html5lib
Repozytorium zawiera plik requirements.txt za pomocą którego w prosty sposób można zainstalować wszystkie wymagane pakiety.
Aby to uczynić należy wykonać komendę pip install: –r requirements.txt
Agrumentem funkcji jest ramka danych zawierająca listę terytów. Przykładowy plik do wczytania został załączony w repozytorium
Program zapisuje wyniki wyborów do sejmu, senatu oraz frekwencję na poziomie gminy do trzech odrębnych plików csv.

'''


teryt_code_list = pd.read_excel('terytki.xls', header=0, converters={'TERYT': str})
# sejm_df, turnout_df, senat_df = crawl_2011(teryt_code_list[0:10])
# sejm_df_2007, turnout_df_2007 = crawl_2007(teryt_code_list)
sejm_df_2005, turnout_df_2005 = crawl_2005(teryt_code_list)

# print(sejm_df.to_string())


# sejm_df.to_csv("wybory_do_sejmu_2011_po_gminach_wyniki.csv", index=False, encoding='utf-8-sig')
# turnout_df.to_csv("frekwencja_wybory_2011_po_gminach.csv", index=False, encoding='utf-8-sig')
# senat_df.to_csv("wybory_do_senatu_2011_po_gminach_wyniki.csv", index=False, encoding='utf-8-sig')


sejm_df_2005.to_csv("wybory_do_sejmu_2005_po_gminach_wyniki.csv", index=False, encoding='utf-8-sig')
turnout_df_2005.to_csv("frekwencja_wybory_2005_po_gminach.csv", index=False, encoding='utf-8-sig')













