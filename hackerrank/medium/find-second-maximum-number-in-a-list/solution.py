if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    first = max(arr)  # Subse bada number
    
    # Jab tak max number list me hai, use hataate raho
    while first in arr:
        arr.remove(first)
        
    # Ab jo bacha usme se maximum runner-up hoga
    print(max(arr))
