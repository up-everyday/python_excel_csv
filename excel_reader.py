import csv
with open('egg.csv','r')as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
          
