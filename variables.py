import gspread
import gspread_formatting

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import *
import datetime
import pytz
from contextlib import closing
import sqlite3
import gspread_formatting

already_sent_number = ['my phone number is ', 'my cell is', 'my number is', 'Feel free to call me at', 'My contact information is', 'you can reach me at']

reply = """I'd love to discuss opportunities with you, what's a good number I can reach you at?"""

prompt_is_interested = """Please classify the following sentences and return 1 or 2. 1 if the person sounds like they may be interested to know more and talk with us and 2 if they are not interested or it's hard to tell.

Here are some examples for you that I classify as group 2 and you should classify similar ones as group 2 as well:

'I’m actually looking for help in my marketing dept if you’re interested'

'Will do. Thanks!'

'I’m not looking for a new role at this time'

'Congrats on your work anniversary!'

'Thanks Jonathan, it’s nice to meet you here.'

'Thank you, Jonathan L.'

'did you actually research me, my background, and my firm, before sending this to me?'

'I just don’t think that I would be a fit for any of these roles'

'I’m open for suggestions.'

'I’m not a good fit for the role, however a colleague would be perfect.'

'I'm happy to connect'

'I just left my firm in January and started a solo practice.  Pretty acrimonious split.  So not interested in another firm at this time.  I might consider in house if it were the right opportunity.'

'Great meeting you, Jonathan!' 

'Thanks Jonathan L., will do'

'Will do, thanks and have a good weekend!'

'Thanks Jonathan!'

Here's the actual client's reply:
"""

# Define the Eastern Standard Time (EST) timezone
est_tz = pytz.timezone('US/Eastern')

print('connecting to browser')
opt = Options()

opt.add_experimental_option('debuggerAddress', 'localhost:9222')
try:
    browser = webdriver.Chrome(service=Service(executable_path="/usr/bin/chromedriver"), options=opt)
except:
    browser = webdriver.Chrome(service=Service(executable_path="chromedriver.exe"), options=opt)
action = ActionChains(browser)

print('found browser')

# connect to GS
gc = gspread.service_account(filename='creds.json')
google_sheet = gc.open('JLB dripify leads')
sheet = google_sheet.worksheet('Sheet1')

print('connected to GS')