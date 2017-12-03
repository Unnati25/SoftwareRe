import pandas
import xlrd
import csv
import re
df = pandas.read_excel('C:\Users\Unnati\Downloads\jira.xlsx')
uniquenames = []

import numpy as np


for data in df['Assignee'].unique():
    if data is not 'Unassigned':
        try:
            uniquenames.append(str(data).encode("utf-8", errors='ignore'))
        except UnicodeEncodeError:
            continue
for data in df['Reporter'].unique():
    if data is not 'Unassigned':
        try:
            uniquenames.append(str(data).encode("utf-8", errors='ignore'))
        except UnicodeEncodeError:
            continue
for data in df['Creator'].unique():
    if data is not 'Unassigned':
        try:
            uniquenames.append(str(data).encode("utf-8", errors='ignore'))
        except UnicodeEncodeError:
            continue
#get a data frame with selected columns
FORMAT = ['Key', 'Assignee', 'Reporter','Creator']
df_selected = df[FORMAT]
networkOfContributors = {}
for index, row in df_selected.iterrows():
    if type(row[1]) is not float and type(row[2]) is not float and type(row[3]) is not float:
        try:
            setOne = row[1].encode("utf-8", errors='ignore')+ " "+ row[2].encode("utf-8", errors='ignore')
            setTwo = row[2].encode("utf-8", errors='ignore') + " " + row[3].encode("utf-8", errors='ignore')
            setThree = row[3].encode("utf-8", errors='ignore') + " " + row[1].encode("utf-8", errors='ignore')
        except UnicodeEncodeError:
            continue
        if setOne in networkOfContributors:
            networkOfContributors[setOne] += 1
        else:
            networkOfContributors[setOne] = 1
        if setTwo in networkOfContributors:
            networkOfContributors[setTwo] += 1
        else:
            networkOfContributors[setTwo] =1
        if setThree in networkOfContributors:
            networkOfContributors[setThree] += 1
        else:
            networkOfContributors[setThree] = 1

#print("hey")
#print(len(networkOfContributors))
#print(len(listOFContributors))
Matrix = [[0 for x in range(len(uniquenames))] for y in range(len(uniquenames))]
# for name in uniquenames:
#     print name,
with open('foo.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(uniquenames,)

#UniqueContributers =['Andreas Lehmkuhler','Tilman Hausherr','Adam Nichols','Maruan Sahyoun','John Hewson', 'Guillaume Bailleul','Thomas Chojecki','Jukka Zitting','Timo Boehme','Philipp Koch','Jeremias Maerki','Eric Leleu','asf-sync-process','Villu Ruusmann']
for i in range(0, len(uniquenames)):
    for j in range(0,len(uniquenames)):
        combo = uniquenames[i].encode('utf-8') + " " + uniquenames[j].encode('utf-8')
        if combo in networkOfContributors.keys():
            #print(combo)
            #print(networkOfContributors[combo])
            Matrix[i][j] = networkOfContributors[combo]
#np.savetxt("FILENAME.csv", Matrix, delimiter=",")
# a = np.asarray(Matrix)
# a.tofile('foo.csv',sep=',',format='%10.5f')

with open("file1", "wb") as f:
    writer = csv.writer(f,delimiter=",")

    writer.writerow(['index'] + uniquenames)
    # If your mat is already a python list of lists, you can skip wrapping
    # the rows with list()
    writer.writerows(uniquenames[i:i+1] + list(row) for i, row in enumerate(Matrix))
print(np.matrix(Matrix))


