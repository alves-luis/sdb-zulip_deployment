import sys
import csv
import random

num_users = int(sys.argv[1])

row_list = [["EMAIL","PASSWORD","PRIVATE_TO"]]

for i in range(num_users):
    row = ["user"+str(i+1)+"@email.com","exemplo","user"+str(random.randint(1,num_users))+"@email.com"]
    row_list.append(row)

with open(str(num_users)+'users.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)
