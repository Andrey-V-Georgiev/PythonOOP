def vowel_filter(function):
    def wrapper():
        letters = function()
        volew_letters = [x for x in letters if x in 'aeiou']
        return volew_letters
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
