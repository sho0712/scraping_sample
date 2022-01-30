import time

# noinspection PyUnresolvedReferences
import chromedriver_binary
from selenium import webdriver


def main():
    food = 'とまと'
    # ドライバーの立ち上げ（グーグルクロームを操作する人を立ち上げる）
    driver = webdriver.Chrome()

    # Googleにアクセス
    driver.get('https://google.com')

    time.sleep(10)
    driver.close()


if __name__ == '__main__':
    main()
