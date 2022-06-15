class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, 
                training_type: str,
                duration: float, 
                distance: float, 
                speed: float, 
                calories: float):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
       return f'Тип тренировки: {self.training_type}; Длительность: {round(self.duration, 3)} ч.; Дистанция: {round(self.distance, 3)} км; Ср. скорость: {round(self.speed, 3)} км/ч; Потрачено ккал: {round(self.calories, 3)}. '

class Training:
    """Базовый класс тренировки."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = 1
        self.M_IN_KM = 1000


    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self, self.duration, self.get_distance(), self.get_mean_speed(), self.get_spent_calories())
        

class Running(Training):
    """Тренировка: бег."""
    def __init__(self, action, duration, weight) -> None:
        super().__init__(action, duration, weight)
        self.LEN_STEP = 0.65

    def get_spent_calories(self) -> float:
        return (18 * self.get_mean_speed() - 20) * self.weight / self.M_IN_KM * self.duration

    def __str__(self) -> str:
        return 'Бег'

class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self, action: int, duration: float, weight: float, height: float):
        super().__init__(action, duration, weight)
        self.height = height
        self.LEN_STEP = 0.65

    def get_spent_calories(self) -> float:
        return (0.035 * self.weight + (self.get_mean_speed()**2 // self.height) * 0.029 * self.weight) * self.duration 

    def __str__(self) -> str:
        return 'Спортивная ходьба'

class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self, action: int, duration: float, weight: float, length_pool: int, count_pool: int):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
        self.LEN_STEP = 1.38

    def get_mean_speed(self) -> float:
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration 

    def get_spent_calories(self) -> float:
        return (self.get_mean_speed() + 1.1) * 2 * self.weight

    def __str__(self) -> str:
        return 'Плавание'

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    
    packages = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    return packages[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

