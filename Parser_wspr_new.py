from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from Conversion_tables import converse_tab
import pandas as pd
import os

driver = webdriver.Chrome()
driver.get('http://wsprnet.org/drupal/wsprnet/spotquery')
login = driver.find_element_by_id('edit-name')
password = driver.find_element_by_id('edit-pass')
btn_elem_log = driver.find_element_by_id('edit-submit--2')
login.send_keys('r2aja')  # Логин
password.send_keys('lis58')  # Пароль
btn_elem_log.click()


def main():
    page_elements('All', '50', 'R2AJA', '86400', 'date')
    page = driver.page_source  # считываем содердимое страницы браузером
    df1 = pd.read_html(page)  # присваиваем содердимое страницы Data Frame-у pandas (по факту таблица)
    df1[0].to_csv('Temp1.csv', index=False)  # Выводим содержимое в csv первый раз
    spec_param = driver.find_element_by_link_text("Specify query parameters").click()
    page_elements('All', '50', 'QR2AJA', '86400', 'date')
    page2 = driver.page_source
    df2 = pd.read_html(page2)
    df2[0].to_csv('Temp2.csv', index=False)  # Выводим содержимое во второй раз
    pnd_magic()
    driver.quit()


def page_elements(bnd, cnt, cll, tmt, srt):
    #  Band
    Band_find = Select(driver.find_element_by_id('edit-band'))
    Band_find.select_by_value(bnd)  # (по умолчанию All)
    #  Count
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'edit-count'))).clear()  # Очищаем Count
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'edit-count'))).send_keys(cnt)  # Вводим Count
    #  Call
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'edit-call'))).clear()  # Очищаем Call
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'edit-call'))).send_keys(cll)  # Позывной
    # Reporter
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'edit-reporter'))).send_keys('')

    # Timelimit
    In_last_find = Select(driver.find_element_by_id('edit-timelimit'))
    In_last_find.select_by_value(tmt)  # 24 часа
    # Sort by
    Sort_by_find = Select(driver.find_element_by_id('edit-sortby'))
    Sort_by_find.select_by_value(srt)  # Сортировка по дате
    # Reverse
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'edit-sortrev'))).click()
    # Unique
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'edit-unique'))).click()
    Exclude_special_find = driver.find_element_by_id("edit-excludespecial").is_selected()  # Проверка статус чек-бокса
    if Exclude_special_find:  # if Exclude_special_find == True Если галочка стоит
        driver.find_element_by_id("edit-excludespecial").click()  # кликаем мышкой и снимаем галку
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'edit-excludespecial'))).click()  # снимаем
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'edit-submit'))).click()  # подтверждаем всё
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'table')))  # ожидаем таблицу <table>


def pnd_magic():
    pd.set_option('expand_frame_repr', False)
    pd.set_option('display.max_rows', 100)
    pd.set_option('expand', False)
    converse_tab()
    path1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Temp1.csv')
    path2 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Temp2.csv')
    os.remove(path1)
    os.remove(path2)


main()
