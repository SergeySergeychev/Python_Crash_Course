"""
def valid_parentheses(string):
    # Return True if string is empty
    if not string:
        return True
    # Count all "(" and ")" parentheses.
    open_par = string.count("(")
    close_par = string.count(")")

    # Find positions of  "(" and ")" parentheses from Left to right.
    loc_of_fst_ele = string.find("(")
    loc_of_sec_ele = string.find (")")

    # Find position of "(" and ")" parentheses from Right to left.
    loc_of_lst_ele = string.rfind(")")
    loc_of_prev_ele = string.rfind("(")
    # Check if the order of parentheses is valid return True , else return False.
    if loc_of_fst_ele < loc_of_sec_ele  and open_par == close_par and loc_of_lst_ele > loc_of_prev_ele:
        return True
    else:
        return False

string = " hhvelkdfm()((xrfes)zhxuv(glpim)l(m)e)fi"
err_string = "i(dduwqyqyqi)rpaj)lschrgt((kiz(w)jjeh)(cxn)"
err_string_num_two = "i(dduwqyqyqi)rpaj)lschrgt((kiz(w)jjeh)(cxn)"
loc_of_lst_ele = string.find(")")
loc_of_prev_ele = string.find("(")

def make_list_of_parentheses(err_string):
    list_of_parentheses = []
    for symb in err_string:
        if symb == ")":
            list_of_parentheses.append(')')
        elif symb == "(":
            list_of_parentheses.append('(')
    return list_of_parentheses
def sum_of_open_and_close_par(err_string):
    list_of_parentheses = make_list_of_parentheses(err_string)
    sum_of_open_par = 0
    sum_of_close_par = 0
    for par in list_of_parentheses:
        if par == "(":
            make_to_ord = ord('(')
            sum_of_open_par += make_to_ord
        elif par == ")":
            make_to_ord = ord(')')
            sum_of_close_par += make_to_ord


print(make_list_of_parentheses(err_string_num_two))
print(make_list_of_parentheses(err_string))
print(make_list_of_parentheses(string))
print(valid_parentheses(err_string))
print(len(make_list_of_parentheses(err_string)))
"""
"""
def make_list_of_parentheses(string):
    list_of_parentheses = []
    for symb in string:
        if symb == ")":
            list_of_parentheses.append(')')
        elif symb == "(":
            list_of_parentheses.append('(')
    return list_of_parentheses



def convert_list_to_str(string):
    str = "".join(make_list_of_parentheses(string))
    return str

string = "(((((())))))"
new_string = convert_list_to_str(string)
print(isValid(string))
"""

def isValid(string):
    # Close the last seen opening symbol w/stack.
    close_map = {"(":")"}
    opens = []

    for symbol in string:
        if symbol in close_map.keys():
            opens.append(symbol)
            print(opens)
        elif opens == [] or symbol != close_map[opens.pop()]:
            return False
    print(opens)
    return opens == []

string = ['(', '(', '(', ')', ')', '(', ')', ')']
print(isValid(string))
