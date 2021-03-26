
# TODO: import some code

# TODO: test the code


# once we have some tests ... 
# we will run our tests using the pytest package 
# pytest needs to be installed via pip just like any other third party package 
# pytest is already listed in the requirements.txt file 

from app.shopping import format_usd
# this lets us import the function we dfined from the application shopping cart 
# the reason we can do this is because of the presence of the __init__.py file 
# this allows us to import functionality 
# the presence of this file helps us import code from one python file to another 

def test_format_usd():
    assert format_usd(9.5) == "$9.50"