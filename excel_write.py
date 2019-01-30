import csv
with open('egg2.csv','w') as csvfile:
##    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|',
##                             quoting=csv.QUOTE_MINIMAL)
    spamwriter = csv.writer(csvfile,dialect='excel')
    spamwriter.writerow(['a','1','1','2','2',])
    spamwriter.writerow(['b','3','3','6','4',])
    spamwriter.writerow(['c','7','7','10','4',])
    spamwriter.writerow(['d','1','1','2','2',])
