Code:
python
Copy
Edit
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge=[]
        intervals.sort(key=lambda interval:interval[0])
        for interval in intervals:
            if not merge or merge[-1][1]<interval[0]:
                merge.append(interval)
            else:
                merge[-1]=[merge[-1][0],max(merge[-1][1],interval[1])]
        return merge
Step-by-Step Explanation:
Step 1: Class Definition
python
Copy
Edit
class Solution:
class Solution: This defines a class named Solution.
In Python, a class is like a blueprint for creating objects.
LeetCode often requires you to define a class with a function inside it.
Step 2: Function Definition
python
Copy
Edit
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
def: This is how you define a function in Python.
merge: The name of the function.
self: This refers to the current instance of the class (Solution).
intervals: List[List[int]]:
intervals is the input argument, which is a list of lists.
Each inner list contains two numbers [start, end], representing an interval.
-> List[List[int]]:
This means the function will return a list of lists (a list of merged intervals).
This return type hint is not necessary but helps understand the function.
Step 3: Initialize an Empty List
python
Copy
Edit
merge=[]
merge=[] creates an empty list to store the merged intervals.
Step 4: Sort the Intervals
python
Copy
Edit
intervals.sort(key=lambda interval:interval[0])
.sort(): This sorts the intervals list in increasing order.
key=lambda interval:interval[0]:
lambda interval:interval[0] is an anonymous function (lambda function).
It tells Python to sort by the first value (start time) of each interval.
Example:
python
Copy
Edit
intervals = [[8,10], [1,3], [2,6], [15,18]]
intervals.sort(key=lambda interval: interval[0])
print(intervals)  # Output: [[1,3], [2,6], [8,10], [15,18]]
Step 5: Iterate Over Intervals
python
Copy
Edit
for interval in intervals:
This loops through each interval in the sorted list.
Step 6: Check If Merging is Needed
python
Copy
Edit
if not merge or merge[-1][1]<interval[0]:
if not merge:
This checks if merge is empty (first interval case).
If merge is empty, we add the first interval without checking anything.
merge[-1][1] < interval[0]:
merge[-1]: The last interval in the merge list.
merge[-1][1]: The end time of the last merged interval.
interval[0]: The start time of the current interval.
If merge[-1][1] < interval[0], it means the last merged interval does not overlap with the current one.
Step 7: Add Non-Overlapping Interval
python
Copy
Edit
merge.append(interval)
If there is no overlap, we add the current interval to merge.
Step 8: Merge Overlapping Intervals
python
Copy
Edit
else:
    merge[-1] = [merge[-1][0], max(merge[-1][1], interval[1])]
Else means the intervals overlap.
merge[-1] = [...]: We update the last interval in merge.
merge[-1][0]: The start time remains the same.
max(merge[-1][1], interval[1]):
We take the maximum of the two end times to extend the interval.
Example:
lua
Copy
Edit
merge = [[1,6]] and interval = [2,5]
max(6, 5) = 6 → merge = [[1,6]]
Step 9: Return the Merged Intervals
python
Copy
Edit
return merge
Finally, the function returns the merge list, which contains the merged intervals.
Example Walkthrough
Input:
python
Copy
Edit
intervals = [[1,3], [2,6], [8,10], [15,18]]
Step-by-Step Execution:
Sort the intervals:
lua
Copy
Edit
[[1,3], [2,6], [8,10], [15,18]]
First interval:
merge = [], so we add [1,3] → merge = [[1,3]]
Second interval [2,6]:
merge[-1][1] = 3 < 2 → False (overlap exists)
Update merge[-1] = [1, max(3,6)] = [1,6]
Third interval [8,10]:
merge[-1][1] = 6 < 8 → True (no overlap)
Add [8,10] → merge = [[1,6], [8,10]]
Fourth interval [15,18]:
merge[-1][1] = 10 < 15 → True (no overlap)
Add [15,18] → merge = [[1,6], [8,10], [15,18]]
Return [[1,6], [8,10], [15,18]]
Final Output:
python
Copy
Edit
[[1,6], [8,10], [15,18]]
Summary
Sort the intervals by start time.
Iterate through the sorted intervals.
If merge is empty or there is no overlap, add the interval.
If there is overlap, merge the intervals by updating the end time.
Return the merged list.
This is an efficient approach with O(n log n) time complexity (due to sorting) and O(n) space complexity. 🚀
