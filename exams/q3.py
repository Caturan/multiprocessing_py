"""
    Complete the function main to use get_weather_from_google to create threads for each city given in cities,
    start the threads, and fetch the responses into the dictionary data. 

    import threading
    import requests

    def get_weather_from_google(city: str, data: dict = None):
        response = request.get(
            f"https://www.google.com/search?q=weather+{city}"
        )
        data[city] = response.text

    def main():
        cities = ["London", "Paris", "Manisa", "Tokyo"]
        data = {}
"""

import threading
import requests

def get_weather_from_google(city: str, data: dict = None):
    response = requests.get(
        f"https://www.google.com/search?q=weather+{city}"
    )
    data[city] = response.text

def main():
    cities = ["London", "Paris", "Manisa", "Tokyo"]
    data = {}
    threads = []
    for city in cities:
        thread = threading.Thread(target=get_weather_from_google, args=(city,data))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(data)

if __name__ == "__main__":
    main()