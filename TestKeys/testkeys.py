from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys


class YandexSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome("C:/Users/MrShiki/Desktop/operadriver_win64/operadriver.exe")
        self.driver.get('https://rasp.yandex.ru')

    def test_01(self):
        driver = self.driver
        input_from = driver.find_element_by_id('from')
        time.sleep(2)
        input_from.send_keys('Кемерово')
        input_to = driver.find_element_by_id('to')
        input_to.send_keys('Москва')
        input_when = driver.find_element_by_id('when')
        input_when.send_keys('7 июля')
        input_when.send_keys(Keys.ENTER)
        time.sleep(2)
        titles = driver.find_element_by_class_name('SearchTitle>span')
        for title in titles:
            assert "Расписание рейсов из Кемерова в Москву" in title.text

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == 'main':
    unittest.main()
