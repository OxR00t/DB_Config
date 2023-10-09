from DB_Config.cores.conndb import ConnectDB
from DB_Config.utilities.database_helper import parse_list


class CRUD(ConnectDB):
    """CRUD (Create, Read, Update, Delete) operations for a relational database.

    This class provides methods to perform common database operations such as inserting,
    reading, updating, and deleting data in a relational database.

    Attributes:
        None

    Methods:
        - insert_data(table: str, values: set, cols: set = None) -> str:
            Insert data into a specified table.

        - read_data(cols: list, tables: str, distinct: bool = False,
                    condition: str = None, order_cols: list = None,
                    order_method: str = 'ASC', limit: int = 10) -> str:
            Read data from one or more tables with various filtering and ordering options.

        - update_data(table: str, col_val: str, condition: str = None) -> str:
            Update data in a specified table.

        - delete_data(table: str, condition: str) -> str:
            Delete data from a specified table based on a condition.

    Usage:
        Create an instance of CRUD to perform database operations on a connected database.

    Example:
        crud = CRUD()
        crud.insert_data("employees", {"John", "Doe"}, {"first_name", "last_name"})
        crud.read_data(["first_name", "last_name"], "employees", condition="age > 30")
        crud.update_data("employees", "salary = 60000", condition="age > 40")
        crud.delete_data("employees", "age < 25")
    """
    def __init__(self):
        ConnectDB.__init__(self)

    @ConnectDB.create_execute
    def insert_data(self, table: str, values: set, cols: set = None) -> str:
        command = "INSERT INTO {table} ".format(table=table)
        if cols:
            command += "{cols} ".format(cols=cols)
        command += "VALUES {values}".format(values=values)
        return command + ";"

    @ConnectDB.create_execute
    def read_data(
        self,
        cols: list,
        tables: str,
        distinct: bool = False,
        condition: str = None,
        order_cols: list = None,
        order_method: str = 'ASC',
        limit: int = 10,
    ) -> str:
        command = "SELECT"
        if distinct:
            command += f" DISTINCT"
        command += f" {parse_list(cols)} FROM {tables}"
        if condition:
            command += f" WHERE {condition}"
        if order_cols:
            command += f" ORDER BY {parse_list(order_cols)}{order_method}"
        if limit:
            command += f" LIMIT {limit}"
        return command + ";"

    @ConnectDB.create_execute
    def update_data(self, table: str, col_val: str, condition: str = None) -> str:
        command = f"UPDATE {table} SET {col_val}"
        if condition:
            command += f" WHERE {condition}"
        return command + ";"

    @ConnectDB.create_execute
    def delete_data(self, table: str, condition: str) -> str:
        command = f"DELETE FROM {table}"
        if condition:
            command += f" WHERE {condition}"
        return command + ";"
