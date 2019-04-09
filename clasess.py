
class Calc:
    """
    Класс калькулятора
    """
    system_number1 = 0
    number1 = 0
    system_number2 = 0
    number2 = 0
    system_result = 0
    result = 0
    operation = ''
    low = 2
    high = 37
    textForSystem = "Введите систему счисления(2 - 36): "
    errorForSystem = "Некорректный ввод! Введите число в диапазоне от 2 до 36"
    textForNum = "Введите число: "
    errorForNum = "Некорректный ввод! Введите число входящее в систему счисления: "
    textForOper = "Введите оперцию (+,-,*,/): "
    errorForOper = "Некорректный ввод! Введите одну из преложенных операций. "
    errorDivide = "Некорректный ввод!Нельзя делить на 0."
    resutText = "Ответ: "
    operationArr = ['+','-','*','/']
    def check_sys(self,response):
        """
        Проверяет введенную систему счисления
        """
        try:
           if int(response) not in  range(self.low,self.high):
               return False
           else:
               return True
        except ValueError:
           return False
    def system(self):
        """
        Выводит приглашение к вводу системы счисления. В случае успешного завершения всех проверок возвращает число.
        """
        validate = False
        #response = 0
        while validate==False:
            response = input(self.textForSystem)
            validate = self.check_sys(response)
            if validate==False:
               print(self.errorForSystem)               
        return int(response)
    def check_zero(self,num):
        """
        Проверяет деления числа на 0.
        """
        if self.operation==self.operationArr[3] and num==0:
            return False
        return True
    def validate_num(self,num, from_base):
        """
        Проверяет в введеное число в рамках раннее введенной системы счисления.
        """
        try:  
            int(num, from_base)              
            return True
        except ValueError:
            return False
    def number(self,from_base):
        """
        Выводит приглашение к вводу числа. В случае успешного завершения всех проверок возвращает число.
        """
        validate = False
        while validate==False:
            num = input(self.textForNum)
            validate = self.validate_num(num,from_base)
            if validate==True:
                validate = self.check_zero(int(num, from_base))
                if validate==False:
                    print(self.errorDivide)
            else:
                print(self.errorForNum+str(from_base))
        return int(num, from_base)   
    def check_oper(self,response):
        """
        Проверяет входит ли операция в список допустимых.
        """
        if response not in self.operationArr:
            return False
        return True
    def operation(self):
        """
        Выводит приглашение к вводу операции. В случае успешного завершения всех проверок возвращает операцию.
        """
        validate = False
        while validate==False:
            response = input(self.textForOper)
            validate = self.check_oper(response)
            if validate==False:
                print(self.errorForOper)
        return response
    def plus(self, x, y):
        """
        Сложения чисел.
        """
        return  x + y
    
    def minus(self, x, y):
        """
        Вычитание чисел.
        """
        return  x - y
    
    def multiply(self, x, y):
        """
        Умножение чисел.
        """
        return  x * y
    
    def divide(self, x, y):
        """
        Деление чисел.
        """
        return  x // y
        
    def convert_base(self,num, to_base):
        """
        Конвертирование результата в указанную систему счисления и его возвразение.
        """
        if num == 0:
            return 0
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        new_res = ''
        minus=""
        if num < 0:
            minus = "-"
            num = -num 
        while num > 0:            
            new_res = alphabet[num % to_base] + new_res
            num //= to_base       
        return minus+new_res
    def main(self):
        """
        Основная функция.
        """
        self.system_number1 = self.system()
        self.number1 = self.number(self.system_number1)
        self.operation = self.operation()
        self.system_number2 = self.system()          
        self.number2 = self.number(self.system_number2)
        self.system_result = self.system()
        if self.operation==self.operationArr[0]:
            self.result = self.plus(self.number1,self.number2)
        if self.operation==self.operationArr[1]:
            self.result = self.minus(self.number1,self.number2)
        if self.operation==self.operationArr[2]:
            self.result = self.multiply(self.number1,self.number2)
        if self.operation==self.operationArr[3]:
            self.result = self.divide(self.number1,self.number2)
        self.result = self.convert_base(self.result,self.system_result)
