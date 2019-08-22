import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options

try:
    opts = Options()
    opts.set_headless()
    assert opts.headless
    #f = open("log.txt","w")
    browser = webdriver.Firefox(options=opts)
    #browser = webdriver.Firefox()
    browser.get("https://czateria.interia.pl/emb-chat,room,<number>,<name>") 
    #f.write(browser.page_source)
    #print(browser.page_source)
    #input()
    time.sleep(1)
    rodo = browser.find_element_by_class_name("rodo-popup-agree")
    rodo.click()
    time.sleep(1)
    mamStalyNick = browser.find_element_by_xpath("//label[@for='login-user']")
    mamStalyNick.click()
    time.sleep(1)
    username = browser.find_element_by_id("nick-login").send_keys("user", Keys.TAB, "password") 
    wejdz = browser.find_element_by_id("enter-login")
    wejdz.click()
    wait = WebDriverWait(browser, 10)
    time.sleep(2)
    #dupa = wait.until(ec.visibility_of("dupa"))
    #m-msg-item-user-login'
    while True:
        elements = browser.find_elements_by_xpath("//*[@class='m-msg-item']")
        for elem in elements:
            print(elem.text)
            #listNickMsg = elem.text.split(": ", 1)
            #print(listNickMsg)
        print("\n\n#####\n\n", len(elements), "\n\n#####\n\n")
        #item = wait.until(ec.element_to_be_selected((By.XPATH, "//*[@class='m-msg-item']")))
        #print("jstem tu")
        #print("item: ", item)
        time.sleep(5)
        #asd = ActionChains(browser).move_to_element(item).perform()
        #print("mamy: ", asd)
        #time.sleep(4)    
    #input()
    #time.sleep(2000)

    #f.write("\n\n ########################### SEPARATOR ########################## \n\n")
    #f.write(browser.page_source)
    #f.close()
    #print(browser.page_source)
finally:
    input("press any key to exit")
    browser.quit()