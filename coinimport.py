from coinmarketcapscraper.coinsmarketcap import Scraper
# if seting download_all_logos to True don't set download_logo_sybmol={symbol}
app = Scraper(download_all_logos=True , coin_data=True,coin_data_file=True)

app.run()
