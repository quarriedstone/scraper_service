# Amazon Product Scraper
This is an `Amazon Product Scraper` built using `scapy` module of `python`

# Features
it scrape various things
- Product Title
- Product Image
- Product Price
- Product Rating
- Product Description
- Product Reviews
- Product Brand
- Product Colour
- Product Website
- Product URL

# Execute Amazon Scraper

### Second one
you can execute the following command
```bash
scrapy crawl amazon_scraper -o ./data/data.json -a category=product+name
```

It will create `data.json` file inside the `data` folder containing all the scraped data in `JSON` format.

# Sample Data
Already fetched sample data is available in `data` folder

# Troubleshooting
If `data.json` file doesn't generate in proper format then just delete `data.json` file.  
Now you good to go ;)

# Preresuisites
- you have to install `scrapy`
- you have to install `pillow`


[MIT]
