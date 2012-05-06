# -----------
# User Instructions
# 
# Modify the valid_month() function to verify 
# whether the data a user enters is a valid 
# month. If the passed in parameter 'month' 
# is not a valid month, return None. 
# If 'month' is a valid month, then return 
# the name of the month with the first letter 
# capitalized.
#

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_dict = dict((m[:3].lower(), m) for m in months)
print month_dict
                  
def valid_month(month):
    if month:
        m = month[:3].lower()
        return month_dict.get(m)



print valid_month("januaasdfjsidfo") == "January"    
print valid_month("January") == "January"
print valid_month("jaNuary") == "January"
print valid_month("foo") == None
print valid_month("") == None

