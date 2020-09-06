from selenium import webdriver #for fetching dynamic webpage
driver = webdriver.Chrome("E:\Code\webscraping\chromedriver.exe") #webdriver for chrome

def fetchingpagesource():
    URL="https://covid19.mohp.gov.np/" #website of Health Ministry of Nepal
    driver.get(URL)
    htmlsource=driver.page_source
    driver.close()
    return htmlsource