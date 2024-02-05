# IPO Crawler
It is the Simple Python program code that will crawl the IPO Information from the Website `nepsebajar.com`. It is created Only for Eductional purposes and I don't promote any kind of illegal activities. It is developed using the popular python library called `scrapy`. It will crawll the listed IPO Information from the Website and save it in the `ipodata.json` file which can be further used for processing the data. 

##  Usage
Follow the Given Steps to Setup in Your Local System. 
- Navigate to the File Directory
- Create the Virtual Environment (Not Necessary but Recommand) and activate it.
    ```bash
        # For Windows User
        python -m venv venv
        venv\Scripts\activate

        #For Linux User
        python3 -m virtualenv venv
        source venv/bin/activate

    ```
- Install the Requirements
    ```bash
        pip install -r requirements.txt
    ```
- Run the following Command
    ```bash
        scrapy crawl ipo
    ```
## Enjoy Learning