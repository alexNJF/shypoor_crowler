from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse
import urllib
import requests
import time
import re

#لیست صفحه اول آگهی ها 
html_page = urlopen("https://www.sheypoor.com/%D8%A7%DB%8C%D8%B1%D8%A7%D9%86/%D8%A7%D9%85%D9%84%D8%A7%DA%A9/%D8%B2%D9%85%DB%8C%D9%86-%D8%A8%D8%A7%D8%BA").read()
soup = BeautifulSoup(html_page.decode('utf-8'),features="html.parser")

#variable
urls=[] #include all page we need  [کل یو آر ال اگهی های صفحه اصلی را در این لیست ذخیره میکنیم ]

print ("get all link in first page ... ")
urls=[]
for article_tag in soup.findAll('article'): #یو آر ال تبلیغات داخل این تگ هست 
	urls.append(article_tag.a.get("href"))
print("finishing fetch [",len(urls),"]data fetch")


#---------
for link in urls:
	try:
		print("--------------")
		
		link=urllib.parse.quote(link).replace('https%3A//','https://')#چون لینک یو آر ال ها به صورت فارسی بود باید یه صورت کد شده در بیاید 
		print(link)
		print("--------")
		target_page = urlopen(link).read()
		soup = BeautifulSoup(target_page.decode('utf-8'),features="html.parser") #لینک آگهی مورد نظر 
		
		title=soup.title #موضوع آگهی 
		
		id= soup.find_all('meta',attrs={'name':'listing-id'})[0].get('content') # آی دی تبلیغ که برای استفاده در اِی پی آی استفاده میکنیم و یونیک است 
		
		image_links=[]# تصاویر آگهی در این لیست دخیره میشود 
		for tmp in soup.find_all('figure'):
			if(tmp.img.get('src') is not None):
				image_links.append(tmp.img.get('src'))
			elif(tmp.img.get('src') is  None):
				image_links.append(tmp.img.get('data-src'))
			
		special_info="" # قیمت هر متر متراژ و توضیحات اولیه
		tables=soup.findAll('table')
		for singel_table in tables:
			for row in singel_table.findAll("tr"):
				th=row.th.getText()
				td=row.td.getText()
				special_info=special_info+th.strip()+":"+td.strip()+" "
			
		#print(special_info)#قیمت و متراژ و بقیه چیزا 
		
		#price= soup.find_all('span',attrs={'class':'item-price'})[0].getText()
		
		
		"""
		در این قسمت با استفاده از 
		API 
		اطلاعات آگهی را استخراج میکنیم 
		api 
		اگر تعداد زیادی درخواست بهش بفرستیم اسکریپت رو بلاک میکنه 
		"""
		description_url="https://www.sheypoor.com/api/web/listings/"+id+"/description"
		print(description_url)
		print("-------")
		headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
		'Host':'www.sheypoor.com',
		'Accept':'*/*',
		'Sec-Fetch-Dest':'empty',
		'Upgrade-Insecure-Requests':'1'
		}
		
		r = requests.get(description_url, headers=headers)
		print(r.json())
		
	
			
		
	
	
	
	
	
	
	except:
		print("Error")
		
	
	
	
		
	time.sleep(10)	# جهت جلوگیری از بلاک کردن سایت شیپور ده ثانیه صبر میکنیم 

		
	print("****************************************")
	
	
	

	
	
	
	
	
	






	
		
   





