from email.message import EmailMessage
from sql import mydb
import ssl, smtplib
import requests
import selectorlib
import time


URL = "http://programmer100.pythonanywhere.com/tours/"


class Email:
    def send(self, subject, body):
        email_sender = "cbay5122022@gmail.com"
        email_password = "wexhyvexxcjuhwvp"
        email_reciever = "cbay5122022@gmail.com"

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_reciever
        em['Subject'] = subject

        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_reciever, em.as_string())
        print("Email was sent")


class Event:
    def scrape(self, url):
        response = requests.get(url)
        get_data = response.text
        return get_data

    def extract(self, data):
        scrap = selectorlib.Extractor.from_yaml_file("scrapped.yaml").extract(data)['tour']
        return scrap


class Databbase:
    def __init__(self):
        self.connection = mydb
        self.cursor = mydb.cursor()

    def store_tour(self, tour):
        row = tour.split(",")
        row = [item.strip() for item in row]
        band, city, date = row
        val = (band, city, date)
        print(val)
        text = "INSERT INTO information (band, city, date) VALUES (%s, %s, %s)"
        self.cursor.execute(text, val)
        self.connection.commit()

    def read_tour(self, tours):
        row = tours.split(",")
        row = [item.strip() for item in row]
        band, city, date = row
        text = f"SELECT * FROM information WHERE band = '{band}' AND city = '{city}' AND date = '{date}'"
        self.cursor.execute(text)
        row = self.cursor.fetchall()
        print(row)
        return row


if __name__ == "__main__":
    while True:
        event = Event()
        html = event.scrape(URL)
        tour = event.extract(html)
        if tour != "No upcoming tours":
            content = read_tour(tours=tour)
            if not content:
                store_tour(tour=tour)
                email = Email()
                email.send("From Tour with love", tour)
        time.sleep(2)

