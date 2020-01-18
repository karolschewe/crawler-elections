import pandas
from matplotlib import pyplot as plt
import numpy as np


'''
this file is responsible for creating plots with statistics about crawled data
you have to provide file with data crawled by crawler_2011.py in the same folder (relative path is used)


'''


turnout_df = pandas.read_csv('frekwencja_wybory_2011_po_gminach.csv')
turnout_df['turnout_%'] = turnout_df['turnout_%'].str.replace(',','.')
turnout_df['turnout_%'] = turnout_df['turnout_%'].astype('float',True)



# rozklad frekwencji wyborczej po gminie

turnout_distribution = turnout_df.hist(column='turnout_%',bins=69)
plt.xlabel("turnout[%]")
plt.ylabel("frequency")
plt.title("Turnout distribution by gmina\nfor 2011 parliamentary elections")
plt.show()

# porownanie frekwencji najwyzszej z najnizsza
maximal_turnout = turnout_df.loc[turnout_df['turnout_%'].idxmax()]
minimal_turnout = turnout_df.loc[turnout_df['turnout_%'].idxmin()]





objects = (maximal_turnout['gmina'], minimal_turnout['gmina'])
y_pos = np.arange(len(objects))
performance = [maximal_turnout['turnout_%'],minimal_turnout['turnout_%']]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('turnout[%]')
plt.title('Turnout range\nfor 2011 parliamentary elections')

plt.show()


sejm_df = pandas.read_csv('wybory_do_sejmu_2011_po_gminach_wyniki.csv',encoding='utf-8-sig')
sejm_df['n_votes'] = sejm_df['n_votes'].str.replace('\xa0','')
sejm_df['n_votes'] = sejm_df['n_votes'].astype('int',True)
sejm_df['percentage'] = sejm_df['percentage'].str.replace(',','.')
sejm_df['percentage'] = sejm_df['percentage'].astype('float',True)

sejm_df['political_party'] = sejm_df['political_party'].str.replace('Lista nr ','')
sejm_df['political_party'] = sejm_df['political_party'].str.replace('- Komitet Wyborczy ','')
sejm_df['political_party'] = sejm_df['political_party'].str.replace(' - Zarejestrowana','')
sejm_df['political_party'] = sejm_df['political_party'].str[2:30]
# gdzie bylo maksymalne poparcie dla danej partii
max_by_party = sejm_df.groupby(['political_party'], sort=False)['percentage'].max()
where_max_by_party = pandas.merge(max_by_party, sejm_df, how='left', on=['political_party', 'percentage'])
where_max_by_party['label'] = where_max_by_party['political_party'] + "\n" + where_max_by_party['gmina']
where_max_by_party = where_max_by_party.sort_values(by=['percentage'])
where_max_by_party = where_max_by_party[1:]


objects = (where_max_by_party['label'].to_list())
y_pos = np.arange(len(objects))
performance = where_max_by_party['percentage'].to_list()

my_colors = [ 'violet', 'cyan','purple','olive','black','grey', 'red', 'green','orange','navy']
plt.bar(y_pos, performance, align='center', alpha=0.69, color = my_colors)
plt.xticks(y_pos, objects, rotation= 69 )
plt.ylabel('percentage[%]')
plt.title('Gminas where parties had maximum support\nfor 2011 parliamentary elections')
plt.tight_layout()
plt.show()

# ogolny udzial glosow wyborach na dana partie
how_many_votes_for_party = sejm_df.groupby(['political_party'], sort=False).sum()
all_votes_2011 = sum(how_many_votes_for_party['n_votes'])
print(all_votes_2011)
how_many_votes_for_party['percentage']=how_many_votes_for_party['n_votes']/all_votes_2011
how_many_votes_for_party = how_many_votes_for_party.sort_values(by=['percentage'])
how_many_votes_for_party = how_many_votes_for_party[1:]


objects = (how_many_votes_for_party.index.to_list())
y_pos = np.arange(len(objects))
performance = how_many_votes_for_party['percentage'].to_list()

my_colors = [ 'violet', 'cyan','purple','olive','grey', 'red', 'green','black','navy','orange']
plt.bar(y_pos, performance, align='center', alpha=0.69, color = my_colors)
plt.xticks(y_pos, objects, rotation= 69 )
plt.ylabel('percentage[%]')
plt.title('Percentages of votes get by each party\nfor 2011 parliamentary elections')
plt.tight_layout()
plt.show()





