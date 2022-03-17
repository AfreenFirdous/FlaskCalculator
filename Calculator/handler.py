class Calculator:
    _OPERATOR = str()
    _OPERAND_1 = str()
    _OPERAND_2 = str()
    _RESULT = str()

    @classmethod
    def _parse_number(cls, number):
        if number == 'dot':
            number = '.'
        return number

    @classmethod
    def get_number(cls, number):
        number = cls._parse_number(number=number)
        if cls._OPERATOR:
            cls._OPERAND_2 += number
            return cls._OPERAND_2
        cls._OPERAND_1 += number
        return cls._OPERAND_1

    @classmethod
    def get_operator(cls, operator):
        if cls._RESULT or cls._RESULT == 0.0:
            cls._OPERAND_1 = cls._RESULT
        cls._OPERATOR += operator
        return cls._OPERAND_1

    @classmethod
    def get_result(cls):
        operand_1 = float(cls._OPERAND_1)
        operand_2 = float(cls._OPERAND_2)
        result = float()
        if cls._OPERATOR == '+':
            result = operand_1 + operand_2
        elif cls._OPERATOR == '-':
            result = operand_1 - operand_2
        elif cls._OPERATOR == 'x':
            result = operand_1 * operand_2
        elif (cls._OPERATOR == '÷' or cls._OPERATOR == '%') and (cls._OPERAND_2 == 0.0):
            result = '0.0'
        elif cls._OPERATOR == '÷':
            result = operand_1 / operand_2
        elif cls._OPERATOR == '%':
            result = operand_1 % operand_2

        cls.clear_screen()
        cls._RESULT = result
        return result

    @classmethod
    def clear_screen(cls):
        cls._OPERAND_1 = str()
        cls._OPERAND_2 = str()
        cls._OPERATOR = str()
        cls._RESULT = str()
        return str()
