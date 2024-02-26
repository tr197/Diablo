# m: số con quái
# d: độ bền
# k: tiêu hao khi g..t
# c: chi phí sửa
def min_gold(m, d, k, c):
    if m == 0:
        return 0
    if d < k:
        return -1  # không g..t được con nào vì kiếm quá yếu
    if d == k:
        if m == 1:
            return 0  # g..t một lần duy nhất -> không cần sửa
        else:
            return -1  # không g..t nổi đến con thứ hai

    curent_d = d
    count_repair = 0
    while m > 0:

        # sửa
        if curent_d <= k:
            curent_d = d
            count_repair += 1

        # g..t
        curent_d -= k
        m -= 1
    return count_repair * c


if __name__ == "__main__":
    params = [7, 11, 3, 10]
    print(min_gold(*params))
