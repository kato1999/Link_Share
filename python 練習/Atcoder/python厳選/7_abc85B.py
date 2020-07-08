if __name__ == "__main__":

    n = map(int, input().split())
    name = input().split()
    sum = 0
    for i,j in zip(name,n):
        if i == "Alice":
            sum += j
    print(sum)