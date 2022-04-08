#read a csv file , remove last 2 rows from it and create new csv file using csv library not pandas

import csv

# open the file in read mode
file = open("/home/neosoft/Desktop/Position_Salaries.csv", "r")

# creating new file
new_file = open("Name_Data_Copied.csv", 'x')

data = csv.reader(file)
writer = csv.writer(new_file)

data_list = []

for row in data:
    data_list.append(row)


length = len(data_list)
print("Length of list is: "+str(length))

# it copies all the rows except last 2 rows into new file
for i in range(length-2):    
    writer.writerow(data_list[i]) 

file.close()           # closing the file

new_file.close()