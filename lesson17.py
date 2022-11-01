# # Задание 1
class Example:
    stat_num1 = 6
    stat_num2 = 2

    def __init__(self, num_3, num_4):
        self.num_3 = num_3
        self.num_4 = num_4

    def one_(self):
        self.num_5 = 9
        print(self.num_5)

    def two_(self):
        return self.stat_num1 + self.stat_num2

    def three_(self):
        return self.num_3 ** self.num_4


obj = Example(5, 3)
print(obj.stat_num1)
print(obj.two_())
print(obj.three_())
obj.one_()


# Задание 2
class Calculator:

    def __init__(self):
        self.num1 = int(input('Введите первое число: '))
        self.num2 = int(input('Введите второе число: '))

    def summ_(self):
        return self.num1 + self.num2

    def dif_(self):
        return self.num1 - self.num2

    def mult_(self):
        return self.num1 * self.num2

    def div_(self):
        try:
            self.num1 / self.num2
        except ZeroDivisionError:
            return 'Вы пытаетесь разделить на ноль, а делить на ноль нельзя!'
        else:
            return self.num1 / self.num2

    def func(self):
        print('Сумма: ', self.summ_())
        print('Разность: ', self.dif_())
        print('Произведение: ', self.mult_())
        print('Деление: ', self.div_())


object = Calculator()
object.func()

