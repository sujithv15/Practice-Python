
def generate_fibonnaci(num):
    if num == 0:
        return []
    if num == 1:
        return 1
    fib_list = [1, 1]
    index = 2
    while index < num:
        fib_list.append(fib_list[index - 1] + fib_list[index - 2])
        index += 1
    return fib_list

def gen_next_fib(num):
    if num == 1:
        return num
    else:
        return num + gen_next_fib(num - 1)