from send_mail import send_mail
from sql import mydb, cursor
import requests
import selectorlib
import time


URL = "http://programmer100.pythonanywhere.com/tours/"


def get(url):
    response = requests.get(url)
    get_data = response.text
    return get_data


def scrapping(data):
    scrap = selectorlib.Extractor.from_yaml_file("scrapped.yaml").extract(data)['tour']
    return scrap


def store_tour(tour):
    tour = tour.split(",")
    tour = [item.strip() for item in tour]
    band, city, date = tour
    val = (band, city, date)
    print(val)
    text = "INSERT INTO information (band, city, date) VALUES (%s, %s, %s)"
    cursor.execute(text, val)
    mydb.commit()


def read_tour(tours):
    tours = tours.split(",")
    tours = [item.strip() for item in tours]
    band, city, date = tours
    text = f"SELECT * FROM information WHERE band = '{band}' AND city = '{city}' AND date = '{date}'"
    cursor.execute(text)
    tours = cursor.fetchall()
    print(tours)
    return tours


if __name__ == "__main__":
    while True:
        html = get(URL)
        tour = scrapping(html)
        if tour != "No upcoming tours":
            content = read_tour(tours=tour)
            if not content:
                store_tour(tour=tour)
                send_mail("From Tour with love", tour)
        time.sleep(2)

