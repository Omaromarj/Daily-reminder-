from datetime import date, datetime
import requests
import random

def clock():
    hours = datetime.now().hour
    min = datetime.now().minute


def Today():
    dare = str(date.today()).split('-')
    year1 = int(dare[0])
    month1 = int(dare[1])
    day1 = int(dare[2])
    return [date(year1, month1, day1), str(year1)+"?"+str(month1)+"?"+str(day1)]

def numOfDays(date1, date2):
    if date2 > date1:   
        return (date2-date1).days
    else:
        return (date1-date2).days
def reat():
    return open('data.txt','r').read()
def rite(text):
    open('data.txt', 'w').write(text)

def sendmsg(text):
    token = '8198959843:AAFFqPSvAQ2Ry4DiUl3FgB7LXtEQiCRfKXE'
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    parms = {'chat_id': '7909662095', 'text': text}
    print(requests.post(url, data=parms).text)
    
def main():
    a="1"
    if a == "yes":
        a = True
        last_nut = Today()
        print("...")
    else:
        a = False
        last = reat().splitlines()[1].split("?")
        daay = int(last[2])
        moonth = int(last[1])
        yeaar = int(last[0])
        print(last)
        last_nut = [date(yeaar, moonth, daay), str(yeaar)+"?"+str(moonth)+"?"+str(daay)]
        
    the_between = numOfDays(last_nut[0], Today()[0])
    daytext = f"{the_between}"
    if daytext == reat():
        pass
    else:
        msg = [f'keep it up {daytext} days 💪🏿!', f"يا بطل يا بطل استمرر {daytext} يوم 😍"]
        msg = random.choice(msg) 
        rite(daytext+"+\n"+last_nut[1])
        sendmsg(msg)
        
        
        #print(the_between)
main()