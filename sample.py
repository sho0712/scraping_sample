import time

# noinspection PyUnresolvedReferences
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    food = 'とまと'
    # ドライバーの立ち上げ（グーグルクロームを操作する人を立ち上げる）
    driver = webdriver.Chrome()

    # Googleにアクセス
    driver.get('https://google.com')

    driver.find_element(By.NAME, "q").send_keys(food)

    time.sleep(10)
    driver.close()


if __name__ == '__main__':
    main()
