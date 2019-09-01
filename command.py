from selenium.webdriver.common.keys import Keys 

def command(browser, listNickMsg, unique):
    if listNickMsg[0] == 'kot32' and listNickMsg[1] == "w!":
        print("#### jest wyjdz ####")
        browser.quit()