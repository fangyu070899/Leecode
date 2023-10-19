def backspaceCompare(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    if backspace(s)==backspace(t):
        return True
    else:
        return False
    
def backspace(arr):
    while '#' in arr:
        index = arr.index('#')
        if index==0:
            arr = arr[1:]
        elif index==(len(arr)-1):
            arr = arr[:index-1]
        else:
            arr=arr[:index-1]+arr[index+1:]
        print(arr)
    return arr



if __name__=='__main__':
    s="a##c"
    t="#a#c"
    print(backspaceCompare(s,t))

