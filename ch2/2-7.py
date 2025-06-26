fname = "  Stephan  "
lname = "  Python  "
print(f"{fname}{lname}")
name_no_l_space = fname.lstrip() + lname.lstrip()
print(name_no_l_space)
name_no_extra_space = fname.strip() + " " + lname.lstrip()
print(name_no_extra_space)