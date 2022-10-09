# URL-Shortener

The idea is to minimize the web page address into something that's easier to remember and track. There are many URL shorteners on the market today, including Bit.ly, Goog. le and Tinyurl.com.

## PyShortener

PyShortener is a simple URL shortening API wrapper Python library.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyshorteners .

```bash
pip install pyshorteners
```

## Usage

```python
#import library 
import pyshorteners 

#creating object 
s=pyshorteners.Shortener 

#type the url 
url = "type the youtube link here" 

#print the shortend url 
print(s.tinyurl.short(url))
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
