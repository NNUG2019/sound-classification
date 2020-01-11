from datasetTest import testdatalist
import csv
import pandas as pd
import numpy as np

testdatalist
for i in range(len(testdatalist)):
    testdatalist[i] = testdatalist[i][:-4] #usuwanie .png

my_df = pd.DataFrame(testdatalist)
my_df.to_csv('out.csv', index=False, header=False)
