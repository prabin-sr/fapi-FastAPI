from peewee import MySQLDatabase


class DataBaseConnector:
    def __init__(self, name, user, password, host):
        self.name = name
        self.user = user
        self.password = password
        self.host = host

    def get_connection(self):
        connection = MySQLDatabase(database=self.name,
                                   user=self.user,
                                   password=self.password,
                                   host=self.host)

        return connection
