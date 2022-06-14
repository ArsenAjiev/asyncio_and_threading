from threading import Thread
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


def run_threads():
    t1 = Thread(target=firs_data, args=(3,))
    t2 = Thread(target=second_data, args=(2,))

    x1 = time.time()
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    conn.commit()
    cur.close()

    x2 = time.time()
    print(f"Выполнено за: {x2 - x1} секунд")


if __name__ == '__main__':
    run_threads()