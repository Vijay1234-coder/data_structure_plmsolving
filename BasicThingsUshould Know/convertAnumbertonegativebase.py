def DecimalTobinartry(n,negabase):
    converted =""
    if n == 0:
        return "0"

    while n!= 0:
        rem = n % negabase
        n = n // negabase

        if rem<0:
            rem = rem + (-negabase)
            n = n + 1
        converted = str(rem) + converted
    return converted





print(DecimalTobinartry(13,-2))