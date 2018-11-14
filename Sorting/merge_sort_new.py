
def mergesort(m):
    left, right, result = [], [], []
    if len(m) <= 1:
        return m
    else:
        middle = len(m) // 2
        for i in range(0, middle):
            left.append(m[i])
        for j in range(middle, len(m)):
            right.append(m[j])
        #print("Left : ",left)
        #print("Right : ",right)
        left = mergesort(left)
        right = mergesort(right)

        if left[-1] <= right[0]:
            left.extend(right)
            #print("This one was simple")
            return left
        result = merge(left, right)
        return result

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
            #print("After adding left[0] result=",result)
            #print("Left is now ",left)
        else:
            result.append(right[0])
            right = right[1:]
            #print("After adding right[0] result=",result)
            #print("Right is now ", right)

    if len(left) > 0:
        result.extend(left)
        #print("Remaining elements in left added now result=",result)
    elif len(right) > 0:
        result.extend(right)
        #print("Remaining elements in right added now result=", result)
    return result
