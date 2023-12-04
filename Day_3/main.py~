def isNum(val):
    if ord(val) >= ord('0') and ord(val) <= ord('9'):
        return True
    return False

def findSymbol(l, r, i, lines):
    for c in range(l, r+1):
        for x in range(-1, 2):
            for y in range(-1, 2):
                if i + x > -1 and i + x < len(lines) and c + y > -1 and c + y < len(lines[i]):
                    if not isNum(lines[i+x][c+y]) and lines[i+x][c+y] != '.':
                        return True
    return False

def main():

    ifp = open('input.txt')
    lines = ifp.readlines()
    for i in range(len(lines)):
        lines[i] = list(lines[i])
        
    res = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            val = lines[i][j]
            if isNum(val):                
                # look right
                r = j+1
                if r < len(lines[i]):
                    while isNum(lines[i][r]) and r < len(lines[i]):
                        val = val + lines[i][r]
                        r += 1
                r -= 1

                # border is l->r in j
                l = j

                if findSymbol(l, r, i, lines):

                    res += int(val)
                for z in range(l, r+1):
                    lines[i][z] = '.'
                
    print(res)
                
main()
