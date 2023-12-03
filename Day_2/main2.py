def main():
    ifp = open('input.txt')
    res = 0

    for i, line in enumerate(ifp.readlines()):
        ref = {'red': 0, 'blue': 0, 'green': 0}
        line = line.strip()
        line = line.split(':')[1].strip()
        games = line.split(';')
        valid = True
        for j, game in enumerate(games):
            vals = game.split(',')
            for val in vals:
                num = val.split()[0]
                color = val.split()[1]
                print(num, color)
                if int(num) > ref[color]:
                    ref[color] = int(num)

        power = 1
        for a in ref:
            power *= ref[a]
        res += power
    print(res)
                
                
main()            
            
        
        

        
