##This repository contains non compulsory project for "Python in scientific usage"
###This project is a part of Karol's Schewe thesis named: Does the voter model describe behavior of voters ?

The aim of this project is to scrape data from PKW (polish national electoral commision) 
about parlamentary elections in 2011 and 2007. It is important that elections
outcome is scraped with gmina resolution. It is essential because Voter model will be build 
with this resolution.

Links to crawled pages:
https://wybory2007.pkw.gov.pl/SJM/PL/WYN/W/index.htm
https://wybory2011.pkw.gov.pl/wyn/pl/000000.html#tabs-1

Crawler usage:
1. Project consists of 2 main files crawler_2007.py and crawler_2011.py. 
2. As the page layout for these two elections is different it was necessary
to write two different scrapers to accomplish my goal. 
3. These two contain two functions for scraping these elections.
4. In this directory you can also find a file named terytki.xls. It contains
list of teryt codes (numerical identifiers of all gminas). It is needed
to run both functions.
5. Each function needs this file to be imported to dataframe. It is needed to create proper urls to scrape.
6. After running a function it scrapes data about all gminas which teryt codes
are listed in file terytki.xls.
7. The outcome is returned in tuples of dataframes.
8. Sample usage of written functions is in main.py file.

This project also contains program plots_presentation.py. In this script sample graphs are made in matplotlib package.