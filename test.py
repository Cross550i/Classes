class Auto:
    def __init__(self, type: str, brand: str, model: str, year: int | None = None,
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



# car_one = Auto("Легковой автомобиль", brand="BMW", model="M5", year=2015, fuel_type="Дизель")
# car_two = Auto("Легковой автомобиль","Volkswagen", "Golf")
# car_three = Auto("Грузовик","Volvo", "FH")
# car_four = Auto("Мотоцикл","Harley Davidson")


class Truck(Auto):
    def __init__(self, type: str, brand: str, model: str, year: int, fuel_type: str, cargo_capacity: int) -> None:
        super().__init__(type, brand, model, year, fuel_type)
        self.cargo_capacity = cargo_capacity        # Грузоподъемность кг
        self.current_cargo = 0                      # Сколько в ней груза лежит в кг


    def load_cargo(self, weight: int):
        if self.current_cargo + weight <= self.cargo_capacity:
            all_weight = self.current_cargo + weight
            print(f"Загружено {weight}кг., общий вес составляет {all_weight}кг.,"
                  f"Свободно {self.cargo_capacity - all_weight}кг.")

    def get_info(self):
        print(f"{self.brand} {self.model} Груз: {self.current_cargo}/{self.cargo_capacity} Пробег: {self.mileage}км")

# car_five = Truck("MAN", "FX100", 2015, "Diesel", 20000)

class Moto(Auto):
    def __init__(self, type: str,brand: str, model: str, year: int, weelie: bool) -> None:
        super().__init__(type, brand, model, year)
        self.weelie = weelie

    def wellie(self):
        if self.type == "Мотоцикл" and self.weelie == True:
            print("Встает на дыбы")
        else:
            print("Не встает на дыбы")



# car_six = Moto("Мотоцикл", "Kawasaki", "Ninja", 2023, True)
# car_six.wellie()


class PassengerCar(Auto):
    def __init__(self, type: str, brand: str, model: str, year: int, fuel_type: str, max_passengers: int) -> None:
        super().__init__(type, brand, model, year, fuel_type)
        self.max_passengers = max_passengers
