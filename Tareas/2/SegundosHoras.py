n = int (input ("Digite el tiempo en segundos: "))

def sec_a_horas(seg):
    a=str(seg//3600)
    b=str((seg%3600)//60)
    c=str((seg%3600)%60)
    d=["{} horas {} min {} segundos".format(a, b, c)]
    return d


print(sec_a_horas(n))
