class Auto:
    def __init__(self, type: str, brand: str, model: str, year: int | None = None,
                 fuel_type: str | None = None) -> None:
        self.type = type                # Атрибут класса
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.mileage = 0
        self.is_running = False


    def start_engine(self):             # Метод класса
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
    def __init__(self, brand: str, model: str, year: int, cargo_capacity: int) -> None:
        super().__init__("Грузовик", brand, model, year)
        self.cargo_capacity = cargo_capacity        # Грузоподъемность кг
        self.current_cargo = 0                      # Сколько в ней груза лежит в кг


    def load_cargo(self, weight: int):
        if self.current_cargo + weight <= self.cargo_capacity:
            all_weight = self.current_cargo + weight
            print(f"Загружено {weight}кг., общий вес составляет {all_weight}кг.,"
                  f"Свободно {self.cargo_capacity - all_weight}кг.")

    def get_info(self):
        print(f"{self.type} {self.brand} {self.model} Груз: {self.current_cargo}/{self.cargo_capacity} "
              f"Пробег: {self.mileage}км")

# car_five = Truck("MAN", "FX100", 2015, 20000)
# car_five.start_engine()
# car_five.get_info()


class Moto(Auto):
    def __init__(self, brand: str, model: str, year: int, weelie: bool) -> None:
        super().__init__("Мотоцикл", brand, model, year)
        self.weelie = weelie

    def wellie(self):
        if self.weelie:
            print("Встает на дыбы")
        else:
            print("Не встает на дыбы")


    def get_info(self):
        print(f"{self.type} {self.brand} {self.model} {self.year}")



# car_six = Moto("Kawasaki", "Ninja", 2023, False)
# car_six.get_info()


class PassengerCar(Auto):
    def __init__(self, brand: str, model: str, year: int, fuel_type: str, max_passengers: int)\
            -> None:
        super().__init__("Маршрутка", brand, model, year, fuel_type)
        self.max_passengers = max_passengers
        self.current_passengers = 0

    def load_passg(self, passengers: int):
        if self.current_passengers + passengers <= self.max_passengers:
            all_passgrs = self.current_passengers+passengers
            print(f"В автобусе зашли {passengers}, мест занято {all_passgrs}, "
                  f"свободно {self.max_passengers- all_passgrs}")
        else:
            print("Мест свободных нет")


    def get_info(self):
        print(f"{self.type} {self.brand} {self.model} {self.year} {self.fuel_type}" 
              f" \nМаксимальная загрузка {self.max_passengers} человек"
              f" \nТекущее количество пассажиров {self.current_passengers}")


# car_eight = PassengerCar("Mercedes", "Sprinter", 2016, "Patrol", 20) # Экземпляр класса
# car_eight.load_passg(25)


class Electro(Auto):
    def __init__(self, brand: str, model: str, year: int, charge: int) -> None:
        super().__init__("Электро", brand, model, year)
        self.charge = charge

    # Полиморфизм
    def start_engine(self):     # Метод родительского класса переопределен
        if self.charge == 0:
            print(f"Аккумулятор {self.brand} {self.model} разряжен")
        else:
            print(f"Электро-двигатель {self.brand} {self.model} запустился")


    def get_info(self):
        print(f"{self.type} {self.brand} {self.model} {self.year} Заряд аккумулятора-{self.charge}%")



# car_seven = Electro("Tesla", "Model 3", 2024, 50)   # Экземпляр класса
# car_seven.get_info()
# car_seven.start_engine()





