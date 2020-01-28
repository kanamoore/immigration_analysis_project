def expected(year_total, category, pop_size):
    a = category / pop_size
    b = year_total / pop_size
    
    expect_val = (a * b) * pop_size
    
    return round(expect_val, 3)