import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import SafariOptions


URL_DEPARTURES = "https://beg.aero/eng/flights#departures"
URL_ARRIVALS = "https://beg.aero/eng/flights#arrivals"

class Parser:

    def __init__(self, type_of_schedule, day):
        self.type_of_schedule = type_of_schedule
        self.options = None
        self.day = day
        self.url = None
        self.driver = None
        self.options = None
        self.table = None
        self.all_flights = None
        self.day_index = None
        self.days_buttons = None
        self.chosen_button = None
        self.list_of_flights = []

    def run_webdriver(self):
        self.options = SafariOptions()
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Safari(options=self.options)
        self.driver.get(self.url)
        return self.driver

    def choose_the_url(self):
        if self.type_of_schedule == 'Arrivals':
            self.url = URL_ARRIVALS
        elif self.type_of_schedule == 'Departures':
            self.url = URL_DEPARTURES
        return self.url

    def get_the_table(self):
        tables = self.driver.find_elements(By.TAG_NAME, 'tbody')
        if self.type_of_schedule == 'Arrivals':
            self.table = tables[0]
        elif self.type_of_schedule == 'Departures':
            self.table = tables[1]
        return self.table

    def get_the_day_index(self):
        if self.day == "Yesterday":
            self.day_index = '-1'
        elif self.day == "Today":
            self.day_index = '0'
        elif self.day == "Tomorrow":
            self.day_index = '1'
        return self.day_index

    def get_chosen_button(self):
        time.sleep(2)
        self.days_buttons = self.driver.find_elements(By.XPATH, f"//div[@class='flight-day__filter']//p[@data-day="
                                                                f"{self.day_index}]")
        if self.type_of_schedule == 'Arrivals':
            self.chosen_button = self.days_buttons[0]
        elif self.type_of_schedule == 'Departures':
            self.chosen_button = self.days_buttons[1]
        return self.chosen_button

    def get_all_flights(self):
        self.chosen_button.click()
        self.get_the_table()
        time.sleep(2)
        self.all_flights = self.table.find_elements(By.TAG_NAME, 'tr')
        # for flight in self.all_flights:
        #     destination = flight.find_element(By.CLASS_NAME, 'destination__flight')
        #     flight_number = flight.find_element(By.CLASS_NAME, 'number__flight')
        #     scheduled = flight.find_element(By.CLASS_NAME, 'hour__flight')
        #     airline = flight.find_element(By.CLASS_NAME, 'company__flight.thide')
        #     gate = flight.find_element(By.CLASS_NAME, 'hall__flight.thide')
        #     status = flight.find_element(By.CLASS_NAME, 'status__flight')
        #     self.list_of_flights.append([destination.text, flight_number.text, scheduled.text, airline.text, gate.text,
        #                                  status.text])

    def find_flights_by_city(self, city="Vie"):
        for flight in self.all_flights:
            destination = flight.find_element(By.CLASS_NAME, 'destination__flight')
            flag = re.findall(city[:4], destination.text)
            if flag:
                flight_number = flight.find_element(By.CLASS_NAME, 'number__flight')
                scheduled = flight.find_element(By.CLASS_NAME, 'hour__flight')
                airline = flight.find_element(By.CLASS_NAME, 'company__flight.thide')
                gate = flight.find_element(By.CLASS_NAME, 'hall__flight.thide')
                status = flight.find_element(By.CLASS_NAME, 'status__flight')
                self.list_of_flights.append([destination.text, flight_number.text, scheduled.text, airline.text,
                                             gate.text, status.text])

    def run(self):
        self.choose_the_url()
        self.get_the_day_index()
        self.run_webdriver()
        self.get_chosen_button()
        self.get_all_flights()
        self.find_flights_by_city()
        self.driver.quit()


