#Import all the needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import seaborn as sns
import re
import collections
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image

#Store the tweets from txt file to json with all details and list data form
tweets_data = []
tweets_text = []
tweets_id=dict()
print("Parsing the text file")
for filename in ['result1.txt','result2.txt','result3.txt','result4.txt','result5.txt']:
    print("Parsing the text file",filename)
    with open(filename,'r') as file:
        number=0
        for line in file.read().split('\n'):
            field = line.split(' ')
            if field[0] in tweets_id:
                continue
            else:
                tweets_id[field[0]]=1
            tweets=dict()
            if len(field)<5:
                continue
            tweets['id']=field[0]
            tweets['date']=field[1]
            tweets['time']=field[2]
            temp=' '.join(field[4:])
            #temp=temp.replace(r'[a-zA-Z0-9]','')
            tweets['text']=temp
            tweets_text.append(temp)
            tweets_data.append(tweets)
            number+=1
        print(number," is the number of tweets")
    
        



print("The total number of Tweets is:",len(tweets_data))


#To see the most used hashtags.
hashtags = []
hashtag_pattern = re.compile(r"#[a-zA-Z0-9]+")
hashtag_matches=[]
for text in tweets_text:
    hashtag_matches.append(hashtag_pattern.findall(text))
hashtag_dict = {}
for match in hashtag_matches:
    for singlematch in match:
        if singlematch.lower() not in hashtag_dict.keys():
            hashtag_dict[singlematch.lower()] = 1
        else:
            hashtag_dict[singlematch.lower()] = hashtag_dict[singlematch.lower()]+1



#Making a list of the most used hashtags and their values
hashtag_ordered_list =sorted(hashtag_dict.items(), key=lambda x:x[1])
hashtag_ordered_list = hashtag_ordered_list[::-1]
#Separating the hashtags and their values into two different lists
hashtag_ordered_values = []
hashtag_ordered_keys = []
print(len(hashtag_ordered_list))
##print(hashtag_ordered_list)
#Pick the 30 most used hashtags to plot
  
for item in hashtag_ordered_list[4:30]:
    hashtag_ordered_keys.append(item[0])
    hashtag_ordered_values.append(item[1])
    
#Plotting a graph with the most used hashtags
fig, ax = plt.subplots(figsize = (12,12))
y_pos = np.arange(len(hashtag_ordered_keys))
ax.barh(y_pos ,list(hashtag_ordered_values)[::-1], align='center', color = 'green', edgecolor = 'black', linewidth=1)
ax.set_yticks(y_pos)
ax.set_yticklabels(list(hashtag_ordered_keys)[::-1])
ax.set_xlabel("No of appearances")
ax.set_title("Most used #hashtags", fontsize = 20)
plt.tight_layout(pad=3)
plt.show()

#Make a wordcloud plot of the most used hashtags, for this we need a #dictionary 
#where the keys are the words and the values are the number of #appearances
hashtag_ordered_dict = {}
for item in hashtag_ordered_list[4:90]:#leave the top 4 
    hashtag_ordered_dict[item[0]] = item[1]
#wordcloud = WordCloud(width=1000, height=1000, random_state=21, max_font_size=200, background_color = 'white').generate_from_frequencies(hashtag_ordered_dict)
mask = np.array(Image.open('india.jpeg'))
wordcloud = WordCloud(width=1000,height=1000,background_color="white",colormap="inferno",  max_font_size=30,min_font_size=5,mask=mask,
               random_state=7, max_words=200,contour_color='black').generate_from_frequencies(hashtag_ordered_dict)


image = wordcloud.to_image()
image.show()


#Similarly for mentions:
mentions = []
mention_pattern = re.compile(r"@[a-zA-Z_0-9]+")
mention_matches=[]
for text in tweets_text:
    mention_matches.append(mention_pattern.findall(text))

mentions_dict = {}
for match in mention_matches:
    for singlematch in match:
        if singlematch not in mentions_dict.keys():
            mentions_dict[singlematch] = 1
        else:
            mentions_dict[singlematch] = mentions_dict[singlematch]+1



#Create an ordered list of tuples with the most mentioned users and #the number of times they have been mentioned
mentions_ordered_list =sorted(mentions_dict.items(), key=lambda x:x[1])
##print(mentions_ordered_list[0],mentions_ordered_list[-1])
mentions_ordered_list = mentions_ordered_list[::-1]
#Pick the 20 top mentioned users to plot and separate the previous #list into two list: one with the users and one with the values
mentions_ordered_values = []
mentions_ordered_keys = []
print(len(mentions_ordered_list))
for item in mentions_ordered_list[0:20]:
    mentions_ordered_keys.append(item[0])
    mentions_ordered_values.append(item[1])


fig, ax = plt.subplots(figsize = (12,12))
y_pos = np.arange(len(mentions_ordered_values))
ax.barh(y_pos ,list(mentions_ordered_values)[::-1], align='center', color = 'yellow', edgecolor = 'black', linewidth=1)
ax.set_yticks(y_pos )
ax.set_yticklabels(list(mentions_ordered_keys)[::-1])
ax.set_xlabel("No of mentions")
ax.set_title("Most mentioned accounts", fontsize = 20)
plt.show()

#Make a wordcloud representation for the most mentioned accounts too
mentions_ordered_dict = {}
for item in mentions_ordered_list[:]:
    mentions_ordered_dict[item[0]] = item[1]
##wordcloud = WordCloud(width=1000, height=1000, random_state=21, max_font_size=200, background_color = 'white').generate_from_frequencies(mentions_ordered_dict)
mask = np.array(Image.open('india.jpeg'))
wordcloud = WordCloud(width=1000,height=1000,background_color="white",colormap="plasma", max_words=90, mask=mask,
               max_font_size=80,min_font_size=6, random_state=3, contour_color='black').generate_from_frequencies(mentions_ordered_dict)
image = wordcloud.to_image()
image.show()




