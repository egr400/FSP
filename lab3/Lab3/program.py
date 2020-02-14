#Saul Morales, Donald Jalving, Malane Lieng, Brandon Nguyen, Matthew Hernandez,
#Monica Velasco, Kamari Hooks, Gabby Gil- Mazariegos, Gregorio Lopez

from db import DB


def main():
    print("DBAPI Lab starting up...")
    print()
    db = DB()
    db.create_db()
    db.insert_base_data()
    db.show_all_rows()
    db.show_funny_rows()

    txt = input("Want to search for something? Enter a phrase: ")
    db.search(txt)


if __name__ == '__main__':
    main()