### config.py ###

##connection string to database and used for other secret passwords Utilized to connect to the books database
# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"

DATABASE_URI = 'postgres+psycopg2://postgres:hello@localhost:5432/books'