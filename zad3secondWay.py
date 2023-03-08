import tracemalloc,time
t_start=time.perf_counter()
tracemalloc.start()
a=[7,3,4,9,1,5,6,0,2,8]

def bubble_sort(array):
    last_unsorted=len(array)-1
    holder=0
    counter=0
    for i in range(last_unsorted):
        for j in range(len(a)-i-1):
            if(array[j]>array[j+1]):
                holder=array[j]
                array[j]=array[j+1]
                array[j+1]=holder








bubble_sort(a)
print((a))
print("time is %s",time.perf_counter()-t_start)
print(tracemalloc.get_tracemalloc_memory())
tracemalloc.stop()