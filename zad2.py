import tracemalloc,time



def merge(a):
    if(len(a)>1):
        middle=len(a)//2
        L_subarray=a[:middle]
        R_subarray=a[middle:]

        merge(L_subarray)
        merge(R_subarray)

        i=j=c=0

        while i<len(L_subarray) and j<len(R_subarray):
            if(L_subarray[i]>=R_subarray[j]):
                a[c]=R_subarray[j]
                j+=1
            else:
                a[c]=L_subarray[i]
                i+=1
            c+=1

        while (i<len(L_subarray)):
            a[c]=L_subarray[i]
            i+=1
            c+=1
        while (j<len(R_subarray)):
            a[c]=R_subarray[j]
            j+=1
            c+=1

    # answer validation
    answer = ""
    for i in range(len(a) - 1):
        answer += str(a[i]) + " "
    answer += str(a[-1])

    # answer written
    f = open('output.txt', 'w')
    f.write(answer)
    f.close()

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
merge(a)