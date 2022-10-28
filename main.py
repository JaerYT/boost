from selenium import webdriver
from time import sleep

siddharth1= webdriver.Chrome(executable_path="C:\chromedriver.exe") #In executable path give the path of chromedriver that you have downloaded. In my case it is in downloads.

siddharth1.get("https://youtu.be/1Ci39PaqG2g") #provide the link

#i have used siddharth 1,2,3  so it will open 3 tabs 
#if you want to add more tabs you can also do it 

while True:
    sleep(27) #sleep 18 meanes after 18 seconds page will refresh
    siddharth1.refresh()
    
    #To execute - Simple run this code
    #Happy coding - Siddharth
