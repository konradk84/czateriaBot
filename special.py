from selenium.webdriver.common.keys import Keys 

def special(browser, listNickMsg, unique):
    if unique == "kot32: xD" or unique == "Ashele: xD":
        browser.find_element_by_class_name("text-input").send_keys("xD", Keys.ENTER)