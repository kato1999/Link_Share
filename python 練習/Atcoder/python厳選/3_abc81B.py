if __name__ == "__main__":

    N = int(input())
    A = list(map(int,input().split()))
    count = 0
    while all(a % 2 == 0 for a in A): #Aの全ての要素が偶数かを判断
        A = [a/2 for a in A]
        count += 1
    print(count)


    #自分
    # N = int(input())
    # A = list(map(int, input().split()))
    # T = []
    # for i in A:
    #     t = 0
    #     while i % 2 == 0:
    #         i = i / 2
    #         t += 1
    #     T.append(t)
    # print(min(T))

    '''
    all() 全ての要素がtrueか判定
    
    リンク　→　https://atcoder.jp/contests/abs/tasks/abc081_b
    '''