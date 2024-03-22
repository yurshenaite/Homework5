n, k, m = map(int, input('Введите количество станций, исходную и конечную станцию: ').split())

if k <= m:
    stations = min(m - (k + 1), k + m - (m + 1))
else:
    stations = min(k - (m + 1), m + n - (k + 1))
print(stations)