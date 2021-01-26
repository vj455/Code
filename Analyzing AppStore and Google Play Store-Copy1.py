#!/usr/bin/env python
# coding: utf-8

#    # Analyze Appstore & Google Play Store
#    
#    In this project we are going to analyze the appstore, both Google Play and App Store by Apple for our\ developers to better understand the market and user behaviour. We will be providing with detailed analysis entailing but not limited to User Rating based off the categories of apps. The analysis would further be deconstructed by age, sex and demographics.
#    
#    After the analysis the software developers would be in a better position to choose the correct market and type of the app that they would like to build. 

# In[1]:


# Defining Explore_Data function to explore a slice of the dataset
from csv import reader

### The Google Play data set ###
opened_file = open('/Users/vishrutjain/my_datasets/googleplaystore.csv')
read_file = reader(opened_file)
android = list(read_file)
android_header = android[0]
android = android[1:]

### The App Store data set ###
opened_file = open('/Users/vishrutjain/my_datasets/AppleStore.csv')
read_file = reader(opened_file)
ios = list(read_file)
for i in ios:
    del i[0]
ios_header = ios[0]
ios = ios[1:]
        
def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line between rows
        
    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))

print(android_header)
print('\n')
explore_data(android, 0, 3, True)

print(ios_header)
print('\n')
explore_data(ios, 0, 3, True)


# In[2]:


for row in ios:
    if len(row) != len(ios_header):
        print(row)
        print(ios.index(row))    

wrong_data = []
for row in ios:
    if len(row) !=len(ios_header):
        #print(row) #this will print the row data.
        wrong_data.append(row)       

print(wrong_data)        

        


# In[3]:


for row in android:
    if len(row) != len(android_header):
        print(android_header)
        print(row)
        print(android.index(row))

        #del(android[10472]) -- Delete the rows where number of cols dont match to number of headers


# In[4]:


#print(android_header)
#print(android[10472])

wrong_data = []
for row in android:
    if len(row) !=len(android_header):
        #print(row) #this will print the row data.
        wrong_data.append(row)       

print(wrong_data)        


# ### Deleting the Wrong Data
# 
# Above we identify rows where the number of columns in our header do not match the number of columns in our data set. This helps us get rid of any data that might create false results and insights or fail the compilation of the program.

# In[5]:


del android[10472]


# In[6]:


for row in ios:
    if len(row) !=len(ios_header):
        print(row) #this will print the row data.
        print(ios.index(row))


# ### Duplicate Data
# 
# In the next section of the project we want to identify the duplicate values in our data set so the accuracy of the insights we provide is not compromised.
# For this we create 2 lists. Unique and Duplicate. We then loop through our data set. If the name (stored in a variable) already exists in our Unique List then we append that name into Duplicate List. Hence providing us with a fresh list of names of Unique Values in our data set.

# In[7]:


# Search for duplicates in the data set and identify which 
# criteria is best to remove duplicate from our data set

duplicate_name = []
unique_name = []
for row in android:
    name = row[0]
    if name in unique_name:
        duplicate_name.append(name)
    else:
        unique_name.append(name)

print(len(duplicate_name))        
print(len(unique_name))        


# In[8]:


duplicate_name_ios = []
unique_name_ios = []
for row in ios:
    name = row[1]
    if name in unique_name_ios:
        duplicate_name_ios.append(name)
    else:
        unique_name_ios.append(name)

print(len(duplicate_name_ios))  
print(duplicate_name_ios)
for row in ios:
    name = row[1]
    if name == "VR Roller Coaster" or name == "Mannequin Challenge":
        print(row)
        print('\n')
print(len(unique_name_ios))    


# Using Dictionary to Identify the correct record
# Now that we have our unique list and duplicate list. We want to make sure that we keep the most current row of the our duplicate records giving us the latest and most up to date information to calculate the profitability of the apps in Google Play Store.

# In[9]:


print(ios_header)
print(ios[1:5])


# In[10]:


reviews_max_ios = {}

for app in ios:
    name = app[1]
    n_reviews = float(app[5])
    
    if name in reviews_max_ios and reviews_max_ios[name] < n_reviews:
        reviews_max_ios[name] = n_reviews
        
    elif name not in reviews_max_ios:
        reviews_max_ios[name] = n_reviews      


# In[11]:


print("Total Duplicates: ", len(duplicate_name_ios))

x = len(unique_name_ios)

print("Expected_list:", str(x))

print("Actual Review_Max Length:", str(len(reviews_max_ios)))


# In[12]:


reviews_max = {}

for app in android:
    name = app[0]
    n_reviews = float(app[3])
    
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
        
    elif name not in reviews_max:
        reviews_max[name] = n_reviews  
print(len(reviews_max))        


# In[13]:


print("Total Duplicates: ", len(duplicate_name))

x = len(unique_name)

print("Expected_list:", str(x))

print("Actual Review_Max Length:", str(len(reviews_max)))


# Creating Clean List
# The final step in achieving our final data set is to append each row for each app once into a clean data set.
# To achieve this we start with 2 empty list: Android_Clean and Already_Added
# We then loop through our old data set and assign Name and Number of Reviews to 2 variables that are Name and n_reviews.
# We then check if the number of reviews in our variable match the number of reviews for that particular application in our dictionary and the name does not already exist in our list of list "already_added" then we append that entire row into our list of list Android Clean.

# In[14]:


android_clean = []
already_added = []

for row in android:
    name = row[0]
    n_reviews = float(row[3])
    
    if n_reviews == reviews_max[name] and name not in already_added:
        android_clean.append(row)
        already_added.append(name)

print(android_clean[1], '\n')
print(len(android_clean))


# In[15]:


print(android_clean[2])


# Function to identify non English letters for deleting apps that are not catered to English speaking audience

# In[16]:


android_final =[]
def is_english(characters):
    counter = 0
    for char in characters:
        if ord(char) > 127:
            counter += 1
        if counter > 3:
            return False
    return True

print(is_english('Instagram'))
print(is_english('爱奇艺PPS -《欢乐颂2》电视剧热播'))
print(is_english('Docs To Go™ Free Office Suite'))
print(is_english('Instachat 😜'))

android_english = []
ios_english = []

for app in android_clean:
    name = app[0]
    if is_english(name):
        android_english.append(app)
        
for app in ios:
    name = app[1]
    if is_english(name):
        ios_english.append(app)
        
explore_data(android_english, 0, 3, True)
print('\n')
explore_data(ios_english, 0, 3, True)
        


# In[17]:


android_free = []
for i in android_english:
    price = i[7]
    if price == '0':
        android_free.append(i)
        
print(len(android_free))  
print(len(android_english)) 
print(android_free[1:5])


# In[18]:


ios_free = []
for i in ios_english:
    price = float(i[4])
    if price == 0.0:
        ios_free.append(i)
        
print(len(ios_free)) 
print(len(ios_english))
print(ios_free[1:5])


# We used multiple techniques to identify false data in our set which are: 
# 
# - Removing Duplicates
# - Remove incomplete data rows
# - Use only apps that are targeted to English speaking Audience
# - Picked apps which are Free
# 
# After cleaning our data set we are left with 8864 apps in our googplaystore data set and 3222 in apple store data set. 

# In[19]:


print(ios_header) # prime genre: 12, 
print(ios_free[1])

print('\n')

print(android_header) # Genres : 8, Category: 2
print(android_free[1])


# # Most Common Apps by Genre
# 
# ## Part One
# 
# As we mentioned in the introduction, our aim is to determine the kinds of apps that are likely to attract more users because our revenue is highly influenced by the number of people using our apps.
# 
# To minimize risks and overhead, our validation strategy for an app idea is comprised of three steps:
# 
# - Build a minimal Android version of the app, and add it to Google Play.
# - If the app has a good response from users, we then develop it further.
# - If the app is profitable after six months, we also build an iOS version of the app and add it to the App Store.
# 
# Because our end goal is to add the app on both the App Store and Google Play, we need to find app profiles that are successful on both markets. For instance, a profile that might work well for both markets might be a productivity app that makes use of gamification.
# Let's begin the analysis by getting a sense of the most common genres for each market. For this, we'll build a frequency table for the prime_genre column of the App Store data set, and the Genres and Category columns of the Google Play data set.
# 
# Part Two
# 
# We'll build two functions we can use to analyze the frequency tables:
# 
# - One function to generate frequency tables that show percentages
# - Another function that we can use to display the percentages in a descending order

# In[38]:


def freq_table(dataset, index):
    
    freq_dict = {}
    total = 0
    for row in dataset:
        total += 1
        col = row[index]
        if col in freq_dict:
            freq_dict[col] += 1
        else:
            freq_dict[col] = 1
    
    table_percentage = {}
    for key in freq_dict:
        percentage = (freq_dict[key]/total)*100
        percentage = round(percentage,2)
        table_percentage[key] = percentage
    return table_percentage


# In[39]:


def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])


# In[41]:


print("Most Popular Free Android APP by Category")
print('\n')
display_table(android_free, 1)

print('\n')

print("Most Popular Free Android APP by Genre")
print('\n')
display_table(android_free, 9)

print('\n')

print("Most Popular Free IOS APP by Genre")
print('\n')
display_table(ios_free, 11)


# ## Android App Analysis
# 
# As seen above the best way to draw assumptions and give recommendation for android apps should be based on the Category and not Genre. As the Genre in the android development is more detailed and doesn't let us pin down one category or area of category to build our app in. Based on the above data we can assume:
# 
# - Apps associated to Families have a hefty lead when it comes to Free apps catered to English speaking audience. 
# - Games are the second most popular which can be further categorized based on the detailed level analysis through the genre distribution closely followed by Tools. 
# - the next 8 popular types of apps are in close competition to each other including Business, Lifestyle, Sports, Medical and Finance. 
# 
# 
# ## IOS App Analysis
# 
# While the IOS appstore tells a different story. Based on the distribution of the apps on appstore:
# 
# - Games are the most identified apps in the appstore. 
# - The games take up more than half of the number of apps on the appstore with the filters of being free and English centric being in place. 
# - The next type of app Entertainment and Photo and Video apps are far behind the games but closely following each other. 
# 
# ***One important thing to note here is that these numbers just suggest the most number of type of applications in both these stores available with special filters in place. The popularity among users, number of downloads, average rating for such categories is not disclosed thus not telling the complete picture. 
# But at the same time its safe to say that Games being equally popular in both these stores gives some confidence that such applications are high in demand and would recommend our developers to build apps in a similar category.
# 
# 

# In[42]:


ios_genre = freq_table(ios_free, 11)
ios_genre

for genre in ios_genre:
    total = 0
    len_genre = 0
    for row in ios_free:
        genre_app = row[11]
        if genre_app == genre:
            total += float(row[5])
            len_genre += 1
            
    average_user_rating = round((total/len_genre),2)
    
    print(genre,' : ',average_user_rating)


# On average, navigation apps have the highest number of user reviews, but this figure is heavily influenced by Waze and Google Maps, which have close to half a million user reviews together.
# 
# 
# The same pattern applies to social networking apps, where the average number is heavily influenced by a few giants like Facebook, Pinterest, Skype, etc. Same applies to music apps, where a few big players like Pandora, Spotify, and Shazam heavily influence the average number.
# 
# Our aim is to find popular genres, but navigation, social networking or music apps might seem more popular than they really are. The average number of ratings seem to be skewed by very few apps which have hundreds of thousands of user ratings, while the other apps may struggle to get past the 10,000 threshold. We could get a better picture by removing these extremely popular apps for each genre and then rework the averages, but we'll leave this level of detail for later.
# 
# Reference apps have 74,942 user ratings on average, but it's actually the Bible and Dictionary.com which skew up the average rating.
# 
# However, this niche seems to show some potential. One thing we could do is take another popular book and turn it into an app where we could add different features besides the raw version of the book. This might include daily quotes from the book, an audio version of the book, quizzes about the book, etc. On top of that, we could also embed a dictionary within the app, so users don't need to exit our app to look up words in an external app.
# This idea seems to fit well with the fact that the App Store is dominated by for-fun apps. This suggests the market might be a bit saturated with for-fun apps, which means a practical app might have more of a chance to stand out among the huge number of apps on the App Store.
# Other genres that seem popular include weather, book, food and drink, or finance. The book genre seem to overlap a bit with the app idea we described above, but the other genres don't seem too interesting to us:
# Weather apps — people generally don't spend too much time in-app, and the chances of making profit from in-app adds are low. Also, getting reliable live weather data may require us to connect our apps to non-free APIs.
# Food and drink — examples here include Starbucks, Dunkin' Donuts, McDonald's, etc. So making a popular food and drink app requires actual cooking and a delivery service, which is outside the scope of our company.
# Finance apps — these apps involve banking, paying bills, money transfer, etc. Building a finance app requires domain knowledge, and we don't want to hire a finance expert just to build an app.
# 
# Now let's analyze the Google Play market a bit.
# 
# ## Most Popular Apps by Genre on Google Play
# 
# For the Google Play market, we actually have data about the number of installs, so we should be able to get a clearer picture about genre popularity. However, the install numbers don't seem precise enough — we can see that most values are open-ended (100+, 1,000+, 5,000+, etc.):

# In[46]:


android_genre = freq_table(android_free, 1)

android_genre

for category in android_genre:
    total = 0
    len_category = 0
    for row in android_free:
        category_app = row[1]
        if category == category_app:
            n_installs = row[5]
            n_installs = n_installs.replace('+','')
            n_installs = n_installs.replace(',','')
            total += float(n_installs)
            len_category += 1
    average_installs = round(total/len_category,2)
    print(category, ' : ', average_installs)


# The book and reference genre includes a variety of apps: software for processing and reading ebooks, various collections of libraries, dictionaries, tutorials on programming or languages, etc. It seems there's still a small number of extremely popular apps that skew the average.
# 
# It looks like there are only a few very popular apps, so this market still shows potential. Let's try to get some app ideas based on the kind of apps that are somewhere in the middle in terms of popularity.
# 
# On average, communication apps have the most installs: 38,456,119. This number is heavily skewed up by a few apps that have over one billion installs (WhatsApp, Facebook Messenger, Skype, Google Chrome, Gmail, and Hangouts), and a few others with over 100 and 500 million installs.
# 
# If we removed all the communication apps that have over 100 million installs, the average would be reduced roughly ten times.
# 
# We see the same pattern for the video players category, which is the runner-up with 24,727,872 installs. The market is dominated by apps like Youtube, Google Play Movies & TV, or MX Player. The pattern is repeated for social apps (where we have giants like Facebook, Instagram, Google+, etc.), photography apps (Google Photos and other popular photo editors), or productivity apps (Microsoft Word, Dropbox, Google Calendar, Evernote, etc.).
# 
# Again, the main concern is that these app genres might seem more popular than they really are. Moreover, these niches seem to be dominated by a few giants who are hard to compete against.
# 
# The game genre seems pretty popular, but previously we found out this part of the market seems a bit saturated, so we'd like to come up with a different app recommendation if possible.

# In[ ]:




