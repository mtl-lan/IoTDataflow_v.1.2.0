import csv
import time
import datetime

with open('data/iiot_30min_norm.csv', 'r') as fs:
    iotcsv = csv.reader(fs, delimiter=",")
    header = next(iotcsv)
    for row in iotcsv:
        print(row)
        process_epoch = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = 'iot_'+ str(process_epoch)+".csv"
        with open(f'data/iotpartition/{filename}', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow(row)
        time.sleep(1)

