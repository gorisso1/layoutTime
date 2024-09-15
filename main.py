import time

import requests
import schedule


def plan():
    url = 'http://localhost:8000/api/plan-break/'

    try:

        response = requests.put(url)

        if response.status_code == 200:
            print("Ответ от сервера:")
            print(response.json())
        else:
            print(f"Ошибка: {response.status_code}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка: {e}")


def main():

    schedule.every().day.at("20:40").do(plan)
    while True:
        schedule.run_pending()
        time.sleep(60)



if __name__ == "__main__":
    main()