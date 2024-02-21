class MathDictionary:
    def __init__(self):
        self.data = {}

    def add_entry(self, topic, content):
        self.data[topic] = content

    def edit_entry(self, topic, new_content):
        if topic in self.data:
            self.data[topic] = new_content
        else:
            print("Тема не знайдена.")

    def delete_entry(self, topic):
        if topic in self.data:
            del self.data[topic]
        else:
            print("Тема не знайдена.")

    def sort_entries(self):
        sorted_entries = sorted(self.data.items())
        return dict(sorted_entries)

    def display_entries(self):
        print("Математичний довідник:")
        for topic, content in self.data.items():
            print(f"Тема: {topic}\nВміст: {content}\n")


def run_program():
    math_guide = MathDictionary()

    # Додавання даних
    math_guide.add_entry("Додавання", "Додавання - це операція об'єднання двох або більше чисел.")
    math_guide.add_entry("Віднімання", "Віднімання - це операція відокремлення одного числа від іншого.")
    math_guide.add_entry("Множення", "Множення - це операція додавання числа до себе деяку кількість разів.")
    math_guide.add_entry("Ділення", "Ділення - це операція розподілу одного числа на інше.")
    math_guide.add_entry("Дроби", "Дроби - це числа, які виражають частину цілого числа.")
    math_guide.add_entry("Проценти", "Проценти - це частина з 100 відсотків.")
    math_guide.add_entry("Потужність", "Потужність - це множення числа на себе декілька разів.")
    math_guide.add_entry("Квадратний корінь", "Квадратний корінь - це число, яке підносять до квадрату, щоб отримати вихідне число.")
    math_guide.add_entry("Лінійні рівняння", "Лінійне рівняння - це рівняння першого ступеня, де невідома знаходиться в першому ступені.")
    math_guide.add_entry("Квадратне рівняння", "Квадратне рівняння - це рівняння другого ступеня, що може бути записане у вигляді ax^2 + bx + c = 0.")
    math_guide.add_entry("Геометрія", "Геометрія - це галузь математики, що вивчає властивості простору, фігур і взаємне розташування об'єктів.")
    math_guide.add_entry("Площа", "Площа - це міра, яка вимірює площу поверхні фігури.")
    math_guide.add_entry("Об'єм", "Об'єм - це міра, яка вимірює кількість простору, який займає тіло.")
    math_guide.add_entry("Тригонометрія", "Тригонометрія - це галузь математики, що вивчає взаємозв'язки між кутами і сторонами трикутників.")
    math_guide.add_entry("Функція", "Функція — це залежність, при якій кожному значенню х з деякої множини відповідає єдине значення змінної у.")
    
    while True:
        print("\nВиберіть опцію:")
        print("1. Показати посібник")
        print("2. Редагувати запис")
        print("3. Видалити запис")
        print("4. Відсортувати посібник")
        print("5. Вийти з програми")

        choice = input("Введіть номер опції: ")

        if choice == "1":
            math_guide.display_entries()
        elif choice == "2":
            topic = input("Введіть тему, яку ви хочете відредагувати: ")
            new_content = input("Введіть новий вміст: ")
            math_guide.edit_entry(topic, new_content)
        elif choice == "3":
            topic = input("Введіть тему, яку ви хочете видалити: ")
            math_guide.delete_entry(topic)
        elif choice == "4":
            math_guide.data = math_guide.sort_entries()
            math_guide.display_entries()
        elif choice == "5":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    run_program()
