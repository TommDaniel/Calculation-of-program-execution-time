def fib_r(position):
    """
    Cálculo recursivo simples de Fibonacci (sem memoização).
    """
    if position == 1:
        return 0
    elif position == 2:
        return 1
    else:
        return fib_r(position - 1) + fib_r(position - 2)
