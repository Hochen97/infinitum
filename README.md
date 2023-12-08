# Infinitum
## Description
Databases suck. ORMs are tedious. I got tired of all that, so I developed an abstraction layer that leverages existing functionality in your database.

Why build boilerplate objects for SerDe when you can just use the existing DB schema.

Right now, it's just postgres. In the future I intend to expand to other DB systems.

Feel free to fork and contribute. Ideas are welcome.

This is really meant for JSON-based transactional systems, like API backends, so for data analytics you're better off using something like pandas, polars, or something of the like. 

## Installation
`pip install infinitum`

## Usage
1. Connect to your database
```
from infinitum import main as inf

conn = inf.connect_to_database(host, database, user, password)
```

2. Crud operations
```
# Create
data = {
    'id': 1,
    'name': 'test'
}
inf.create(conn, table_name, data)

# Read
#   this function leverages column names to build a filtered query.
#   make sure your column has "id" in its name so it can generate the list of filters
#   this will be less dumb in the future
data = {
    'id': 1
}
inf.read(conn, table_name, data)

# Update
data = {
    'id': 1,
    'name': 'test2'
}
inf.update(conn, table_name, data)

# Delete
data = {
    'id': 1
}
inf.delete(conn, table_name, data)

# Read all
# This just pulls everything.
inf.read(conn, table_name, {})
```