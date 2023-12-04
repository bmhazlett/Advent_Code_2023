def isNum(val):
    if ord(val) >= ord('0') and ord(val) <= ord('9'):
        return True
    return False

def findGears(l, r, i, lines):
    gears = []
    for c in range(l, r+1):
        for x in range(-1, 2):
            for y in range(-1, 2):
                if i + x > -1 and i + x < len(lines) and c + y > -1 and c + y < len(lines[i]):
                    if lines[i+x][c+y] == '*':
                        if (i+x, c+y) not in gears:
                            gears.append((i+x, c+y))
    return gears


def main():

    ifp = open('input.txt')
    lines = ifp.readlines()
    for i in range(len(lines)):
        lines[i] = list(lines[i])

    # {(0,0}: ['124', '324', '654']
    gears = {}
    
    final_res = 0
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
                l = j
                res = findGears(l, r, i, lines)
                
                for gear in res:
                    if gear in gears:
                        gears[gear].append(val)
                    else:
                        gears[gear] = [val]
                for z in range(l, r+1):
                    lines[i][z] = '.'

    for gear in gears:
        if len(gears[gear]) == 2:
            one = int(gears[gear][0])
            two = int(gears[gear][1])
            final_res = final_res +  (one * two)
    print(final_res)

main()    
                
