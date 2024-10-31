def plusMinus(arr):
    # Write your code here
    count = [0,0,0] #1 0 -1
    for num in arr:
        if num > 0:
            count[0] = count[0] + 1
        elif num == 0:
            count[1] = count[1] + 1
        else:
            count[2] = count[2] + 1
        
    for i in range(len(count)):
        ratio = count[i]/len(arr)
        print("{:.6f}".format(ratio));

if __name__ == '__main__':

    plusMinus([-4, 3, -9, 0, 4, 1])