def my_generator():
    yield "One"
    yield "Two"
    yield "Three"


gen = my_generator()

for item in gen:
    print(item)


def generator_cycle():
    for i in range(3):
        yield i


for item in generator_cycle():
    print(item)


def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

for item in my_range(4, 20):
    print(item)
