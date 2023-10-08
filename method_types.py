class A:

    def sum_of(self,*args):
        result = 0
        for _ in args:
            result+= _
        return  result

class B(A):

    def sum_of(self,value1,value2):
        return value1 + value2


if __name__ == "__main__":
    myobj = A()
    print(myobj.sum_of(10))
    print(myobj.sum_of(10,20))
    print(myobj.sum_of(10,20,40))

    myobj_2 = B()
    print(myobj_2.sum_of(1,2))
    print(myobj_2.sum_of(1,2,3))
