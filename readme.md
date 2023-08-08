# Scrapy

## Applications for scraping work.ua

## Розгортаня проекту локально (команди для Windows)

1. Склонувати репозиторій
    ```bash    
    git clone https://github.com/AtamanAA/hillel_home_work_27.git
    ```
2. Встановити venv та активувати його
    ```bash
    python -m venv venv
   .\venv\Scripts\activate    
    ```
3. Інсталювати сторонні пакети у venv
    ```bash
    python -m pip install -r requirements.txt    
    ```
4. Перейти до осноної дерикторії проекту
    ```bash
    cd workua    
    ```
5. Запустити скрипт для збереження ынформації у файл "data.jsonl"
    ```bash
    scrapy crawl vacancy -o data.jsonl   
    ```



