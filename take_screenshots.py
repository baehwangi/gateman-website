from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
import os

# Edge 옵션 설정
options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('--force-device-scale-factor=1')

# Edge 드라이버 시작
driver = webdriver.Edge(options=options)

try:
    # 1. index.html 스크린샷
    index_path = 'file:///C:/Users/ASDS/Desktop/GATEMAN/index.html'
    driver.get(index_path)
    time.sleep(2)

    # 헤더만 스크린샷
    driver.set_window_size(1920, 200)
    driver.save_screenshot('claudedocs/screenshot_index_header.png')
    print("✓ index.html 헤더 스크린샷 저장: claudedocs/screenshot_index_header.png")

    # 2. 제품 페이지 스크린샷
    product_path = 'file:///C:/Users/ASDS/Desktop/GATEMAN/products/gm-900s.html'
    driver.get(product_path)
    time.sleep(2)

    # 헤더만 스크린샷
    driver.set_window_size(1920, 200)
    driver.save_screenshot('claudedocs/screenshot_product_header.png')
    print("✓ 제품 페이지 헤더 스크린샷 저장: claudedocs/screenshot_product_header.png")

finally:
    driver.quit()

print("\n스크린샷 촬영 완료!")
