import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# ---------- Sorting Generators (yield after each swap) ----------
def bubble_sort(arr):
    arr = arr.copy()
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr
        arr[j + 1] = key
        yield arr

def selection_sort(arr):
    arr = arr.copy()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
            yield arr
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr

# ---------- Visualization ----------
def visualize(sort_func, n=30):
    arr = [random.randint(1, 100) for _ in range(n)]
    generator = sort_func(arr)

    fig, ax = plt.subplots()
    ax.set_title(f"{sort_func.__name__} visualization")
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")

    def update(arr, rects):
        for rect, val in zip(rects, arr):
            rect.set_height(val)

    ani = animation.FuncAnimation(fig, update, fargs=(bar_rects,),
                                  frames=generator, repeat=False, blit=False,
                                  interval=100)
    plt.show()

if __name__ == "__main__":
    # Change sort_func to try different sorts
    visualize(bubble_sort)
    # visualize(insertion_sort)
    # visualize(selection_sort)
