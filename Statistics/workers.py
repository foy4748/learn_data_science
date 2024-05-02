import sqlite3, csv

con = sqlite3.connect("./data/workers.db")

cur = con.cursor()

'''
cur.execute(
    """
    CREATE TABLE Workers (
        id INT AUTO_INCREMENT,
        wage INT,
        age INT,
        religion TEXT,
        days_absent INT,
        family_size TEXT,
        education TEXT,
        PRIMARY KEY (id)
    );

       """
)
'''

cur.execute("DELETE from Workers;")

with open("./data/workers.csv") as F:
    dr = csv.DictReader(F)
    db_content = [
        (
            row["Worker"],
            row["Wage"],
            row["Age"],
            row["Religion"],
            row["Days absent"],
            row["Family size"],
            row["Education"],
        )
        for row in dr
    ]

    cur.executemany(
        "INSERT INTO Workers(id,wage, age, religion, days_absent,family_size,education) VALUES (?,?,?,?,?,?,?);",
        db_content,
    )

con.commit()
con.close()
