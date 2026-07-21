class Solution:
    def sortArray(self,nums):
        n=len(nums)   
        def merge(arr,L,M,R):
            i=L
            j=M+1
            temp=[]
            while i<=M and j<=R:
                if arr[i]>arr[j]:
                    temp.append(arr[j])
                    j+=1
                else:
                    temp.append(arr[i])
                    i+=1
            while i<=M:
                temp.append(arr[i])
                i+=1
            while j<=R:
                temp.append(arr[j])
                j+=1
            for k in range(len(temp)):
                arr[L+k]=temp[k]
        def mergesort(arr,left,right):
            if left>=right:
                return 
            mid=(left+right)//2
            mergesort(arr,left,mid)
            mergesort(arr,mid+1,right)
            merge(arr,left,mid,right)
        mergesort(nums,0,n-1)
        return nums
