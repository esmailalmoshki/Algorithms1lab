a=[1,8,4,2,3,7,5,6,9]

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



merge(a)
print(a)