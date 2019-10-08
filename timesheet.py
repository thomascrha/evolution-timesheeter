import argparse
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
waitMain = WebDriverWait(driver, 10)


def login(username, password):

    username_feild = waitMain.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_txtUsername"]')))
    password_feild = waitMain.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_txtPassword"]'))) 
    sign_in = waitMain.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_cmdLogin"]')))

    username_feild.send_keys(username) 
    password_feild.send_keys(password) 

    sign_in.click()

    timesheet_link = waitMain.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_pnlNormal"]/table/tbody/tr[4]/td/ul/li[1]/a'))) 
    timesheet_link.click()

def enter_timesheets(start='09', end='18', lunch='01', submit=False):

    timesheet_period = waitMain.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_cboAvailableTimeSheets"]'))) 
    timesheet_period.click()
    select_timesheet_period = Select(timesheet_period)
    select_timesheet_period.select_by_index(1)

    monday_add_button = waitMain.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_ASPxPanelMain_gvMain_cmdimggvMainAdd_0"]')))
    monday_add_button.click()

    days_worked_textbox = waitMain.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_ASPxPanelAdd_txtDayWorked"]')))
    days_worked_textbox.click()
    days_worked_textbox.send_keys(1)

    start_time_list = waitMain.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_ASPxPanelAdd_ddlstStartHours"]')))
    start_time_list.click()
    start_time_list.send_keys(start) 

    end_time_list = waitMain.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_ASPxPanelAdd_ddlstFinishHours"]')))
    end_time_list.click()
    end_time_list.send_keys(end) 

    lunch_time_list = waitMain.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_ASPxPanelAdd_ddlstLunchHours"]')))
    lunch_time_list.click()
    lunch_time_list.send_keys(lunch) 

    save_button = waitMain.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_ASPxPanelAdd_cmdImgSave"]')))
    save_button.click()

    tues_copy_button = waitMain.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_ASPxPanelMain_gvMain_cmdimggvMainCopy_1"]'))) 
    tues_copy_button.click() 

    waitMain.until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()

    wed_copy_button = waitMain.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_ASPxPanelMain_gvMain_cmdimggvMainCopy_2"]'))) 
    wed_copy_button.click() 

    waitMain.until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()

    thurs_copy_button = waitMain.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_ASPxPanelMain_gvMain_cmdimggvMainCopy_3"]'))) 
    thurs_copy_button.click() 

    waitMain.until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()

    fri_copy_button = waitMain.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_ASPxPanelMain_gvMain_cmdimggvMainCopy_4"]'))) 
    fri_copy_button.click() 

    waitMain.until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()

    if submit:
        submit = waitMain.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_ASPxRoundPanel1_cmdSubmitTimesheet"]'))) 
        submit.click()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-l",
        "--login-page",
        required=False,
        type=str,
        default="https://efiling.evolutionjobs.com.au/portalhome.aspx"
    )

    parser.add_argument(
        "-u",
        "--username",
        required=True,
        type=str
    )

    parser.add_argument(
        "-p",
        "--password",
        required=True,
        type=str
    )
    parser.add_argument(
        "-s",
        "--submit",
        action="store_true",
        default=False
    )

    args = parser.parse_args()

    driver.get(args.login_page)

    login(args.username, args.password)
    
    enter_timesheets(submit=args.submit)

    driver.close()