"""
Scraping Twitter data!
Below code run in spider and must be run in parts on the specificied data. 
Four Steps:
1. Get a list of all MP's twitter handles. 
2. Extract the specific @ and remove the @ from the name as twitter url's work 
without the @
3. We need to generate twitterscrapper command lines to be fed into the command line
4. once pasted into the command line we now have a list of json files. these files now
are converted into CSV files. 

!!!Ensure directories match up!!!

"""

#Step 1 - Obtain list of handles

import pandas as pd
#Step 1 get a list of all MP's twitter handles
dfs = pd.read_html('https://www.mpsontwitter.co.uk/list',header=0)
for df in dfs:
    print(df)

mps = df.loc[:,['Name','Screen Name','Party','Followers']]

###if needed the above data is converted into CSV format
mps.to_csv('members_data.csv')

#Step 2 - remove the twitter names from the datafram and separate name from @ symbol.

##separate list of handles
list_of_handles = []

for index,row in mps.iterrows():
    list_of_handles.append(row['Screen Name'])

##separate @ symbol from actual handle
j = 0
new = []
for i in list_of_handles:    
    y = i.strip('@')
    new.append(y)
    j += 1

#Step 3 - generates twitterscrapper command lines to be inputted
code = []
for i in new:
     code.append('twitterscraper {} -u -o {}.json'.format(i,i))   

###this gets from the code list in batches of 100 or so. change x <= 581 to get all. 
x = 0 
for i in code:
    if x <= 100:
        print(i)
        x += 1
    else:
        break

#Step 4 - convert to CSV files
import json
import re
import csv

y = 0
for a in new:
    try:
        if y <= 100:
            with open('{}.json'.format(a)) as f:
                data = json.load(f) 
            
            new_dict = {}
            timestamp_increment = 0
            html_increment = 0  
            for i in data: 
                timestamp = data[timestamp_increment]['timestamp']
                tweetOne = data[html_increment]['html']
                tweetTwo = re.sub('<[^>]+>', '', tweetOne)
                new_dict[timestamp] = tweetTwo
                timestamp_increment += 1
                html_increment += 1
            
            #print(new_dict)
            
            w = csv.writer(open("{}.csv".format(a),"w"))
            for key,val in new_dict.items():
                w.writerow([key,val])
            y += 1
        else:
            break
    #need this try except block as sometimes not all json files are there. 
    except FileNotFoundError:
        pass

