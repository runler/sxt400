# 拿第一个作为基准数，分别从左右往中间 比较
def quick_sort(alist, start, end):
    # 递归退出条件
    if start >= end:
        return

    # 第一个数作为基准数
    mid = alist[start]  # 1、基准数保存好，这位置过度用可能被修改
    low = start  # 指针1
    high = end  # 指针2

    while low < high:
        # a、从右往左 比较 找出比基准数小的数给alist[low]
        while alist[high] >= mid and low < high:
            high -= 1
        alist[low] = alist[high]
        # b、从左往右 比较 找出比基准数数大的给alist[high]
        while alist[low] < mid:
            low += 1
        alist[high] = alist[low]

    # 两端找齐后吧基准数恢复放到对应的位置
    alist[low] = mid

    quick_sort(alist, start, low - 1)
    quick_sort(alist, low + 1, end)


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 14]
    print('排序前数组：', alist)
    quick_sort(alist, 0, len(alist) - 1)
    print('排序后数组：', alist)
