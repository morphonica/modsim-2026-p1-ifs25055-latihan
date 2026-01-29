from functools import partial

def pangkat(base, exp):
    return base ** exp

kuadrat = partial(pangkat, exp=2)
print(kuadrat(5))
