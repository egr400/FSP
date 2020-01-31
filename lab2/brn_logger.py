"""
    Created by Brandon Aldridge, Robbie Sollie, Nick Gualtney
"""

import platform
import datetime
import os


class Logger:
    def __init__(self, logfile):
        self.logfile = logfile

        # TODO: Verify directory exists (note file not needed)
        if not os.path.exists(logfile):
            print("Directory does not exist")
        # TODO: Verify logfile is not itself a directory
        if not os.path.isfile(logfile):
            print(logfile, " is not a file")

        # Throw Exception?

    def log(self, msg):
        machine = platform.node()
        now = datetime.datetime.now()
        date = "{0}_{1}_{2} {3}:{4}:{5}".format(
            now.year, now.month, now.day,
            now.hour, now.minute, now.second)

        text = "{0}/{1}: {2}".format(machine, date, msg)
        # Print to console
        print(text)
        # Append line to log file
        with open(self.logfile, "a+") as workData:
            workData.write('{}\n'.format(text))
            # workData.write("\n")
