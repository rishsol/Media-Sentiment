import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pickle
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import OrderedDict

class Scraper:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.site_links = ['https://www.morningstar.com/', 'https://www.fool.com/', 'https://www.benzinga.com/', 'https://seekingalpha.com/', 'https://finance.yahoo.com/', 'https://www.marketwatch.com/', 'https://www.thestreet.com/']
        self.markup = [requests.get(link).text for link in self.site_links]

        pickle_in_morningstar = open('pickle/morningstar.pickle', 'rb')
        self.morningstar_links = pickle.load(pickle_in_morningstar)
        self.morningstar_daily = dict()

        pickle_in_fool = open('pickle/fool.pickle', 'rb')
        self.fool_links = pickle.load(pickle_in_fool)
        self.fool_daily = dict()

        pickle_in_benzinga = open('pickle/benzinga.pickle', 'rb')
        self.benzinga_links = pickle.load(pickle_in_benzinga)
        self.benzinga_daily = dict()

        pickle_in_seekingalpha = open('pickle/seekingalpha.pickle', 'rb')
        self.seekingalpha_links = pickle.load(pickle_in_seekingalpha)
        self.seekingalpha_daily = dict()

        pickle_in_yahoofinance = open('pickle/yahoofinance.pickle', 'rb')
        self.yahoofinance_links = pickle.load(pickle_in_yahoofinance)
        self.yahoofinance_daily = dict()
 
        pickle_in_marketwatch = open('pickle/marketwatch.pickle', 'rb')
        self.marketwatch_links = pickle.load(pickle_in_marketwatch)
        self.marketwatch_daily = dict()

        pickle_in_street = open('pickle/street.pickle', 'rb')
        self.street_links = pickle.load(pickle_in_street)
        self.street_daily = dict()

    def parse(self):
        for i in range(len(self.site_links)):

            soup = BeautifulSoup(self.markup[i], 'html.parser')
            if i == 0:
                links = soup.findAll('a', {'class': 'mdc-link mds-link mds-link--no-underline'})

                self.morningstar_daily.update({link.text: self.sia.polarity_scores(link.text)['compound'] for link in links if link.text[0] != '\n' and len(link.text.split()) > 4}) 
                self.morningstar_links.update(self.morningstar_daily)

                pickle_out_morningstar = open('pickle/morningstar.pickle', 'wb')
                pickle.dump(self.morningstar_links, pickle_out_morningstar)
                pickle_out_morningstar.close()

            if i == 1:
                links = soup.findAll('h2', {'class': 'hp-news-panel-article-header'})

                self.fool_daily.update({link.text : self.sia.polarity_scores(link.text)['compound'] for link in links if len(link.text.split()) > 4}) 
                self.fool_links.update(self.fool_daily)

                pickle_out_fool = open('pickle/fool.pickle', 'wb')
                pickle.dump(self.fool_links, pickle_out_fool)
                pickle_out_fool.close()
            
            if i == 2:
                links = soup.findAll('div', {'class': 'views-field-title'})

                self.benzinga_daily.update({link.text: self.sia.polarity_scores(link.text[1:len(link.text) - 1])['compound'] for link in links if len(link.text.split()) > 4}) 
                self.benzinga_links.update(self.benzinga_daily)

                pickle_out_benzinga = open('pickle/benzinga.pickle', 'wb')
                pickle.dump(self.benzinga_links, pickle_out_benzinga)
                pickle_out_benzinga.close()

            if i == 3:
                links = soup.findAll('li', {'class': 'article-elem'})

                self.seekingalpha_daily.update({link.text : self.sia.polarity_scores(link.text)['compound'] for link in links if len(link.text.split()) > 4}) 
                self.seekingalpha_links.update(self.seekingalpha_daily)

                pickle_out_seekingalpha = open('pickle/seekingalpha.pickle', 'wb')
                pickle.dump(self.seekingalpha_links, pickle_out_seekingalpha)
                pickle_out_seekingalpha.close()

            if i == 4:
                links = soup.findAll('a', {
                    'class': 'Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled'})

                self.yahoofinance_daily.update({link.text : self.sia.polarity_scores(link.text)['compound'] for link in links if len(link.text.split()) > 4}) 
                self.yahoofinance_links.update(self.yahoofinance_daily)

                pickle_out_yahoofinance = open('pickle/yahoofinance.pickle', 'wb')
                pickle.dump(self.yahoofinance_links, pickle_out_yahoofinance)
                pickle_out_yahoofinance.close()

            if i == 5:
                links =  soup.findAll('a', {'class': 'link'})
                for i in range(len(links)):
                    links[i] =  links[i].text.replace("\r", "")
                    links[i] =  links[i].replace("\n", "")
                    links[i] = links[i].strip()

                self.marketwatch_daily.update({link : self.sia.polarity_scores(link)['compound'] for link in links if len(link.split()) > 4})
                self.marketwatch_links.update(self.marketwatch_daily)

                pickle_out_marketwatch = open('pickle/marketwatch.pickle', 'wb')
                pickle.dump(self.marketwatch_links, pickle_out_marketwatch)
                pickle_out_marketwatch.close()

            if i == 6:
                links = soup.findAll('h2', {'class': 'm-ellipsis--text m-card--header-text'})

                self.street_daily.update({link.text : self.sia.polarity_scores(link.text)['compound'] for link in links if len(link.text.split()) > 4})
                self.street_links.update(self.street_daily)
                
                pickle_out_street = open('pickle/street.pickle', 'wb')
                pickle.dump(self.street_links, pickle_out_street)
                pickle_out_street.close()

    def rank(self):

        website_list_cumulative = {'Morningstar': 0, 'Motley Fool': 0, 'Benzinga': 0, 'SeekingAlpha': 0, 'Yahoo Finance': 0, 'Marketwatch': 0, 'The Street': 0}
        website_list_daily = {'Morningstar': 0, 'Motley Fool': 0, 'Benzinga': 0, 'SeekingAlpha': 0, 'Yahoo Finance': 0, 'Marketwatch': 0, 'The Street': 0}

        keys = list(website_list_cumulative.keys())

        self.all_links_cumulative = [self.morningstar_links, self.fool_links, self.benzinga_links, self.seekingalpha_links, self.yahoofinance_links, self.marketwatch_links, self.street_links]
        self.all_links_daily = [self.morningstar_daily, self.fool_daily, self.benzinga_daily, self.seekingalpha_daily, self.yahoofinance_daily, self.marketwatch_daily, self.street_daily]
        
        sum = 0
        count = 0
        for website in self.all_links_cumulative:
            for key in website:
                sum += website[key]

            website_list_cumulative[keys[count]] = sum/len(website) 
            sum = 0
            count += 1

        sum = 0
        count = 0
        for website in self.all_links_daily:
            for key in website:
                sum += website[key]

            website_list_daily[keys[count]] = sum/len(website) 
            sum = 0
            count += 1

        self.sorted_website_list_cumulative =  sorted(website_list_cumulative.items(), key=lambda x: x[1], reverse=True)
        self.sorted_website_list_daily = sorted(website_list_daily.items(), key=lambda x: x[1], reverse=True)

        return [dict(self.sorted_website_list_daily), dict(self.sorted_website_list_cumulative)]