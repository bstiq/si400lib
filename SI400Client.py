import pyodbc


class SI400Client():
    def __init__(self, system, schema, user, password):
        self.__connection = pyodbc.connect(
            driver='{iSeries Access ODBC Driver}',
            system=system,
            uid=user,
            pwd=password,
            CommitMode=0)
        self.connect(schema)

    def connect(self, schema=None):
        if schema is not None:
            self.current_schema = schema
            self.cursor = self.__connection.cursor()
            self.cursor.execute("SET CURRENT SCHEMA " + schema)

    def execute(self, instruction, values=None):
        if values is None:
            self.cursor.execute(instruction)
        else:
            self.cursor.execute(instruction, values)

        return self.cursor
