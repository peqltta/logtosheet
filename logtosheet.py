import os
import pygsheets
client = pygsheets.authorize(service_account_file='service_account.json')
gsheet = client.open_by_key('1NOPx9VTeGiP00xnWtP0c-PXei6dy0kYnzsMZAu_yZSE')
wks = gsheet.sheet1
basepath = "./"
rows = []
prevlogs = wks.get_col(1)
prevlogs = list(filter(None, prevlogs))
print(prevlogs)

for filename in os.listdir(basepath):
    row = []
    if filename.endswith(".log"): 
        with open(basepath + filename) as openfile: 
            if filename not in prevlogs:
                row.append(filename) 
                for line in openfile:
                    if 'Selected winner!' in line:
                        row.append(line.strip())
                    if 'Delaying' in line:
                        row.append(line.strip())
                    if 'Logged' in line:
                        row.append(line.strip())
                    if 'Requesting' in line:
                        row.append(line.strip())
                rows.append(row)
i = 0
wks.update_values('A'+str(len(prevlogs)+1), rows)



