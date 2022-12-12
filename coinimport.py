from coinmarketcapscraper.coinsmarketcap import scraper
app = scraper(downloadlogo=True , coin_data=True,coin_data_file=True)
app.Run()
