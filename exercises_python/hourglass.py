def hourglassSum(arr):
    if not isinstance(arr, list):
        return None
    if arr:
        for row in arr:
            if len(row) != len(arr):
                return None
        # suma por filas
        suma = []
        cont = 0
        for numRow in arr[:len(arr) - 2]:
            colS = 0
            colM1 = 1
            colRange = 3
            for _ in range(1 + (len(arr) - 3)):
                sumaP = 0
                if colRange <= len(numRow) - 1:
                    sumTop = 0
                    sumBottom = 0
                    sumBottom2 = 0
                    # top
                    for x in numRow[colS:colRange]:
                        sumTop += x
                    sumaP += sumTop
                    # med
                    sumaP += arr[cont + 1][colM1]
                    colM1 += 1
                    # bottom
                    for x in arr[cont + 2][colS:colRange]:
                        sumBottom += x
                    sumaP += sumBottom
                    colRange += 1
                    colS += 1
                else:
                    y = 0
                    for x in numRow[colS:]:
                        y += x
                    sumaP += y
                    sumaP += arr[cont + 1][colM1]
                    for x in arr[cont + 2][colS:colRange]:
                        sumBottom2 += x
                    sumaP += sumBottom2
                suma.append(sumaP)
            cont += 1
    suma = max(suma)
    return suma

arr = [
    [-9, -9, -9,  1, 1, 1],
    [0, -9,  0,  4, 3, 2],
    [-9, -9, -9,  1, 2, 3],
    [0,  0,  8,  6, 6, 0],
    [0,  0,  0, -2, 0, 0],
    [0,  0,  1,  2, 4, 0]
    ]

print(hourglassSum(arr))