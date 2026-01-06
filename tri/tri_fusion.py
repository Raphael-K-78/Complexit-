def tri_fusion(tab):
    if len(tab) <= 1:
        return tab
    mid = len(tab) // 2
    left = tri_fusion(tab[:mid])
    right = tri_fusion(tab[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result