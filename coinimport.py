from coinmarketcap.coinmarketcap import scraper

s = scraper(downloadlogo=True , coin_data=True)
s.TerminalScraper()


# from coinmarketcap import SetOptions

# SetOptions(downloadlogo=False , coin_data=True)