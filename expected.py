# This function calculates the expected values for a particular subset of immigration data, in a particular year

# year_total = the sum of the year column, for the year you want to analyze
# category = the secondary dimension you're analyzing (e.g. "number of petitions filed" or "Mexico")
# pop_size = the entire population size (e.g. all countries, from all years)

def expected(year_total, category, pop_size):
    a = category / pop_size
    b = year_total / pop_size
    
    expect_val = (a * b) * pop_size
    
    return round(expect_val, 3)