def gen_range(start, end):
    for number in range(start, end + 1):
        yield number


print(list(gen_range(1, 10)))
