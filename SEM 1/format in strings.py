# Python Program for 
# Old Style Formatting 
# of Integers 
  
Integer1 = 12.3456789
print("Formatting in 3.2f format: ") 
print('The value of Integer1 is %3.2f' %Integer1) 
print("\nFormatting in 3.4f format: ") 
print('The value of Integer1 is %3.4f' %Integer1)
# String alignment 
String1 = "|{:<1000}|{:^10}|{:>23}|".format('Geeks','for','Geeks') 
print("\nLeft, center and right alignment with Formatting: ") 
print(String1)
# Positional Formatting 
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life') 
print("\nPrint String in Positional order: ") 
print(String1) 
# Formatting of Integers 
String1 = "{1:b} {0:b}".format(3,4) 
print("\nBinary representation of 16 is ") 
print(String1)
# Formatting of Floats 
String1 = "{0:e}".format(165.6458) 
print("\nExponent representation of 165.6458 is ") 
print(String1) 
  
# Rounding off Integers 
String1 = "{0:.2f}".format(1/6) 
print("\none-sixth is : ") 
print(String1) 
# Python Program for 
# Old Style Formatting 
# of Integers 
  
Integer1 = 12.3456789
print("Formatting in 3.2f format: ") 
print('The value of Integer1 is %3.2f' %Integer1) 
print("\nFormatting in 3.4f format: ") 
print('The value of Integer1 is %3.4f' %Integer1)
