from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests
import aiohttp
import asyncio
import random
import base64
import json
import time
import os

# Setup Chrome options
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

# Path ke driver Chrome
service = webdriver.ChromeService()
# service = Service("C:\Program Files\Google\Chrome\Application\chrome.exe")  # Ganti dengan path driver

# Inisialisasi WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Fungsi login
def login(driver, username, password):
    try:
        driver.get("https://elearning.budiluhur.ac.id")
        print("Navigasi ke halaman login berhasil.")
        
        # Debug: Tunggu elemen username tersedia
        username_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-username"))
        )
        print("Elemen username ditemukan.")
        username_field.send_keys(username)

        # Debug: Tunggu elemen password tersedia
        password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-password"))
        )
        print("Elemen password ditemukan.")
        password_field.send_keys(password)

        # Debug: Submit form
        form = driver.find_element(By.TAG_NAME, "form")
        form.submit()
        print("Form berhasil disubmit.")

        # Debug: Tunggu elemen berikutnya untuk memastikan login berhasil
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
        print("Login berhasil dan halaman berikutnya dimuat.")

    except Exception as e:
        # Debugging jika ada masalah
        print(f"Terjadi kesalahan: {e}")
        driver.save_screenshot("debug_screenshot.png")  # Simpan tangkapan layar untuk investigasi
    finally:
        driver.quit()
        print("Browser ditutup.")

# Main program
if __name__ == "__main__":
    username = "2211510629"  # Ganti dengan username Anda
    password = "P29082003"  # Ganti dengan password Anda
    
    login(driver, username, password)


try:
    username_field = driver.find_element(By.ID, "login-username")
    print("Elemen username tersedia.")
except Exception as e:
    print(f"Masalah dengan elemen username: {e}")