# -*- coding: UTF-8 -*-

import os
import json

f = open('ll_result.txt', 'rb')
#f = open('ll_result1000-2000.txt', 'rb')
#f = open('ll_result1740-2¡3000.txt', 'rb')
count=0
for i in f.readlines():
	count=count+1
	dic= json.loads(i)
	print 'namePincipal',dic['name']
	for y in  dic['pageGroups']:
		for pages in y['pages']:
			for questions in pages['questions']:
				print 'qKeys:',questions.keys()
				print ' name:',questions['name']
				print ' sH:',questions['showHide']
				print ' tableData:',questions['tableData']
				print ' dropdownValues:',questions['dropdownValues']
				print ' answer:',questions['answer']
				print ' inputFieldID:',questions['inputFieldID']
				print ' type:',questions['type']
				print ' options:',questions['options']
				print ' help:',questions['help']
				print '-'*10
				if questions['questions'] is not None:
					for subq in questions['questions']:
						print 'dd',subq.keys()
	if count == 5:
		break