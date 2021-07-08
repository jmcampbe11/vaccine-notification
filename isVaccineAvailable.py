import yaml
import requests
import re
import smtplib
import os

os.chdir("/Users/John/projects/vaccine-notification")

conf = yaml.load(open('./config.yaml'), yaml.Loader)

txAddress = conf['user']['address']
password = conf['user']['password']

rxAddress = conf['recipient']['address']

age = 24
isVaccineAvailable = 0

response = requests.get("https://novascotia.ca/coronavirus/book-your-vaccination-appointment/#appointments-age-group")

matchStr = re.search(r"(#appointments-age-group).*", response.text)
ageStr = re.findall(r'\d+', matchStr.group())

vaccineAge = int(ageStr[0])

if age >= vaccineAge:
    isVaccineAvailable = 1

if isVaccineAvailable:
    message = "Vaccine is ready!"
    port = 587
    server = smtplib.SMTP("smtp.gmail.com", port)
    server.starttls()

    server.login(txAddress, password)

    server.sendmail(txAddress, rxAddress, message)