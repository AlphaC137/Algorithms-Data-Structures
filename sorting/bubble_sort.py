"""
Bubble Sort Algorithm
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted:", data)
    print("Sorted:", bubble_sort(data))
