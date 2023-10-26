#First import all the necessary libraries

from matplotlib import pyplot as pyp
import pandas as pd
import numpy as np
import seaborn as sb


# # #IMPORT U.DATA

# # mine = pd.read_csv("C:/Users/felia/OneDrive/Desktop/Python Practicals/ml-100k/ml-100k/u.data",
##                   sep='\t',names=['user id', 'item id', 'rating', 'timestamp'])
# # #mine.head()



# #IMPORT U.ITEM

# col = ['movie id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure', 'Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
# mini = pd.read_csv("C:/Users/felia/OneDrive/Desktop/Python Practicals/ml-100k/ml-100k/u.item",sep='|', encoding = 'latin-1', names= col)

#mini1= mini.drop(mini.columns[3:5], axis=1)  #DROP UNNECESSARY COLUMNS
#mini1.head()

#mini1['unknown'].value_counts()  # sum of appearance of each value in unknown

# #looking at the counts of individual genres
# l = []
# for i in mini1.loc[:,'unknown' : 'Western'].columns:
#     b = mini1[i].value_counts()[1]
#     l.append(b)
# print(l)
# print(mini1.loc[:,'unknown' : 'Western'].columns)

# mini1[mini1['unknown']==1]  #unknown has just 2 significant entries

# mine[mine['item id']==1373]  #lets check its rating to see if the genre 'unknown' is significant

# mine[mine['item id']==267]  #checking if the genre 'unknown' is significant


# mini1.drop(mini1[mini1['unknown'] == 1].index, axis=0, inplace=True)
# mini1.drop(columns= 'unknown', inplace=True) #unknown genre consist of only 2 movie id's with rlatively low ratings, we drop it


# mini1.isna().apply(pd.value_counts)  #missing value check



# # #IMPORT U.USER
mina = pd.read_csv("C:/Users/felia/OneDrive/Desktop/Python Practicals/ml-100k/ml-100k/u.user",
                    sep='|',names=['user id', 'age', 'gender', 'occupation', 'zip code'])
mina.isna().apply(pd.value_counts)  #missing value check



# GENDER DISTRIBUTION

fig, ax = pyp.subplots()
x = mina.gender.value_counts().index    #Values for x-axis
y = [mina['gender'].value_counts()[i] for i in x]   #count on y-axis 

bar_labels = ['blue','pink']
bar_colors = ['tab:blue', 'tab:pink']

ax.bar(x,y, align='center', label=bar_labels, color=bar_colors, edgecolor = 'black', alpha = 0.7)  #plot a bar chart
pyp.xlabel('Gender')
pyp.ylabel('Count')
pyp.title('Gender Distribution')
pyp.legend(title='Gender Color')

pyp.show()


# #DISTRIBUTION OF OCCUPATION
# pyp.figure(figsize=(15,8))
# mat = sb.countplot(mina['occupation'], color= 'lightblue')
# pyp.yticks(rotation=0)
# pyp.xticks(rotation=90)
# pyp.show()



#DISTRIBUTION OF RELEASE DATE
# # pyp.figure(figsize=(10,10))
# # myn = sb.histplot(mini['release date']) 
# # pyp.show(myn)



#DISTRIBUTION OF RATING

#pyp.figure(figsize=(10,10))
# # mon = sb.histplot(mine['rating']) 
# # pyp.show()