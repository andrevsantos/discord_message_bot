import requests
import schedule
import time
import json

baseURL = "https://discord.com/api/v9/channels/"

header = {
    'authorization': 'AUTHORIZATION HEADER HERE'
}

# Reads file with all ids that want to send message to
def doCreateURLs():
    file1 = open('id_list_dev.txt', 'r')
    Lines = file1.readlines()
    urlList = []

    for line in Lines:
        discID = line.strip()
        newURL = baseURL + discID + "/messages"
        urlList.append(newURL)
    
    return urlList

# Reads file with message to send
def readMessage():
    file2 = open('message_dev.txt','r')
    message = file2.read()
    payload = {
        'content': message
    }
    return payload

# Sends post request based on message and discord IDs captured above
def postDiscord():
    print("Sending message!")
    urlList = doCreateURLs()
    payload = readMessage()
    for url in urlList:
       r = requests.post(url, data=payload, headers=header)

postDiscord()
schedule.every(30).seconds.do(postDiscord)

while 1:
    schedule.run_pending()
    time.sleep(1)