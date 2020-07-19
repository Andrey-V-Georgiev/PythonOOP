def reverse_text(string):
    rev_string = list(string)[::-1]
    start = 0
    end = len(rev_string) - 1
    while start <= end:
        yield rev_string[start]
        start += 1


for char in reverse_text("step"):
    print(char, end='')
