from selenium.webdriver.common.keys import Keys 

def notification(browser, listNickMsg, unique):
    if listNickMsg[0] == "+ kot32 wszedł":
        browser.find_element_by_class_name("text-input").send_keys("siema kocie", Keys.ENTER)
        print("szukalismy kot wszedl")
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
    if listNickMsg[0] == "+ CzarnaWdowa... wszedł":
        browser.find_element_by_class_name("text-input").send_keys("CzarnaWdowa... <u-pok2>", Keys.ENTER)
    if listNickMsg[0] == "~Zostałeś rozłączony":
        browser.quit()