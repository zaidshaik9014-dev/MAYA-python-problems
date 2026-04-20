class A:
    def one(self):
        print("This is python")
class B(A):
    def two(self):
        print("This is OOPS")
class C(B):
    def three(self):
        print("This is multi-level")
obj = C()
dbj.one()
obj.two()
obj.three()
