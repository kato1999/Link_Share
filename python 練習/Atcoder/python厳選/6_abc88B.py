if __name__ == "__main__":

    N = int(input())
    a = sorted(map(int, input().split()))[::-1]
    print(sum(a[::2]) - sum(a[1::2]))

    #自分
    # N = int(input())
    # A = [*map(int, input().split())]
    # reA = sorted(A, reverse=True)
    # arice = 0
    # bob = 0
    # for (i,j) in enumerate(reA):
    #     if i % 2 == 0:
    #         arice += j
    #     else:
    #         bob += j
    # print(arice - bob)

    '''
    リンク　→　https://atcoder.jp/contests/abs/tasks/abc088_b
    '''

