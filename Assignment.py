#First import all the necessary libraries
from matplotlib import pyplot as pyp
import pandas as pd
import numpy as np
import seaborn as sb

#IMPORT U.DATA
mine = pd.read_csv("C:/Users/felia/OneDrive/Desktop/Python Practicals/ml-100k/ml-100k/u.data",
                   sep='\t',names=['user id', 'item id', 'rating', 'timestamp'])
#print(mine.head())

#IMPORT U.ITEM
col = ['movie id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure', 'Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
mini = pd.read_csv("C:/Users/felia/OneDrive/Desktop/Python Practicals/ml-100k/ml-100k/u.item",sep='|', encoding = 'latin-1', names= col)
#print(mini.head())
pyp.figure(figsize=(10,10))
myn = sb.histplot(mina['release date']) 
pyp.show(mat)

#IMPORT U.USER
#mina = pd.read_csv("C:/Users/felia/OneDrive/Desktop/Python Practicals/ml-100k/ml-100k/u.user",
#                   sep='|',names=['user id', 'age', 'gender', 'occupation', 'zip code'])
#print(mina.head())
#my = sb.distplot(mina['age'])
#man = sb.histplot(mina['gender'])
#pyp.figure(figsize=(10,10))
#mat = sb.histplot(mina['occupation'])
#pyp.show(mat)
# rating relase date age gender occupation