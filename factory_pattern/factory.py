class Car:

    def __init__(self):
        self.color = None
        self.brand = None
        self.number_of_wheels = None

    def pprint(self):
        print('I am a {} and my color is: {}'.format(
            self.brand,
            self.color
        ))


class Mercedes(Car):

    def __init__(self, color):
        super().__init__()
        self.color = color
        self.brand = 'Mercedes'
        self.number_of_wheels = 4


class BMW(Car):

    def __init__(self, color):
        super().__init__()
        self.color = color
        self.brand = 'BMW'
        self.number_of_wheels = 6


class Nissan(Car):

    def __init__(self, color):
        super().__init__()
        self.color = color
        self.brand = 'Nissan'
        self.number_of_wheels = 8


class CarFactory:

    def get_car(self, car_type, color):
        factory_dict = {
            'BMW': BMW(color=color),
            'Nissan': Nissan(color=color),
            'Mercedes': Mercedes(color=color)
        }

        return factory_dict.get(car_type, None)


if __name__ == '__main__':
    factory = CarFactory()

    car = factory.get_car('BMW', 'pink')
    if car:
        car.pprint()
    else:
        print('The type of car you want is not available!')
