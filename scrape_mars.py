#dependecies 
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import os
import pandas as pd
import time 



def scrape_info():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)



    # URL of page to be scraped
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"


    browser.visit(url)



    # Retrieve page with the requests module
    response = requests.get(url)



    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')



    results = soup.find_all('div', class_="slide")
    results


    mars={}
    for result in results:
        try:
            title=result.find('div',class_="content_title").a.text
            description=result.find('div',class_="rollover_description_inner").text
            print("title and descriptions are :")
            print("-----------------------------")
            if(title and description):
                print(title)
                print(description)
        except AttributeError as e:
            print(e)



    title=result.find('div',class_="content_title").a.text
    mars["title"]=title
    news_p=result.find('div',class_="rollover_description_inner").text
    mars["news_paragraph"]=news_p
    print(mars["title"])
    print(mars["news_paragraph"])


    for x in range(0,1):
        html=browser.html
        soup = BeautifulSoup(html, 'html.parser')
        results =soup.find_all('li', class_='slide')
        
        for result in results:
            try: 
                news_title= soup.find("div", class_='content_title').text
                news_p= soup.find("div", class_='article_teaser_body').text
                print("title description")
                print("----")
                if(news_title and news_p):
                    print(news_title)
                    print(news_p)
            except Attributeerror as e:
                print (e)




    # print(soup.prettify())


    #Find news title and paragraph 
    news_title= soup.find("div", class_='content_title').text
    news_title 



    news_p= soup.find("div", class_='rollover_description').text
    news_p



    #executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome')



    #JPL mars space images 
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)



    html = browser.html
    soup = BeautifulSoup(html, "lxml")



    time.sleep(5)



    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()
    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()
    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')

    # find the relative image url
    img_url_rel = img_soup.select_one('figure.lede a img').get("src")
    img_url_rel
    # Use the base url to create an absolute url
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    img_url




    mars["featured_image_url"]=img_url


    #Mars Weather 
    url="https://twitter.com/marswxreport?lang=en"
    browser.visit(url)



    html = browser.html
    weather_soup = BeautifulSoup(html, "lxml")



    mars_weather = weather_soup.find('div', class_="js-tweet-text-container").text
    mars_weather



    mars["weather"]=mars_weather



    #mars facts
    url="https://space-facts.com/mars/"



    fact_tables = pd.read_html(url)
    fact_tables


    df = fact_tables[0]
    df.columns = ["Stat","Value"]
    df.head()


    df.set_index('Stat', inplace=True)
    df.head()



    html_table = df.to_html()
    html_table

    html_table.replace('\n', '')
    
    mars["facts"]=html_table


    #mars hemisphere 
    url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)



    browser.visit(url)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.prettify)


    results=soup.find_all("div", class_="item")
    results


    hemisphere_image_urls=[]



    hemisphere={}
    for result in results:
        hemisphere['title']=result.find('div',class_="description").h3.text
        hemisphere['img_url']=result.img['src']
        hemisphere_image_urls.append(hemisphere)
    #    print(title)
    #    print(img_url)
    hemisphere_image_urls
    mars["hemisphere"]=hemisphere_image_urls
    mars["hemisphere"]

    return mars
if __name__ == "__main__":
    print(scrape_info())











