import pickle


class Car:
    def __init__(self, speed, car_class, car_drive):
        self.speed = speed
        self.car_class = car_class
        self.car_drive = car_drive

    def car_info(self):
        return (f'\nавтомобиль класса {self.car_class} развивает максимальную скорость {self.speed}\n'
                f'оснащен {self.car_drive} приводом\n')

    def car_select(self, car_color):
        self.car_color = car_color
        return f'автомобиль класса {self.car_class} окрашен в цвет {self.car_color}'

car_for_ex=Car(120,'легковой', 'полный')
print(car_for_ex.car_info())
print(car_for_ex.car_select('черный'))


