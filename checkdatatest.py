#Sprawdzam czy dane do testowania są w tej samej kolejności co labelsy

from datasetTest import X_testdata, testdatalist
from masklabels import dumperlabels, dumperitemid
import numpy as np

testdatalabels = dumperlabels
print(testdatalist[0:10])
print(testdatalabels[0:10])
print(np.unique(dumperlabels))
print(dumperlabels)
