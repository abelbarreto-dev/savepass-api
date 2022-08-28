from peewee import MySQLDatabase


class Database:
    """
    Dtabase Singleton.
    """

    _database = None
    # MYSQL Database Configuration
    _params = {
        'database': 'mysql-database',
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': ''
    }

    @classmethod
    def open(cls) -> MySQLDatabase:
        if not cls._database:
            cls._database = MySQLDatabase(**cls._params)
        return cls._database

    @classmethod
    def close(cls) -> None:
        if isinstance(cls._database, MySQLDatabase):
            cls._database.close()
            cls._database = None
