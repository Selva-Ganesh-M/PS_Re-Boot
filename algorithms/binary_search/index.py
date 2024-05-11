import unittest

def binary_search(arr, item, start, end):
    if(start>end): return -1
    mid = (start+end)//2
    if(item==arr[mid]):
        return mid
    elif(item<arr[mid]):
        return binary_search(arr, item, 0, mid-1)
    else:
        return binary_search(arr, item, mid+1, len(arr)-1)


class Testing(unittest.TestCase):
    def test_bs(self):
        arr = [1,2,5,8,9,11]
        self.assertEqual(binary_search(arr, 5, 0, len(arr)-1), 2)
        self.assertEqual(binary_search(arr, 1, 0, len(arr)-1), 0)
        self.assertEqual(binary_search(arr, 11, 0, len(arr)-1), 5)
        self.assertEqual(binary_search(arr, 9, 0, len(arr)-1), 4)
        self.assertEqual(binary_search(arr, 20, 0, len(arr)-1), -1)

unittest.main()