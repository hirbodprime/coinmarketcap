# requirements 
``` sudo apt install python3-venv ```  
``` python -m venv myvenv ```  
``` cd myvenv/bin/ && source activate ```  
``` pip install -r req.txt ```  

# if using terminal 
## use -d to download logos && use -c to extract coin data
## use -h to see help
``` python3 coinmarketcap.py -h   
Usage:&ensp;coinmarketcap.py --download-logos --coin-data  
Options:   
&nbsp;-h, --help            show this help message and exit    
&nbsp;-d, --download-logos  download the top 10 coinmarketcap.com coin logos     
&nbsp;-c, --coin-data       extracts coin data   
```  

# version coinmarketcap-0.0.2.py
```
from coinmarketcap.coinmarketcap import scraper  
s = scraper(downloadlogo=True , coin_data=True)  
s.TerminalScraper()  
```

# version coinmarketcap-0.0.1.py
# if importing (check coinimport)
## first import 
``` from coinmarketcap import SetOptions ```

## then use SetOptions function to set if you want coin_data or to download logos
``` SetOptions(downloadlogo=False , coin_data=True) ```

