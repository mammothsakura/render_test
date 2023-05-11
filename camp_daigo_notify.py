# -*- coding: utf-8 -*-


from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import datetime
from webdriver_manager.chrome import ChromeDriverManager
from dateutil.relativedelta import relativedelta
import os
from glob import glob
import pandas as pd
import shutil
from tkinter import messagebox
import time
import requests

# LineNotify設定

if __name__ == '__main__':
    # URL関連
    url = "http://www.greenvila.jp/cgi-local/schedule/schedule.cgi?mode=1&year=2023&month=5"
    # ヘッドレスモードの設定。
    # True => ブラウザを描写しない。
    # False => ブラウザを描写する。
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')#コメント解除で描写なし
    # Chromeを起動
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # ログインページを開く
    driver.get(url)
    # ログオン処理
    messagebox.showinfo('確認', 'ページを開く')

    start = time.time()  # forループ開始前のエポック時間を変数startに保存しておく。
    # duration = int(input("forループを実行する期間(秒数)を入力してください")) #　キーボードからループする秒数を取得する。
    duration = 36000000
    end = start + duration  # forループの開始時間＋forループの実行時間 = forループの終了時間
    sleep(1)
    while time.time() <= end:  # 今の時刻が、終了時間(開始時間＋キーボードから入力された秒数)以下であれば、ループを続ける
        # whileループで繰り返し実行する処理のコードをここに書く。Printは、その一例。

        driver.get(url)
        sleep(1)
        a = driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div/table/tbody/tr/td/table/tbody/tr[6]/td[28]').text  # .click()  # ここを変更_最後のtr(数字内を変更)変更末尾/aはそのままで残す
        print(a)
        if a == "×":
            print("空いてないやでー")
            sleep(30)
        else:
            # 予約したい日のURLを取得。Lineに送る
            cur_url = driver.current_url  # 現在のurl取得

            # LineNotify設定
            lineurl = "https://notify-api.line.me/api/notify"
            token = "VkupzpRxAmbJC1M4GcPpMmhMuCQPrUYXbU5NQFzuvFR"
            headers = {"Authorization": "Bearer " + token}
            message = 'フリーサイト空いてるで！' + cur_url
            payload = {"message": message}
            r = requests.post(lineurl, headers=headers, params=payload)

            # messagebox
            print(cur_url)
            # messagebox.showinfo('確認', '空いてるで！')
            # 30分入力待ち
            sleep(1800)

print("finish")
