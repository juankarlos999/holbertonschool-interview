def arrayManipulation(n, queries):

    array = [0] * n

    for row in queries:
        for i in range((row[0] - 1), (row[1])):
            array[i] = array[i] + row[2]
    array = max(array)
    print(array)


arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]])


def arrayManipulation2(n, queries):
    arr = [0] * (n+1)
    # add the value at first index
    # subtract the value at last index + 1
    for q in queries:
        start, end, amt = q
        arr[start-1] += amt
        arr[end] -= amt

    # max value and running sum
    mv = -1
    running = 0
    for a in arr:
        running += a
        if running > mv:
            mv = running

    return mv