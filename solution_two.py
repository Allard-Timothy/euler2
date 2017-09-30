  def fib():
        x,y = 0,1
        while True:
            yield x
            x,y = y, x+y

def is_even(seq):
        for number in seq:
            if not number % 2:
                yield number

 def less_than_mill(seq):
        for number in seq:
            if number > 1000000:
                break
            yield number   

    print sum(is_even(less_than_mill(fib())))
