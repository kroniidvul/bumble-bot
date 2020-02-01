from selenium import webdriver
from time import sleep

from secret import phone_number, password

class BumbleBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Windows\System32\chrome-driver\chromedriver.exe')

    def login(self):
        self.driver.get('https://bumble.com')

        sleep(2)

        sign_in_btn = self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
        sign_in_btn.click()
        sleep(2)

        use_cell = self.driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/main/div/div[2]/form/div[3]/div/span/span')
        use_cell.click()
        sleep(2)

        cell_num_in = self.driver.find_element_by_xpath('//*[@id="phone"]')
        cell_num_in.send_keys(phone_number)
        sleep(2)
        
        confirm_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/main/div/div[2]/form/div[4]/button/span/span')
        confirm_btn.click()
        sleep(2)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)
        sleep(2)
        
        login_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/main/div/div[2]/form/div[2]/button/span/span')
        login_btn.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/span/span')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/span/span')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[1]/div/div[2]/div/div[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = BumbleBot()
# bot.login()