count_list = []

def count():
    count_list.append(1)
    return len(count_list)

def _search(key, a, lo, hi):
    
    print("this is try number {} of binary search".format(count()))
    print("lo: {}\nhi: {}\nkey: {}\nlist: {}\n\n".format(lo, hi, key, a))
    
    if hi <= lo:
        return -1
    mid = (lo + hi) // 2

    if key < a[mid]:
        return _search(key, a, lo, mid)
    elif a[mid] < key:
        return _search(key, a, mid+1, hi)
    else:
        return mid

# The binary search method (do not modify!)
# Return the index of key in array a, or -1 if key is not present.

def binary_search(key, a):
    lo = 0
    hi = len(a)
    return _search(key, a, lo, hi)


a = ["apple", "banana", "cherry", "date"]
key = "coconut"

result = binary_search(key, a)

print(result)
