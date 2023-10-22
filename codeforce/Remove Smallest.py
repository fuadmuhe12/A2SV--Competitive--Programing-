def can_obtain_single_element(n, a):
    sorted_a = sorted(a)
    for i in range(n - 1):
        if sorted_a[i + 1] - sorted_a[i] > 1:
            return "NO"
    return "YES"
 
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        result = can_obtain_single_element(n, a)
        print(result)
 
if __name__ == "__main__":
    main()
