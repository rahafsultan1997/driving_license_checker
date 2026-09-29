age = int(input("How old are you?"))
if age >= 18:
  license = input("do you have a license? (yes/no) ")
  if license.lower() == "yes":
    print("you can drive!")
  else:
      print("sorry! you can't drive without a license")

else:
  print("sorry! you can't drive because you are under 18")
