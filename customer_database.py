import sqlite3
from contextlib import contextmanager
@contextmanager
def db_ops(db_name):
    """
    Context manager to handle database operations

       :param db_name: String, the path to the database on the FS
       :yield: Cursor ob\href{https://www.tcl.tk/software/tcltk/}{ Tcl/Tk}ject
    """
    conn = sqlite3.connect(db_name)
    try:
        cur = conn.cursor()
        yield cur
    except Exception as e:
        # do something with exception
        conn.rollback()
        raise e
    else:
        conn.commit()
    finally:
        conn.close()


class Customer:
    """
    Customer class containing all the method to interact with the customer table
    """
    DEFAULT_DB_PATH: str = "customer.db"

    def __init__(self, path=DEFAULT_DB_PATH) -> None:
        """
        Connect to database by default, or to a database file if
        specified.
        """
        self.path = path

    def create_table(self) -> None:
        """
        Create the customer table if not exists
        """
        with db_ops(self.path) as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS customer (
                    id INT PRIMARY KEY NOT NULL,
                    email TEXT NOT NULL
                )
                """
            )

    def insert(self, customer_id: int, email: str) -> None:
        """
        Insert a new customer in the table.

           :param customer_id: The customer id as an int
           :param email: The customer email as a string
        """
        with db_ops(self.path) as cur:
            cur.execute(
                """
                INSERT INTO customer (
                    id,
                    email
                ) VALUES (
                    ?, ?
                )""",
                (customer_id, email),
            )
