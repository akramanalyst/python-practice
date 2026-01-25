# Hierarachial inheritance/

class A:
	def m1(self):
		print("m1 from class A ")
class B(A):
	def m2(self):
		print("m2 from class B")
class C(A):
	def m3(self):
		print("m3 from class C")
class D(B):
	def m4(self):
		print("m4 from class D")
class E(B):
	def m5(self):
		print("m5 from class E")
class F(C):
	def m6(self):
		print("m6 from class F")
class G(C):
	def m7(self):
		print("m7 from class G")
objE = E()
objE.m1()
objE.m2()
objE.m5()
#objE.m4()# this will through attributes error.
print("      ")
objG = G()
objG.m1()
objG.m3()
objG.m7()
 