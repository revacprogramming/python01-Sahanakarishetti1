# Loops & Iterators

largest = None
smallest = None

while True:
    num = input("Enter a number? ")

    if num == "done":
        break
    try:
      num=int(num)
      if smallest is None:
        smallest=num
      elif num < smallest :
        smallest=num

        
      if largest is None:
        largest=num
      elif num>largest:
        largest=num
    except:
      print("invalid input")
            

   

print("Maximum", largest)
print("Minimum",smallest)
