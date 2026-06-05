from db import get_connection
from contextlib import contextmanager


@contextmanager
def db_cursor():
    """
    Context manager for DB connection + cursor.
    Automatically handles commit/rollback and closing.
    """
    conn = get_connection()
    cursor = conn.cursor()

    try:
        yield cursor
        conn.commit()

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        cursor.close()
        conn.close()