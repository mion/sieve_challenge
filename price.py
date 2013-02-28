# Price

class Price
    def __init__(self, amount, cents):
        self.amount = amount
        self.cents = cents
    
    @staticmethod
    def parse(s, money_sym='$', delim=','):
        price = ""
        delim_flag = False
        cents_digit_counter = 2
        beg = s.find(money_sym)

        if beg == -1:
            return nil

        for i in range (beg, len(s)):
            if s[i].isdigit() and cents_digit_counter > 0:
                price += s[i]
                if delim_flag:
                    cents_digit_counter -= 1
            elif s[i] == delim:
                price += s[i]
                delim_flag = True
    
        if not delim_flag:
            price += (delim + "00")
    
        return price

