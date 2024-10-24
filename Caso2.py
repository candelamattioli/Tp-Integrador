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

botones_agregar_al_carrito = driver.find_elements(By.CLASS_NAME, "btn_inventory") #contiene la lista de todos los botones q dicen agregar al carrito
for elemento_boton in botones_agregar_al_carrito: 
    elemento_boton.click()

time.sleep(1)

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)

nueva_lista_del_carrito = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
if  len(nueva_lista_del_carrito) == len(botones_agregar_al_carrito):
    print('Todos los elementos están en el carrito')
else:
    print('Faltan elementos')

time.sleep(1)

driver.find_element(By.CLASS_NAME, "checkout_button ").click()
time.sleep(1)

driver.find_element(By.ID, "first-name").send_keys("Pepe")
driver.find_element(By.ID, "continue").click()
texto_error = driver.find_element(By.CSS_SELECTOR, ".error-message-container h3").text
if texto_error == "Error: Last Name is required":
    print('Muestra el error esperado')
else:
    print('Fallo')
time.sleep(1)

driver.find_element(By.ID, "last-name").send_keys("Argento")
driver.find_element(By.ID, "continue").click()
texto_error = driver.find_element(By.CSS_SELECTOR, ".error-message-container h3").text
if texto_error == "Error: Postal Code is required":
    print('Muestra el error esperado')
else:
    print('Fallo')


time.sleep(1)
time.sleep(5)
driver.quit()