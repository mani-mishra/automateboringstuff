# Say you have a list value like this:
#
#
# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns a string with all
# the items separated by a comma and a space, with and inserted before the last item.
# For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
# But your function should be able to work with any list value passed to it.


def concat_list(input):
    first = ', '.join(map(str,input[0:-1]))
    last = str(input[-1])
    print(first + ', and '+ last)


concat_list(['apples', 'bananas', 'tofu', 'cats'])
concat_list([22,33,112,92])
concat_list([2,3,'##',22])
concat_list([2.2,33,'fotu',42])
