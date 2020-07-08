if __name__ == "__main__":

    N, A, B = map(int, input().split())
    print(sum(i for i in range(1, N + 1) if A <= sum(map(int, str(i))) <= B))

    #自分
    # N,A,B = map(int,input().split())
    # lists = []
    # for i in range(1,N+1):
    #     num = len(str(i)) #桁数
    #     for ii in reversed(range(num)): #例　3桁の時　10^2、10^1の順に割っていく
    #         t = i // 10**ii
    #         n = i % 10**ii
    #         if n < 10: #nが一桁になったら終了
    #             break
    #     if t+n >= A and t+n <= B:
    #         lists.append(i)
    # print(sum(lists))

    '''
    map(int, str)
    リンク　→　https://atcoder.jp/contests/abs/tasks/abc083_b
    '''