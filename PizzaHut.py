from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



# access chrome webdriver
driver = webdriver.Chrome("C:\Drivers\chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(5) #implicity wait

# accesss web
driver.get("https://www.pizzahut.ca/home")
driver.maximize_window()


# to click on continoue
continoue = driver.find_element_by_xpath("//button[@class='button secondary']").click()



# Procedure to create account

signin = driver.find_element_by_xpath("//div[@class='pointer sign-in']").click()

# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") #scroll to end
# time.sleep(3)
# create_acc = driver.find_element_by_xpath("//button[@data-qa-label='CreateAccountLnk']").click()



# # fill info
# element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-qa-label='FirstNameTxt']")))        # web driver wait



# first_name = driver.find_element_by_xpath("//input[@data-qa-label='FirstNameTxt']")
# first_name.clear()
# first_name.send_keys("James")


# last_name = driver.find_element_by_xpath("//input[@data-qa-label='LastNameTxt']")
# last_name.clear()
# last_name.send_keys("Bond")


# email = driver.find_element_by_xpath("//input[@data-qa-label='EmailTxt']")
# email.clear()
# email.send_keys("abc.abcd@gmail.com")


# number = driver.find_element_by_xpath("//input[@data-qa-label='MobileTxt']")
# number.clear()
# number.send_keys("6476276250")


# time.sleep(1)
# checkbox = driver.find_element_by_xpath("""//*[@id="opt-in"]""")
# checkbox.click()


# pw = driver.find_element_by_xpath("//input[@data-qa-label='AccountPasswordTxt']")
# pw.clear()
# pw.send_keys("James@123")


# rpw = driver.find_element_by_xpath("//input[@data-qa-label='AccountRetypePasswordTxt']")
# rpw.clear()
# rpw.send_keys("James@123")


# submit = driver.find_element_by_xpath("//button[@data-qa-label='AccountCreateAccountBtn']").click()


# sign in

email = driver.find_element_by_xpath("//input[@name='username']")
email.clear()
email.send_keys("abc.abcd@gmail.com")

pw = driver.find_element_by_xpath("//input[@name='password']")
pw.clear()
pw.send_keys("James@123")

sign_in = driver.find_element_by_xpath("//button[@data-qa-label='SignInBtn']").click()



# to enter postal code
time.sleep(5)
postalcode = driver.find_element_by_name("zipCode").send_keys("N9B2N5")

# find my hurt
time.sleep(3)
find = driver.find_element_by_xpath("//button[@data-qa-label='FindMyHutBtn']").click()



# text field

streetnumber = driver.find_element_by_xpath("//input[@data-qa-label='StreetNumberTxt']")
streetnumber.clear()
streetnumber.send_keys("427")

streetname = driver.find_element_by_xpath("//input[@data-qa-label='StreetNameTxt']")
streetname.clear()
time.sleep(1)
streetname.send_keys("Josephine")


city = driver.find_element_by_xpath("//input[@data-qa-label='CityTxt']")
city.clear()
city.send_keys("Windsor")


order = driver.find_element_by_xpath("//button[@data-qa-label='FindStoreBtn']")
order.click()
time.sleep(5)
acceptance = driver.find_element_by_xpath("//button[@data-qa-label='PartialMatchFoundConfirmBtn']").click()
time.sleep(5)

# pizza preparation

# create = driver.find_element_by_xpath("//img[@class='image create-your-own-pizza']").click()
# create = driver.find_element_by_xpath("//div[text()='Create Your Own Pizza']").click()
# create = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Create Your Own Pizza']")))
# driver.find_element_by_partial_link_text("Create Your Own Pizza").click()

create = driver.find_element_by_xpath("""/html/body/div[1]/div[2]/div/div[2]/div/div[2]/ul/li[1]/a/div[1]/img""").click()
# create = driver.find_element_by_xpath("//div[contains(text(),'Create Your Own Pizza')]").click()


size_option = driver.find_element_by_xpath("//div[@data-qa-label='PizzaBuilderSizeAccordian']")
size_option.click()
time.sleep(5)

size = driver.find_element_by_xpath("""//span[contains(text(),'12" Medium')]""")
size.click()
time.sleep(2)
size_option.click()

# Mozzarella_option = driver.find_element_by_xpath("//div[@data-qa-label='PizzaBuilderCheeseAccordian']").click()
# time.sleep(3)
# extra = driver.find_element_by_xpath("//li[@menu-item-id='e_ZPyef9egh9cCn8_DOK9atEiDmAVbrYtVQHwvh90fg']").click()
# time.sleep(3)


# scroll
driver.execute_script("window.scrollBy(0,6000)")

time.sleep(3)
add_order = driver.find_element_by_xpath("//button[@data-qa-label='AddToOrderBtn']").click()
close = driver.find_element_by_xpath("//div[@class='close-button']").click()

# ele = EC.element_to_be_clickable(By.XPATH, "//button[@class='button cancel expanded']")
#
# if ele==true:
#     driver.find_element_by_xpath("//button[@class='button cancel expanded']").click()
# else:
#     close = driver.find_element_by_xpath("//div[@class='close-button']").click()




# no = driver.find_element_by_xpath("//button[@class='button cancel expanded']").click()

navigate_cart = driver.find_element_by_xpath("//i[@data-qa-label='CartIcon']").click()
time.sleep(3)
# navigate_cart = driver.find_element_by_class_name("cart-icon").click()

checkout = driver.find_element_by_xpath("//button[contains(text(),'Checkout')]").click()
time.sleep(3)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") #scroll
time.sleep(3)
# place_order = driver.find_element_by_xpath("//button[@data-qa-label='PlaceYourOrderBtn']").click()
# time.sleep(3)
driver.quit()