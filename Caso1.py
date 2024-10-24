from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service(r'C:\Users\PC\AppData\Local\Programs\Python\chromedriver-win64\chromedriver.exe')

driver = webdriver.Chrome(service=service)
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(1)

desplegable = driver.find_element(By.CLASS_NAME, "product_sort_container")
desplegable.click()
desplegable.find_element(By.XPATH, "//option[@value='lohi']").click()
time.sleep(1)

elementos = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
lista_de_precios = [float(elemento.text.replace('$', '')) for elemento in elementos]


print(elementos)

estan_ordenados = lista_de_precios == sorted(lista_de_precios)
if estan_ordenados:
    print('Está ordenado')
else:
    print('Está desordenado')

time.sleep(1)
driver.quit()