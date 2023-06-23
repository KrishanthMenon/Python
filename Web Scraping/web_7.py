import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self , url):
        self.url = url
        self.user_agent = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}
        self.response = requests.get(url = self.url , headers = self.user_agent).text
        self.soup = BeautifulSoup(self.response , "lxml")

    def product_title(self):
        title = self.soup.find("span" , {"id":"productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag Not Found"

    def product_price(self):
        price = self.soup.find("span" , {"id" : "priceblock_ourprice"})
        if price is not None:
            return price.text
        else:
            return "Tag Not Found"



#device = PriceTracer(url="https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B07KXC7QRS/ref=sr_1_4?dchild=1&keywords=samsung+s10&qid=1613300195&sr=8-4")
#print(device.product_title())
#print(device.product_price())

samsung = PriceTracer(url = "https://www.amazon.in/dp/B08LRFZ4LZ/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B08LRFZ4LZ&pd_rd_w=bvaPf&pf_rd_p=b9175453-ca9b-41ce-82bc-58f20ea9bb05&pd_rd_wg=zyTKx&pf_rd_r=SER0SXG8N0TKP0NXV934&pd_rd_r=681f8dd5-0791-47a3-aaba-4856f72c1572&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyOUZTNlJVM1BNU0Y1JmVuY3J5cHRlZElkPUEwMzg5ODAxMVlEMEE0NUhZTzRSMSZlbmNyeXB0ZWRBZElkPUEwMDg2NjgwREREVVRGM0YwVTZPJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")
print(samsung.product_title())
print(samsung.product_price())