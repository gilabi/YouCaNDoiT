from main import *
import pytest

class Test_Bank:

    def test1(self):
        driver= open_site(url)
        customer_login(driver, customer_login, name_customer)
        actual = balance(driver)
        deposit(driver)
        withdraw(driver, amount, texte)
        expected=balance(driver)
        assert actual != expected

    def test2(self):
         driver = open_site(url)
         actual = url_open_site(driver)
         bank_manger_login(driver)
         expected = open_account(driver)
         assert actual != expected


    def test3(self):
        driver = open_site(url)
        name_customer= 'Hermoine Granger'
        customer_login(driver, customer_login, name_customer)
        text='1500'
        withdraw(driver,amount, text)
        transaction(driver)
        actual = int(amount(driver))
        expected = 1500
        assert actual == expected

