from bs4 import BeautifulSoup
from selenium import webdriver # naršyklės kontroleris
from selenium.webdriver.chrome.options import Options #Naršyklės
from time import sleep
from selenium.webdriver.common.by import By

opcijos = Options()
# Incognito mode
opcijos.add_argument('--incognito')
# Nustatome, jog mums neatidarinėtų naršyklės:
#opcijos.add_argument('--headless')

driver = webdriver.Chrome(options=opcijos)
url = "https://www.baldoras.lt/katalogas/valgomojo-stalai/"

#sleep(10)
driver.get(url) #puslapio atsisiuntimas

source = driver.page_source # pasiimam puslapio html kodą

bs = BeautifulSoup(source, 'html.parser') 

prices = bs.select('.product-card__prices')
#sleep(5)
#driver.find_element(By.CSS_SELECTOR, '.page-link.page-link--with-arrow[aria-label="Next"]').click()
#sleep(5)

#for price in prices:
    #print(price.text.strip())
    

loop = 0
average = 0
while True:
    source = driver.page_source
    bs = BeautifulSoup(source, 'html.parser')
    
    prices = bs.select('.product-card__prices')
    
    for price in prices:
        print(price.text.strip())
        price = price.text.strip().replace("€", "")
        average += int(price)
        loop += 1

    try:
        next_button = driver.find_element(By.CSS_SELECTOR, '.page-link.page-link--with-arrow[aria-label="Next"]')
        next_button.click()
        sleep(5) 
    except:
        print("No more pages.")
        break
print(average / loop)