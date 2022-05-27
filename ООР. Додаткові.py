#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
class Shop():
   def __init__(self, shop_name, store_type):
     self.shop_name = shop_name
     self.store_type = store_type

   def open_shop (self):

        return f"онлайн-магазин {self.shop_name} відкритий"

   def describe_shop(self):
        return f" Магазин {self.shop_name} продає {self.store_type}"

   def number_of_units(self):
       start = 0
       return f"Кількість видів товару в магазині: {start}"

store = Shop('FOOD', 'food')
store1 = Shop('SPORT', 'sport')
store2 = Shop('CLOTHES', 'clothes')

print(store.open_shop())
print(store.describe_shop())
print(store1.describe_shop())
print(store2.describe_shop())


print(store.number_of_units())


class Discount(Shop):
    def __init__(self, discount_products):
        self.discount_products = discount_products

    def get_discounts_ptoducts(self):
        return f"Список товарів, на які встановлена знижка: {self.discount_products}"

store_discount = Discount(['pears', 'peaches', 'bananas'])
print(store_discount.get_discounts_ptoducts())




#2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
class User:
    def __init__(self, first_name, last_name, age, sex, login_attempts ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = login_attempts


    def describe_user(self):
        return f" Користувач {self.first_name} {self.last_name}"

    def greeting_user(self):
        return f" Вітаю, {self.first_name}!"

    def increment_login_attempts(self):
        return self.login_attempts + 1

    def reset_login_attempts(self):
        login_attempts = 0
        return login_attempts

User1 = User('Mira', 'Iliuk', 18, 'female,', 1)
User2 = User('Tom', 'Hanks', 65, 'male,', 2)
User3 = User('Ruby', 'Skot', 28, 'female,', 3)

print(User1.describe_user())
print(User1.greeting_user())

print(User2.increment_login_attempts())
print(User2.reset_login_attempts())
print(User3.increment_login_attempts())
print(User3.reset_login_attempts())

