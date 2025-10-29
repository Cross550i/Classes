class Auto:
    def __init__(self, type: str, brand: str, model: str| None = None, year: int | None = None,
                 fuel_type: str | None = None) -> None:
        self.type = type
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.mileage = 0
        self.is_running = False


    def start_engine(self):
        if self.is_running:
            print(f"Двигатель {self.brand} {self.model} уже запущен")
        else:
            self.is_running = True
            print(f"Двигатель {self.brand} {self.model} запустился")


    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            print(f"Двигатель {self.brand} {self.model} остановился")
        else:
            print(f"Двигатель {self.brand} {self.model} уже остановлен")


    def drive(self, distance: int):
        if self.is_running:
            self.mileage += distance
            print(f"Проехали {distance}км. Общий пробег: {self.mileage}км")
        else:
            print("Запустите двигатель")


    def get_info(self):
        print(f"{self.type} {self.brand} {self.model} \nГод выпуска: {self.year} \nВид топлива:"
              f" {self.fuel_type} \nПробег: {self.mileage}км")



car_one = Auto("Легковой", brand="БМВ", model="M5", year=2015, fuel_type="Дизель")
car_two = Auto("Легковой","Volkswagen", "Golf")
car_three = Auto("Грузовик","Volvo", "FH")
car_four = Auto("Мото","Harley Davidson")


car_one.start_engine()
car_one.drive(5)
car_one.get_info()
car_one.stop_engine()

#
# car_two.start_engine()
# car_two.drive(10)
# car_two.get_info()
# car_two.stop_engine()
#
# car_three.start_engine()
# car_three.drive(7)
# car_three.get_info()
# car_three.stop_engine()
#
# car_four.start_engine()
# car_four.drive(12)
# car_four.get_info()
# car_four.stop_engine()


