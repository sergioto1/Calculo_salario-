# A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora. 
# Si la cantidad de horas trabajadas es mayor 40 horas. 
# La tarifa se incrementa en un 50% para las
# horas extras. Calcular el salario del trabajador dadas las horas trabajadas y 
# la tarifa ingresadas por el usuario.

def calculoSalario (horas: int, tarifa: float) -> float:
    if (horas > 40):
        salario = horas * tarifa
        horas_extra = horas - 40
        tarifa_extra = tarifa * 1.5
        salario_extra = horas_extra * tarifa_extra
        salario += salario_extra
        print (salario_extra)
        return salario
    else:
        salario = horas * tarifa
        return salario
        
print(calculoSalario(41,30000))
