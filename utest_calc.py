

import unittest
import clasess
 
class CalcTest(unittest.TestCase):
    """
    Класс тестирования методов класса Calc.
    """

    def test_add(self):
        """
        Проверяет сложение чисел.
        """
        clas=clasess.Calc()
        self.assertEqual(clas.plus(1, 2), 3)
        
    def test_sub(self):
        """
        Проверяет вычитание чисел.
        """
        clas=clasess.Calc()
        self.assertEqual(clas.minus(4, 2), 2)
        
    def test_mul(self):
        """
        Проверяет умножение чисел.
        """
        clas=clasess.Calc()
        self.assertEqual(clas.multiply(2, 5), 10)
        
    def test_div(self):
        """
        Проверяет деление чисел.
        """
        clas=clasess.Calc()
        self.assertEqual(clas.divide(8, 4), 2)
        
    def test_check_oper1(self):
        """
        Проверяет оперцию на существование ее в заданном массиве.
        """
        clas=clasess.Calc()
        self.assertEqual(clas.check_oper("+"), True)
        
    def test_validate_num1(self):
        """
        Проверяется возможность преобразование числа с заданной системой счисления.
        """
        clas=clasess.Calc()
        self.assertEqual(clas.validate_num("5",6), True)
        
    def test_validate_num2(self):
        """
        Проверяется возможность преобразование числа с заданной системой счисления.
        """
        clas=clasess.Calc()
        self.assertEqual(clas.validate_num("0",6), True)
        
    def test_check_zero1(self):
        """
        Проверяет является ли второе число нулем при делении.
        """
        clas=clasess.Calc()
        clas.operation='/'
        self.assertEqual(clas.check_zero(1), True)
            
    def test_check_sys1(self):
        """
        Проверка системы счисления.
        """
        clas=clasess.Calc()
        self.assertEqual(clas.check_sys(2), True)
        
        
    def test_check_sys3(self):
        """
        Проверка системы счисления.
        """
        clas=clasess.Calc()
        self.assertEqual(clas.check_sys(36), True)
if __name__ == '__main__':
    unittest.main()
