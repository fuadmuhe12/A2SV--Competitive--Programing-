def swap_case(s):
    last = ''
    for i in s:
        if i.isupper():
            last += i.lower()
        else:
            last += i.upper()
    return last

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
