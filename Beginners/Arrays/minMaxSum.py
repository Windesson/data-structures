def miniMaxSum(arr):
    arr.sort();
    _sum = sum(arr)
    _min = _sum - arr[-1]
    _max = _sum - arr[0]
    print(f"{_min} {_max}")


if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5]

    miniMaxSum(arr)