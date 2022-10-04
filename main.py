# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import django
import collections

#def square_mass(height):
#    list_ = []
#    for i in range(len(height)):
#        for j in range(len(height)):
#            m = min(height[i], height[j])
#            index = j - i
#            list_.append(m * index)
#    return max(list_)

nums = [3,4,5,6,7,0,1,2]
target = 2

ind = int(len(nums) / 2)

left_ = 0
right_ = 0
end_ = 0
start_ = 0

if nums[ind] < nums[ind + 1]:
    ind += 1

start_ = nums[0]
left_ = nums[ind - 1]

end_ = nums[len(nums) - 1]
right_ = nums[ind + 1]


if target >= start_:
    if 0 == right_ and -(ind - target) <= ind:
        print("index: ",  (-(ind - target - 1)))

if target >= end_:
    if 0 == left_:
        print("index: ", -(ind + target - 1))