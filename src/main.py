import time
import json
import os
from api_client import get_sky_price
from llm_analyzer import analyze_market_data

HISTORY_FILE = "trading_history.csv"

def log_decision(price, decision):
    with open(HISTORY_FILE, "a") as f:
        f.write(f"{time.ctime()},{price},{decision}\n")

def main():
    print("Sky Trading Bot started. Monitoring price...")
    while True:
        try:
            data = get_sky_price()
            price = data.get("price")
            
            # Анализ
            decision = analyze_market_data(f"Current price: {price}. History context: {open(HISTORY_FILE, 'r').readlines()[-5:] if os.path.exists(HISTORY_FILE) else 'None'}")
            
            print(f"[{time.ctime()}] Price: {price} | Decision: {decision}")
            log_decision(price, decision)
            
            time.sleep(60) # Проверка раз в минуту
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()
