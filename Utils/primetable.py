# the 10000000th prime is 179424691

def get_prime_under(n):
    res = []
    with open("D:/Documents/codePractice/eulerProject/Utils/prime_10000000.txt", 'r') as f:
        while True:
            num = int(f.readline())
            # print(num)
            if num > n:
                return res
            res.append(num)


def get_prime(end, start=1):
    res = []
    with open("D:/Documents/codePractice/eulerProject/Utils/prime_10000000.txt", 'r') as f:
        cnt = 1
        while True:
            num = int(f.readline())
            if cnt > end:
                return res
            if cnt >= start and cnt <= end:
                res.append(num)
            cnt += 1
