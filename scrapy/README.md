# scrapy_diningcopy
This is the spider.
---

## Prepare environment

To execute this spider, you need Python 2.7, Scrapy framework and pymongo support. You can install Python and Scrapy one by one. Or you can try a quick path.
The quick path is Anaconda.

* Quick path - Anaconda

You can visit [CONTINUUM](https://www.continuum.io/) to learn more about Anaconda.
Or you can go to [Download](https://www.continuum.io/downloads) here to download directly.

* Scrapy & Pymongo

After you have anaconda in your environment, you can use the package management function of it to install and manage your packages.
Here are the commands.
```
      conda install scrapy
      conda install pymongo
```

## Start crawling

* Clone this project in your local file system
* Go into the project folder '***scrapy\_diningcopy/scrapy\_diningcopy***'
* Call scrapy to crawl
```
      scrapy crawl diningcopy
```

#### ./output folder
* You may need a ***./output*** folder to save the json file
* If you don't need, you can go to ***settings.py*** file to disable the ***JsonFilePipeline***
* In the spider source code, you can find the following varables. That define the crawling scope.
```
      _GLB_START_POINT_URL
      _GLB_SEARCH_KEYWORDS
```
* So, can compare to the original data source.

## Check crawling result

* You can check crawling result during the scrawling from console debugging message if you enable the ***DumpPipeline***
* After crawling, you can find the output file in ***./output*** folder, if you enable the ***JsonFilePipeline***
* You can also find the result in online MongoDB service. [Robomongo](https://robomongo.org/) can help make this more visual friendly.
* You can clear the crawling result in MongoDB and crawl again.
* To learn more about online MongoDB service, please visit [mlab](https://mlab.com/).

## Web App & Web Service

* After you double checked the crawling result in MongoDB, you can visit the [Web App](https://ror-diningcopy.herokuapp.com/deals)
* You can see the deals list, you can show details, you can delete some of the deals within the Web App.
* [Web Service](https://ror-diningcopy.herokuapp.com/deals.json)
* This REST API will provide json format deals result to all other web applications or mobile applicaitons.
* You can install ***JSONView*** plug-in for ***Chrome*** to make it easy to read the REST API output.
* ***Because the Web App & Web Service hosting is free, and the mongoDB is free as well, you may need to to refresh the page to active the backend data. ***

## One Page Web Application

* At the end, we can visit the [One Page Web Application](https://yunzhiwei.github.io/bs_diningcopy/) with decorated UI.
* Google map is used in ***MAP***. So please make sure you have VPN to Google.
* Click the ***MAP*** to see more details.
* Click ***SPECIALS*** to display the crawling results with well designed page layout.
* For this is a ***One Page Web Application***, the URL will not change.
* You can go back to the home page by refresh the page or click the menu button.
* Delete some deals with ***Robomongo*** or ***Web App***, and then see the change by clicking ***SPECIAL*** again.
