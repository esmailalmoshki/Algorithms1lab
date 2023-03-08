import tracemalloc,time
t_start=time.perf_counter()
tracemalloc.start()

a=[7,3,4,9,1,5,6,0,2,8]

def bubble_sort(array):
    last_unsorted=len(array)-2
    holder=0
    counter=0
    for i in range(last_unsorted):
        counter=0
        while (counter<len(array)-1):
            if(array[counter]>array[counter+1]):
                holder=array[counter]
                array[counter]=array[counter+1]
                array[counter+1]=holder
                counter+=1
            else:
                counter+=1






bubble_sort(a)
print((a))
print("time is %s",time.perf_counter()-t_start)
print(tracemalloc.get_tracemalloc_memory())
tracemalloc.stop()

