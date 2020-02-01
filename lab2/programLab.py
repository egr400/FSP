#!/usr/local/bin/python3
import os
import json
from logger import Logger
import xml.etree.ElementTree as xmltree


class Program:
    def __init__(self):
        this_folder = os.path.dirname(__file__)
        data_folder = os.path.join(this_folder, "data")
        self.data_folder = os.path.abspath(data_folder)
        self.logger = Logger(os.path.join(self.data_folder, "log.txt"))

    def run(self):
        try:
            self.log_startup()
            self.load_xml()
            self.load_json()
            self.load_csv()
        except Exception as e:
            print(e.__repr__())

    def log_startup(self):
        self.logger.log("Application starting up...")
        self.logger.log("Data folder: {0}".format(self.data_folder))

    def load_xml(self):
        filename = os.path.join(self.data_folder, "michael-kennedy-blog.xml")
        self.logger.log("XML file Loading: {0}".format(filename))
        dom = xmltree.ElementTree()
        dom.parse(filename)

        print("Titles of recent posts:")
        items = list(dom.findall("channel/item"))
        self.logger.log("Found {0} titles in RSS feed.".format(len(items)))
        for item in items:
            print("{0} [{1}]".format(item.find("title").text, item.find("link").text))

    def load_json(self):
        filename = os.path.join(self.data_folder, "python-course.json")
        self.logger.log("JSON file Loading: {0}".format(filename))
        with open(filename) as file:

            data = json.loads(file.read())
            print("Course title: {0}".format(data["Name"]))
            self.logger.log("Found course title to be: {0}".format(data["Name"]))
            engagements = data["Engagements"]
            print("Number of engagements: {0}".format(len(engagements)))
            for engage in engagements:
                print(engage["City"] + " on " + engage["StartDate"] + " [active? " + str(engage["ActiveEngagement"]) + "]")

    def load_csv(self):
        filename = os.path.join(self.data_folder, "fx-seven-day.csv")
        self.logger.log("CSV file Loading: {0}".format(filename))

        rupee = self.build_currency(filename, "INR")
        usd = self.build_currency(filename, "USD")
        rupees_per_cad = self.average(rupee["values"])
        usd_per_cad = self.average(usd["values"])

        rupee_per_usd = usd_per_cad / rupees_per_cad

        self.logger.log("One USD is worth {0} INR.".format(rupee_per_usd))
        print("One USD is worth {0} INR.".format(rupee_per_usd))

    @staticmethod
    def average(numbers):
        if len(numbers) <= 0:
            return float('nan')

        return sum(numbers) / float(len(numbers))


if __name__ == "__main__":
    p = Program()
    p.run()

