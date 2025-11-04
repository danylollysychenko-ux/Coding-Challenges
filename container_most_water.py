"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

· eg. in the example below, the coordinates of the two red lines are (1,0) to (1, 8) and (8,0) and (8,7)

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
"""

height = [1,8,6,2,5,4,8,3,7]
#height = [6, 4, 8, 9, 0, 2, 7, 9, 1]
#height = [1,1]
start = 0
end = len(height) - 1
max = 0

while start != end:
    area = min(height[start], height[end]) * (end - start)

    if area > max:
        max = area

    if height[start] < height[end]:
        start += 1
    else:
        end -= 1

print(max)