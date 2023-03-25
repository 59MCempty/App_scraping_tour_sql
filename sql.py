import mysql.connector

config = {
    'user': 'root',
    'password': 'cuong59abc',
    'host': 'localhost',
    'database': 'tour'
}

DB_NAME = "tour"

TABLES = {}

TABLES['information'] = (
    "CREATE TABLE `information` ("
    " `id` INT NOT NULL AUTO_INCREMENT,"
    " `band` VARCHAR(150) NOT NULL,"
    " `city` VARCHAR(150) NOT NULL,"
    " `date` VARCHAR(150) NOT NULL,"
    " PRIMARY KEY (id))"
)

mydb = mysql.connector.connect(**config)
cursor = mydb.cursor()


def create_database(db_name):
    text = "CREATE DATABASE {}".format(db_name)
    cursor.execute(text)


def create_table(tables):
    cursor.execute(tables)


if __name__ == "__main__":
    # create_database(DB_NAME)
    # create_table(TABLES['information'])
    sql = "DELETE FROM information"
    cursor.execute(sql)
    mydb.commit()
