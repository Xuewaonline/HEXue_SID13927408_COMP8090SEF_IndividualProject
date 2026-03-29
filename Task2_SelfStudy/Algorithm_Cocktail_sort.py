"""
Cocktail Sort Algorithm
COMP8090SEF - Task 2 Self Study
Student: HE Xue (SID: 13927408)

Cocktail Sort (also known as Bidirectional Bubble Sort)
is a variation of Bubble Sort that sorts in both directions.

Time Complexity:
  - Best case:    O(n)   - already sorted array
  - Average case: O(n^2)
  - Worst case:   O(n^2) - reverse sorted array
Space Complexity: O(1)   - in-place sorting
"""


def cocktail_sort(arr):
    """
    Sort a list using Cocktail Sort algorithm.
    
    How it works:
    1. Forward pass: move largest element to the right end
    2. Backward pass: move smallest element to the left end
    3. Repeat until no swaps occur
    
    Parameters:
        arr: list of comparable elements
    Returns:
        The sorted list (sorts in-place)
    """
    n = len(arr)
    if n <= 1:
        return arr

    start = 0       # Left boundary
    end = n - 1     # Right boundary
    swapped = True

    while swapped:
        swapped = False

        # Forward pass: left to right
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # If no swaps, array is sorted
        if not swapped:
            break

        end -= 1  # Shrink right boundary
        swapped = False

        # Backward pass: right to left
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1  # Shrink left boundary

    return arr


# ============== DEMONSTRATION ==============

if __name__ == "__main__":
    print("=" * 50)
    print("  COCKTAIL SORT DEMONSTRATION")
    print("=" * 50)

    # Example 1: Basic sorting
    print("\n1. Basic Example:")
    arr1 = [8, 7, 4, 8, 1]
    print(f"   Before: {arr1}")
    cocktail_sort(arr1)
    print(f"   After:  {arr1}")

    # Example 2: Already sorted (Best case O(n))
    print("\n2. Already Sorted (Best Case O(n)):")
    arr2 = [1, 2, 3, 4, 5]
    print(f"   Before: {arr2}")
    cocktail_sort(arr2)
    print(f"   After:  {arr2}")

    # Example 3: Reverse sorted (Worst case O(n^2))
    print("\n3. Reverse Sorted (Worst Case O(n^2)):")
    arr3 = [5, 4, 3, 2, 1]
    print(f"   Before: {arr3}")
    cocktail_sort(arr3)
    print(f"   After:  {arr3}")

    # Example 4: Nearly sorted (Cocktail sort advantage)
    print("\n4. Nearly Sorted (Cocktail Sort Advantage):")
    arr4 = [2, 3, 4, 5, 1]
    print(f"   Before: {arr4}")
    cocktail_sort(arr4)
    print(f"   After:  {arr4}")

    # Example 5: Sorting strings
    print("\n5. Sorting Strings:")
    arr5 = ["Eve", "Alice", "Diana", "Bob", "Charlie"]
    print(f"   Before: {arr5}")
    cocktail_sort(arr5)
    print(f"   After:  {arr5}")

    print("\n" + "=" * 50)
    print("  All demonstrations completed!")
    print("=" * 50)
