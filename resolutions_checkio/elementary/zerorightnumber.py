def end_zeros(num: int) -> int:
    nums = str(num)
    b = 0
    for i in range(len(nums),0,-1):
        if nums[i-1] == '0':
            b = b +1
            continue
        else:
            break
    return b


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")

