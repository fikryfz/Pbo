class Customer_fikry:
    def __init__(self, cust_id: int, cust_name: str):
        self.cust_id = cust_id
        self.cust_name = cust_name
    
    def add_fikry(self):

        return {
            'cust_id': self.cust_id,
            'cust_name': self.cust_name
        }
    
    def update_fikry(self, new_name):
        self.cust_name = new_name
        return True
    
    def delete_fikry(self):
        self.cust_id = None
        self.cust_name = None
        return True
    
    @staticmethod
    def header_fikry():
        print("\n+"+"-"*8+"+"+"-"*25+"+")
        print("|{:^8}|{:^25}|".format("ID", "Nama Customer"))
        print("+"+"-"*8+"+"+"-"*25+"+")
    
    def show_fikry(self):
        return "|{:^8}|{:^25}|".format(self.cust_id, self.cust_name)
    
    def __str__(self):
        return self.show_fikry() 