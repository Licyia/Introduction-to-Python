#First import all the necessary libraries

from matplotlib import pyplot as pyp
import pandas as pd
import numpy as np
import seaborn as sb


#IMPORT U.DATA

mine = pd.read_csv("C:/Users/felia/OneDrive/Desktop/Python Practicals/ml-100k/ml-100k/u.data",
                  sep='\t',names=['user id', 'item id', 'rating', 'timestamp'])
#mine.head()



# # #IMPORT U.ITEM

col = ['movie id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure', 'Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
mini = pd.read_csv("C:/Users/felia/OneDrive/Desktop/Python Practicals/ml-100k/ml-100k/u.item",sep='|', encoding = 'latin-1', names= col)

mini1= mini.drop(mini.columns[3:5], axis=1)  #DROP UNNECESSARY COLUMNS
mini1.head()
mini1['unknown'].value_counts()  # sum of appearance of each value in unknown


# #looking at the counts of individual genres
l = []
for i in mini1.loc[:,'unknown' : 'Western'].columns:
     b = mini1[i].value_counts()[1]
     l.append(b)
print(l)
print(mini1.loc[:,'unknown' : 'Western'].columns)


##CHECKING FOR SIGNIFICANT ENTRIES
mini1[mini1['unknown']==1]  #unknown has just 2 significant entries
mine[mine['item id']==1373]  #lets check its rating to see if the genre 'unknown' is significant
mine[mine['item id']==267]  #checking if the genre 'unknown' is significant


###unknown genre consist of only 2 movie id's with relatively low ratings, we drop it
mini1.drop(mini1[mini1['unknown'] == 1].index, axis=0, inplace=True)
mini1.drop(columns= 'unknown', inplace=True) 


#missing value check
mini1.isna().apply(pd.value_counts) 



# # # # #IMPORT U.USER
mina = pd.read_csv("C:/Users/felia/OneDrive/Desktop/Python Practicals/ml-100k/ml-100k/u.user",
                     sep='|',names=['user id', 'age', 'gender', 'occupation', 'zip code'])
mina.isna().apply(pd.value_counts)  #missing value check



# # # GENDER DISTRIBUTION

# fig, ax = pyp.subplots()
# x = mina.gender.value_counts().index    #Values for x-axis
# y = [mina['gender'].value_counts()[i] for i in x]   #count on y-axis 

# bar_labels = ['blue','pink']
# bar_colors = ['tab:blue', 'tab:pink']

# ax.bar(x,y, align='center', label=bar_labels, color=bar_colors, edgecolor = 'black', alpha = 0.7)  #plot a bar chart
# pyp.xlabel('Gender')
# pyp.ylabel('Count')
# pyp.title('Gender Distribution')
# pyp.legend(title='Gender Color')

# pyp.show()


# # #DISTRIBUTION OF OCCUPATION
# pyp.figure(figsize=(15,8))
# mat = sb.countplot(mina['occupation'], color= 'lightblue')
# pyp.yticks(rotation=0)
# pyp.xticks(rotation=90)
# pyp.show()



# #DISTRIBUTION OF RELEASE DATE
# mini1['release_year'] = mini1['release date'].str.split('-', expand = True)[2]  #seperating out the year from the date
# mini1['release_year'] = mini1.release_year.astype(int)  # changing the type to int
# pyp.figure(figsize=(15,6))    #increasing the figure size
# sb.distplot(mini1.release_year)
# pyp.show()



# #DISTRIBUTION OF RATING

# x = mine.rating.value_counts().index    #Values for x-axis
# y = [mine['rating'].value_counts()[i]/1000 for i in x]   #count(in thousands) on y-axis


# pyp.bar(x,y, align='center',color = 'blue',edgecolor = 'black', alpha = 0.7)  #plot a bar chart
# pyp.xlabel('Stars')
# pyp.ylabel('Count (in thousands)')
# pyp.title('Rating')
# pyp.show()


#VISUALIZATION OF HoW POPULARITY OF GENRES HAS CHANGED OVER THE YEARS

#genre_by_year = mini1.groupby('release_year').sum()
# genre_by_year = genre_by_year.drop(columns = 'movie id').T
# genre_by_year
#print(mini1.release_year)


#setting the figure size
# pyp.figure(figsize=(15,7))  
# sns.heatmap(genre_by_year, cmap='YlGnBu')  #heat map to plot the above table
# pyp.show()


#Display the top 25 movies by average rating,as a list/series/dataframe.
#Note:-Consider only the movies which received atleast a 100 ratings


mak = mine.groupby('itemid').count()
# mak= mak[mine.groupby('itemid').count().userid > 100].index
# mak = mine.loc[mine.itemid.isin(mak)]
# mak= mak.groupby('itemid').mean()
# mak = mak.sort_values('rating',ascending = False)
# order = mak.index
