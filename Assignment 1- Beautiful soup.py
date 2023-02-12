#!/usr/bin/env python
# coding: utf-8

# # Ques1 

# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[3]:


from bs4 import BeautifulSoup
import requests


# In[4]:


page=requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[5]:


page


# In[6]:


soup=BeautifulSoup(page.content)
soup


# In[7]:


header=[]
 
for i in soup.find_all('h2',class_="mp-h2"):
    header.append(i.text)
header


# In[8]:


# Making DATA FRAME
import pandas as pd
df = pd.DataFrame({'header':header})
df


# # Ques 2

# In[10]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[11]:


from bs4 import BeautifulSoup
import requests


# In[12]:


page=requests.get('https://www.imdb.com/list/ls055386972')


# In[13]:


page


# In[14]:


soup=BeautifulSoup(page.content)
soup


# In[15]:


movie=[i.text.split('\n')[2] for i in soup.find_all(class_="lister-item-header")]
movie


# In[16]:


rating=[i.text.strip() for i in soup.find_all('div',class_="ipl-rating-star small")]
     
rating   


# In[17]:


year=[]
 
for i in soup.find_all('span',class_="lister-item-year text-muted unbold"):
     year.append(i.text)
year 


# In[18]:


import pandas as pd
df=pd.DataFrame({'movie':movie,'rating':rating,'year':year})
df


# # Ques3 

# In[19]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[20]:


from bs4 import BeautifulSoup
import requests


# In[21]:


page=requests.get('https://www.imdb.com/list/ls077629380/')


# In[22]:


page


# In[23]:


soup=BeautifulSoup(page.content)
soup


# In[24]:


movie=[i.text.split('\n')[2] for i in soup.find_all(class_="lister-item-header")]
movie


# In[25]:


rating=[i.text.strip() for i in soup.find_all('div',class_="ipl-rating-star small")]
     
rating    


# In[26]:


year=[]
 
for i in soup.find_all('span',class_="lister-item-year text-muted unbold"):
     year.append(i.text)
year  


# In[27]:


import pandas as pd
df=pd.DataFrame({'movie':movie,'rating':rating,'year':year})
df


# # Ques4 
# 

# In[28]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[29]:


from bs4 import BeautifulSoup
import requests


# In[30]:


page=requests.get('https://presidentofindia.nic.in/former-presidents.htm')


# In[31]:


page


# In[32]:


soup=BeautifulSoup(page.content)
soup


# In[33]:


president=[]
 
for i in soup.find_all('h3'):
    president.append(i.text)

president


# In[34]:


term=[]
 
for i in soup.find_all('p'):
    term.append(i.text)

term


# In[35]:


term.pop(1)


# In[36]:


term.pop()


# In[37]:


term.pop()


# In[38]:


term.pop()


# In[39]:


term


# In[40]:


term.pop(2)


# In[41]:


term


# In[42]:


term.pop(5)


# In[43]:


term


# In[44]:


term.pop(3)


# In[45]:


len(term)


# In[46]:


import pandas as pd
df=pd.DataFrame({'president':president,'term':term})
df


# # Ques7

# In[47]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[48]:


from bs4 import BeautifulSoup
import requests


# In[49]:


page=requests.get('https://www.cnbc.com/world/?region=world')


# In[50]:


page


# In[51]:


soup=BeautifulSoup(page.content)
soup


# In[52]:


heading=[]
 
for i in soup.find_all('a',class_="LatestNews-headline"):
    heading.append(i.text)
heading


# In[53]:


time=[]
 
for i in soup.find_all('span',class_="LatestNews-wrapper"):
     time.append(i.text)
time     


# In[54]:


link=[]
 
for i in soup.find_all('a',class_="LatestNews-headline"):
    link.append(i.get('href'))
link


# In[55]:


import pandas as pd
df=pd.DataFrame({'heading':heading,'time':time,'link':link})
df


# # Ques 8

# In[56]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[57]:


from bs4 import BeautifulSoup
import requests


# In[58]:


page=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[59]:


page


# In[60]:


soup=BeautifulSoup(page.content)
soup


# In[61]:


titles=[]
 
for i in soup.find_all('a',class_="sc-5smygv-0 fIXTHm"):
    titles.append(i.text)
titles


# In[62]:


author=[]
 
for i in soup.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    author.append(i.text)
author


# In[63]:


date=[]
 
for i in soup.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    date.append(i.text)
date


# In[64]:


url=[]
for i in soup.find_all('a',class_="sc-5smygv-0 fIXTHm"):
    url.append(i.get('href'))
url


# In[65]:


import pandas as pd
df=pd.DataFrame({'titles':titles,'author':author,'date':date,'url':url})
df


# # Ques 9

# In[66]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[67]:


from bs4 import BeautifulSoup
import requests


# In[68]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[69]:


page


# In[70]:


soup=BeautifulSoup(page.content)
soup


# In[71]:


name=[]
 
for i in soup.find_all('a',class_="restnt-name ellipsis"):
    name.append(i.text)
name


# In[72]:


location=[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
location


# In[73]:


cuisine=[]
for i in soup.find_all('span',class_="double-line-ellipsis"):
    cuisine.append(i.text.split('|')[1])
cuisine


# In[74]:


ratings=[]
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    ratings.append(i.text)
ratings


# In[75]:


images=[]
for i in soup.find_all('img',class_="no-img"):
    images.append(i.get('data-src'))
images


# In[76]:


import pandas as pd
df=pd.DataFrame({'name':name,'location':location,'cuisine':cuisine,'ratings':ratings,'images_url':images})
df


# In[ ]:




