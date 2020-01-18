import pandas
from matplotlib import pyplot as plt


'''
this file is responsible for creating plots with statistics about crawled data
you have to provide file with data crawled by crawler_2011.py in the same folder (relative path is used)


'''


turnout_df = pandas.read_csv('frekwencja_wybory_2011_po_gminach.csv')
print(turnout_df[['turnout_%']])

# trzeba skonwertowac na floata

turnout_df.hist(column='turnout_%')
