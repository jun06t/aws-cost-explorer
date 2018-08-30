#!/usr/bin/python3
# coding: UTF-8

import os
import datetime
import slackweb
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from collections import OrderedDict

# headless chrome
CHROME_BIN = "/usr/bin/chromium-browser"
CHROME_DRIVER = os.path.expanduser("/usr/bin/chromedriver")

options = Options()
options.binary_location = CHROME_BIN
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1280,3000")

driver = webdriver.Chrome(CHROME_DRIVER, chrome_options=options)

# login
print('login')
account_id = os.environ.get("ACCOUNT_ID")
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
login_url = "https://%s.signin.aws.amazon.com/console" % account_id
driver.get(login_url)
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('signin_button').click()
sleep(3)

print('move cost report dashboard')
driver.get("https://console.aws.amazon.com/cost-reports/home?#/savedReports")
sleep(3)

# skip tutorial
print('skip tutorial')
driver.execute_script("localStorage.setItem('aws-cost-explorer-hasSeenTutorial', true)")

print('move saved report')
driver.find_element_by_link_text('Monthly costs by service').click()
sleep(3)

# set period
driver.find_element_by_xpath('//*[@class="picker-dropdown"]').click()

# target_at
target_date = os.getenv("TARGET_DATE", "1")
target_at = datetime.date.today() - datetime.timedelta(int(target_date))
target_at_str = target_at.strftime('%m/%d/%Y')

# from
elem = driver.find_element_by_xpath('//label[text()="From"]/following::input')
elem.clear()
elem.send_keys(target_at_str)
sleep(1)

# to
elem = driver.find_element_by_xpath('//label[text()="To"]/following::input')
elem.clear()
elem.send_keys(target_at_str)
sleep(1)

# apply
elem = driver.find_element_by_xpath('//div[text()="Apply"]').click()
sleep(1)

# change granularity
elem = driver.find_element_by_xpath('//granularity//div[@class="ui-dropdown"]').click()
elem = driver.find_element_by_link_text('Daily').click()
sleep(1)

# for slack report
slack_link = driver.current_url

# get cost
costs = OrderedDict()
for row in range(1, 7):
    title_xpath = '//div[@class="left-container"]//tr[%d]/td' % row
    title = driver.find_element_by_xpath(title_xpath).text
    value_xpath = '//div[contains(@class, "right-container")]//tr[%d]/td[1]' % row
    value = driver.find_element_by_xpath(value_xpath).text
    costs[title] = value

# post slack
webhook_url = os.environ.get("WEBHOOK_URL")
slack = slackweb.Slack(url=webhook_url)
# create message
text = target_at.strftime('%Y/%m/%d') + "\n"
text += "```\n"
for k, v in costs.items():
    text += k + ":\t" + v +"\n"
text += "```\n"
text += "<"+slack_link+"|cost explorer>"

slack.notify(text=text)

driver.quit()
