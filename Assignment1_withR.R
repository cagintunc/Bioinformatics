

my_data1 <- read.csv("example-DEGs.csv")
my_data2 <- read.csv("ensembl-IDs.csv")
data1 <- c()
data2 <- c()
for(i in my_data1["GeneID"]){
  for(m1 in i){
    for(j in my_data2["GeneIDs"]){
      for(m2 in j){
        if(m1 == m2){
          data1 <- c(data1,my_data1["Log2FC"][my_data1["GeneID"]==m1])
          data2 <- c(data2,m1)
        }
      }
    }
  }
}
rm(my_data2["GeneIDs"])
my_data2["GeneIDs"] <- data2
my_data2["Log2FC Values"] <- data1
write.csv(my_data2, file = "newCsvDoc.csv")






