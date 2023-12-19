class Restaurant:
    def __init__(self, name, address, phone_number, menu):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.menu = menu
        self.tables = []

    def add_table(self, table):
        self.tables.append(table)

    def list_tables(self):
        for table in self.tables:
            print(f"Table {table.table_number} - Capacity: {table.capacity} - Availability: {table.availability}")

    def reserve_table(self, customer_name, party_size, reservation_time):
        for table in self.tables:
            if table.table_number ==  table.is_available():
                table.mark_unavailable()
                reservation = Reservation(customer_name, party_size, reservation_time)
                return reservation
        return None

class Table:
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.availability = True

    def is_available(self):
        return self.availability

    def mark_available(self):
        self.availability = True

    def mark_unavailable(self):
        self.availability = False

class Reservation: