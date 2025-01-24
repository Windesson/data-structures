def runLengthEncoding(string):
    # Write your code here.
    i, j = 0,0
    res = ""
    curr = ""
    while j < len(string):
        while j < len(string) and string[i] == string[j] and j - i + 1 <= 9:
            curr = f"{j - i + 1}{string[i]}"
            j += 1

        i = j
        res += curr
        curr = ""
        
    return res