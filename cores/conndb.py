from DB_Config.utilities.database_helper import (
    database_configuration,
    check_commit,
    check_database,
)
import mysql.connector


class ConnectDB:
    def __init__(self):
        self.__conf = database_configuration()
        self.__tables = list()
        self.conn = (
            mysql.connector.connect(**self.__conf)
            if check_database(self.__conf)
            else exit(-1)
        )
        self.refresh_database()

    def _execute_query(self, query, fetchall=True):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(query)
                if check_commit(query):
                    self.conn.commit()
                if fetchall:
                    data = cursor.fetchall()
                    cursor.close()
                    return data
            except mysql.connector.errors.Error as error:
                print("Error: {}".format(error))

    def create_execute(func):
        def wrapper(self, *args, **kwargs):
            query = func(self, *args, **kwargs)
            result = self._execute_query(query)
            return result

        return wrapper

    @create_execute
    def create_table(self, table_name, attributes):
        return f"CREATE TABLE {table_name} {attributes};"

    @create_execute
    def describe_table(self, table_name):
        return f"DESCRIBE {table_name};"

    @create_execute
    def find_all_tables(self):
        return "SHOW TABLES;"

    def refresh_database(self):
        self.__tables.clear()
        for table in self.find_all_tables():
            self.__tables.append(table[0])

    def __len__(self):
        return len(self.__tables)

    def get_tables(self):
        return self.__tables
