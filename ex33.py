def number_loop(limit, increment=1):
    i = 0
    numbers = []

    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers

result = number_loop(5, 2)

print "The numbers: "

for num in result:
    print num
