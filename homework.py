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

    def get_message(self) -> str:
        message = f'Тип тренировки: {self.training_type}; \
Длительность: {self.duration:.3f} ч.; \
Дистанция: {self.distance:.3f} км; \
Ср. скорость: {self.speed:.3f} км/ч; \
Потрачено ккал: {self.calories:.3f}.'

        return message


class Training:
    """Базовый класс тренировки."""
    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65
    MIN_IN_HOUR: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = (self.action * self.LEN_STEP / self.M_IN_KM)
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = self.get_distance() / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        message = InfoMessage(
            self, self.duration, self.get_distance(),
            self.get_mean_speed(), self.get_spent_calories())
        return message


class Running(Training):
    """Тренировка: бег."""
    LEN_STEP = 0.65

    def __init__(self, action, duration, weight) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        coeff_calorie_1 = (18 * self.get_mean_speed() - 20) \
            * self.weight / self.M_IN_KM * (self.duration * 60)
        return coeff_calorie_1

    def __str__(self) -> str:
        return 'Running'


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float):
        super().__init__(action, duration, weight)
        self.height = height
        self.LEN_STEP = 0.65

    def get_spent_calories(self) -> float:
        coeff_calorie_2 = ((0.035 * self.weight
                            + (self.get_mean_speed()**2 // self.height)
                            * 0.029 * self.weight) * (self.duration * 60))
        return coeff_calorie_2

    def __str__(self) -> str:
        return 'SportsWalking'


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        coeff_calorie_3 = self.length_pool * self.count_pool \
            / self.M_IN_KM / self.duration
        return coeff_calorie_3

    def get_spent_calories(self) -> float:
        return (self.get_mean_speed() + 1.1) * 2 * self.weight

    def __str__(self) -> str:
        return 'Swimming'


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    packages = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    return packages[workout_type](*data)


def main(training: Training):
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
