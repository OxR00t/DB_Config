from DB_Config.settings import Database
import mysql.connector


def database_configuration():
    required_keys = ["host", "username", "password", "database"]
    if all(key in Database for key in required_keys):
        return Database
    return None


def check_commit(query: str) -> bool:
    statements = ["UPDATE", "INSERT"]
    request = query.split()
    if request[0] in statements:
        return True
    return False


def check_database(configuration: dict) -> bool:
    try:
        connector = mysql.connector.connect(**configuration)
        connector.close()
        return True
    except mysql.connector.errors.Error as error:
        print("ERROR: ", error)
        return False


def parse_list(new_list: list) -> str:
    statement = ""
    for item in new_list:
        if new_list.index(item) == 0:
            statement += "{} ".format(item)
            continue
        statement += ",{} ".format(item)
    return statement
