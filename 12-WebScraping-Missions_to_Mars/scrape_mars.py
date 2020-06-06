from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver "/usr/local/bin/chromedriver"
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():

    ### NASA Mars News -----------------------------------------------------------------

    browser = init_browser()

    # Visit mars.nasa.gov/news/
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get headline
    Mars_headline = soup.find_all("div", class_="content_title")[1].text

    # Get article
    Mars_article = soup.find("div", class_="article_teaser_body").get_text()



    ### JPL Mars Space Images - Featured Image------------------------------------------

    # Visit the url for JPL Featured Space Image
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #Get image
    featured_image_path = soup.find('article')['style'].replace('background-image: url(', '').replace(')', '') .strip(";(')")
    featured_image_url = "https://www.jpl.nasa.gov" + featured_image_path



    ### Mars Weather------------------------------------------------------------------------

    # Visit the Mars Weather twitter account
    url = "https://twitter.com/marswxreport?lang%3Den"
    browser.visit(url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    mars_weather = soup.find_all('span', class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")[34].text


    ### Mars Facts---------------------------------------------------------------------

    # Visit the Mars Weather twitter account
    url = "https://space-facts.com/mars/"
    browser.visit(url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    mars_ed = soup.find_all('td', class_="column-2")[0].text
    mars_pd = soup.find_all('td', class_="column-2")[1].text
    mars_mass = soup.find_all('td', class_="column-2")[2].text
    mars_moons = soup.find_all('td', class_="column-2")[3].text
    mars_od = soup.find_all('td', class_="column-2")[4].text
    mars_op = soup.find_all('td', class_="column-2")[5].text
    mars_st = soup.find_all('td', class_="column-2")[6].text
    mars_fr = soup.find_all('td', class_="column-2")[7].text
    mars_rb = soup.find_all('td', class_="column-2")[8].text


    ### Mars Hemispheres -----------------------------------------------------------------

    # Visit the Mars Weather twitter account
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    mars_hem = soup.find_all('img', class_='thumb')

    # Dictionary with the image url string and the hemisphere title
    hemisphere_image_urls = []
    for image in mars_hem:
        hemisphere_image_urls.append({'title': image['alt'], 'img_url': 'https://astrogeology.usgs.gov' + image['src'] })

    img_title1 = hemisphere_image_urls[0]['title']
    img_url1 = hemisphere_image_urls[0]['img_url']
    img_title2 = hemisphere_image_urls[1]['title']
    img_url2 = hemisphere_image_urls[1]['img_url']
    img_title3 = hemisphere_image_urls[2]['title']
    img_url3 = hemisphere_image_urls[2]['img_url']
    img_title4 = hemisphere_image_urls[3]['title']
    img_url4 = hemisphere_image_urls[3]['img_url']

    # Store data in a dictionary
    Mars_data = {
        "headline": Mars_headline,
        "article": Mars_article,
        "Mars_img": featured_image_url,
        "weather": mars_weather,
        "fact1": mars_ed,
        "fact2": mars_pd,
        "fact3": mars_mass,
        "fact4": mars_moons,
        "fact5": mars_od,
        "fact6": mars_op,
        "fact7": mars_st,
        "fact8": mars_fr,
        "fact9": mars_rb,
        "hem_title1": img_title1,
        "hem_img1": img_url1,
        "hem_title2": img_title2,
        "hem_img2": img_url2,
        "hem_title3": img_title3,
        "hem_img3": img_url3,
        "hem_title4": img_title4,
        "hem_img4": img_url4
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return Mars_data