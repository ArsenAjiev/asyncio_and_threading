import asyncio
import time

import psycopg2
import csv

# connect to DB
conn = psycopg2.connect(
    database='test_db',
    user='my_user',
    password=123456,
    host='localhost',
)

cur = conn.cursor()


async def first_function():
    with open('data.csv', newline='') as d1:
        reader = csv.reader(d1)
        data = tuple(reader)
    for i in range(len(data)):
        cur.execute(f"INSERT INTO some_test (name, value) VALUES {tuple(data[i])};")
    await asyncio.sleep(3)
    print('Data added')


async def second_function():
    with open('data_2.csv', newline='') as d2:
        reader = csv.reader(d2)
        data_2 = tuple(reader)
    for i in range(len(data_2)):
        cur.execute(f"INSERT INTO some_test (name, value) VALUES {tuple(data_2[i])};")
    await asyncio.sleep(2)
    print('Data_2 added')


if __name__ == '__main__':
    x1 = time.time()

    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(first_function()), loop.create_task(second_function())]
    wait_tasks = asyncio.wait(tasks)
    loop.run_until_complete(wait_tasks)
    loop.close()

    conn.commit()
    cur.close()

    x2 = time.time()
    print(f"Выполнено за: {x2 - x1} секунд")
