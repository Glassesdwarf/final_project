# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

persons = []
with open(os.path.join(__location__, 'persons.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        persons.append(dict(r)) 
print(persons) 

class Table:
    def __init__(self, file_path, table_name):
        self.file_path = file_path
        self.table_name = table_name
        self.data = []

        # Load existing data from the CSV file
        self._load_data()

    def _load_data(self):
        with open(self.file_path, 'r') as f:
            rows = csv.DictReader(f)
            self.data = [dict(row) for row in rows]

    def _save_data(self):
        with open(self.file_path, 'w', newline='') as f:
            fieldnames = self.data[0].keys() if self.data else []
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(self.data)

    def insert_entry(self, entry):
        self.data.append(entry)
        self._save_data()

    def update_entry(self, entry_key, key, value):
        for row in self.data:
            if row[entry_key] == key:
                row[key] = value
        self._save_data()
class Database:
    def __init__(self, file_path):
        self.file_path = file_path

    def create_table(self, table_name):
        return Table(self.file_path, table_name)


# add in code for a Database class

# add in code for a Table class

# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated
