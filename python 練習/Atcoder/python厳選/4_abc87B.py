if __name__ == "__main__":

    A,B,C,X = [int(input()) for i in range(4)]
    print(500*a + 100*b + 50*c == X for a in range(A+1) for b in range(B+1) for c in range(C+1))


    #自分
    # A,B,C,X = [int(input()) for i in range(4)]
    # count = 0
    # for a in range(A+1):
    #     for b in range(B+1):
    #         for c in range(C+1):
    #             if X == 500*a + 100*b + 50*c:
    #                 count += 1
    # print(count)

    '''
    sum() true=1,false=0を合計
    リンク　→　https://atcoder.jp/contests/abs/tasks/abc087_b
    '''
