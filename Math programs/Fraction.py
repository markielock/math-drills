# Fraction module
# this find_common_multiples function should likely exist in a different module
# in the future


def find_common_multiples(number):
    common_multiples = [1]
    table = 2
    while table < 12:
        for num in range(10 + 1):
            temp = num * table
            if temp == number:
                common_multiples.append(table)
        table += 1
    return common_multiples


def compare_common_denominator(fn, fd, sn, sd):
    denominator = fd * sd
    new_fn = fn * sd
    new_sn = fd * sn
    return (new_fn, new_sn, denominator)


def simplify_fraction(numerator, denominator):
    n_common = find_common_multiples(numerator)
    d_common = find_common_multiples(denominator)
    # need to check lenghts of both lists, start going through them and finding common ones,
    # put them in a list and pick smallest one.
    # then I can divide until i reach the smallest. 

    return

# primary methods


def add(fn, fd, sn, sd):
    if fd != sd:
        fractions = compare_common_denominator(fn, fd, sn, sd)
    else:
        fractions = (fn, sn, fd)  # both denominators are the same

    # result
    denominator = fractions[2]
    numerator = fractions[0] + fractions[1]
    return (numerator, denominator)


def subtract(fn, fd, sn, sd):
    if fd != sd:
        fractions = compare_common_denominator(fn, fd, sn, sd)
    else:
        fractions = (fn, sn, fd)

    denominator = fractions[2]
    numerator = fractions[0] - fractions[1]
    return (numerator, denominator)


def multiply(fn, fd, sn, sd):
    denominator = fd * sd
    numerator = fn * sn
    return (numerator, denominator)


def divide(fn, fd, sn, sd):
    numerator = fn * sd
    denominator = fd * sn
    return (numerator, denominator)
