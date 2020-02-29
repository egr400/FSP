# the scheme in the comment shows how to structure the connection string
# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"

# the DATABASE_URI contains the parameters used for the local database
DATABASE_URI = 'postgres+psycopg2://postgres:hello@localhost:5432/books'
