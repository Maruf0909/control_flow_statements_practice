def find_max(a,b,c):
    """
    Find the maximum number.
    Args:

        a: int
        b: int
        c: int
    return:
        int
    """
    max=a
    if max<b:
        max=b
    if max<c:
        max=c
    return max
print(find_max(-1,12,3))

# Example:
# find_max(1,2,3) -> 3
# find_max(-1,12,3) -> 12

def find_max_idx(a,b,c):
    """
    Find the index of the maximum number.
    Args:
        a: int
        b: int
        c: int
    return:
        int
    """
    ind=0
    if ind>0:
        ind +=a
    if ind>0:
        ind +=b
    if ind>0:
        ind +=c
    return ind
print(find_max_idx(-1,2,13))

# Example:
# find_max_idx(10,2,13) -> 3
# find_max_idx(-1,12,3) -> 2