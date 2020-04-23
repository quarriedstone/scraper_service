# scraper_service
Scraper service


## DEPLOYMENT
```docker build -t scraper_service .```

```docker run -d --name scraper_service scraper_service```

Service is working on **6379** port

## HTTP ENDPOINTS
**/get_amazon?category=<category_name>**

**/get_airbnb?city=<city_name>**
