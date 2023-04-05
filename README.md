# Update me!

# TODO 1 - We need to try move the transaction Class back into a module and pass the connection object (cursor) as a argument into the functions/methods using it so you dont need to import back into app.py

# TODO Note that from some testing I concluded that our circular import partially initialized issue meant for example if app.py imports from transactions, then transactions cannot import back from app.py at all, A solution to this is figuring out how to achieve TODO 1 - or maybe moving the connection altogether into its own module

# TODO Class methods could be rewritten

# TODO Possibly condense modules

# TODO Update, Moved connection into its own module and transactions, create tables import from the db_connect module with app.py gaining connection to the db_connect through the create_tables module.
