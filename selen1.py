from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math, os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']")
    input1.send_keys("Chin")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']")
    input2.send_keys("Khis")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']")
    input3.send_keys("blya@ogr.com")
    current_dir = os.path.abspath(r"C:\Users\czkn\Documents")    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'selen.txt')           # добавляем к этому пути имя файла 
    input4 = browser.find_element(By.CSS_SELECTOR, "input[id='file']")
    input4.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
<<<<<<< HEAD
<<<<<<< HEAD
# для вас старался
=======
>>>>>>> fc9b56cbf7779283f125c08d1cda9f7f2abd8177
=======
>>>>>>> fc9b56cbf7779283f125c08d1cda9f7f2abd8177
