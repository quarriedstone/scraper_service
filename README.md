# scraper_service
Scraper service


## DEPLOYMENT
```docker build -t scraper_service .```

```docker run -d --name scraper_service -p6379:6379 scraper_service```

Service is working on **6379** port

## HTTP ENDPOINTS
**/get_amazon?category=<category_name>**

You may also specify the list of categories:
**/get_amazon?category=[laptops, iphone]**

**/get_airbnb?city=<city_name>**
