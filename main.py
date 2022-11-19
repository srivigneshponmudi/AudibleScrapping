from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "C:\Development\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)



