#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    sort.Sort
    Sort algorithm.
'''
class Sort(object):
    __CUTOFF = 5

    def _median3(arr, beg, end):
        mid = (beg + end) // 2

        if arr[beg] > arr[mid]:
            arr[beg], arr[mid] = arr[mid], arr[beg]
        
        if arr[mid] > arr[end]:
            arr[mid], arr[end] = arr[end], arr[mid]

        if arr[beg] > arr[mid]:
            arr[beg], arr[mid] = arr[mid], arr[beg]

        arr[mid], arr[end-1] = arr[end-1], arr[mid]

        return arr[end-1]

    def _qsort(arr, low, high, cmp_obj):
        if high - low < Sort.__CUTOFF:
            Sort._isort(arr, low, high, cmp_obj)
        else:
            pivot = Sort._median3(arr, low, high)
            lbeg = low + 1
            rend = high - 2

            while True:
                while arr[lbeg] < pivot:
                    lbeg += 1
                while arr[rend] > pivot:
                    rend -= 1
    
                if lbeg < rend:
                    arr[lbeg], arr[rend] = arr[rend], arr[lbeg]
                    lbeg += 1
                    rend -= 1
                else:
                    arr[lbeg], arr[high-1] = arr[high-1], arr[lbeg]
                    break
            
            Sort._qsort(arr, low, lbeg - 1, cmp_obj)
            Sort._qsort(arr, lbeg + 1, high, cmp_obj)
           
    def _isort(arr, low, high, cmp_obj):
        i = low + 1

        while i <= high:
            tmp = arr[i]
            j = i - 1

            while j >= low:
                if tmp < arr[j]:
                    arr[j+1] = arr[j]
                else:
                    break

                j -= 1

            arr[j+1] = tmp # bug: j+1 instead of j
            i += 1
    
    def _perc_down(arr, pos, cnt, cmp_obj):
        '''Used for heap ajustment'''

        lchild = lambda x: 2 * x + 1
        tmp = arr[pos]
        p = pos
        
        while lchild(p) < cnt:
            lc = lchild(p)
            rc = lc + 1
            min_child = rc if rc < cnt and arr[rc] < arr[lc] else lc

            if tmp > arr[min_child]:
                arr[p] = arr[min_child]
                p = min_child
            else:
                break
        
        arr[p] = tmp

    def _swim_up(arr, pos, cmp_obj):
        '''Used for heap ajustment'''

        root = lambda x: x//2-1 if x%2 == 0 else x//2
        tmp = arr[pos]
        p = pos

        while root(p) >= 0:
            min_child = root(p)
            
            if tmp < arr[min_child]:
                arr[p] = arr[min_child]
                p = min_child
            else:
                break

        arr[p] = tmp

    def make_heap(arr, cmp_obj):
        cnt = len(arr)
        pos = cnt // 2 - 1

        # From the last node which has children,
        # to the first node, do perc_down
        while pos >= 0:
            Sort._perc_down(arr, pos, cnt, cmp_obj)
            pos -= 1

    def is_sorted(arr, cmp_obj = None):
        ret = True
        i = 1

        while i < len(arr):
            if arr[i] < arr[i-1]:
                ret = False
                break
            i += 1
            
        return ret
                           
    def qsort(arr, cmp_obj=None):
        Sort._qsort(arr, 0, len(arr)-1, cmp_obj)
    
    def isort(arr, cmp_obj=None):
        Sort._isort(arr, 0, len(arr)-1, cmp_obj)
    
    def hsort(arr, cmp_obj=None):
        Sort.make_heap(arr, cmp_obj=None)
        print(arr)

        i = len(arr) - 1
        while i > 0:
            arr[0], arr[i] = arr[i], arr[0]
            Sort._perc_down(arr, 0, i, cmp_obj)
            i -= 1

if __name__ == '__main__':
    import random

    arr = random.sample(range(500), 10)
    arr = arr * 3
    print("before sort: %s" %arr)

    Sort.hsort(arr)
    print("after hsort: %s" %arr)

    Sort.qsort(arr)
    assert Sort.is_sorted(arr)

    Sort.qsort(arr)
    assert Sort.is_sorted(arr)

    print("after qsort: %s" %arr)
