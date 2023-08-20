import textwrap

def wrap(string, max_width, indx = 0, v = '' ):
    mins = string[indx:indx+max_width]
    v += mins +'\n'
    if indx < len(string):
        return wrap(string,max_width, indx+max_width, v)
    return v

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
