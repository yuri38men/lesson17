# Задание 1
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

# Домашнее задание
class Homework:                                                # объявляю класс
    inform = input('Введите строку либо число: ')

    def str_num(self):                                         # метод один
        if self.inform.isdigit():                              # если введено число
            sum_ = sum([int(i) for i in str(self.inform) if int(i) % 2 == 0])  # то определяю сумму четных цифр числа
            return sum_ * self.long()                          # возвращаю произведение суммы четных цифр на длину числа
        elif self.inform.isalpha():                            # если введена строка
            vow_list = []                                      # создаю пустой список для гласных букв
            cons_list = []                                     # и пустой список для согласных букв
            for h in self.inform:                              # запускаю цикл и прохожу по строке
                if h in 'аоуэыяюеи':                           # если нахожу в строке гласные буквы
                    vow_list.append(h)                         # то добавляю их в список для гласных букв
                else:
                    cons_list.append(h)                        # иначе добавляю буквы в список для согласных букв
            if len(vow_list) * len(cons_list) <= self.long():  # если произведение гласных и согласных букв меньше длины строки
                return vow_list                                # возвращаю список гласных букв
            else:
                return cons_list                               # иначе возвращаю список согласных букв
        else:
            print('Вами введены некорректные данные')

    def long(self):                                            # метод два
        return len(self.inform)                                # нахожу длину введенного объекта (строки или числа)


object = Homework()                                            # создаю объект класса
print(object.str_num())

