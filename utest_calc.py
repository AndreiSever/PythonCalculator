

import unittest
import clasess
 
class CalcTest(unittest.TestCase):
    """
    Класс тестирования методов класса Calc.
    """
    clas=clasess.Calc()
    def test_add(self):
        """
        Проверяет сложение чисел.
        """
        self.assertEqual(self.clas.plus(1, 2), 3)
        
    def test_sub(self):
        """
        Проверяет вычитание чисел.
        """
        self.assertEqual(self.clas.minus(4, 2), 2)
        
    def test_mul(self):
        """
        Проверяет умножение чисел.
        """
        self.assertEqual(self.clas.multiply(2, 5), 10)
        
    def test_div(self):
        """
        Проверяет деление чисел.
        """
        self.assertEqual(self.clas.divide(8, 4), 2)
        
    def test_check_oper1(self):
        """
        Проверяет оперцию. Если входит в список - возвращает True
        """
        self.assertEqual(self.clas.check_oper("+"), True)
        
    def test_check_oper2(self):
        """
        Проверяет оперцию. Поданная оперция не входит в список - возвращает False
        """
        self.assertEqual(self.clas.check_oper("sdfds"), False)
        
    def test_validate_num1(self):
        """
        Проверяет валидность числа. Подается число и его система счисления.
        Проверяется возможность преобразование числа с данной системой счисления.
        Число = sdfds
        Система счисления = 6
        Возврат False.
        """
        self.assertEqual(self.clas.validate_num("sdfds",6), False)
        
    def test_validate_num2(self):
        """
        Проверяет валидность числа. Подается число и его система счисления.
        Проверяется возможность преобразование числа с данной системой счисления.
        Число = 412
        Система счисления = 6
        Возврат True.
        """
        self.assertEqual(self.clas.validate_num("412",6), True)
        
    def test_validate_num3(self):
        """
        Проверяет валидность числа. Подается число и его система счисления.
        Проверяется возможность преобразование числа с данной системой счисления.
        Число = 812
        Система счисления = 6
        Возврат False.
        """
        self.assertEqual(self.clas.validate_num("812",6), False)
        
    def test_check_zero1(self):
        """
        Проверяет является ли второе число нулем при делении.
        Оперция = /
        Число = 6
        Возврат True. Не вызовет ошибку.
        """
        self.clas.operation='/'
        self.assertEqual(self.clas.check_zero(6), True)
        
    def test_check_zero2(self):
        """
        Проверяет является ли второе число нулем при делении.
        Оперция = /
        Число = 0
        Возврат False. Вызовет ошибку.
        """
        self.clas.operation='/'
        self.assertEqual(self.clas.check_zero(0), False)
        
    def test_check_zero3(self):
        """
        Проверяет является ли второе число нулем при делении.
        Оперция = ""
        Число = 6
        Возврат True.
        """
        self.assertEqual(self.clas.check_zero(6), True)       
    def test_check_sys1(self):
        """
        Проверка системы счисления.
        Проверяет является ли введеннай текст  - числом.
        Подается число.
        Возврат True.
        """
        self.assertEqual(self.clas.check_sys(6), True)
        
    def test_check_sys2(self):
        """
        Проверка системы счисления.
        Проверяет является ли введеннай текст  - числом.
        Подается текст.
        Возврат False.
        """
        self.assertEqual(self.clas.check_sys("sdfsdf"), False)
        
    def test_check_sys3(self):
        """
        Проверка системы счисления.
        Проверяет взодит ли числр в заданный диапазон (2-36). 
        Возврат False.
        """
        self.assertEqual(self.clas.check_sys(123), False)
if __name__ == '__main__':
    unittest.main()
