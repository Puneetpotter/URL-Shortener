pip install pyshorteners

#import library 
import pyshorteners 

#creating object 
s=pyshorteners.Shortener 

#type the url 
url = "type the youtube link here" 

#print the shortend url 
print(s.tinyurl.short(url))
