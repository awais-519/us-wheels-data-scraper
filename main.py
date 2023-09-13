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


USERNAME = "info@buffcarparts.com"
PASSWORD = "Testpassword123"


options = webdriver.ChromeOptions()

# my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"

options.add_argument("--user-data-dir=C:\\Users\\Awais Ul Hassan\\AppData\\Local\\Google\\Chrome\\User Data\\Profile1")
options.add_argument("--profile-directory=Profile1")

options.headless = False

# options.add_argument(f'--user-agent='+my_user_agent)
# options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"


browser = webdriver.Chrome(options= options)


all_products_url = "https://wheelpros.my.site.com/dealerline/all-products?viewState=ListView&cartID=df1c21f0-d88a-4d92-ba1f-a56a8e4fe829&portalUser=&store=&effectiveAccount=0016Q00001vUWmGQAW&cclcl=en_US"

browser.get(all_products_url)
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="emailField"]').send_keys(USERNAME)
browser.find_element(By.XPATH,'//*[@id="passwordField"]').send_keys(PASSWORD)
time.sleep(5)
browser.find_element(By.XPATH,'//*[@id="send2Dsk"]').click()
print('Logged in')
time.sleep(5)



select = Select(browser.find_element(By.CSS_SELECTOR,'select.cc_page_size_control'))
select.select_by_value('75')

PRODUCTS = list()
LAST_LOOP = list()
index = 0
while True:

    try:
        if index == 3:
            break
        PAGE_PRODUCTS = list()
        search_list = ""
        INNER_JSON = list()

        time.sleep(8)
        product_container = browser.find_element(By.CSS_SELECTOR,'div.productListContent').get_attribute('outerHTML')
        soup = BeautifulSoup(product_container, 'lxml')
        all_products = soup.find_all('span','cc_product_container')
        for i in all_products:
            SKU = i.find('span','cc_product_sku').text.strip()
            name = i.find('a','cc_product_name').text.strip()
            category = i.find('div','cc_price').find_all('span')[-1]['productcategoryforproduct']
            MSRP = i.find('div','cc_price').find_all('span')[-1].text.strip().replace('$','').replace('.','').replace(',','')
            try:
                MSRP = float(MSRP) / 100
            except ValueError:
                MSRP = 0
            json_text = '{'+f'"sku":"{SKU}", "category":"{category}", "randomString":""'+'}'
            INNER_JSON.append(json_text)
            PAGE_PRODUCTS.append([SKU, name, category, MSRP])
        search_list = ",".join(INNER_JSON)
        search_list = f'[{search_list}]'
        
        RESPONSE = dealer_prices(search_list)
        dealer_price_list = json.loads(RESPONSE.text)[0]['result']['data']['All']['prices']
        for i in dealer_price_list:
            for j in PAGE_PRODUCTS:
                if i["sku"] == j[0]:
                    j.append(i['price']['Dealer Price'])
                    
        if LAST_LOOP == PAGE_PRODUCTS:
            # If last page is resulting the same, it means page got stuck and next button didnt work. 
            print('Page got stuck')
            break
           
        try:

            browser.find_elements(By.CSS_SELECTOR,"button.cc_show_more")[-1].click()
        except Exception as e:
            print('Something is wrong with clicking the next button.',e)
            PRODUCTS.append(PAGE_PRODUCTS)
            break

        LAST_LOOP = PAGE_PRODUCTS
        PRODUCTS.append(PAGE_PRODUCTS)
        print(index, " :TESTING")
        index +=1
    except KeyboardInterrupt:
        print('Keyboard interrupted')
        break
    except NoSuchWindowException:
        print("Browser closed")
        break
    
import csv
with open('result.csv','w', encoding='utf-8', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(['SKU','Name','Category','MSRP','Dealer Price'])
    for product in PRODUCTS:
        for j in product:
            csvwriter.writerow(j)


