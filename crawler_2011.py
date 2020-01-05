import requests
import lxml.html as lh
import pandas as pd


# url='http://pokemondb.net/pokedex/all'
# #Create a handle, page, to handle the contents of the website
# page = requests.get(url)
# #Store the contents of the website under doc
# doc = lh.fromstring(page.content)
# #Parse data that are stored between <tr>..</tr> of HTML
# tr_elements = doc.xpath('//tr')
#
# #Check the length of the first 12 rows
# [len(T) for T in tr_elements[:12]]
#
# tr_elements = doc.xpath('//tr')
# #Create empty list
# col=[]
# i=0
# #For each row, store each first element (header) and an empty list
# for t in tr_elements[0]:
#     i+=1
#     name=t.text_content()
#     print (i,name)
#     col.append((name,[]))



import pandas as pd

url = r'https://wybory2011.pkw.gov.pl/wyn/300000/pl/306401.html#tabs-1'
tables = pd.read_html(url) # Returns list of all tables on page
n_tables = len(tables)
gmina_name = tables[0][0][0]
year = 2011
elections_name = "sejm"
teryt = 306401
powiat = "Poznan"
dict_list = []
for lista in range(2,n_tables-2):
    political_party = tables[lista].iloc[0,0]
    n_of_votes = tables[lista].iloc[-1,2]
    votes_percentage = tables[lista].iloc[-1,3]
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
    dict_list.append(df_row)
final_df = pd.DataFrame.from_dict(dict_list)
print(final_df)
print(gmina_name)
