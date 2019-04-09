
class Calc:
    """
    Класс калькулятора
    """
    
    def __init__(self) :
        """
        Инициалирует переменные.
    
        Атрибуты
        --------       
        system_number1 : int
            Система счисления первого числа. (Значение 0)
        number1 : int
            Первое число. (Значение 0)
        system_number2 : int
            Система счисления второго числа. (Значение 0)
        number2 : int
            Второе число. (Значение 0)
        system_result : int
            Система счисления результата. (Значение 0)
        result : int
            Число результата. (Значение 0)
        operationArr : array
            Массив с возможными операциями.
        operation : string
            Значение операции. (Значение "")
        low : int
            Нижняя граница возможной системы счисления. (Значение 2)
        high : int
            Верхняя граница возможной системы счисления. (Значение 37)
        textForSystem : string
            Сообщение при вводе системы счисления.
        errorForSystem : string
            Сообщение ошибки при вводе системы счисления.
        textForNum : string
            Сообщение при вводе числа.
        errorForNum : string
            Сообщение ошибки при вводе числа.
        textForOper : string
            Сообщение при вводе операции.
        errorForOper : string
            Сообщение ошибки при вводе операции.
        errorDivide : string
            Сообщение ошибки при делении на 0.
        resutText : string
            Сообщение при получении результата.
        """
        self.system_number1 = 0
        self.number1 = 0
        self.system_number2 = 0
        self.number2 = 0
        self.system_result = 0
        self.result = 0
        self.operationText = ""
        self.low = 2
        self.high = 37
        self.textForSystem = "Введите систему счисления(2 - 36): "
        self.errorForSystem = "Некорректный ввод! Введите число в диапазоне от 2 до 36"
        self.textForNum = "Введите число: "
        self.errorForNum = "Некорректный ввод! Введите число входящее в систему счисления: "
        self.textForOper = "Введите оперцию (+,-,*,/): "
        self.errorForOper = "Некорректный ввод! Введите одну из преложенных операций. "
        self.errorDivide = "Некорректный ввод!Нельзя делить на 0."
        self.resutText = "Ответ: "
        self.operationArr = ['+','-','*','/']
        
    def check_sys(self,response):
        """
        Проверяет введенную систему счисления
		
    	Параметры
        ---------
    	response : string
            Введенная система счисления.
		
    	Возврат
        -------
        bool
            Возвращает True.
        bool
            Возвращает False.
			
        Ошибки
        ------
        ValueError
            Возникает если введено не число.
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
        Выводит приглашение к вводу системы счисления.
		
    	Возврат
        -------
        response : int
            Возвращает введеную систему счисления.
		
    	Ошибки
        ------
        validate
            Возникает если не число или не входит в заданный диапазон чисел.
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
		
    	Параметры
        ---------
    	num : int
            Введенное число.
		
    	Возврат
        -------
        bool
            Возвращает True.
        bool
            Возвращает False.
        """
        if self.operation==self.operationArr[3] and num==0:
            return False
        return True
    def validate_num(self,num, from_base):
        """
        Проверяет в введеное число в рамках раннее введенной системы счисления.
		
    	Параметры
        ---------
    	num : int
            Введенное число.
        from_base : int
            Система счисления.
		
    	Возврат
        -------
        bool
            Возвращает True.
        bool
            Возвращает False.
		
    	Ошибки
        ------
        ValueError
            Возникает если введено не число.
        """
        try:  
            int(num, from_base)              
            return True
        except ValueError:
            return False
    def number(self,from_base):
        """
        Выводит приглашение к вводу числа.
		
    	Параметры
        ---------
        from_base : int
            Система счисления.
		
    	Возврат
        -------
        num : int
            Возвращает введеное число в рамках ранее заданной системы счисления.
		
    	Ошибки
        ------
        validate
            Возникает если не число или равно нулю.
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
		
    	Параметры
        ---------
    	response : string
            Введенная операция.
		
    	Возврат
        -------
        bool
            Возвращает True.
        bool   
            Возвращает False.
        """
        if response not in self.operationArr:
            return False
        return True
    def operation(self):
        """
        Выводит приглашение к вводу операции.
		
    	Возврат
        -------
        response : string
            Возвращает введеную операцию.
		
        Ошибки
        ------
        validate
            Возникает если нету введенного элемента в заданном массиве с операциями.
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
		
    	Параметры
        ---------
        x : int
            Первое число.
        y : int
            Второе число.
		
    	Возврат
        -------
        int
            Возвращает число.
        """
        print(x + y)
        return  x + y
    
    def minus(self, x, y):
        """
        Вычитание чисел.
		
    	Параметры
        ---------
        x : int
            Первое число.
        y : int
            Второе число.
		
    	Возврат
        -------
        int
            Возвращает число.
        """
        return  x - y
    
    def multiply(self, x, y):
        """
        Умножение чисел.
		
    	Параметры
        ---------
        x : int
            Первое число.
        y : int
            Второе число.
		
    	Возврат
        -------
        int
            Возвращает число.
        """
        return  x * y
    
    def divide(self, x, y):
        """
        Деление чисел.
		
    	Параметры
        ---------
        x : int
            Первое число.
        y : int
            Второе число.
		
    	Возврат
        -------
        int
            Возвращает число.
        """
        return  x // y
        
    def convert_base(self,num, to_base):
        """
        Конвертирование результата в указанную систему счисления.
		
    	Параметры
        ---------
        num : int
            Число с результатом.
        to_base : int
            Система счисления.
		
    	Возврат
        -------
        int
            Если число равно 0, возвращает 0.
        result : string
            Возвращает переконвертированное значение если не равен 0.
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
		
        result = minus+new_res
        return result
    def main(self):
        """
        Основная функция, которая вызывает все остальные.
        """
        self.system_number1 = self.system()
        self.number1 = self.number(self.system_number1)
        self.operationText = self.operation()
        self.system_number2 = self.system()          
        self.number2 = self.number(self.system_number2)
        self.system_result = self.system()
        if self.operationText==self.operationArr[0]:
            self.result = self.plus(self.number1,self.number2)
        if self.operationText==self.operationArr[1]:
            self.result = self.minus(self.number1,self.number2)
        if self.operationText==self.operationArr[2]:
            self.result = self.multiply(self.number1,self.number2)
        if self.operationText==self.operationArr[3]:
            self.result = self.divide(self.number1,self.number2)
        self.result = self.convert_base(self.result,self.system_result)
