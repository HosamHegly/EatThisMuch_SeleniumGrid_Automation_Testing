def is_contained_in(value,list):
    for item in list:
        if value in list:
            return True
    return False


def calculate_macro_calories(protiens,fats,carbs):
    return protiens*4 + carbs*4 + fats*9