from selenium.webdriver.common.keys import Keys 

def general(browser, listNickMsg, unique):
    if listNickMsg[0] == 'kot32' and listNickMsg[1] == "kim jestem?":
        browser.find_element_by_class_name("text-input").send_keys((listNickMsg[0])+": jesteś zwyciężcą!", Keys.ENTER)
    if listNickMsg[1] == "hej" or listNickMsg[1] == "hejka" or listNickMsg[1] == "witam" or listNickMsg[1] == "cześć" or listNickMsg[1] == "czesc":
        print("jest hej")
        value = browser.find_element_by_class_name("text-input").send_keys((listNickMsg[0])+ ": witaj :)", Keys.ENTER)
        print(value)
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