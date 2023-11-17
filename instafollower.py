from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time


class InstaFollower():
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        
        self.driver = webdriver.Chrome(options=self.chrome_options)

        self.wait = WebDriverWait(self.driver, 60)

    
    def login(self, username, password):
        self.driver.get('https://www.instagram.com/accounts/login/')

        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
        username_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)

        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)

        login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_btn.click()

        time.sleep(3)
        print('test')
        # self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mount_0_0_NT > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > div > div')))
        not_now_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        not_now_button.click()

        time.sleep(3)
        not_now_button2 = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]') 
        not_now_button2.click()


    def find_followers(self):
        self.driver.get('https://www.instagram.com/marvel/')

        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')))
        followers_btn = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')
        followers_btn.click()
        #self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div')))
        #self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]')))
        time.sleep(3)
        print('test2')
        follower_box = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]')
        scroll = 0
        while scroll < 2:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_box)
            time.sleep(2)
            scroll += 1
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollTop)", follower_box)
        self.follow()

        

    def follow(self):
        following_accts = self.driver.find_elements(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div')
        print(following_accts)
        for _ in range(len(following_accts)):
            follow_btn = self.driver.find_element(By.XPATH, f'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[{_+1}]/div/div/div/div[3]/div/button') 
            # /html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[1]/div/div/div/div[3]/div/button
            # /html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[2]/div/div/div/div[3]/div/button
            # follow_btn.click
            try:
                follow_btn.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
                cancel_button.click()
                time.sleep(1)
                

            # follow_btn.click()
            # if self.driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div'):
            #     cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
            #     cancel_button.click()
            #     time.sleep(1)
            # else: 
            #     follow_btn.click()
            #     time.sleep(1)
            

            # /html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[1]
            # /html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[1]/div/div/div/div[3]/div/button/div/div
        #     /html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[1]
        # /html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[2]

    def add_followers(self, username, password):
        self.login(username, password)
        time.sleep(1)
        self.find_followers()