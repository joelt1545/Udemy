temperatures =[10, -20, -289, 100]

def c_to_f(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return temp_f

for temp in temperatures:
    temp_f = c_to_f(temp)
    if temp_f > -273.15:
        with open('/home/joel1/temp2.txt', 'a') as file:
            file.write(str(temp_f)+"\n")


