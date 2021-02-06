
from datetime import date
from datetime import time
from datetime import datetime

# Open a file for writing and create it if it doesn't exist
response = input("What did you do today (meditate, run, or swim)? ")
timeTaken = input("How long did it take you (mins)? ")
f = open("journalfile.txt", "a")
today = date.today()
entry = str(today) + ' --- ' + response + ', Amount of Time: ' + timeTaken + ' mins \n'
print(entry)
f.write(entry)



# close the file when done
f.close()