import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options

global oldListElements
oldListElements = []

def setupBrowser():
    opts = Options()
    opts.set_headless()
    assert opts.headless
    browser = webdriver.Firefox(options=opts)
    #browser = webdriver.Firefox()
    return browser

def joinChat(browser):
    browser.get("https://czateria.interia.pl/emb-chat,room,") 
    time.sleep(1)
    rodo = browser.find_element_by_class_name("rodo-popup-agree")
    rodo.click()
    time.sleep(1)
    mamStalyNick = browser.find_element_by_xpath("//label[@for='login-user']")
    mamStalyNick.click()
    time.sleep(1)
    browser.find_element_by_id("nick-login").send_keys(user, Keys.TAB, password) 
    wejdz = browser.find_element_by_id("enter-login")
    wejdz.click()
    wait = WebDriverWait(browser, 10)
    time.sleep(2)

def getFiveLastElements(browser):
    elements = browser.find_elements_by_xpath("//*[@class='m-msg-item']")
    #print("elements type: ", type(elements)) #list
    listElements = []
    for intElement in range(len(elements)-10, len(elements)):
        #print(elements[intElement].text) #string
        listElements.append(elements[intElement].text)
    return listElements

def compareListsElement(listElements, oldListElements):
    #print("sprawdzamy: \n")
    #print("element: ", element)
    #for elem in prevElements:
    #    print("prevElements", elem.text)
    #jak obsluzy element to musi go usunac
    #print("\nlistElements: " , listElements)
    #print("\noldListElements: ", oldListElements)
    #comparedSet = set(listElements).intersection(oldListElements)
    elementsSet = set(listElements)
    oldElementsSet = set(oldListElements)
    returnedSet = elementsSet - oldElementsSet
    #print("\ndiff: ", returnedSet)
    return returnedSet 

try:
    browser = setupBrowser()
    joinChat(browser)
    oldListElements = getFiveLastElements(browser)
    time.sleep(5)
    while True:
        listElements = getFiveLastElements(browser)
        uniqueSet = compareListsElement(listElements, oldListElements)
        uniqueList = list(uniqueSet)
        print("unique: ", uniqueList)
        for unique in uniqueList:
            listNickMsg = unique.split(": ", 1)
            print("MSG: ", listNickMsg)
            if len(listNickMsg) == 2:
                if listNickMsg[0] == 'kot32' and listNickMsg[1] == "kim jestem":
                    #print("tak")
                    #username = browser.find_element_by_id("nick-login").send_keys("zwyciezca!", Keys.Enter)
                    browser.find_element_by_class_name("text-input").send_keys("zwyciezca!", Keys.ENTER)    
            
            #print(type(listNickMsg))
            #print("0: ", listNickMsg[0])
            #print(len(listNickMsg))
        
        
        oldListElements = listElements
        #respond(uniqueList)
        

        #print("mamy: ", listElements)
        #print(type(listElements))
    
        time.sleep(10)
    
    #while True:
        #print(elements[2].text)
        #print("prevElements type: ", type(prevElements))
        
        #fun getFiveLastElements
        #look for any of last five in last 10
        #do some stuff
        #set last 10 elements
        #repeat
                #print(intElement)
     #           compareElements(elements[intElement].text, prevElements)
      #          prevElements = prevElements.append(elements[intElement].text)
        #prevElements = elements
finally:
    input("press any key to exit")
    browser.quit()