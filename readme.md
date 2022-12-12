# requirements 
``` sudo apt install python3-venv ```  
``` python -m venv myvenv ```  
``` cd myvenv/bin/ && source activate ```  
``` pip install -r req.txt ```  

# install from pip
```
pip install git+https://github.com/hirbodprime/coinmarketcap.git
```


# if using terminal 
## use -d to download logos && use -c to extract coin data
## use -h to see help
```
python3 coinmarketcap.py -h
```
```   
Usage: &ensp; coinsmarketcap.py  --download-logos  --coin-data  --coin-file  
Options:     
    -h, --help            show this help message and exit      
    -d, --download-logos  download the top 10 coinmarketcap.com coin logos       
    -c, --coin-data       extracts coin data     
```  


# if importing (check coinimport)
## first import 
``` from coinmarketcapscraper.coinsmarketcap import scraper ```

## then use create an object from scraper class and set the options based on your needs
``` 
app = scraper(downloadlogo=True , coin_data=True,coin_data_file=True)  
app.Run()  
```



