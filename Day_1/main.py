def main():
    ifp = open('input.txt')
    numbers = set(['0','1','2','3','4','5','6','7','8','9'])


    
    
    res = 0
    for i, line in enumerate(ifp.readlines()):
        line = line.strip()
        for pair in mapping:
            line.replace(pair, mapping[pair])
        # go left to right
        for char in line:
            if char in numbers:
                left = char
                break
            
        # go right to left
        for j in range(len(line) -1, -1, -1):
            if line[j] in numbers:
                right = line[j]
                break
        
        res += int(left + right)
        print(i, line, left, right ,res)
    print(res)
        

main()    
