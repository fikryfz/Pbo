from .motorcycle import MotorCycle_fikry

class ElectricMotorCycle_fikry(MotorCycle_fikry):
    def __init__(self, id_product: int, name: str, price: int, cylinder: int, tank_capacity: int, battery: int, mileage: int):
        super().__init__(id_product, name, price, cylinder, tank_capacity)
        self.battery = battery
        self.mileage = mileage
    
    def show_rizky(self):
        return "|{:^8}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|".format(
            self.id_product,
            self.name,
            f"Rp{self.price:,.0f}",
            f"{self.battery}kWh",
            f"{self.mileage}km",
            "Motor Listrik"
        ) 