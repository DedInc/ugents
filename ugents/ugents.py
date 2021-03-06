# -*- coding: utf-8 -*-
from random import randint as rnt, choice
from requests import get
from json import load
from os.path import dirname, abspath, join

def getAgent(browser='all', os='Windows'):
	with open(join(dirname(abspath(__file__)), 'agents.json')) as file:
		agents = load(file)
	browsers = ['chrome', 'firefox', 'opera']
	agent = ''
	i = rnt(0, 3)
	if browser == 'all' and i == 0 or browser == 'chrome':
		agent = 'Mozilla/' + choice(agents['mozilla'])
	elif i == 1 or i == 2:
		agent = 'Mozilla/5.0'
	else:
		agent = 'Opera/' + choice(agents['operav'])
	agent = agent + ' ' + choice(agents['os'])
	if browser == 'all':
		browser = choice(browsers)
	if agent.__contains__('Opera'):
		browser = 'opera'
		agent = agent + ' Presto/' + choice(agents['presto'])
		agent = agent + ' Version/' + choice(agents['opera'])
	else:
		if browser == 'opera' or browser == 'firefox':
			agent = agent + ' Gecko/' + choice(agents['gecko'])
		elif browser == 'chrome':
			agent = agent + ' AppleWebKit/' + choice(agents['kits']) + ' (KHTML, like Gecko)'
	if agent.__contains__('Gecko') and browser == 'opera':
		agent = agent + ' Opera ' + choice(agents['opera'])
	if browser == 'chrome':
		agent = agent + ' Chrome/' + choice(agents['chrome']) + ' Safari/' + choice(agents['safari'])
	elif browser == 'firefox':
		agent = agent + ' Firefox/' + choice(agents['firefox'])
	return agent