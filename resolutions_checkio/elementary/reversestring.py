def backward_string(val: str) -> str:
    teste = ''
    
    #c = 0
    for i in range(len(val),0,-1):
        #for b in range(len(val) + 1):
            teste += val[i-1]
            print(i-1)
            print(teste)
            continue
    return teste


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    print(backward_string('val'))
    print(backward_string(''))
    print(backward_string('ohho'))
    print(backward_string('123456789'))
    print("Coding complete? Click 'Check' to earn cool rewards!")

