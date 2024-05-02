import sqlite3
from functools import reduce

con = sqlite3.connect("./data/workers.db")

cur = con.cursor()

res = cur.execute(
    """
SELECT family_size,count(family_size) from Workers
GROUP BY family_size;
"""
)

freq_dist = res.fetchall()
print(freq_dist)
sum_over = 0
for item in freq_dist:
    sum_over = sum_over + item[1]


percentage_sum = 0
for item in freq_dist:
    print(item[0], "\t", item[1], "\t", item[1] * 100 / sum_over)
    percentage_sum = percentage_sum + item[1] * 100 / sum_over

print("Total", "\t", sum_over, "\t", percentage_sum)
