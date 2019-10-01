#--------------------------------------------------
# Name		: Manga-downloader
# Purpose	:To download your favorite manga
# license       : feel free to modify and distribute
#------------------------------------------------

# example input link : https://www.mangaeden.com/en/en-manga/soul-eater/0/1/

import bs4
import urllib.request as ur
import re
import os
import time

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}

def download_page(link,count):
	try: 
		req=ur.Request(link,headers=hdr)
	except:
		req=ur.Request(link,headers=hdr)
	reg_obj=re.compile('[\s\S]*.(jpg|jpeg|png)')
	extension=re.match(reg_obj,link)
	print("Downloading...")
	with ur.urlopen(req) as response, open(file_name,'wb') as write_file:
		try:
			block_sz = 8192
			while True:
			    buffer = response.read(block_sz)
			    if not buffer:
			        break
			    write_file.write(buffer)
		except:				
			data=response.read()
			write_file.write(data)

def get_chapter(chap):
	req=ur.Request(chap,headers=hdr)
	obj=ur.urlopen(req)
	soup=bs4.BeautifulSoup(obj,features='lxml')
	next='https://www.mangaeden.com'+soup.find_all(id='nextA')[0]['href']
	reg_comp=re.compile('[\s\S]*/(\d*)/\d*/')
	chap_num=re.match(reg_comp,next).groups()[0]
	img_link='https:'+soup.find_all(id='mainImg')[0]['src']
	counter=0
	while(re.match(reg_comp,next).groups()[0] == chap_num):
		download_page(img_link,counter)
		counter+=1
		req=ur.Request(next,headers=hdr)
		obj=ur.urlopen(req)
		soup=bs4.BeautifulSoup(obj,features='lxml')
		next='https://www.mangaeden.com'+soup.find_all(id='nextA')[0]['href']
		img_link='https:'+soup.find_all(id='mainImg')[0]['src']
	download_page(img_link,counter)
	print('Finished Downloading!')

chap_link=input('url: ')
get_chapter(chap_link)
