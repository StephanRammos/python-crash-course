#8-15.py  must also upload printing_functions.py to github for this file to run on github.
"""import the 2 printing functions: print_models(unprinted_designs, completed_models),
  show_completed_models(completed_models)	in 'printing_functions.py'  """
unprinted_designs = ['phone case','robot pendant', 'dodecahedron']
completed_models = []
completed_models2 = []


from printing_functions import print_models as pm , show_completed_models as scm
pm(unprinted_designs, completed_models)
print()
scm(completed_models)
print()

""" My addition - 2nd call , different list; shows can call functions w/diff names than in definition."""
pm(['laptop case','robot chain', 'tetrahedron'], completed_models2)
print()
scm(completed_models2)
