import time
import tracemalloc
# start timecount and memory monitoring
tracemalloc.start()
start_t = time.perf_counter()
# read input
f = open('input.txt', 'r')
length = f.readline()
massive = f.readline()
a = massive.split()

# type preperation
for i in range(0, len(a)):
    a[i] = int(a[i])

# algorithm body
for i in range(0, int(length) - 1):
    order = i + 1
    value = a[i + 1]

    while (order > 0 and a[order] < a[order - 1]):
        a[order] = a[order - 1]
        a[order - 1] = value
        order = order - 1

# answer validation
answer=""
for i in range(len(a)-1):
    answer+=str(a[i])+" "
answer+=str(a[-1])

# answer written
f = open('output.txt', 'w')
f.write(answer)
f.close()

#timecount and memory usage
print("Time spent is %s",(time.perf_counter()-start_t))
print("The memory used is:%n ",tracemalloc.get_tracemalloc_memory())

tracemalloc.stop()