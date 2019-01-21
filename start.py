
'''
python library import:
this is how you can import tools built in with python already (say the math library which contains helper methods for finding square roots or exponents)
'''
import math

'''
import other py files within the same module:
this allows you to import another file with could have variables and methods within it. Ideal for code-reuse and keeping
the code here in start.py clear and concise

putting py files within the same module usually implies it is used heavily or depends heavily on other files within
the same module.
'''
import samemodulehelpers

'''
import other py files in another module:
this has the same use as being within the same module, it is just isolated further into its own module. Note when its
in another module, the import name includes the module name within it. To make life easier when using the 'differentmoduleshelpers'
file we have given it an alias name of 'dmh'. Now we can refer to that file by `dmh`
'''
import utils.differentmodulehelpers as dmh





'''
main method - python will automatically begin execution here if this 'IF' statement is present, otherwise if it is not present
it will start from top to bottom executing everything an anything it can
'''
if __name__ == '__main__':
    print("Beginning Demonstration")

    print("Using An Imported Python Library")
    answer = math.pow(5, 2)
    print(answer)

    print("Using An Imported File Within The Same Module")
    answer2 = samemodulehelpers.add_together(8, 10)
    print(answer2)

    print("Using An Imported File In Another Module")
    dmh.print_hello_world()

    # note if we did not assign the alias of 'dmh' we would have to call this method using its full name. Because its in
    # another module we would have to call it as: utils.differentmodulehelpers.print_hello_world()

    print("Demonstration Complete. Terminating")

