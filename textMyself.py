import schedule
import time
from twilio.rest import Client


account_sid = ""
auth_token = ""

twilioNumber = ''

client = Client(account_sid, auth_token)

def textmyself():
	print("Please enter a message you wish to send in the text: ")	
	message = input()
	print("Please enter your target number: " + "in this form:")
	target = input()
	client.api.account.messages.create(
	    to=target,
	    from_=twilioNumber,
    	    body=message)


def textdaily(message):
	client.api.account.messages.create(
	    to='',
	    from_=twilioNumber,
    	    body=message)


schedule.every().day.at("04:00").do(textdaily, "You got this bro")

schedule.every().day.at("07:20").do(textdaily, "Ayyy they gonna watch your CSPAN today")

schedule.every().day.at("08:20").do(textdaily, "Do dat chemistry")

schedule.every().day.at("09:13").do(textdaily, "Oof advisory time")

schedule.every().day.at("09:35").do(textdaily, "Get your science on you ready for the test?")

schedule.every().day.at("10:28").do(textdaily, "Stuff your face time")

schedule.every().day.at("11:03").do(textdaily, "Have fun with your socrative seminar")

schedule.every().day.at("11:51").do(textdaily, "Oh la la!!! Tu vas au salle de francais")

schedule.every().day.at("12:44").do(textdaily, "Have fun doing nothing in resource")

schedule.every().day.at("13:37").do(textdaily, "Have fun in tech dr/design")

schedule.every().day.at("14:30").do(textdaily, "School is over, now you gots homework to do")

schedule.every().day.at("16:00").do(textdaily, "Start studying math")

schedule.every().day.at("17:30").do(textdaily, "Chemistry")

schedule.every().day.at("18:15").do(textdaily, "Physics")

schedule.every().day.at("19:00").do(textdaily, "SAT PREP")

schedule.every().day.at("19:45").do(textdaily, "You are free to go soldier!")


while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute


