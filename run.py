from cores.crud import CRUD
from settings import report

if __name__ == "__main__":
    # Introduction
    print("+-+-+-+-+-+")
    print("| Result: |")
    print("+-+-+-+-+-+")

    # your code
    instance = CRUD()
    print(instance.get_tables())
    cols = ["username", "password", "email"]
    order_cols = ['email']
    print(instance.read_data(cols, "auth_user",order_cols=order_cols,order_method='DESC'))
    instance.conn.close()

    # Conclusion
    print(report)
