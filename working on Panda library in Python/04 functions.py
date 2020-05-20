#FUNCTION EXAMPLE

car_data.insert(11 , "Age_Converted" , 0)

def c_convert(val):
    val_converted = val / 12
    return val_converted

car_data["Age_converted"] = c_convert(car_data['Age'])

car_data["Age_converted"] = round(car_data['Age_converted'] , 1)



#FUNCTION with MULTIPLE INPUT and OUTPUT

car_data.insert(12 , "KM_Converted" , 0)

def c_convert(val1 , val2):
    val_converted = val1 / 12
    ratio = val2 / val1
    return [val_converted , ratio]

car_data["Age_converted"] , car_data["KM_converted"] = \

c_convert(car_data['Age']) , car_data['KM'])