#2-10
#Take 2-7 and comment code to improve readability
#make 2 variables and add space to left and right
fname = "  Stephan  "
lname = "  Python  "
print(f"{fname}{lname}")

#remove left hand space and concatenate
name_no_l_space = fname.lstrip() + lname.lstrip()
print(name_no_l_space)

#remove all extra spaces 
name_no_extra_space = fname.strip() + " " + lname.lstrip()
print(name_no_extra_space)
