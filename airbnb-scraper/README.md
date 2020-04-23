## Installation (nix)

    # Create venv
    python3 -m venv env
    
    # Enable venv
    . env/bin/activate
    
    # Install required packages
    pip install -Ur requirements.txt
    
    # Create settings.py
    cp deepbnb/settings.py.dist deepbnb/settings.py
    
    # @NOTE: Don't forget to set AIRBNB_API_KEY in settings.py. To find your API key, 
    # search Airbnb using Chrome, open dev tools, and look for to the url parameter  
    # named "key" in async requests to /api/v2/explore_tabs under the Network tab.

## Example Usage

#### Minimal scraper usage:

    scrapy crawl bnb -a query="Kazan" -o kazan.json
    

#####  fixed dates
```
scrapy crawl bnb -a query="Kazan" -a checkin=2020-10-01 -a checkout=2020-11-31 -o madrid.json
```

