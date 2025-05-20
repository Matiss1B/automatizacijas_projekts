from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
def check_add(driver):
    time.sleep(1)
    try:
        add = driver.find_element(By.ID, "skip128356")
        add.click()
    except NoSuchElementException:
        return

    try:
        close = driver.find_element(By.ID, "xS_1143401_Close")
        close.click()
    except NoSuchElementException:
        return
def add_addressee(find, email_list):
    for email in email_list:
        find.send_keys(email)
        time.sleep(1)
        find.send_keys(",")
        time.sleep(1)
        find.send_keys(" ")


def send_email(email_list, file_path):
    file_path = f"content/{file_path}"
    subject = os.path.basename(file_path)
    with open(file_path, "r", encoding="utf-8") as file:
        body_text = file.read()
    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=option)
    wait = WebDriverWait(driver, 2)
    url = "https://www.inbox.lv/"
    driver.get(url)

    check_add(driver)

    wait.until(EC.presence_of_element_located((By.ID, "imapuser"))).send_keys("testprofilestruktura@inbox.lv")
    wait.until(EC.presence_of_element_located((By.ID, "pass"))).send_keys("testProfileStruktura1!")
    wait.until(EC.element_to_be_clickable((By.ID, "btn_sign-in"))).click()

    check_add(driver)

    wait.until(EC.element_to_be_clickable((By.ID, "mail-menu__link_compose"))).click()
    wait.until(EC.presence_of_element_located((By.ID, "suggest-to")))
    subject_input = wait.until(EC.presence_of_element_located((By.ID, "subject")))
    subject_input.send_keys(subject[:-4])

    find_to = wait.until(EC.presence_of_element_located((By.ID, "suggest-to")))
    add_addressee(find_to, email_list)
    time.sleep(2)
    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.cke_wysiwyg_frame")))
    driver.switch_to.frame(iframe)
    editor_body = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cke_editable_themed")))
    editor_body.send_keys(body_text)
    driver.switch_to.default_content()

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-send"))).click()
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
        return True
    except NoSuchElementException:
        return False
