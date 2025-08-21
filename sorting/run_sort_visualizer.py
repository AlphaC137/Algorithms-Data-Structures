import argparse
from visualize_sorting import visualize, bubble_sort, insertion_sort, selection_sort

# Later we’ll plug in merge_sort + quick_sort visuals too

algorithms = {
    "bubble": bubble_sort,
    "insertion": insertion_sort,
    "selection": selection_sort,
}

def main():
    parser = argparse.ArgumentParser(
        description="Visualize Sorting Algorithms (AlgoLab)"
    )
    parser.add_argument(
        "algorithm",
        choices=algorithms.keys(),
        help="Sorting algorithm to visualize"
    )
    parser.add_argument(
        "-n", "--size",
        type=int,
        default=30,
        help="Number of elements to sort (default=30)"
    )

    args = parser.parse_args()
    sort_func = algorithms[args.algorithm]
    visualize(sort_func, args.size)

if __name__ == "__main__":
    main()
