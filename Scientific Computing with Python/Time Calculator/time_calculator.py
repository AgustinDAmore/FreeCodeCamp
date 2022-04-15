def add_time(t1, t2,day=False):
    nextday = False
    cambios = 0
    horast1 = t1[:t1.find(":")]
    minutost1 = t1[t1.find(":")+1:t1.find(" ")]
    mañadaotarde = t1[t1.find(" ")+1:]

    horast2 = t2[:t2.find(":")]
    minutost2 = t2[t2.find(":")+1:]

    horasTotal = int(horast1)+int(horast2)
    minutosTotal = int(minutost1)+int(minutost2)
    if minutosTotal > 60:
        horasTotal += minutosTotal//60
        minutosTotal -= 60
        if minutosTotal<9:
            minutosTotal = "0"+str(minutosTotal)

    if horasTotal >= 12:
        if horasTotal == 12:
            horasTotal
        else:
            cambios = horasTotal//12
            horasTotal = horasTotal-(cambios*12)
            if horasTotal == 0:
                horasTotal=12

        if mañadaotarde == "PM":
            mañadaotarde = "AM"
            nextday = True
            cambios += 1

        else:
            mañadaotarde = "PM"

    if day != False and cambios == 1:
        day = day.capitalize()
        return(f"{horasTotal}:{minutosTotal} {mañadaotarde}, {day}") 

    elif nextday and cambios == 2:
        return(f"{horasTotal}:{minutosTotal} {mañadaotarde} (next day)")

    elif day != False and cambios > 1:
        day = day.capitalize()
        dias = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        dia = (dias.index(day)+cambios//2)
        if dia <= 6:
            return(f"{horasTotal}:{minutosTotal} {mañadaotarde}, {dias[dia]} ({cambios//2} days later)")
        else:
            dia = dia//6
            return(f"{horasTotal}:{minutosTotal} {mañadaotarde}, {dias[dia-1]} ({cambios//2} days later)")

    elif cambios != 0:
        return(f"{horasTotal}:{minutosTotal} {mañadaotarde} ({cambios//2} days later)")   

    else:
        return(f"{horasTotal}:{minutosTotal} {mañadaotarde}")