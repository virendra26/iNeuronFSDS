#Armstrong numbers in interval


low=int(input('Enter lower limit '))
up=int(input('Enter upper limit '))

for num in range(low,up+1):
    num_dig = len(str(num))

    dummy = num
    dsum = 0
    while dummy:
        s = dummy % 10
        dsum += s ** num_dig
        dummy = dummy // 10
    if dsum==num:
        print(num)