# -*- coding: utf-8 -*-


def quick_sort(list):
    pass


def merge_sort(list):
    if len(list) == 1:
        return list

    median_element_index = len(list)/2
    left_part, right_part = (merge_sort(list[:median_element_index]),
                             merge_sort(list[median_element_index:]))

    return merge_sorted_lists(left_part, right_part)


def merge_sorted_lists(list1, list2):
    i, j = 0, 0

    merged_list = []
    while i < len(list1) or j < len(list2):
        if i >= len(list1):
            map(lambda x: merged_list.append(x), list2[j:])
            j = len(list2)
            return merged_list

        if j >= len(list2):
            map(lambda x: merged_list.append(x), list1[i:])
            i = len(list1)
            return merged_list

        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i = i + 1
        elif list1[i] > list2[j]:
            merged_list.append(list2[j])
            j = j + 1

    return merged_list
