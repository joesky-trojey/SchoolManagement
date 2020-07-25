import numpy as np
import time

list_of_lists=[
    [1,2],
    [3,4,5],
    [6,7,8,9]
]
print('original array')
print(list_of_lists)
print('\n')


numpy_array=np.array(list_of_lists)
print('Numpy array')
print(numpy_array)
print('\n')

print (sum(list_of_lists[0]))


print((127+146+155+154)/4)
#print (sum(sum(inner_list) for inner_list in list_of_lists))



# class book():
#     def __init__(self,title):
#         self.title=title
#     def setNumberOfPages(self,pages):
#         self.__no_of_pages=pages

# book1=book("Secret of living upto 100 years")
# book1.setNumberOfPages(500)


# print(book1.__dict__)

# list1=[i for i in range(0,10)]
# print (list1)