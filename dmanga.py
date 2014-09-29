#-------------------------------------------------------------------------------
# Name		: Manga-downloader
# Purpose	:To download your favorite manga
#
# Authors	: Prasanth Louis
#Edited by      : 
# Created	:
# Copyright	: 
# Licence	: GPL v3
#-------------------------------------------------------------------------------
import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
name=raw_input("Enter comic name")
chapter=raw_input("Enter chapter number")
chapter=int(chapter)
x=1
z=0
for y in range(0,20):
	url = "http://mangahit.com/"+name+"/"+str(chapter)+"/"+str(x)
	html = urllib2.urlopen(url)
	data=html.read()
	soup = BeautifulSoup(data)
	for link in soup.find_all('img'):
		y=(link.get('src'))
		print y
		z=z+1
		if(z==1):
			break
	urllib.urlretrieve(y,'page'+str(x)+'.jpg')	
	print("Downloaded page"+str(x))	
	x=x+1
	z=0
