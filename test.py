import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from parser import URL_ARRIVALS, URL_DEPARTURES


class ParserTest(unittest.TestCase):

    def test_arrivals(self):
        driver = webdriver.Chrome()
        driver.get(URL_ARRIVALS)
        tables = driver.find_elements(By.TAG_NAME, 'tbody')
        arrivals_button = tables[0]
        days_buttons = driver.find_elements(By.XPATH, "//div[@class='flight-day__filter']//p[@data-day='1']")
        tomorrow_button = days_buttons[0]
        self.assertTrue(arrivals_button.is_displayed())
        self.assertTrue(tomorrow_button.is_displayed())

    def test_departures(self):
        driver = webdriver.Chrome()
        driver.get(URL_DEPARTURES)
        tables = driver.find_elements(By.TAG_NAME, 'tbody')
        departure_button = tables[1]
        days_buttons = driver.find_elements(By.XPATH, "//div[@class='flight-day__filter']//p[@data-day='1']")
        tomorrow_button = days_buttons[1]
        self.assertTrue(departure_button.is_displayed())
        self.assertTrue(tomorrow_button.is_displayed())


if __name__ == "__main__":
    unittest.main()
