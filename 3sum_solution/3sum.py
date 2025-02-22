def threeSum(nums):
    nums.sort()  # Step 1: Sort the array
    result = []
    
    for i in range(len(nums) - 2):  # Step 2: Loop through the array
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate numbers
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:  # Step 3: Two-pointer search
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1  # Move left pointer to increase sum
            elif total > 0:
                right -= 1  # Move right pointer to decrease sum
            else:
                result.append([nums[i], nums[left], nums[right]])  # Found a triplet
                
                # Step 4: Skip duplicate numbers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1  # Move to the next unique elements

    return result

