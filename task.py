import os
from requests import get
import json
import csv
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class Task(object):
    def __init__(self):
        self.response = get(
            'https://labrinidis.cs.pitt.edu/cs1656/data/hours.json',
            verify=False
        )
        self.hours = json.loads(self.response.content)

    def part4(self):
        # write output to hours.csv
        f = open('hours.csv', 'w')
        w = csv.writer(f)

        # WRITE HEADER (REQUIRED)
        w.writerow(['name', 'day', 'time'])

        for entry in self.hours:
            w.writerow([entry['name'], entry['day'], entry['time']])

        f.close()

    def part5(self):
        # write output to 'part5.txt'
        fin = open('hours.csv', 'r')
        contents = fin.read()
        fin.close()

        f = open('part5.txt', 'w')
        f.write(contents)
        f.close()

    def part6(self):
        # write output to 'part6.txt'
        fin = open('hours.csv', 'r')
        reader = csv.reader(fin)

        f = open('part6.txt', 'w')

        # SKIP HEADER
        next(reader)

        for row in reader:
            f.write(str(row))

        f.close()
        fin.close()

    def part7(self):
        # write output to 'part7.txt'
        fin = open('hours.csv', 'r')
        reader = csv.reader(fin)

        f = open('part7.txt', 'w')

        # SKIP HEADER
        next(reader)

        for row in reader:
            for cell in row:
                f.write(cell)

        f.close()
        fin.close()


if __name__ == '__main__':
    task = Task()
    task.part4()
    task.part5()
    task.part6()
    task.part7()
