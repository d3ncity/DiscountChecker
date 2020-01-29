# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 18:29:47 2020

@author: 01uni
"""
import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL= 'https://www.amazon.in/Sony-WH-1000XM3-Wireless-Cancellation-Headphones/dp/B07HZ8JWCL/ref=sr_1_1?crid=30OIDFT8C8AAW&keywords=sony+wx1000&qid=1580035054&smid=A14CZOWI0VEHLG&sprefix=sony+wmx%2Caps%2C340&sr=8-1'

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}


def checkForIdeal():
    page = requests.get(URL, headers=headers)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.find(id="productTitle").get_text()
    price= soup.find(id="priceblock_dealprice").get_text()
    converted_price=float(price[2:8].replace(",","."))

    print(title.strip())
    print(converted_price)
    
    if(converted_price < 20.00):
        send_email()
    
def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('dennythomas13@gmail.com', 'wwnwggjlvrszyqin')
    
    subject = "Price has fallen - Check it out"
    
    body = "Check this Amazon link: https://www.amazon.in/Sony-WH-1000XM3-Wireless-Cancellation-Headphones/dp/B07HZ8JWCL/ref=sr_1_1?crid=30OIDFT8C8AAW&keywords=sony+wx1000&qid=1580035054&smid=A14CZOWI0VEHLG&sprefix=sony+wmx%2Caps%2C340&sr=8-1"
    
    mesg = f"Subject: {subject}\n\n\n{body}"
    
    server.sendmail(
            'dennythomas13@gmail.com',
            '01univars@gmail.com',
            mesg      
    )
    
    print('Found Something - Email Sent Successfully!')
    
    server.quit()
    
while (True):
    checkForIdeal()
    time.sleep(2)