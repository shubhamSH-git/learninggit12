import json
import requests
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass

def RealTimeCurrencyExchangeRate(from_curr,to_curr,api_key):
  base_url=r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
  main_url = base_url + "&from_currency=" + from_curr + "&to_currency=" + to_curr+"&apikey=" + api_key 
  req_ob=requests.get(main_url)
  result=req_ob.json()
  return(result['Realtime Currency Exchange Rate']['8. Bid Price'])
  

def send_email(rate):
  # create message object instance
  msg = MIMEMultipart()
  
  # the parameters of the message
  password = your_password
  msg['From'] = your_email
  msg['To'] = send_email_to
  msg['Subject'] = "EUR-INR High, ACT FAST"

  # your message
  message = "Dear " + your_name + "\n1 EUR to INR is now " + str(rate) + ". Better act.\nRegards,\n" + my_name
  
  # adds in the message from the above variable
  msg.attach(MIMEText(message, 'plain'))
  
  # create the gmail server
  server = smtplib.SMTP('smtp.gmail.com: 587')
  
  server.starttls()
  
  # Login Creds for sending the email
  server.login(msg['From'], password)
  
  # sends the message
  server.sendmail(msg['From'], msg['To'], message)
  
  server.quit()
  

  print("successfully sent email to %s:" % (msg['To']))
  print("Price of bitcoin was at " + str(rate))

# user inputs
my_name="Shubham Bhatt"
your_name = input("Enter the name to sent to :")
your_email = input("Email to send from: ")
your_password = getpass.getpass()
send_email_to = input('Enter email address to send to: ')
alert_amount = input('Alert EUR rise : ')


while True:
  curr_rate= RealTimeCurrencyExchangeRate("EUR","INR","NS40ZTCJCU5C7RLG")
  time.sleep(10)
  if float(curr_rate) > float(alert_amount):
    send_email(curr_rate)
    print('Will check again in 3 minutes. Ctrl + C to quit.')
    time.sleep(180)
  else:
    time.sleep(300)
    print('Price is ' + str(curr_rate) + '. Will check again in 5 minutes. Ctrl + C to quit.')
	


	

