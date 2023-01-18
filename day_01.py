INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

def parse_by_double_linebreaks(str):
        return str.split("\n\n")

def parse_by_single_linebreaks(str):
    return list(map(int, str.split()))

def parse_elves(str):
    return [parse_by_single_linebreaks(elf) for elf in parse_by_double_linebreaks(str)]

def subtotal_elf(elf):
    return sum(elf)

if __name__ == '__main__':
    elves = parse_elves(INPUT)
    subtotals = [subtotal_elf(elf) for elf in elves]
    highest = max(subtotals)
    print("The elf with the most calories is carrying " + str(highest) + " calories.")