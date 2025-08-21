import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield arr

def visualize():
    arr = [random.randint(1, 50) for _ in range(30)]
    generator = bubble_sort(arr)

    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")

    def update(arr, rects):
        for rect, val in zip(rects, arr):
            rect.set_height(val)

    ani = animation.FuncAnimation(fig, update, fargs=(bar_rects,),
                                  frames=generator, repeat=False, blit=False, interval=100)
    plt.show()

if __name__ == "__main__":
    visualize()
