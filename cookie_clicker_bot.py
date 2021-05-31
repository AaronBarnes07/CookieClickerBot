from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://orteil.dashnet.org/cookieclicker/'
browser.get(url)

browser.implicitly_wait(30)
#cookie = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'bigCookie')))
items = []
all_upgrade_list = []
cookie = browser.find_element_by_id('bigCookie')
current_cookies = browser.find_element_by_id('cookies')
shimmers = browser.find_element_by_id('shimmers')
upgrades = browser.find_element_by_id('upgrades')

for i in range(0,18):
    ele = browser.find_element_by_id('product'+ str(i))
    print ele.get_attribute('innerHTML')
    items.append(ele)

def check_item_unlocked(item_list):
    unlocked_list = []
    for x in range(len(item_list)):
        if item_list[x].get_attribute('class') == 'product unlocked enabled':
            unlocked_list.append(x)
    return unlocked_list

unlocked = []
while True:
    c = ''
    count_text = current_cookies.text.split('\n')[0]
    count = count_text.split(" ")[0]
    if ',' in count:
        counts = count.split(',')
        count = c.join(counts)
    count = int(count)
    
    unlocked = check_item_unlocked(items)
    if upgrades.get_attribute('innerHTML'):
        next_upgrade = upgrades.find_element_by_id('upgrade0')
        if next_upgrade and next_upgrade.get_attribute('class') == 'crate upgrade enabled':
            next_upgrade.click()
            
    if shimmers.get_attribute('innerHTML'):
        shimmer = shimmers.find_element_by_class_name('shimmer')
        if shimmer:
            shimmer.click()
            
    for x in unlocked:
        new_item = items[x].find_element_by_id('productPrice'+str(x))
        cost = new_item.text
        if ',' in cost:
            costs = cost.split(',')
            cost = c.join(costs)
        cost = int(cost)
        if cost < count:
            items[x].click()
    
    cookie.click()    