from selenium.webdriver.common.keys import Keys 

def accosted(browser, listNickMsg, unique):
    if listNickMsg[1] == "klakier_xD co słychać?":
        browser.find_element_by_class_name("text-input").send_keys((listNickMsg[0])+ ": stare komuchy nie chcą zdychać :-/", Keys.ENTER)
    