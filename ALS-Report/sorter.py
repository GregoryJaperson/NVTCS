import time

list = []
file = open("Book1.txt")
for line in file:
    list.append(int(line.strip()))

print(list)

def selection_sort(item_list):
    #Loop through every single items
    for i in range(len(list)-1):
        #minimum is started at the next item
        min = i
        #Loop through the other number not yet sorted
        for j in range(i+1, len(list)):
            #If the number went through is smaller than the initial next item
            if item_list[j]<item_list[min]:
                #minimum index turns into the smaller item's index
                min = j
        #After finding the smallest number from the unsorted list, if a smaller number is found
        if min != i:
            # Swapping of next item, and the smallest item
            t = item_list[i]
            item_list[i] = item_list[min]
            item_list[min] = t

def insertion_sort(item_list):
    for i in range(1 , len(item_list)):
        j = i
        while j > 0 and item_list[j-1] > item_list[j]:
            t = item_list[j-1]
            item_list[j-1] = item_list[j]
            item_list[j] = t
            j = j-1

def merge_sort(item_list):
   if len(item_list) > 1 :
      mid = len(item_list) // 2
      left = item_list[:mid]
      right = item_list[mid:]
      merge_sort(left)
      merge_sort(right)
      merge(item_list, left, right)


def merge(item_list, left, right):
   i = j = k = 0
   while i < len(left) and j < len(right):
      if left[i] < right[j]:
         item_list[k] = left[i]
         i += 1
      else:
         item_list[k] = right[j]
         j += 1
      k += 1

   while i < len(left):
      item_list[k] = left[i]
      i += 1
      k += 1

   while j < len(right):
      item_list[k] = right[j]
      j += 1
      k += 1

start = time.time()
selection_sort(list)
end = time.time()
length = end-start
print(list)
print("Took {} seconds".format(length))
