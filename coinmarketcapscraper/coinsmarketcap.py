import requests
from bs4 import BeautifulSoup 
import os
import json
from optparse import OptionParser
import colorama

# print(__name__)

# resets the colorama colors to default after every call
colorama.init(autoreset=True)

# when python3 coinmarketcap -h or --help it shows the project name and options
# %prog is built in for OptionParser 
usage = "usage: %prog  --download-logos  --coin-data  --coin-file"

# creates a instance of OptionParser to parser
parser = OptionParser(usage=usage)

parser.add_option("-s", "--logo-symbol",type="str" ,action="store",dest="logosymbol",
    help="downloads logo by the symbol")

# when running the file if we use -d or --dowload-logos this parser will return True
parser.add_option("-d", "--download-logos", dest="logo",
        action="store_true", # if -d is called it will store True
        default=False, # by default it's false which means we are not parsing -d to it
        help="download the top 10 coinmarketcap.com coin logos")

parser.add_option('-f', "--coin-file",dest='file',
        action="store_true",
        default=False,
        help="saves coin data in a file")

parser.add_option('-c', "--coin-data",dest='data',
        action="store_true",
        default=False,
        help="extracts coin data")

# storing the values of options and any args
(options , args) = parser.parse_args()

# the url to target
url = "https://coinmarketcap.com/"

# gets the html of the target as text
result = requests.get(url).text

# creates an instance of BeautifulSoup using the result 
doc = BeautifulSoup(result , "html.parser")

# getting the tbody tag from text file
tbody = doc.tbody

# getting the contents of the tbody tag and storing it into trs
trs = tbody.contents

data_list = []
dict_data = {}



class Scraper:

    def __init__(self, download_all_logos, coin_data, coin_data_file ,download_logo_sybmol=None):
        self._downloadlogo = download_all_logos
        self._coin_data = coin_data
        self._coin_data_file = coin_data_file
        self._download_logo_symbol = download_logo_sybmol


    def _main(self):
        # make a dir named logos if doesn't exists
        # os.makedirs("logos",exist_ok=True)
        # cd to the created dir
        # os.chdir("logos")
        for tr in trs[:10]:
            # getting the name and price from tr content in td tags
            name , price = tr.contents[2:4]

            # getting the symbol from tr content in td tags
            symbol = name.find('p' , class_="sc-e225a64a-0 dfeAJi coin-item-symbol")
            
            # getting the logo from tr content in td tags
            logo = tr.find("img", class_="coin-logo")

            # creating a dynamic cool filename
            filename = f"logo-{symbol.string}.jpg"

            # downloading the logo (logo['src'] is the direct url to the logo )
            reqlogo = requests.get(logo['src'])

            # just acting like a hacker and printing the logo symbol when downloaded in green
            print(f'{colorama.Fore.LIGHTGREEN_EX} downloaded {symbol.string} LOGO successfully')
            
            # opening the url and writing the content to the file
            with open(filename , 'wb') as f:
                f.write(reqlogo.content)
            f.close()
            dict_data = {
                'name':name.p.string,
                'symbol':symbol.string,  
                'price':price.a.string
                }
            data_list.append(dict_data)

            print(f"{colorama.Fore.LIGHTGREEN_EX} {name.p.string} coin data extracted successfully")
        if self._coin_data_file == True:
            os.chdir('../')
            os.makedirs('data',exist_ok=True)
            os.chdir('data')
            # wrting the extracted data into a json file
            with open('data.json' , 'w') as f:
                json.dump(data_list , f ,ensure_ascii=False)
        else:
            if __name__ == "__main__":
                print(data_list)
            else:
                return data_list

    def run(self):
        if __name__ == "__main__":
            if options.data == True and options.logo == True:
                self._main()
            else:
                if options.data == True:
                    self.get_coin_data()
                elif options.logo == True:
                    self.get_logo()
                elif options.logosymbol:
                    self.download_logo_symbol()
                else:
                    print("either -d or -c should be set")
        else:
            if self._downloadlogo == True and self._coin_data == True:
                self._main()
            else:
                if self._coin_data == True:
                    self.get_coin_data()
                elif self._downloadlogo == True:
                    self.get_coin_data()
                else:
                    print("either -d or -c should be set")

    def get_logo(self):
        my_list = []
        my_dict = {}
        if __name__ == "__main__":
            # make a dir named logos if doesn't exists
            os.makedirs("logos",exist_ok=True)
            # cd to the created dir
            os.chdir("logos")

        for tr in trs[:10]:
            name , price = tr.contents[2:4]
            # getting the symbol from tr content in td tags
            symbol = name.find('p' , class_="sc-e225a64a-0 dfeAJi coin-item-symbol")
            
        
            # getting the logo from tr content in td tags
            logo = tr.find("img", class_="coin-logo")

            # creating a dynamic cool filename
            filename = f"logo-{symbol.string}.jpg"

            # downloading the logo (logo['src'] is the direct url to the logo )
            reqlogo = requests.get(logo['src'])

            # just acting like a hacker and printing the logo symbol when downloaded in green
            print(f'{colorama.Fore.LIGHTGREEN_EX} downloaded {symbol.string} LOGO successfully')
            
            if __name__ == "__main__":    
                # opening the url and writing the content to the file
                with open(filename , 'wb') as f:
                    f.write(reqlogo.content)
                f.close()   

    def get_coin_data(self):
        for tr in trs[:10]:
            # getting the name and price from tr content in td tags
            name , price = tr.contents[2:4]

            # getting the symbol from tr content in td tags
            symbol = name.find('p' , class_="sc-e225a64a-0 dfeAJi coin-item-symbol")
            
            dict_data = {
                        'name':name.p.string,
                        'symbol':symbol.string,  
                        'price':price.a.string
                        }
            data_list.append(dict_data)

            print(f"{colorama.Fore.LIGHTGREEN_EX} {name.p.string} coin data extracted successfully")
        
        if self._coin_data_file == True:
            os.makedirs('data',exist_ok=True)
            os.chdir('data')
            # wrting the extracted data into a json file
            with open('data.json' , 'w') as f:
                json.dump(data_list , f ,ensure_ascii=False)
        else:
            if __name__ == "__main__":
                print(data_list)
            else:
                return data_list

    def download_logo_symbol(self):
        for tr in trs[:10]:
            name , price = tr.contents[2:4]
            # getting the symbol from tr content in td tags
            symbol = name.find('p' , class_="sc-e225a64a-0 dfeAJi coin-item-symbol")
            # getting the logo from tr content in td tags
            if tr.find("img", class_="coin-logo",alt=f"{self._download_logo_symbol} logo"):
                logo = tr.find("img", class_="coin-logo",alt=f"{self._download_logo_symbol} logo")
                print(symbol.string , logo['src'])
                # creating a dynamic cool filename
                filename = f"logo-{symbol.string}.jpg"

                # downloading the logo (logo['src'] is the direct url to the logo )
                reqlogo = requests.get(logo['src'])
                logo_link = logo['src']
                # just acting like a hacker and printing the logo symbol when downloaded in green
                print(f'{colorama.Fore.LIGHTGREEN_EX} downloaded {symbol.string} LOGO successfully')
                my_list = [logo_link , symbol.string , reqlogo]
                return my_list
                # opening the url and writing the content to the file
                # with open(filename , 'wb') as f:
                #     f.write(reqlogo.content)
                # f.close()   
                break
                

if __name__ == "__main__":
    scraperOBJ = Scraper(download_all_logos=options.logo,coin_data=options.data,coin_data_file=options.file , download_logo_sybmol=options.logosymbol)
    scraperOBJ.run()
