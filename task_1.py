# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Grass:
    def __init__(self, height: float, color: str, is_growing: bool):
        """
        Создание и подготовка к работе объекта «Трава».
        :param height: Высота травы в сантиметрах
        :param color: Цвет травы (например, «зелёный», «жёлтый»)
        :param is_growing: Признак роста травы (True — растёт, False — не растёт)
        Примеры:
        >>> grass = Grass(10.5, "зелёный", True)  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота травы должна быть типа int или float")
        if height < 0:
            raise ValueError("Высота травы не может быть отрицательной")
        self.height = height
        if not isinstance(color, str):
            raise TypeError("Цвет травы должен быть типа str")
        if not color:
            raise ValueError("Цвет травы не может быть пустым")
        self.color = color
        if not isinstance(is_growing, bool):
            raise TypeError("Признак роста травы должен быть типа bool")
        self.is_growing = is_growing
    def grow(self, growth_rate: float) -> None:
        """
        Метод, описывающий рост травы.
        :param growth_rate: Скорость роста травы в сантиметрах за период
        :raises TypeError: Если growth_rate не является числом
        :raises ValueError: Если growth_rate отрицательное
        Примеры:
        >>> grass = Grass(10.5, "зелёный", True)
        >>> grass.grow(2.3)
        """
        if not isinstance(growth_rate, (int, float)):
            raise TypeError("Скорость роста должна быть типа int или float")
        if growth_rate < 0:
            raise ValueError("Скорость роста не может быть отрицательной")
        self.height += growth_rate
    def change_color(self, new_color: str) -> None:
        """
        Метод, изменяющий цвет травы.
        :param new_color: Новый цвет травы
        :raises TypeError: Если new_color не является строкой
        :raises ValueError: Если new_color пустая строка
        Примеры:
        >>> grass = Grass(10.5, "зелёный", True)
        >>> grass.change_color("жёлтый")
        """
        if not isinstance(new_color, str):
            raise TypeError("Новый цвет должен быть типа str")
        if not new_color:
            raise ValueError("Новый цвет не может быть пустым")
        self.color = new_color
    def stop_growth(self) -> None:
        """
        Метод, останавливающий рост травы.
        Примеры:
        >>> grass = Grass(10.5, "зелёный", True)
        >>> grass.stop_growth()
        >>> assert grass.is_growing is False
        """
        self.is_growing = False

class Cat:
    def __init__(self, name: str, age: int, is_hungry: bool):
        """
        Создание и подготовка к работе объекта «Кот».
        :param name: Имя кота
        :param age: Возраст кота в годах
        :param is_hungry: Признак голода (True — голоден, False — сыт)
        Примеры:
        >>> cat = Cat("Барсик", 3, True)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя кота должно быть типа str")
        if not name:
            raise ValueError("Имя кота не может быть пустым")
        self.name = name
        if not isinstance(age, int):
            raise TypeError("Возраст кота должен быть типа int")
        if age < 0:
            raise ValueError("Возраст кота не может быть отрицательным")
        self.age = age
        if not isinstance(is_hungry, bool):
            raise TypeError("Признак голода должен быть типа bool")
        self.is_hungry = is_hungry
    def eat(self, food_amount: float) -> None:
        """
        Метод, описывающий процесс поедания пищи котом.
        :param food_amount: Количество съеденной пищи в граммах
        :raises TypeError: Если food_amount не является числом
        :raises ValueError: Если food_amount отрицательное
        Примеры:
        >>> cat = Cat("Барсик", 3, True)
        >>> cat.eat(50.0)
        """
        if not isinstance(food_amount, (int, float)):
            raise TypeError("Количество пищи должно быть типа int или float")
        if food_amount < 0:
            raise ValueError("Количество пищи не может быть отрицательным")
        self.is_hungry = False
    def sleep(self, hours: int) -> None:
        """
        Метод, описывающий сон кота.
        :param hours: Продолжительность сна в часах
        :raises TypeError: Если hours не является целым числом
        :raises ValueError: Если hours отрицательное
        Примеры:
        >>> cat = Cat("Барсик", 3, False)
        >>> cat.sleep(8)
        """
        if not isinstance(hours, int):
            raise TypeError("Продолжительность сна должна быть типа int")
        if hours < 0:
            raise ValueError("Продолжительность сна не может быть отрицательной")
    def meow(self) -> str:
        """
        Метод, воспроизводящий звук, который издаёт кот.
        :return: Звук, который издаёт кот («Мяу!»)
        Примеры:
        >>> cat = Cat("Барсик", 3, False)
        >>> cat.meow()
        'Мяу!'
        """
        return "Мяу!"

class Phone:
    def __init__(self, brand: str, battery_level: int, is_on: bool):
        """
        Создание и подготовка к работе объекта «Телефон».
        :param brand: Бренд телефона (например, «Samsung», «Apple»)
        :param battery_level: Уровень заряда батареи в процентах (от 0 до 100)
        :param is_on: Состояние телефона (True — включён, False — выключен)
        Примеры:
        >>> phone = Phone("Samsung", 75, True)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд телефона должен быть типа str")
        if not brand:
            raise ValueError("Бренд телефона не может быть пустым")
        self.brand = brand
        if not isinstance(battery_level, int):
            raise TypeError("Уровень заряда батареи должен быть типа int")
        if battery_level < 0 or battery_level > 100:
            raise ValueError("Уровень заряда батареи должен быть в диапазоне от 0 до 100")
        self.battery_level = battery_level
        if not isinstance(is_on, bool):
            raise TypeError("Состояние телефона должно быть типа bool")
        self.is_on = is_on
    def turn_on(self) -> None:
        """
        Метод, включающий телефон.
        Примеры:
        >>> phone = Phone("Samsung", 75, False)
        >>> phone.turn_on()
        >>> assert phone.is_on is True
        """
        self.is_on = True
    def turn_off(self) -> None:
        """
        Метод, выключающий телефон.
        Примеры:
        >>> phone = Phone("Samsung", 75, True)
        >>> phone.turn_off()
        >>> assert phone.is_on is False
        """
        self.is_on = False
    def charge(self, charge_amount: int) -> None:
        """
        Метод, заряжающий телефон.
        :param charge_amount: Количество процентов заряда, которое добавляется
        :raises TypeError: Если charge_amount не является целым числом
        :raises ValueError: Если charge_amount отрицательное или превышает доступный лимит для зарядки
        Примеры:
        >>> phone = Phone("Samsung", 75, True)
        >>> phone.charge(15)
        """
        if not isinstance(charge_amount, int):
            raise TypeError("Количество заряда должно быть типа int")
        if charge_amount < 0:
            raise ValueError("Количество заряда не может быть отрицательным")
        new_level = self.battery_level + charge_amount
        self.battery_level = min(new_level, 100)  # не позволяем уровню заряда превышать 100%

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass