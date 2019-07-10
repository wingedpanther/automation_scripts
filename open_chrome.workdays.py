import webbrowser
import datetime

now = datetime.datetime.now()
today_is = now.strftime("%A")
work_days = ['Sunday','Monday','Tuesday','Wednesday','Thursday']

if today_is in work_days:
    url = 'http://workemail.domain.name' #Work Email
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
