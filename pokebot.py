from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#budget= input("enter your budget: ")
budget=1000
def purchase():
    print("purchesed")
opt=Options()
def checkout():
    print("checkout")
#opt.add_argument("--disable-blink-features=AutomationControlled")
opt.add_experimental_option(name="detach", value=True)
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=opt)
#hbvurl="https://hobbiesville.com/collections/pokemon-pre-orders-1"
hbvurl="https://hobbiesville.com/collections/pokemon-booster-boxes"
pkcurl = "https://www.pokemoncenter.com/en-ca/category/tcg-cards"
youtube = "https://www.youtube.com/"
demourl= "https://bot.sannysoft.com/"
url401 = "https://store.401games.ca/collections/all-pokemon"
with open("stealth.min.js") as f:
    inject_js = f.read()

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": inject_js 
})
driver.get(hbvurl)
try:
    #productpage = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Journey Together Booster Box"))) 
    productpage = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Pokemon Scarlet & Violet Surging Sparks Booster Box")))
finally:
    print("not found")
    #driver.find_element(By.PARTIAL_LINK_TEXT, "Journey Together Booster Box")
print(productpage)
productpage.click()
try:
    addToCartButton = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, "add"))) 
finally:
    print("not found")
sleep(2)
while budget > 0 :
    addToCartButton.click()
    sleep(1)
    budget-=450