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

        pickle_in_marketwatch = open('marketwatch.pickle', 'rb')
        self.marketwatch_links = pickle.load(pickle_in_marketwatch)

pickle_out_benzinga = open('benzinga.pickle', 'wb')
                pickle.dump(self.benzinga_links, pickle_out_benzinga)
                pickle_out_benzinga.close()