def calculate_winning_numbers(lines, i):
    if i >= len(lines):
        return 0
    winning_numbers = set()
    win, nums = lines[i].split(' | ')
    count = 0
    for num in win.split():
        winning_numbers.add(num)
    for num in nums.split():
        if num in winning_numbers:
            count += 1
    res = 0
    for j in range(i+1, i + count+1):
        res += calculate_winning_numbers(lines, j) + 1
    return res

def main():

    ifp = open('input.txt')
    lines = ifp.readlines()
    for i, line in enumerate(lines):
        lines[i] = line.split(':')[1].strip()

    res = 0
    for i in range(len(lines)):
        res += calculate_winning_numbers(lines, i) + 1
        print(i, res)
    print(res)
main()    
