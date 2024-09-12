
# Roman conversion is remaining

class numbers:
    number_system_literals = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

    def validate_base(self, base):
        if base < 2 or base > 36:
            raise ValueError(f"Base {base} is out of range. Must be between 2 and 36.")
    
    def is_valid_literal(self, text, base):
        return all(char in self.number_system_literals[:base] for char in text)
    
    def decimal(self, text, text_base):
        if not text:
            return 0
        return self.decimal(text[:-1], text_base) * text_base + self.number_system_literals.index(text[-1])
    
    def decimal_to_base(self, text, output_base):
        digits = []
        while text > 0:
            digits.append(self.number_system_literals[text % output_base])
            text //= output_base
        return ''.join(reversed(digits)) if digits else '0'
    
    def base_to_base(self, text, text_base, output_base):
        self.validate_base(text_base)
        self.validate_base(output_base)

        if not self.is_valid_literal(text, text_base):
            raise ValueError(f"invalid literal for base() with base {text_base} : '{text}'")

        return self.decimal_to_base(self.decimal(text, text_base), output_base)


obj = numbers()
print(obj.base_to_base("777", 8, 16))