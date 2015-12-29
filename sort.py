# -*- coding: utf-8 -*-


def quick_sort(begin, end, list):
    if begin >= end:
        return

    pivot_index = partition(begin, end, list)

    quick_sort(begin, pivot_index, list)
    quick_sort(pivot_index + 1, end, list)

    print(list[begin:end])


def partition(begin, end, list):
    pivot = list[end-1]

    pivot_index = begin
    for i in range(begin, end):
        if list[i] < pivot:
            swap(i, pivot_index, list)
            pivot_index = pivot_index + 1

    swap(pivot_index, end-1, list)

    return pivot_index


def swap(index1, index2, list):
    list[index1], list[index2] = list[index2], list[index1]


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
