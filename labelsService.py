# LABELSY Z CSV POSORTOWANE

from pandas import DataFrame
import pandas as pd

data = pd.read_csv("./ptaki/train/ff1010bird_metadata_2018.csv") 
df = DataFrame(data, columns = ['itemid','hasbird'])
df.sort_values(by=['itemid'], inplace=True)
test=df.loc[:,"hasbird"]
test2=df.loc[:, "itemid"]
items = list(test2)
labels = list(test)
#print((items)[0:10])
#print((labels)[0:10])
#print(len(labels))