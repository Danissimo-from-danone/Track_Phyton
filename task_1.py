if __name__ == "__main__":

    class Animal:
        """
        Базовый класс для представления животных.

        Атрибуты:
            name (str): имя животного
            species (str): вид животного
            age (int): возраст животного в годах
        """

        def __init__(self, name: str, species: str, age: int) -> None:
            """
            Инициализирует экземпляр класса Animal.

            Args:
                name (str): имя животного
                species (str): вид животного
                age (int): возраст животного в годах
            """
            self.name = name
            self.species = species
            self.age = age

        def make_sound(self) -> str:
            """
            Возвращает звук, который издает животное.

            Returns:
                str: звук животного (общий для всех животных)
            """
            return "Some generic animal sound"

        def info(self) -> str:
            """
            Возвращает общую информацию о животном.

            Returns:
                str: информация о животном
            """
            return f"{self.name} is a {self.species} and is {self.age} years old."

        def __str__(self) -> str:
            """
            Строковое представление объекта для удобного вывода.

            Returns:
                str: краткое описание животного
            """
            return f"Animal: {self.name}, Species: {self.species}, Age: {self.age}"

        def __repr__(self) -> str:
            """
            Строковое представление объекта для отладки.

            Returns:
                str: детальное описание животного в формате инициализации
            """
            return f"Animal(name='{self.name}', species='{self.species}', age={self.age})"



    class Dog(Animal):
        """
        Дочерний класс для представления собак, наследует от класса Animal.

        Дополнительные атрибуты:
            breed (str): порода собаки
            _training_level (int): уровень дрессировки (инкапсулированный атрибут)
        """

        def __init__(self, name: str, age: int, breed: str, training_level: int = 0) -> None:
            """
            Инициализирует экземпляр класса Dog. Расширяет конструктор базового класса.

            Args:
                name (str): имя собаки
                age (int): возраст собаки в годах
                breed (str): порода собаки
                training_level (int): уровень дрессировки собаки (по умолчанию 0)
            """
            super().__init__(name, "Dog", age)  # наследуем и расширяем конструктор
            self.breed = breed
            self._training_level = training_level  # инкапсуляция: уровень дрессировки — внутреннее состояние

        def make_sound(self) -> str:
            """
            Перегруженный метод: возвращает звук, специфичный для собак.

            Причина перегрузки: собаки издают специфический звук (гав), отличный от общего звука животных.

            Returns:
                str: звук, который издаёт собака
            """
            return "Woof! Woof!"

        def info(self) -> str:
            """
            Перегруженный метод: расширяет информацию о животном данными о породе и уровне дрессировки.

            Причина перегрузки: для собак важно указывать породу и уровень дрессировки, что добавляет детализацию.

            Returns:
                str: расширенная информация о собаке
            """
            base_info = super().info()
            return f"{base_info} Breed: {self.breed}, Training Level: {self._training_level}"

        def train(self, level_increase: int) -> None:
            """
            Повышает уровень дрессировки собаки.

            Инкапсуляция атрибута _training_level: изменение уровня дрессировки должно
            происходить через контролируемый метод, чтобы избежать некорректных значений.

            Args:
                level_increase (int): величина, на которую повышается уровень дрессировки
            """
            if level_increase > 0:
                self._training_level += level_increase

        def __str__(self) -> str:
            """
            Перегруженный метод: добавляет породу в строковое представление.

            Returns:
                str: краткое описание собаки с указанием породы
            """
            return f"Dog: {self.name}, Breed: {self.breed}, Age: {self.age}"

        def __repr__(self) -> str:
            """
            Перегруженный метод: включает породу и уровень дрессировки в детальное представление.

            Returns:
                str: детальное описание собаки в формате инициализации
            """
            return (f"Dog(name='{self.name}', age={self.age}, "
                    f"breed='{self.breed}', training_level={self._training_level})")


    # Пример использования классов
    generic_animal = Animal("Leo", "Tiger", 5)
    my_dog = Dog("Buddy", 3, "Golden Retriever", 2)

    print("--- Generic Animal ---")
    print(str(generic_animal))
    print(repr(generic_animal))
    print(generic_animal.make_sound())
    print(generic_animal.info())

    print("\n--- Dog Instance ---")
    print(str(my_dog))
    print(repr(my_dog))
    print(my_dog.make_sound())  # перегруженный метод
    print(my_dog.info())       # перегруженный метод

    print("\n--- After Training ---")
    my_dog.train(3)  # увеличиваем уровень дрессировки
    print(my_dog.info())
