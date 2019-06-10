from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


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
        time.sleep(5)
        titles = driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/div/div[1]/div[1]/div/section/article[1]/header/div/h3')
        print(titles.text)
        times = driver.find_element_by_class_name('SearchSegment__duration')
        print(times.text)
        try:
            driver.find_element_by_tag_name('svg')
        except NoSuchElementException:
            return print('no icon')
        countElements = len(driver.find_elements_by_class_name('SearchSegment'))
        if countElements < 5:
            return print('False')

    def test_02(self):
        driver = self.driver
        input_from = driver.find_element_by_id('from')
        time.sleep(2)
        input_from.send_keys('Кемерово проспект Ленина')
        input_to = driver.find_element_by_id('to')
        input_to.send_keys('Кемерово Бакинский переулок')
        input_when = driver.find_element_by_id('when')
        input_when.send_keys('среда')
        bus = driver.find_element_by_xpath(
            '//*[@id="root"]/div/header/div[1]/div/div[4]/span/label[5]')
        bus.click()
        button = driver.find_element_by_xpath('//*[@id="root"]/div/header/div[1]/div/div[5]/form/button[2]')
        button.click()
        try:
            driver.find_elements_by_class_name('ErrorPage')
        except NoSuchElementException:
            return print('False, no error page')

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == 'main':
    unittest.main()
