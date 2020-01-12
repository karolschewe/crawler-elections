##This repository contains non compulsory project for "Python in scientific usage"
###This project is a part of Karol's Schewe thesis named: Does the voter model describe behavior of voters ?

The aim of this project is to scrape data from PKW (polish national electoral commision) 
about parlamentary elections in 2011 and 2007. It is important that elections
outcome is scraped with gmina resolution. It is essential because Voter model will be build 
with this resolution.

Crawler usage:
1. Project consists of 2 main files crawler_2007.py and crawler_2011.py. 
2. As the page layout for these two elections is different it was necessary
to write two different scrapers to accomplish my goal. 
3. These two files are two independent programs.
4. In this directory you can also find a file named terytki.xls. It contains
list of teryt codes (numerical identifiers of all gminas). It is needed
to run both programs.
5. Each program imports this list. It is needed to create proper urls to scrape.
6. After running a program it scrapes data about all gminas which teryt codes
are listed in file terytki.xls.
7. The outcome is saved in 3 csv files in the same directory. First file
contains information about Sejm elections, second about senate. Last file lists
contains information about turnout.