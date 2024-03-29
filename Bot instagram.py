from selenium import webdriver
import time

navegador = webdriver.Chrome()
navegador.get('https://www.instagram.com')
time.sleep(1.5)
navegador.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]').click()
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('dexgame4006@gmail.com')
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('juxKah-sudvun-xowzy7')
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()

time.sleep(6)
navegador.find_element_by_xpath('//*[@id="mount_0_0_eb"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[5]/div/div/div/span/div/a').click()