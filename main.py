from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, json
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from get_dealer_price import dealer_prices
from selenium.common.exceptions import NoSuchWindowException, WebDriverException
from bs4 import BeautifulSoup
from copy import deepcopy


start_time = time.time()
print(start_time)

USERNAME = "info@buffcarparts.com"
PASSWORD = "Testpassword123"


options = webdriver.ChromeOptions()

#my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

options.add_argument("--user-data-dir=C:\\Users\\Awais Ul Hassan\\AppData\\Local\\Google\\Chrome\\User Data\\Profile1")
options.add_argument("--profile-directory=Profile1")

options.headless = False

#options.add_argument(f'--user-agent='+my_user_agent)
# options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"


browser = webdriver.Chrome(options= options)
browser.set_page_load_timeout(600)




all_products_url = "https://wheelpros.my.site.com/dealerline/all-products?viewState=ListView&cartID=df1c21f0-d88a-4d92-ba1f-a56a8e4fe829&portalUser=&store=&effectiveAccount=0016Q00001vUWmGQAW&cclcl=en_US"

browser.get(all_products_url)
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="emailField"]').send_keys(USERNAME)
browser.find_element(By.XPATH,'//*[@id="passwordField"]').send_keys(PASSWORD)
time.sleep(5)
browser.find_element(By.XPATH,'//*[@id="send2Dsk"]').click()
print('Logged in')
time.sleep(5)

# select = Select(browser.find_element(By.CSS_SELECTOR,'select.cc_page_size_control'))
# select.select_by_value('25')
# print('Page size 25 selected')
# time.sleep(5)


def wait_till_show_more_button_appears_and_click():
    while True:
        if browser.find_elements(By.CSS_SELECTOR,"button.cc_show_more")[-1].is_enabled():
            browser.find_elements(By.CSS_SELECTOR,"button.cc_show_more")[-1].click()
            break
        
        time.sleep(2)


# def wait_till_price_appears():
#     while True:
#         if browser.find_elements(By.CSS_SELECTOR,"div.cc_price")[-1].is_displayed():
#             break
        
#         time.sleep(2)


def show_dealer_price():
        select = Select(browser.find_element(By.CSS_SELECTOR,'select.CustomerCodeSelect'))
        time.sleep(3)
        # wait_till_price_appears()

        select.select_by_value('MSRP')
        # wait_till_price_appears()
        time.sleep(4)
        
        select.select_by_value('Dealer Price')
        # wait_till_price_appears()
        time.sleep(4)


PRODUCTS = list()
LAST_LOOP = list()
PAGE_PRODUCTS = list()
index = 0

while True:
    try:
        print('Index: ', index)

        
        time.sleep(8)

        show_dealer_price()

        product_container = browser.find_element(By.CSS_SELECTOR,'div.productListContent').get_attribute('outerHTML')
        soup = BeautifulSoup(product_container, 'lxml')
        all_products = soup.find_all('span','cc_product_container')
        
        for i in all_products:
            SKU = i.find('span','cc_product_sku').text.strip()
            name = i.find('a','cc_product_name').text.strip()
            category = i.find('div','cc_price').find_all('span')[-1]['productcategoryforproduct']
            dealer_price = i.find('div','cc_price').find_all('span')[-1].text.strip().replace('$','').replace('.','').replace(',','')
            
            try:
                dealer_price = float(dealer_price) / 100
            except ValueError:
                dealer_price = 0

            PRODUCTS.append([SKU, name, category, dealer_price])
        
        # print(len(PAGE_PRODUCTS))
                    
        # if LAST_LOOP == PAGE_PRODUCTS:
        #     # If last page is resulting the same, it means page got stuck and next button didnt work. 
        #     print('Page got stuck')
        #     break
           

        try:
            wait_till_show_more_button_appears_and_click()
            
        except Exception as e:
            print('Something is wrong with clicking the next button.',e)
            # PRODUCTS.append(PAGE_PRODUCTS)
            break

        # LAST_LOOP = PAGE_PRODUCTS
        # PRODUCTS.append(PAGE_PRODUCTS)
        index +=1
        print(len(PRODUCTS), ' PRO LEN')
        if index == 2:
            print('Products Limit Reached. All Products have been scrapped')
            break
        
        time.sleep(8)
    
    
    except KeyboardInterrupt:
        print('Keyboard interrupted')
        break
    except NoSuchWindowException:
        print("Browser closed")
        break
    except TimeoutError:
        print('Browser Timed out')
        break
    except Exception as e:
        print('Exception: ', e)
    




import csv
header = ['SKU', 'Name', 'Category', 'Dealer Price']
file_name = 'result.csv'


unique_rows = set()

# Open the file in 'w' mode with automatic newline handling
with open(file_name, 'w', encoding='utf-8', newline='') as f:
    csvwriter = csv.writer(f)
    
    # Write the header row only once
    csvwriter.writerow(header)
    
    # Iterate through each product and write its data
    for product in PRODUCTS:
        product_tuple = tuple(product)

        if product_tuple not in unique_rows:
            csvwriter.writerow(product)
            unique_rows.add(product_tuple)
    
print('CSV Writing Completed.')