import time, configparser

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options

'''
from notifications import notification
from general import general
from command import command
from special import special
from accosted import accosted
'''

global oldListElements
oldListElements = []

def selectChat():
    #TODO: menuitem
    chat = "ZAMOSC"
    return chat

def readConfig(chat):
    cfg = configparser.ConfigParser()
    cfg.read('settings.ini', encoding="utf-8")
    chat = cfg['czaty'][chat]
    login = cfg['login']['LOGIN']
    password = cfg['login']['PASSWORD']
    #print("chat: ", chat, "login: ", login, "password: ", password)
    #input("asd")
    configParams = [chat, login, password]
    #configParams = configParams.append(chat, login, password)
    return configParams

def setupBrowser(browserWindow):
    if browserWindow == True:
        browser = webdriver.Firefox()
    elif browserWindow == False:
        opts = Options()
        opts.set_headless()
        assert opts.headless
        browser = webdriver.Firefox(options=opts)
    return browser

def joinChat(browser, chat, login, password):
    browser.get(chat) 
    time.sleep(1)
    rodo = browser.find_element_by_class_name("rodo-popup-agree")
    rodo.click()
    time.sleep(1)
    mamStalyNick = browser.find_element_by_xpath("//label[@for='login-user']")
    mamStalyNick.click()
    time.sleep(1)
    browser.find_element_by_id("nick-login").send_keys(login, Keys.TAB, password) 
    wejdz = browser.find_element_by_id("enter-login")
    wejdz.click()
    wait = WebDriverWait(browser, 10)
    time.sleep(2)

def getFiveLastElements(browser):
    elements = browser.find_elements_by_xpath("//*[@class='m-msg-item']")
    accosted = browser.find_elements_by_xpath("//*[@class='m-msg-item accosted']")
    elements = elements + accosted
    #print("elements type: ", type(elements)) #list
    listElements = []
    maxSize = 0
    #sprawdzamy ilosc elementow, jesli mniej niz 12, ustawiamy na ilosc obecna ilosc elementow
    if len(elements) < 12:
        maxSize = len(elements)
    #jesi wiecej, ustawiamy na 12 - modyfikowac jesli czat jest bardzo aktywny, poniewaz zacznie przegapiac wiadomosci.
    #zbyt wysoka wartosc, zamuli skrypt poniewaz ilosc elementow urosnie do 500+
    else:
        maxSize = 12
    #jesli maxSize bedzie wiekszy niz ilosc elementow, skrypy sie wysypie
    for intElement in range(len(elements)-maxSize, len(elements)):
        #print(elements[intElement].text) #string
        listElements.append(elements[intElement].text)
    return listElements

def compareListsElement(listElements, oldListElements):
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

def killBanner(browser):
    try:
        print("szukamy banera")
        banner = browser.find_element_by_class_name("close").click()
        print("baner: ", banner)
    finally:
        return False
    
    '''
    class vj-tech" 
    <div class="close">Zamknij</div>
    '''

def notification(browser, listNickMsg, unique):
    try:
        if listNickMsg[0] == "+ kot32 wszedł":
            browser.find_element_by_class_name("text-input").send_keys("siema kocie", Keys.ENTER)
        #if listNickMsg[0] == "+ 3piotrus3:D wszedł" or listNickMsg[0] == "+ banzaii:D wszedł":
        #    browser.find_element_by_class_name("text-input").send_keys("siema babzaj <piwo>", Keys.ENTER)
        if listNickMsg[0] == "+ Ashele wszedł":
            browser.find_element_by_class_name("text-input").send_keys("Ashele szelka:*", Keys.ENTER)
        if listNickMsg[0] == "+ Seby wszedł":
            browser.find_element_by_class_name("text-input").send_keys("elo sebi", Keys.ENTER)
        if listNickMsg[0] == "+ epokalodowcowa## wszedł" or listNickMsg[0] == "+ miazgaorzechowa wszedł":
            browser.find_element_by_class_name("text-input").send_keys("foczka:*", Keys.ENTER)
        if listNickMsg[0] == "+ CuKierKoWa:-)_ wszedł":
            browser.find_element_by_class_name("text-input").send_keys("CuKierKoWa:-)_ no cześć maleńka:*", Keys.ENTER)
        if listNickMsg[0] == "+ Blondyneczkaaa. wszedł":
            browser.find_element_by_class_name("text-input").send_keys("Blondyneczkaaa. kizia mizia:*", Keys.ENTER)
        if listNickMsg[0] == "~Zostałeś rozłączony":
            browser.quit()
    finally:
        return True    

def general(browser, listNickMsg, unique):
    try:
        if listNickMsg[0] == 'kot32' and listNickMsg[1] == "kim jestem?":
            browser.find_element_by_class_name("text-input").send_keys((listNickMsg[0])+": jesteś zwyciężcą!", Keys.ENTER)
        if listNickMsg[1] == "hej" or listNickMsg[1] == "hejka" or listNickMsg[1] == "witam" or listNickMsg[1] == "cześć" or listNickMsg[1] == "czesc":
            browser.find_element_by_class_name("text-input").send_keys((listNickMsg[0])+ ": witaj :)", Keys.ENTER)
        if (str(listNickMsg[1]).find("ide")) != -1 or (str(listNickMsg[1]).find("idę")) != -1:
            browser.find_element_by_class_name("text-input").send_keys((listNickMsg[0])+": idź", Keys.ENTER)
        if (str(listNickMsg[1]).find("skarbus")) != -1 or (str(listNickMsg[1]).find("skarbuś")) != -1:
            browser.find_element_by_class_name("text-input").send_keys((listNickMsg[0])+": skarbuś... <u-rzyganie>", Keys.ENTER)
        if (str(listNickMsg[1]).find("ssij")) != -1:
            browser.find_element_by_class_name("text-input").send_keys((listNickMsg[0])+": zrób mi <u-lodzik2>", Keys.ENTER)
        if (str(listNickMsg[1]).find("brak bolca")) != -1:
            browser.find_element_by_class_name("text-input").send_keys((listNickMsg[0])+": brak stolca?:o", Keys.ENTER)     
        if (str(listNickMsg[1]).find("brak stolca")) != -1:
            browser.find_element_by_class_name("text-input").send_keys((listNickMsg[0])+": brak bolca?:o", Keys.ENTER)
        if (str(listNickMsg[1]).find("prezes ciota")) != -1:
            browser.find_element_by_class_name("text-input").send_keys((listNickMsg[0])+": no ciota, ciota <u-n06>", Keys.ENTER)
    finally:
        return True

def accosted(browser, listNickMsg, unique):
    try:
        if listNickMsg[1] == "klakier_xD co słychać?":
            browser.find_element_by_class_name("text-input").send_keys((listNickMsg[0])+ ": stare komuchy nie chcą zdychać :-/", Keys.ENTER)
    
    finally:
        return True
    
def special(browser, listNickMsg, unique):
    try:
        if unique == "kot32: xD" or unique == "Ashele: xD":
            browser.find_element_by_class_name("text-input").send_keys("xD", Keys.ENTER)

    finally:
        return True

def command(browser, listElements, unique):
    try:
        if listNickMsg[0] == 'kot32' and listNickMsg[1] == "w!":
            print("#### jest wyjdz ####")
            browser.quit()
    
    finally:
        return True

'''def getRandomRespond(query):
    try:
        browserWindow = True
        browser = setupBrowser(browserWindow)
        browser.get("https://google.pl")
        search = browser.find_element_by_name('q')
        search.send_keys(query)
        search.send_keys(Keys.RETURN)
        time.sleep(2)
        search = browser.find_element_by_class_name("r").click()
        time.sleep(2)
        content = browser.find_element_by_tag_name("body")
        #print(content.text)
    finally:
        browser.quit()
        '''
#def parseRadomRespond

try:
    bannerKilled = False
    configParams = readConfig(selectChat())
    browserWindow = False
    browser = setupBrowser(browserWindow)
    joinChat(browser, configParams[0], configParams[1], configParams[2])
    oldListElements = getFiveLastElements(browser)
    time.sleep(5)
    while True:
        listElements = getFiveLastElements(browser)
        uniqueSet = compareListsElement(listElements, oldListElements)
        uniqueList = list(uniqueSet)
        #print("unique: ", uniqueList)
        for unique in uniqueList:
            time.sleep(1)
            #print("MSG: ", unique)
            listNickMsg = unique.split(": ", 1)
            print("SPLIT: ", listNickMsg)
            '''notifications'''
            if len(listNickMsg) == 1:
                if (notification(browser, listNickMsg, unique)) == False:
                    print("### notification false ###")
            '''notifications'''
            
            '''users input '''
            if len(listNickMsg) == 2:
                if (general(browser, listNickMsg, unique)) == False:
                    print("### general false ###")
                if (accosted(browser, listNickMsg, unique)) == False:
                    print("### accosted false ###")
                if (special(browser, listNickMsg, unique)) == False:
                    print("### special false ###")
                if (command(browser, listNickMsg, unique)) == False:
                    print("### command false ###")    
            '''users input'''         
            #TODO: jak sie czujesz

            #uwalamy baner
            if bannerKilled == False:
                bannerKilled = killBanner(browser)
                if bannerKilled == True:
                    print("### BANNER KiLLED", bannerKilled)
                    input()

        #robimy kopie elementow do sprawdzenia w nastpnej iteracji by nie dublowac
        oldListElements = listElements
        time.sleep(7)
finally:
    print("zamykamy")
    browser.quit()