
def find(s):
    i = 0
    while i < len(s):
        if s.startswith(str(int(s[:i+1])+1), i+1):
            return int(s[:i+1])
        i += 1
    return int(s)
    pass
print(find("17181920"))
