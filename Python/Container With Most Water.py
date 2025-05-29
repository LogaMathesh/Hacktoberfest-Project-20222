## 🔧 What I Added:
# Python solution for the "Container With Most Water" problem.
#File name: `Container With Most Water.py`
#his script calculates the maximum area of water that can be held between vertical lines using the two-pointer approach.

## 🧠 Algorithm Used:
# Two-pointer technique to optimize space and time.
# Time Complexity: O(n)
# Space Complexity: O(1)

# GitHub username: LogaMathesh
# Aim: Find the maximum area of water container formed between vertical lines
# Date: 2025-05-29

def maxArea(heights):
    """
    Calculate the maximum water container area formed by vertical lines.

    Parameters:
    heights (list of int): List of non-negative integers representing line heights.

    Returns:
    int: Maximum area of water container.
    """
    l, r = 0, len(heights) - 1
    area = 0
    while r > l:
        breadth = r - l
        if heights[l] >= heights[r]:
            height = heights[r]
            area = max(area, height * breadth)
            r -= 1
        else:
            height = heights[l]
            area = max(area, height * breadth)
            l += 1
    return area

# Sample input and run

height = [1, 7, 2, 5, 4, 7, 3, 6]
print("Maximum water area:", maxArea(height))





