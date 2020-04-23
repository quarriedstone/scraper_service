# scraper_service
Scraper service


## DEPLOYMENT
```docker build -t scraper_service .```

```docker run -d --name scraper_service scraper_service```

## HTTP ENDPOINTS
**/get_amazon?category=<category_name>**

**/get_amazon?city=<city_name>**
