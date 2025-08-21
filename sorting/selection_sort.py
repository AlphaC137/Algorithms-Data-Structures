"""
Selection Sort Algorithm
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print("Unsorted:", data)
    print("Sorted:", selection_sort(data))
