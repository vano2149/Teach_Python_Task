"""
Инструмент для измерения времени выполнения вызова функции.
Определеляют суммарное время, лучшее время и лучшее сумарное время.
"""


import time, sys

timer = time.perf_counter if sys.platform[:3] == 'win' else time.time()

def total(reps, func, *pargs, **kwargs):
    """
    Сумарное время выполнения функции func() reps раз
    Возвращает (сумарное время, последний результат)
    """
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kwargs)
    elapsed = timer() - start
    return (elapsed, ret)


def bestof(reps, func, *pargs, **kwargs):
    """
    Самая быстрая функция func() среди reps запусков.
    Возврашает (Лучшее время, последний результат)
    """
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kwargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return (best, ret)


def bestoftotal(reps1, reps2, func, *pargs, **kwargs):
    """
    Лучшее суммарное время 
    """
    return bestof(reps1, reps2, func, *pargs, **kwargs)