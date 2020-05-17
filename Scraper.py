import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pickle
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Scraper:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.site_links = ['https://www.morningstar.com/', 'https://www.fool.com/', 'https://www.benzinga.com/', 'https://seekingalpha.com/', 'https://finance.yahoo.com/']
        self.markup = [requests.get(link).text for link in self.site_links]

        pickle_in_morningstar = open('morningstar.pickle', 'rb')
        self.morningstar_links = pickle.load(pickle_in_morningstar)

        pickle_in_fool = open('fool.pickle', 'rb')
        self.fool_links = pickle.load(pickle_in_fool)

        pickle_in_benzinga = open('benzinga.pickle', 'rb')
        self.benzinga_links = pickle.load(pickle_in_benzinga)

        pickle_in_seekingalpha = open('seekingalpha.pickle', 'rb')
        self.seekingalpha_links = pickle.load(pickle_in_seekingalpha)

        pickle_in_yahoofinance = open('yahoofinance.pickle', 'rb')
        self.yahoofinance_links = pickle.load(pickle_in_yahoofinance)

    def parse(self):
        for i in range(len(self.site_links)):
            if i == 0:
                soup = BeautifulSoup(self.markup[0], 'html.parser')
                links = soup.findAll('a', {'class': 'mdc-link mds-link mds-link--no-underline'})

                self.morningstar_links.update({link.text:self.sia.polarity_scores(link.text)['compound'] for link in links if link.text[0] != '\n' and len(link.text.split()) > 4}) 
                pprint(len(self.morningstar_links))
                pickle_out_morningstar = open('morningstar.pickle', 'wb')
                pickle.dump(self.morningstar_links, pickle_out_morningstar)
                pickle_out_morningstar.close()

            if i == 1:
                soup = BeautifulSoup(self.markup[1], 'html.parser')
                links = soup.findAll('h2', {'class': 'hp-news-panel-article-header'})

                self.fool_links.update({link.text:self.sia.polarity_scores(link.text)['compound'] for link in links if len(link.text.split()) > 4}) 

                pickle_out_fool = open('fool.pickle', 'wb')
                pickle.dump(self.fool_links, pickle_out_fool)
                pickle_out_fool.close()
            
            if i == 2:
                soup = BeautifulSoup(self.markup[2], 'html.parser')
                links = soup.findAll('div', {'class': 'views-field-title'})

                self.benzinga_links.update({link.text[1:len(link.text) - 1] : self.sia.polarity_scores(link.text[1:len(link.text) - 1])['compound'] for link in links if len(link.text.split()) > 4}) 

                pickle_out_benzinga = open('benzinga.pickle', 'wb')
                pickle.dump(self.benzinga_links, pickle_out_benzinga)
                pickle_out_benzinga.close()

            
            if i == 3:
                soup = BeautifulSoup(self.markup[3], 'html.parser')
                links = soup.findAll('li', {'class': 'article-elem'})

                self.seekingalpha_links.update({link.text:self.sia.polarity_scores(link.text)['compound'] for link in links if len(link.text.split()) > 4}) 

                pickle_out_seekingalpha = open('seekingalpha.pickle', 'wb')
                pickle.dump(self.seekingalpha_links, pickle_out_seekingalpha)
                pickle_out_seekingalpha.close()

            if i == 4:
                soup = BeautifulSoup(self.markup[4], 'html.parser')
                links = soup.findAll('a', {
                    'class': 'Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled'})

                self.yahoofinance_links.update({link.text:self.sia.polarity_scores(link.text)['compound'] for link in links if len(link.text.split()) > 4}) 

                pickle_out_yahoofinance = open('yahoofinance.pickle', 'wb')
                pickle.dump(self.yahoofinance_links, pickle_out_yahoofinance)
                pickle_out_yahoofinance.close()


    def rank(self):
        website_list = {'Morningstar': 0, 'Motley Fool': 0, 'Benzinga': 0, 'SeekingAlpha': 0, 'Yahoo Finance': 0}
        keys = list(website_list.keys())
        self.all_links = [self.morningstar_links, self.fool_links, self.benzinga_links, self.seekingalpha_links, self.yahoofinance_links]
        sum = 0
        count = 0
        for website in self.all_links:
            for key in website:
                sum += website[key]

            website_list[keys[count]] = sum/len(website) 
            sum = 0
            count += 1

        self.sorted_website_list =  sorted(website_list.items(), key=lambda x: x[1])
        pprint(self.sorted_website_list)
        
s = Scraper()
s.parse()