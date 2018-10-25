import schedule
import time
from twilio.rest import Client


account_sid = "AC6539b20aac8f122fccd2654f98c57fad"
auth_token = "9b568826df59a8b04aaae9fb307c0c17"

twilioNumber = '+1 910 415 1870'

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
	    to='+1 848 234 5354',
	    from_=twilioNumber,
    	    body=message)


schedule.every().day.at("07:30").do(textdaily, "Yeet 1")
schedule.every().day.at("08:30").do(textdaily, "Yeet 2")
schedule.every().day.at("10:30").do(textdaily, "Yeet 3")
schedule.every().day.at("11:30").do(textdaily, "Yeet 4")
schedule.every().day.at("12:30").do(textdaily, "Yeet 5")
schedule.every().day.at("13:30").do(textdaily, "Yeet 6")
schedule.every().day.at("14:30").do(textdaily, "Yeet 7")

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute


