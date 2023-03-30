import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from datetime import date
from selenium.webdriver.common.keys import Keys


url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/?userSelect=1#/login'
balance ='body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)'
texte= '250'
name_customer= 'Ron Weasly'

# 1. כנס לבנק בתור משתמש תעשה הפקדה- 1000 ש"ח משיכה- 250 ש"ח ותבדוק שהמצב של החשבון 750 ש"ח
def open_site(url):
    driver= webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    driver.maximize_window()
    return driver

def customer_login (driver, customer_login, name_customer):
    customer_login = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button')
    customer_login.click()
    time.sleep(3)
    user = driver.find_element(By.CSS_SELECTOR, '#userSelect')
    user.click()
    time.sleep(4)
    sel = Select(driver.find_element(By.CSS_SELECTOR, '#userSelect'))
    sel.select_by_visible_text(name_customer)
    time.sleep(2)
    login_selector = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > form > button')
    login_selector.click()
    time.sleep(3)
    return customer_login

def balance(driver):
    balance = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)').text
    print(balance)
    return balance
# ----------------deposit-------------------------
def deposit(driver):
    deposit= driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)')
    deposit.click()
    time.sleep(3)
    amount = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
    amount.send_keys('1000')
    time.sleep(3)
    deposit_btn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button')
    deposit_btn.click()
    time.sleep(3)
    return deposit
# ----------------deposit-------------------------

# ----------------withdraw-------------------------
def withdraw(driver, amount, text):
    withdraw = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)')
    withdraw.click()
    time.sleep(3)
    amount = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
    amount.send_keys(text)
    time.sleep(3)
    withdraw_btn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button')
    withdraw_btn.click()
    time.sleep(3)
    return withdraw
#  ----------------withdraw-------------------------

#2. כתוב קוד שנכנס למערכת בתור מנהל ותוסיף חשבון חדש תבדוק שאתה בURL המתאים
def bank_manger_login(driver):
    bank_manager_login = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button')
    bank_manager_login.click()
    time.sleep(3)

def url_open_site(driver):

        print(driver.current_url)
        return driver

def open_account(driver):
    open_account = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[2]')
    open_account.click()
    time.sleep(2)
    customer_table = driver.find_element(By.XPATH, '//*[@id="userSelect"]')
    customer_table.click()
    time.sleep(2)
    sel = Select(driver.find_element(By.CSS_SELECTOR, '#userSelect'))
    sel.select_by_visible_text('Neville Longbottom')
    time.sleep(2)
    currency = driver.find_element(By.CSS_SELECTOR, '#currency')
    currency.click()
    time.sleep(1)
    sel= Select(driver.find_element(By.CSS_SELECTOR, '#currency'))
    sel.select_by_visible_text('Rupee')
    time.sleep(2)
    process = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button')
    process.click()
    time.sleep(3)
    driver.switch_to.alert.accept()
    time.sleep(2)
    print('Account created successfully')
    print(driver.current_url)


def transaction(driver):
    transaction = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)')
    transaction.click()
    time.sleep(3)
    datetime= driver.find_element(By.CSS_SELECTOR, '#start')
    datetime.click()
    time.sleep(2)
    datetime.send_keys('29/03/2023')
    datetime.click()
    time.sleep(3)
    return transaction

def amount (driver):
    amount = driver.find_element(By.CSS_SELECTOR, '#anchor0 > td:nth-child(2)').text
    return (amount)


# # ** ** ** *test1** ** *
# driver = open_site(url)
# customer_login(driver, customer_login, name_customer)
# balance(driver)
# deposit(driver)
# withdraw(driver, amount, texte)
# balance(driver)

# # *******test2*****
# driver= open_site(url)
# bank_manger_login(driver)
# open_account(driver)
# url_open_site(driver)

# ********test3********
# driver=open_site(url)
# name_customer = 'Hermoine Granger'
# customer_login (driver, customer_login, name_customer)
# text='1500'
# withdraw(driver, amount, text)
# transaction(driver)
# amount(driver)
