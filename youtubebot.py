from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# ChromeDriver'ı başlatın
service = Service("C:/Users/Bilgisayar/Desktop/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Youtube anasayfasına gidin
    driver.get("https://www.youtube.com/")

    # Şarkıyı arayın
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("Şarkının adı buraya")  # Şarkı adını yazın
    search_box.submit()

    time.sleep(2)  # Arama sonuçlarının yüklenmesi için bekleyin

    # İlk sonuca tıklayın
    first_video = driver.find_element(By.XPATH, '//*[@id="video-title"]')
    first_video.click()

    # Sürekli olarak oynatmayı tekrar eden döngü
    while True:
        time.sleep(1)  # Her saniye bir kez kontrol eder
        try:
            # Video bitmişse "Tekrar Oynat" butonuna basın
            replay_button = driver.find_element(By.CLASS_NAME, "ytp-play-button")
            if replay_button.get_attribute("title") == "Tekrar Oynat":
                replay_button.click()
                print("Video yeniden oynatılıyor...")
        except Exception as e:
            print("Tekrar oynat butonu henüz görünmüyor.")
            pass  # Eğer buton henüz görünmüyorsa beklemeye devam eder
finally:
    driver.quit()  # Tarayıcıyı kapat
