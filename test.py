from SI400Client import SI400Client
from ExampleClient import ExampleClient

si400 = ExampleClient("host", "schema", "user", "password")
results = si400.example_request("table").fetchall()

print(str(results))
