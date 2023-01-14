#python 3.7.1
# Implementation of Boyer Moore Algorithm using python


# Name   : Dharineesh K S
# Regno  : 123013012

char = 256
 
def bad(string, size):
    badChar = [-1]*char
    for i in range(size):
        badChar[ord(string[i])] = i;
    return badChar
 
def search(text, pattern):
    
    m = len(pattern)
    n = len(text)
    badChar = bad(pattern, m)
    s = 0
    while(s <= n-m):
        j = m-1
        while j>=0 and pattern[j] == text[s+j]:
            j -= 1
        if j<0:
            print("Pattern occur at shift = {}".format(s))
            s += (m-badChar[ord(text[s+m])] if s+m<n else 1)
        else:
            s += max(1, j-badChar[ord(text[s+j])])

            

def main():
    seq1 = "ATCGCGACGTCG"
    seq2 = "CG"
    search(seq1, seq2)

if __name__ == '__main__':
    main()
 
