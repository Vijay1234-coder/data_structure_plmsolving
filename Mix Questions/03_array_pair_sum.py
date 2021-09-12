def arr_pair(arr,k):
    if len(arr)<2:
        print("you required more elements in array")
    seen = set()
    output = set()
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num,target)),(max(num,target))))
    print('\n'.join(map(str,list(output))))# it will convert that output set into a list thnr then it will join it by a new line



arr_pair([1,3,2,2,4,0],4) 

