#Maska do pliku Crowdsourced dataset, UK ("warblrb10k") - 1000 obrazków
from pandas import DataFrame
import pandas as pd
from datasetTest import testdatalist

dataloading = pd.read_csv("./ptaki/test/warblrb10k_public_metadata_2018.csv")
df = DataFrame(dataloading, columns = ['itemid','hasbird'])
itemid = df.loc[:, "itemid"]

dumperloading = pd.read_csv("./out.csv")
dumper = DataFrame(dumperloading, columns = ['itemid'])
dumpermerge = pd.merge(dumper, df, how='left', left_on='itemid', right_on='itemid')

dumperlabels = list(dumpermerge.loc[:, "hasbird"])
dumperitemid = list(dumpermerge.loc[:, "itemid"])
