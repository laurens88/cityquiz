from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

class Player:
    def __init__(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://cityquiz.io/quizzes/world")

        wait = WebDriverWait(self.driver, 10)
        self.input_box = wait.until(
            EC.element_to_be_clickable((By.ID, "city-input"))
        )

    def guess(self, city):
        time.sleep(0.2)
        self.input_box.send_keys(city)
        time.sleep(0.2)
        self.input_box.send_keys(Keys.RETURN)