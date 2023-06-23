from selenium import webdriver

a = webdriver.Chrome()
a.get("https://www.amazon.in/")
a.maximize_window()

a.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys('iphones')

a.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()

list = a.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")

print (str(len(list)) + ' products found')

for i in list:
    print (i.text)

a.quit()
