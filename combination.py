# 2020-2 인공지능과 보안기술 2주차 과제
# 산업보안학과 20186842 박서영

def recursion(lst1, lst2, arr) :
    arr.append(lst1)
    for i, j, in enumerate(lst2) :
        recursion(lst1 + [j], lst2[i+1:], arr)

def combination(input) :
    s = set(input)
    lst = list(s)
    output = []
    recursion([], lst, output)
    del output[0]
    output.sort(key=len)
    return output
    
    
    
