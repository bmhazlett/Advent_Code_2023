ofp = open('main2.txt', 'w')
class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        pCrawl.isEndOfWord = True

    def search(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return None
            pCrawl = pCrawl.children[index]
            
        return pCrawl.isEndOfWord

def main():
    ifp = open('input.txt')
    numbers = set(['1','2','3','4','5','6','7','8','9'])
    mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
               'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
               'nine': '9'}

    left_trie = Trie()
    right_trie = Trie()
    
    for key in mapping:
        left_trie.insert(key)
        right_trie.insert(key[::-1])
        
    
    res = 0
    for i, line in enumerate(ifp.readlines()):
        line = line.strip()
        print(line)
        # go left to right
        left = 0
        for right, char in enumerate(line):
            if char in numbers:
                first = char
                break
            ret = left_trie.search(line[left:right+1])
            if ret is True:
                first = mapping[line[left:right+1]]
                break
            if ret is None:
                done = False
                while not done:
                    if left_trie.search(line[left:right+1]):
                        first = mapping.get(line[left:right+1])
                        break
                    elif left_trie.search(line[left:right+1]) is not None:
                        done = True
                    else:
                        left += 1

                            
                                               
        # go right to left
        left = 0
        rev_line = line[::-1]
        for right, char in enumerate(rev_line):
            if char in numbers:
                second = char
                break
            ret = right_trie.search(rev_line[left:right+1])
            if ret is True:
                second = mapping[rev_line[left:right+1][::-1]]
                break
            if ret is None:
                done = False
                while not done:
                    if right_trie.search(rev_line[left:right+1]):
                        second = mapping[rev_line[left:right+1][::-1]]
                        break
                    elif right_trie.search(rev_line[left:right+1]) is not None:
                        done = True
                    else:
                        left += 1
                        

        res += int(first + second)
        ofp.write(first + second + '\n')
        print(i, int(first + second), res)
    print(res)
        

main()    
