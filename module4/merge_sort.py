def merge_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    mid = n // 2
    left_lst = lst[:mid]
    right_lst = lst[mid:]
    
    return merge(merge_sort(left_lst), merge_sort(right_lst))


def merge(left_lst, right_lst):
    
    merged = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left_lst) and right_idx < len(right_lst):
  
        if left_lst[left_idx] <= right_lst[right_idx]:
            merged.append(left_lst[left_idx])
            left_idx += 1
        else:
            merged.append(right_lst[right_idx])
            right_idx += 1
    while left_idx < len(left_lst):
        merged.append(left_lst[left_idx])
        left_idx += 1
    while right_idx < len(right_lst):
        merged.append(right_lst[right_idx])
        right_idx += 1
        
    return merged

numbers = [7, 12, 3, 5, 8, 11, 20, 1, 6, 14]
print(merge_sort(numbers))