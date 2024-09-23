# demo.py
from demo_classes import *

# 1. Создайте два банка: green_bank и red_bank
green_bank = Bank()
red_bank = Bank()

# 2. Вызовите справочный метод default_info() для класса Client()
Client.default_info()

# 3. Создайте объект student класса Client и определите его как клиента банка green_bank
student = Client(name="Студент", age=20, bank=green_bank)

# 4. Создайте объект teacher класса Client и определите его как клиента банка red_bank
teacher = Client(name="Учитель", age=40, bank=red_bank)

# 5. Выведите справочную информацию о созданном объекте student (вызовите метод teacher.info())
teacher.info()

# 6. Выведите справочную информацию о созданном объекте teacher (вызовите метод print(teacher))
student.info()
print(teacher)

# 7. Создайте объект класса SmallHouse
small_house = SmallHouse(price=50000)

# 8. Попробуйте для объекта student купить созданный дом, убедитесь в получении предупреждения
student.buy_house(small_house, discount=10)

# 9. Поправьте финансовое положение объекта student - вызовите метод earn_money()
student.earn_money(60000)

# 10. Снова попробуйте купить дом
student.buy_house(small_house, discount=10)

# 11. Посмотрите, как изменилось состояние объекта student
student.info()
