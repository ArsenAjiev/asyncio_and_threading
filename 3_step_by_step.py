import psycopg2
import csv
import time

conn = psycopg2.connect(
    database='test_db',
    user='my_user',
    password=123456,
    host='localhost',
)

cur = conn.cursor()

with open('data.csv', newline='') as d1:
    reader = csv.reader(d1)
    data = tuple(reader)

with open('data_2.csv', newline='') as d2:
    reader = csv.reader(d2)
    data_2 = tuple(reader)


def firs_data(sleep):
    for i in range(len(data)):
        cur.execute(f"INSERT INTO some_test (name, value ) VALUES {tuple(data[i])};")
    time.sleep(sleep)
    return print('Data added')


def second_data(sleep):
    for i in range(len(data_2)):
        cur.execute(f"INSERT INTO some_test (name, value ) VALUES {tuple(data_2[i])};")
    time.sleep(sleep)
    return print('Data_2 added')


if __name__ == '__main__':
    x1 = time.time()
    firs_data(3)
    second_data(2)

    conn.commit()
    cur.close()

    x2 = time.time()
    print(f"Выполнено за: {x2 - x1} секунд")



