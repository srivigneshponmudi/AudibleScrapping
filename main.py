from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "C:\Development\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver_path)

# Scrape the category and display to the user for selection.

driver.get(
    "https://www.audible.in/categories?ref=a_hp_t1_navTop_pl2cg0c1r6&pf_rd_p=bd847071-ce8d-41ea-8fa9-eb314d40b67a&pf_rd_r=28X6MYPPM5SDB9FRDCR9")

category_list = driver.find_elements(By.CLASS_NAME, "categoryLink ")

print("Choose the desired category for the scrapping- Choose option 0-23")

for i, j in enumerate(category_list, start=0):
    print("{}.{}".format(i, j.text))

# Click the relevant category based on the user input

user_selection = input()
category_name=category_list[int(user_selection)].text

cat_button=driver.find_element(By.LINK_TEXT,category_name)
cat_button.click()

