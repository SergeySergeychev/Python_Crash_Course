
import string

quote = "How can mirrors be real if our eyes aren't real"

def to_jaden_case(quote):
    """Make quote neatly formatted."""
    neatly_formatted_quote =  string.capwords(quote)
    return neatly_formatted_quote

print(to_jaden_case(quote))
