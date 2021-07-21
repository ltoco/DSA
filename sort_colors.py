# def sortColors(nums) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         low, mid = 0, 0
#         high = len(nums)-1
#         print(low, mid, high)
#         while(mid <= high):
#             print(nums)
#             # print(f"low: {low}, mid: {mid}, high: {high}")

#             if (nums[mid] == 0):
#                 nums[mid], nums[low] = nums[low], nums[mid]
#                 mid+=1
#                 low+=1
#                 print(f"low: {low}, mid: {mid}, high: {high}")
#             elif (nums[mid] == 1):
#                 mid+=1
#                 print(f"low: {low}, mid: {mid}, high: {high}")
#             elif (nums[mid] == 2):
#                 nums[mid], nums[high] = nums[high], nums[mid]
#                 # mid+=1
#                 high-=1
#                 print(f"low: {low}, mid: {mid}, high: {high}")

#         print("\nSolution")
#         print(nums)

def sort_by_counting(nums):
    count_0, count_1, count_2 = 0, 0, 0
    for num in nums:
        if num == 0:
            count_0+=1
        elif num == 1:
            count_1+=1
        else:
            count_2+=1

    nums = [0]*count_0 + [1]*count_1 + [2]*count_2
    print(nums)

if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    nums = [2,0,1]
    # sortColors(nums)
    sort_by_counting(nums)