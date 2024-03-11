A=[]
n=0

def display():
    print("Sorted list :",A)

def read():
    for i in range(n):
        A.append(int(input(f"Enter {i} element :")))

def bubblesort():
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp
            display()
        print("-------------------------------------------")

n=int(input("Enter the size of list : \t"))
read()
bubblesort()
print("\n")
display()