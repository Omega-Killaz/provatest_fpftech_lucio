# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://www.vanilton.net/triangulo/")
    yield driver
    driver.quit()

def preencher_triangulo(driver, v1, v2, v3):
    driver.find_element(By.NAME, "V1").send_keys(str(v1))
    driver.find_element(By.NAME, "V2").send_keys(str(v2))
    driver.find_element(By.NAME, "V3").send_keys(str(v3))
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

def extrair_resultado(driver):
    try:
        # Espera até aparecer um div com palavras esperadas
        resultado_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                "//div[contains(text(), 'Equilátero') or contains(text(), 'Isósceles') or contains(text(), 'Escaleno') or contains(text(), 'não formam')]"
            ))
        )
        return resultado_div.text.strip()
    except Exception as e:
        print("Erro ao extrair resultado:", str(e))
        print(driver.page_source)  # ajuda a depurar o HTML renderizado
        return "Erro"
#    wait = WebDriverWait(driver, 10)
#    resultado_divs = driver.find_elements(By.TAG_NAME, "div")
#    for div in resultado_divs:
#        texto = div.text.strip()
#        if texto in ["Equilátero", "Isósceles", "Escaleno"]:
#            return texto
#        if "não formam um triângulo" in texto.lower():
#            return "Inválido"
#    return "Desconhecido"

def test_equilatero(driver):
    preencher_triangulo(driver, 10, 10, 10)
    resultado = extrair_resultado(driver)
    assert resultado == "Equilátero"

def test_isosceles(driver):
    preencher_triangulo(driver, 10, 10, 5)
    resultado = extrair_resultado(driver)
    assert resultado == "Isósceles"

def test_escaleno(driver):
    preencher_triangulo(driver, 10, 11, 12)
    resultado = extrair_resultado(driver)
    assert resultado == "Escaleno"

def test_invalido(driver):
    preencher_triangulo(driver, 1, 1, 10)
    resultado = extrair_resultado(driver)
    assert resultado == "Inválido"
