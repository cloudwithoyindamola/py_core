

##CLASS AND OBJECT
# Step 1: Define a class (the blueprint)
class MyComplexNumber:
    def __init__(self, real = 0,img = 0):
        print ("MyComplexNumber constructor executing... ")
        self.real_part= real  # attribute
        self.imag_part = img   # attribute

    def displayComplex(self):
        print("{0} + {1}j".format( self.real_part,self.imag_part))
# Step 2: Create an object against MyComplexNumber class
complx1= MyComplexNumber(40, 50)

#calling displayComplex() function
# Output: 40 + 50j
complx1.displayComplex()

#ANOTHER OBJECT
#Create another object against MyComplexNumber class
# and create a new atrribute 'new_attribute'
complx2= MyComplexNumber(60, 70)
complx2.new_attribute = 80

# Output: 60 70 80
print ((complx2.real_part, complx2.imag_part, complx2.new_attribute))