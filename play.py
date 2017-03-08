from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

## Selenium web drivers
driver = None;url=None

def wait(web_opening_time=3):
	time.sleep(web_opening_time)

## load web driver for selenium : chrome
def web_driver_load():
	global driver
	driver = webdriver.Chrome()
## quit web driver for selenium
def web_driver_quit():
	driver.close()
	wait(1)

# code for music
def load_music():
	global url
	driver.get(url);
	wait(10)
	check_station_off()

# After every 5 seconds it checks if station is offline
def check_station_off():
	web_obj = driver.find_element_by_id("current-song")
	while True :
		wait(5)
		text=web_obj.text
		print "playing song: " + text
		if 'station' in text:
			print ("station is offline restarting music")
			web_driver_quit()
			play()
			break

def play(url_=None):
	global url
	url=url_ if url_ else url
	print "Playing music from channel: " + str(url)
	web_driver_load()
	load_music()
