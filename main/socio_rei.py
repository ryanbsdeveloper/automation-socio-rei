from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class SocioRei:
    def __init__(self):
        chrome_service = Service(executable_path='chromedriver.exe')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(r'--incognito')
        chrome_options.add_argument('--headless')
        self.chrome = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def open_site(self, site):
        self.chrome.get(site)
        sleep(10)

    def enter_account(self):
        botao_entrar = self.chrome.find_element(By.XPATH, '/html/body/app-root/div/app-header/header/div/div/div/a')
        botao_entrar.click()

        sleep(10)

        email = self.chrome.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/app-modal-auth/div/mat-dialog-content/div[2]/form/mat-form-field[1]/div/div[1]/div/input')
        senha = self.chrome.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/app-modal-auth/div/mat-dialog-content/div[2]/form/mat-form-field[2]/div/div[1]/div/input')
        email.send_keys('meucpf')
        senha.send_keys('minhasenha')
        logar = self.chrome.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/app-modal-auth/div/mat-dialog-content/div[2]/form/button')
        logar.click()

    def exit(self):
        self.chrome.quit()


if __name__ == '__main__':
    sociorei = SocioRei()
    sociorei.open_site('https://www.sociorei.com/')
    sociorei.enter_account()
    sleep(10)
    sociorei.exit()

