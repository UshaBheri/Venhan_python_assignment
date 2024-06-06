import csv
import os

def csvFile():
    try:
        with open(r'C:\Users\DELL\Desktop\Venhan assignment\file.csv','r') as file:
            file_read = csv.reader(file,delimiter=',')
            data_list = list(file_read)
            print(data_list)
    except FileNotFoundError:
        print("File not found")

csvFile()