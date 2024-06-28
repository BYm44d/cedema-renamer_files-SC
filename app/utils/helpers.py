import random
from datetime import datetime

class Helper:
    def __init__(self):
        pass

    def implement_casec(self):
        code = self.generate_random_code()
        # day = datetime.now().strftime('%d')
        day = '19'
        month = datetime.now().strftime('%m')
        year = datetime.now().strftime('%Y')
        str_month = self.str_month(month)

        return f'{code}-{day}_{str_month}_{year}-GO5'
        
    def generate_random_code(self):
        characters = '0123456789abcdfghijkmnopqrstuvwyz'
        length=5
        return ''.join(random.choice(characters) for _ in range(length))
    
    def str_month(self, month):
        months = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
        return months[int(month)-1]