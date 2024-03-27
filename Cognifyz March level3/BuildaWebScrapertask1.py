
from bs4 import BeautifulSoup 


file = open("gfg.html", "r") 
contents = file.read() 

soup = BeautifulSoup(contents, "lxml") 


print("Current content in title tag is:-") 
print(soup.title) 
soup.title.append("Using BS") 
print("Content after appending is:-") 
print(soup.title) 

print("\n") 


print("Current content in heading h1 tag is:-") 
print(soup.h1) 
soup.h1.append("contents of tag") 
print("Content after appending is:-") 
print(soup.h1) 

print("\n") 


print("Current content in paragraph p tag is:-") 
print(soup.p) 
soup.p.append("BeautifulSoup library") 
print("Content after appending is:-") 
print(soup.p) 

print("\n") 


print("Current content in anchor a tag is:-") 
print(soup.a) 
soup.a.append("Mumbai Website") 
print("Content after appending is:-") 
print(soup.a) 

 
savechanges = soup.prettify("utf-8") 
with open("output.html", "wb") as file: 
	file.write(savechanges) 
