import csv

class Customer:
    def __init__(self, id, first_name, last_name, current_video_rentals = ''):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals

    #load all customers infos, also with current_video_rentals
    @classmethod
    def all_customers(cls):
        customers = []
        with open("./data/customers.csv") as customers_file:
            data = csv.reader(customers_file)
            for line in data:
                id = line[0]
                first_name = line [1]
                last_name = line [2] 
                current_video_rentals = line [3]  

                customer = cls(id, first_name, last_name, current_video_rentals)
                customers.append(customer)
            
        return customers

    