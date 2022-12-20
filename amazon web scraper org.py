# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 12:32:13 2018

@author: krishna
"""

from lxml import html  
import requests
import csv
import json
def ReadAsin():
    reviews_df=[]
    
    amazon_url = 'https://www.amazon.in/Apple-iPad-Tablet-inch-Wi-Fi/product-reviews/'+asin+'/ref=cm_cr_arp_d_paging_btm_'+str(i)+'?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(i)
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    
    headers = {'User-Agent': user_agent}
    page = requests.get(amazon_url, headers = headers)
    parser = html.fromstring(page.content)
    xpath_reviews = '//div[@data-hook="review"]'
    reviews = parser.xpath(xpath_reviews)
    xpath_rating  = './/i[@data-hook="review-star-rating"]//text()' 
    xpath_title   = './/a[@data-hook="review-title"]//text()'
    xpath_author  = './/a[@data-hook="review-author"]//text()'
    xpath_date    = './/span[@data-hook="review-date"]//text()'
    xpath_body    = './/span[@data-hook="review-body"]//text()'
    xpath_helpful = './/span[@data-hook="helpful-vote-statement"]//text()'
    for review in reviews:
        rating  = review.xpath(xpath_rating)
        review_rating = ''.join(rating).replace('out of 5 stars','')
        title   = review.xpath(xpath_title)
        author  = review.xpath(xpath_author)
        date    = review.xpath(xpath_date)
        body    = review.xpath(xpath_body)
        helpful = review.xpath(xpath_helpful)
        
        review_dict = {'rating': review_rating,
                       'title': title,
                                   
                       'date': date,
                       'body': body,
                      }
        #print(review_dict)
       # csv_file = "Names.csv"
       # csv_columns=['rating','title','author','data','body','helpful']
        #rows = json.loads(str(review_dict))

        #r=zip(*rows.values())

        #fieldnames = ['rating','title','date','body']
        with open('2out.csv', 'a',newline='',encoding='utf-8') as f:
            dict_writer = csv.writer(f)
            #dict_writer.writerow(fieldnames)
            
            #dict_writer.writerow(review_dict.keys())
            dict_writer.writerows(zip(*review_dict.values()))
            reviews_df.append(review_dict)
        print(reviews_df)
if __name__ == '__main__':
        asin=input("enter the product id:")
        z=input("enter the number of pages:")
        fieldnames = ['Rating','Title','Date','Review']
        with open('2out.csv', 'a',newline='',encoding='utf-8') as f:
            dict_writer = csv.writer(f)
            dict_writer.writerow(fieldnames)
        for i in range(1,int(z)+1):
            print("________________________"+str(i))
            print("_______________________________")
            ReadAsin()
            
