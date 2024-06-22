with open('portfolio.txt', 'r') as portfolio:
    lines = portfolio.readlines()
    for line in lines:
        print(line)