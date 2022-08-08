Consider a class named Country that is defined in the prefix code. Your task is to create a list of objects of type Country.

The first line of input is a positive integer nn that denotes the number of countries. nn blocks of input follow. Each block of input will have two lines; the first line will be the name of the country and the second line will be its capital.

Corresponding to each block, create an object of type Country. Append each object to a list named countries. That is, each element of the list should be an object of type Country.

You have to process 2n + 12n+1 lines of input in all. In addition, we will have one final line of input. Ignore this. This will help us in evaluating your output.

n = int(input())
countries = [ ]
for _ in range(n):
    name = input()
    capital = input()
    cnt = Country()
    cnt.set_name(name)
    cnt.set_capital(capital)
    countries.append(cnt)



