from math import floor


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):

            return cls(floor(float_value))
        else:
            return 'value is not a float'

    @classmethod
    def from_roman(cls, value):
        try:
            roman_nums = list(value)
            translate = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            arabic_nums = [translate[r] for r in roman_nums]
            arabic_sum = sum(
                val if val >= next_val else -val
                for val, next_val in zip(arabic_nums[:-1], arabic_nums[1:])
            ) + arabic_nums[-1]

            return cls(int(arabic_sum))
        except Exception:
            pass

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            try:

                return cls(int(value))
            except Exception:
                return 'wrong type'
        else:
            return 'wrong type'

    def add(self, num):
        if isinstance(num, Integer):
            return self.value + getattr(num, 'value')
        else:
            return 'number should be an Integer instance'

    def __repr__(self):
        return self.value


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))
