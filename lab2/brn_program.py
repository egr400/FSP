"""
    Created by Brandon Aldridge, Robbie Sollie, Nick Gualtney
"""

#!/usr/local/bin/python3
import os
import json
import xml.etree.ElementTree as ET
import pandas as pd
from brn_logger import Logger


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
        # self.logger.log("******* LOAD_XML NOT FINISHED ******* ")
        filename = os.path.join(self.data_folder, "michael-kennedy-blog.xml")
        # TODO: log which xml file is being opened
        self.logger.log("Using {0}".format(filename))

        # TODO: Create new ElementTree and parse file
        tree = ET.parse(filename)

        print("Titles of recent posts:")
        # TODO: use the xpath expression channel/item to find all blog posts
        element = tree.findall('channel/item')
        # TODO: loop over and find title and link
        for i in element:
            print(i.find("title").text, "\n", i.find("link").text, "\n")

    def load_json(self):
        filename = os.path.join(self.data_folder, "python-course.json")

        self.logger.log('Opening JSON file: {}'.format(filename))

        try:
            file_text = ''
            with open(filename) as f:

                for line in f:
                    # TODO find which is faster
                    file_text = file_text + line
                    # file_text = '{}{}'.format(file_text, line)
        except FileNotFoundError as e:
            self.logger.log('JSON FILE LOAD FAILED!')
        else:
            working_json = json.loads(file_text)
            self.logger.log('JSON file successfully loaded')
            try:
                self.logger.log('course name: {}'
                                .format(working_json['Name']))
                self.logger.log('number of engagements: {}'
                                .format(len(working_json['Engagements'])))

                for engagement in working_json['Engagements']:

                    self.logger.log('city: {}, start date: {}'.format(
                        engagement['City'], engagement['StartDate']))

            except KeyError as e:
                self.logger.log('JSON NOT IN CORRECT FORMAT!')
            else:
                self.logger.log('JSON file successfully parsed')


    def load_csv(self):
        filename = os.path.join(self.data_folder, "fx-seven-day.csv")
        # self.logger.log("******* LOAD_CSV NOT FINISHED ******* ")
        # TODO: log which csv file is being opened
        self.logger.log(filename)

        # TODO: Answer what is the 7 day average for RUPEEs to USD?
        # (need to go from rupees -> canadian dollars -> usd)
        # hint: build a lookup of each row by ID (e.g. CZK),
        #       store the seven day values as a list of floats.
        df = pd.read_csv(filename, comment="#", index_col=1, sep=', ', engine='python')
        rupee_exchange_vals = df.loc['INR'][1:]
        print("Rupees")
        print(rupee_exchange_vals)

        rupee_per_cad = 1 / (self.average(rupee_exchange_vals))

        usd_exchange_vals = df.loc['USD'][1:]
        print("Dollars")
        print(usd_exchange_vals)

        rupee_per_usd = rupee_per_cad * (self.average(usd_exchange_vals))

        self.logger.log("1 USD is worth {0} INR".format(rupee_per_usd))

        # TODO: show and log the answer 1 USD is worth X Rupees
        # note: this value should be around 60.
        # we have provided an average method below for you to use


    @staticmethod
    def average(numbers):
        if len(numbers) <= 0:
            return float('nan')

        print(numbers)
        return sum(numbers) / float(len(numbers))


if __name__ == "__main__":
    p = Program()
    p.run()
