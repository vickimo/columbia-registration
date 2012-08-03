#!/usr/bin/python
from splinter.browser import Browser
from time import sleep
import subprocess

url = 'https://ssol.columbia.edu/'
username = 'SSOL username'
password = 'SSOL password'
callnumber = 'xxxxx' #e.g., '21815'

def main():
	browser = Browser()
	#browser = Browser('zope.testbrowser') #when you want it to run in the background
	browser.visit(url)
	browser.fill('u_id', username)
	browser.fill('u_pw', password)
	browser.find_by_name('submit')[0].click()
	browser.find_link_by_text('here')[0].click()
	if browser.find_by_name('tran[1]_agree'):
		browser.check('tran[1]_agree')
		browser.check('tran[1]_fj1')
		browser.find_by_name('tran[1]_sched')[0].click()
	browser.fill('tran[1]_CALLNUM', callnumber)
	browser.find_by_name('tran[1]_act')[1].click()
	if browser.is_text_present('%s is full' % callnumber):
		print '%s full :(' % callnumber
	else:
		browser.find_by_name('tran[1]_act')[0].click()
		print 'happy times! enrolled in %s' % callnumber
		subprocess.call('crontab -r', shell=True)
	browser.quit()

	print '__END__'

if __name__ == "__main__":
	main()
