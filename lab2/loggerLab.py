import platform
import datetime
import os


class Logger:
    def __init__(self, logfile):
        self.logfile = logfile

        exists = os.path.exists(logfile)
        print(exists + " Directory does exist")

        path = os.path.dirname(logfile)
        isfile = os.path.isfile(path)
        print('The file present at the path is a regular file:', isfile)

    def log(self, msg):
        machine = platform.node()
        now = datetime.datetime.now()
        date = "{0}_{1}_{2} {3}:{4}:{5}".format(
            now.year, now.month, now.day,
            now.hour, now.minute, now.second)

        text = "{0}/{1}: {2}".format(machine, date, msg)
        print("log is: " + text)

        with open(self.logfile, 'a+') as data:
            data.write("{0}\n".format(text))
