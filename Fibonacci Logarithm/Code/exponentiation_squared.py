def exp_squaring(base, exp):
    if exp == 0:
        return 1
    while exp > 0:
        if exp % 2 == 1:
            return base * exp_squaring( base * base, (exp - 1) / 2 )
        else:
            return exp_squaring( base * base, exp / 2 )
