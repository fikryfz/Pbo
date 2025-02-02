class Order_fikry:
    def __init__(self, id_order: int, customer, product, date, quantity: int):
        self.id_order = id_order
        self.customer = customer
        self.product = product
        self.date = date
        self.quantity = quantity
        self.total = self.product.price * self.quantity
    
    @staticmethod
    def header_fikry():
        print("\n+" + "-"*8 + "+" + "-"*15 + "+" + "-"*20 + "+")
        print("|{:^8}|{:^15}|{:^20}|".format(
            "ID Order", "ID Customer", "Tanggal"
        ))
        print("+" + "-"*8 + "+" + "-"*15 + "+" + "-"*20 + "+")
    
    def show_fikry(self):
        return "|{:^8}|{:^15}|{:^25}|{:^20}|".format(
            self.id_order,
            self.customer.cust_id,
            self.product.name,
            self.date.strftime("%Y-%m-%d %H:%M")
        )
    
    def detail_order_fikry(self):
        print("\n+" + "-"*60 + "+")
        print("|{:^60}|".format("DETAIL ORDER"))
        print("+" + "-"*60 + "+")
        print("|{:<25}: {:<32}|".format("ID Order", self.id_order))
        print("|{:<25}: {:<32}|".format("Tanggal", self.date.strftime("%Y-%m-%d %H:%M")))
        print("|{:<25}: {:<32}|".format("ID Customer", self.customer.cust_id))
        print("|{:<25}: {:<32}|".format("Nama Customer", self.customer.cust_name))
        print("|{:<25}: {:<32}|".format("ID Produk", self.product.id_product))
        print("|{:<25}: {:<32}|".format("Nama Produk", self.product.name))
        print("|{:<25}: Rp{:<30,.0f}|".format("Harga", self.product.price))
        print("|{:<25}: {:<32}|".format("Quantity", self.quantity))
        print("|{:<25}: Rp{:<30,.0f}|".format("Total", self.total))
        print("+" + "-"*60 + "+")