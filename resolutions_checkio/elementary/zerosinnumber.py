def end_zeros(num: int) -> int:
    nums = str(num)
    b = 0
    print(len(nums))
    print(nums)
    for i in range(len(nums),0,-1):
        
        if nums[i-1] == "0":
            b = b +1
            print("i= ",i)
            continue
        else:
            print("i= ",i)
            continue
    return b
#Eu notei que oq eu escrevi só está percorrendo um range do tamanho do numero
#Não está nem tocando na string
#Resolvi o codigo mas percebi que eu tava interpretando a questão de maneira errada

if __name__ == '__main__':
 #   print("Example:")
 #   print(end_zeros(1))
    
  # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
    print(end_zeros(0))
    print(end_zeros(1))
    print(end_zeros(10))
    print(end_zeros(101))
    print(end_zeros(245))
    print(end_zeros(100100))

