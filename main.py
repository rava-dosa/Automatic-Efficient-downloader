from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

profile = webdriver.FirefoxProfile()

profile.set_preference("browser.download.folderList", 2)


#"#address of download directory=give address of directory in which you want to download"

profile.set_preference("browser.download.dir", '#address of download directory')
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

browser = webdriver.Firefox(firefox_profile=profile)



f=open('log.txt','a')



f = open('name.txt','r')
lines=f.readlines()
f.close()
for line in lines:
	browser.get(line)
        f=open('log.txt','a')
        f.write(line + '\n')
	print "Start : %s" % time.ctime()
	browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
	time.sleep(11)
	browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
	print "END : %s\n" % time.ctime()
