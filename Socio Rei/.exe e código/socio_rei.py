from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from myutils.utils_ry import checkNet
from webdriver_manager.chrome import ChromeDriverManager


class SocioRei:
    def __init__(self):
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        # options.add_argument(r'--incognito')
        # options.add_argument('--headless')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.chrome = webdriver.Chrome(service=service, options=options)

    def open_site(self, site):
        sleep(2)
        self.chrome.get(site)

    def enter_account(self):
        sleep(2)
        botao_entrar = self.chrome.find_element(By.XPATH, '/html/body/app-root/div/fengstlayout-header/header/section/nav/a[1]')
        botao_entrar.click()

        sleep(2)

        email = self.chrome.find_element(By.CSS_SELECTOR, '#mat-input-0')
        senha = self.chrome.find_element(By.CSS_SELECTOR, '#password')
        email.send_keys('LOGIN')
        senha.send_keys('SENHA')
        logar = self.chrome.find_element(By.CSS_SELECTOR, '#mat-dialog-0 > app-modal-auth > div > mat-dialog-content > div.form-content.animated.ng-star-inserted > form > button')
        logar.click()

    def exit(self):
        self.chrome.quit()


if __name__ == '__main__':
    if checkNet():
        print('\033[1;32mACESSO A INTERNET SUCEDIDO\033[m')
        try:
            print()
            print('Iniciando o bot...')
            sociorei = SocioRei()
            sociorei.open_site('https://www.sociorei.com/')
            sociorei.enter_account()
            sleep(5)
            sociorei.exit()

        except Exception as error: 
            print('\033[1;31mAlgo inesperado aconteceu\033[m, Tentando novamente. Aguarde... ')
            sleep(3)
            print()
            print('Iniciando o bot...')
            sociorei = SocioRei()
            sociorei.open_site('https://www.sociorei.com/')
            sociorei.enter_account()
            sleep(3)
            sociorei.exit()

        else:
            print()
            print('\033[1;32mBot efetuado com êxito\033[m')
            sleep(2)

    else:
        print('\033[1;31mACESSO A INTERNET NEGADO\033[m')
        print('Outra tentativa será feita, quando houver acesso.')
        while True:
            if checkNet():
                print()
                sleep(5)
                print('\033[1;32mACESSO SUCEDIDO!\033[m')
                try:
                    print()
                    print('Iniciando o bot...')
                    sociorei = SocioRei()
                    sociorei.open_site('https://www.sociorei.com/')
                    sociorei.enter_account()
                    sleep(10)
                    sociorei.exit()

                except Exception as error: 
                    print('\033[1;31mAlgo inesperado aconteceu\033[m, Tentando novamente. Aguarde... ')
                    sleep(3)
                    print()
                    print('Iniciando o Bot...')
                    sociorei = SocioRei()
                    sociorei.open_site('https://www.sociorei.com/')
                    sociorei.enter_account()
                    sleep(3)
                    sociorei.exit()

                else:
                    print()
                    print('\033[1;32mBot efetuado com êxito\033[m')
                    sleep(2)
                    break
