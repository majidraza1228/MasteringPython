# write python singleton class for database connection
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super().__new__(cls)
        return cls._instance

db1 = DatabaseConnection()
print(db1)

db2 = DatabaseConnection()
print(db2)



