import os
import pandas as pd
os.getcwd() 
mydata1 = pd.read_csv("example-DEGs.csv")
mydata2 = pd.read_csv("ensembl-IDs.csv")
data1 =[]
data2 =[]
mydata3 = pd.DataFrame()
for i in mydata1["GeneID"]:
    for j in mydata2["GeneIDs"]:
        if i==j:
            for m in mydata1["Log2FC"][mydata1["GeneID"]==i]:
                data1.append(m)
                data2.append(i)

mydata3["GeneIDs"] = data2
mydata3["Log2FC Values"] =data1
data3 =[]
for i in range(len(data1)):
    m = "RNA {}".format(i)
    data3.append(m)
mydata3.index = data3
mydata3.to_csv("newCsvDoc.csv")
    

    
    
