# LABELSY Z CSV POSORTOWANE

from pandas import DataFrame
import pandas as pd

data = pd.read_csv("./ptaki/train/ff1010bird_metadata_2018.csv") 
df = DataFrame(data, columns = ['itemid','hasbird'])
df.sort_values(by=['itemid'], inplace=True)
test=df.loc[:,"hasbird"]
labels = list(test)
#print((labels)[1:10])