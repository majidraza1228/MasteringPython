def find_sum_of_three(nums, target):
    # Sort the input list
    nums.sort()

    # Fix one integer at a time and find the other two
    for i in range(0, len(nums)-2):
        # Initialize the two pointers
        low = i + 1
        high = len(nums) - 1

        # Traverse the list to find the triplet whose sum equals the target
        while low < high:
            triplet = nums[i] + nums[low] + nums[high]

            # The sum of the triplet equals the target
            if triplet == target:
                return True
                
            # The sum of the triplet is less than target, so move the low pointer forward
            elif triplet < target:
                low += 1
            
            # The sum of the triplet is greater than target, so move the high pointer backward
            else:
                high -= 1
    
    # No such triplet found whose sum equals the given target
    return False

def main():
    nums_lists = [[3, 7, 1, 2, 8, 4, 5],
                  [-1, 2, 1, -4, 5, -3],
                  [2, 3, 4, 1, 7, 9],
                  [1, -1, 0],
                  [2, 4, 2, 7, 6, 3, 1]]

    targets = [10, 7, 20, -1, 8]

    for i in range(len(nums_lists)):
        print(i + 1, ".\tInput array: ", nums_lists[i], sep="")
        if find_sum_of_three(nums_lists[i], targets[i]):
            print("\tSum for", targets[i], "exists")
        else:
            print("\tSum for", targets[i], "does not exist")
        print("-"*100)

if __name__ == '__main__':
    main()