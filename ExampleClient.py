from SI400Client import SI400Client
from SQLWrapper import sql_wrapper


class ExampleClient(SI400Client):
    @sql_wrapper
    def example_request(self, table):
        yield "SELECT * FROM %s" % table
