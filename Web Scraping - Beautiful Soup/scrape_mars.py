## Need Beautiful Soup to parse HTML data
## Need splinter to view full HTML hidden by Javascript
from bs4 import BeautifulSoup 
import pandas as pd
import requests
import re
from splinter import Browser

def init_browser():
    executable_path = {'executable_path': "/usr/local/bin/chromedriver"}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

def scrape_news():
    browser = init_browser()
    # insert news scrape code
    # then put outputs into a dictionary to return 

    url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    ## visit URL

    browser.visit(url)

    ## set what browser finds into variable html

    news_html = browser.html

    ## parse the html to be able to scrape

    soup = BeautifulSoup(news_html, 'html.parser')

    ## After inspection, <li class="slide"> contains the News Title and paragraph text
    ## the News Title is in an <a> title text. 
    ## the paragraph text is in <div class="article_teaser_body">

    lists = soup.find('li', class_="slide")

    ## set variable to content_title to parse through it

    content_title = lists.find('div', class_="content_title")

    ##### News Title #####
    news_title = content_title.a.text

    ##### News Paragraph #####
    news_p = lists.find('div', class_="article_teaser_body").text

    news_data = {"news_title": news_title, "news_p": news_p}

    return news_data

def scrape_featured_img():
    browser = init_browser()
    
    # insert news scrape code
    # then put outputs into a dictionary to return 

    photo_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    ## visit URL

    browser.visit(photo_url)

    # set what browser finds into variable html

    photo_html = browser.html

    ## parse the html to be able to scrape

    soup = BeautifulSoup(photo_html, 'html.parser')

    ## Get the section that has the full sized photo

    photo_class = soup.find('section', class_="centered_text clearfix main_feature primary_media_feature single")

    ## Get the div that the photo is in

    photo_div = photo_class.find('div', class_="carousel_items")

    ## URL is in the style attribute of the article element

    style_url = photo_div.article['style']

    ## Split the string. The split method returns a list

    photo_url = style_url.split("'")

    ## Set the base_url for concatentation

    base_url = "https://www.jpl.nasa.gov"

    ## Concatenate the strings to get the final url

    featured_img_url = base_url + photo_url[1]

    img_dict = {"featured_img_url":featured_img_url}

    return img_dict

def scrape_weather():
    browser = init_browser()
    
    # insert news scrape code
    # then put outputs into a dictionary to return 

    twitter_url = "https://twitter.com/marswxreport?lang=en"

    ## visit URL

    browser.visit(twitter_url)

    # set what browser finds into variable html

    weather_html = browser.html

    ## parse the html to be able to scrape

    soup = BeautifulSoup(weather_html, 'html.parser')

    ## use re library

    weather_string = soup.find(string=re.compile("InSight sol"))

    ## string manipulation

    mars_weather = weather_string.replace("\n","")

    mars_weather_dict = {"mars_weather": mars_weather}

    return mars_weather_dict

def scrape_facts():  ######################### Need to re-run. It was only bring out the Description and Value
    browser = init_browser()
    
    # insert news scrape code
    # then put outputs into a dictionary to return 

    facts_url = "https://space-facts.com/mars/"

    ## using pandas to read html and find the table
    ## pandas returned two tables. We want the second one, that's why the index is 1

    tables = pd.read_html(facts_url)[1]

    tables.columns = ['Description', 'Value']

    html_table = tables.to_html()

    mars_facts_dict = {"mars_facts":html_table}

    return mars_facts_dict

def scrape_hemispheres():
    browser = init_browser()
    
    # insert news scrape code
    # then put outputs into a dictionary to return 

    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # visit URL

    browser.visit(hemisphere_url)

    # set what browser finds into variable html

    hemisphere_html = browser.html

    # parse the html to be able to scrape

    soup = BeautifulSoup(hemisphere_html, 'html.parser')

    ## get down to where there are the four links to click with titles

    link_class = soup.find_all('div', class_="description")

    ## Create list of secondary links that will be concatenated with base url to get the endpoint where the full image 
    ## link can be found. 

    # set empty list
    links = []

    # set base url to concatentate in the for loop

    hem_base_url = "https://astrogeology.usgs.gov"

    # loop through link_class 

    for link in link_class:
        links.append(link.a['href'])

    ## Now that we have the list of secondary links from above, we can write a for loop that will 
    # 1. Concatentate the base url with the secondary links that browser can use to get the html file

    # empty list that will become a list of dicts
    hem_dict = []

    # set base url to concatentate in the for loop

    hem_base_url = "https://astrogeology.usgs.gov"

    # iterate through links to get full url, get html file, find the title and the full img url, then
    # set data in a dict and append to list

    for link in links:
        full_hem_url = hem_base_url + link
        
        browser.visit(full_hem_url)
        
        full_hem_html = browser.html
        
        soup = BeautifulSoup(full_hem_html, 'html.parser')
        
        title = soup.find('h2', class_='title').text
        
        full_image_hem_url = soup.ul.li.a['href']
        
        hem_dict.append({"title": title, "img_url":full_image_hem_url})

    mars_hemispheres = hem_dict

    return mars_hemispheres


def scrape_mars_info():

    news = scrape_news()

    featured_img = scrape_featured_img()

    weather = scrape_weather()

    facts = scrape_facts()

    hemispheres = scrape_hemispheres()

    # put data into "mars_data" dictionary

    mars_data = {"news":news, 
                "featured_img":featured_img,
                "weather":weather,
                "facts":facts,
                "hemispheres":hemispheres}

    return mars_data
