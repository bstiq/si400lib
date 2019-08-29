A simple example of accessing an ISeries Access ODBC Database.

Install the requirements with pip, modify accordingly and run `test.py`

Code was verified with the [wemake python styleguide](https://github.com/wemake-services/wemake-python-styleguide)


The SQL Wrapper can also be used with other SQL databases, as such:

```
# example with an oracle database
yield 'SELECT * from :tableName', {'tableName': table_name}
```