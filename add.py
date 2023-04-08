try:
    with open('test.txt') as file:
        i= file.readlines()
        res=[eval(a) for a in i]
        with open('solution.txt',mode='w') as f2:
            f2.write(str(sum(res)))
except ValueError:
    print("value not found")
