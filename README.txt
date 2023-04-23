This app scrappes the nigerian job site (https://www.nigeriajob.com). The job category selected was "IT, new technologies"
The Scrape job should be executed by following the below steps:

1. Run the "db_model.py" script first. This script executes the  web scrapping job and exports a data in a postgresql

2. Run the FLask app "app.py" to query the postgresql

3. Run unit test using pytest

Note: The data scrapped contained nested features in the technology and location column, which needed to be unnested.

