#!/usr/bin/env python
# coding: utf-8

# In[1]:



import os


# In[2]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import time


# In[3]:



# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


# Assign the url and instruct the browser to visit it.
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[5]:


# Set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[6]:


# Scrape title
slide_elem.find('div', class_='content_title')


# In[7]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[8]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[9]:


# Set up the URL
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[10]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


# Find the relative image url

img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[13]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# # ## Mars Facts

# In[14]:


# Pandas DF
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[15]:


# Convert DF to HTML
df.to_html()


#  D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[16]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

time.sleep(1)


# In[17]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):

    
    # Find Download link for each hemisphere
    browser.links.find_by_partial_text('Hemisphere')[i].click()
    
    # Parse the HTML
    html = browser.html
    hemis_soup = soup(html,'html.parser')
    
    # Find Enchanced Images/Titles aka Scrapping
    title = hemis_soup.find('h2', class_='title').text
    img_url = hemis_soup.find('li').a.get('href')
    
    # Create an empty dictionary
    hemispheres = {}
    # Put Title and img_url into dictionary
    hemispheres['img_url'] = f'https://marshemispheres.com/{img_url}'
    hemispheres['title'] = title
    
    # Append dictionary of mars hempisheres into list
    hemisphere_image_urls.append(hemispheres)
    
    # Browse back to find next hemisphere
    browser.back()

# Quit browser
browser.quit()


# In[18]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[ ]:




