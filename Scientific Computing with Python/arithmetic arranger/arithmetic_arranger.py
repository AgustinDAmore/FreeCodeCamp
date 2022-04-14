# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

def arithmetic_arranger(lista,calcular=False):
        assert not len(lista)>4, 'Error: Too many problems.'
        numeroUno = ""
        numeroDos = ""
        operador = ""
        filaSuperior = ""
        filaMedia = ""
        filainferior = ""
        resultado = ""

        for elemento in lista:
            elemento = elemento.split()

            numeroUno = elemento[0]
            assert numeroUno.isdigit(), "Error: Numbers must only contain digits."
            assert not len(numeroUno)>4, "Error: Numbers cannot be more than four digits."

            operador = elemento[1]
            assert not (operador != "-" and operador != "+"), "Error: Operator must be '+' or '-'."

            numeroDos = elemento[2]
            assert numeroDos.isdigit(), "Error: Numbers must only contain digits."
            assert not len(numeroDos)>4, "Error: Numbers cannot be more than four digits."

            if len(numeroUno)>len(numeroDos):
                filaSuperior=filaSuperior+(("  "+" "*(len(numeroDos)-len(numeroUno)))+numeroUno)+" "*5
                filaMedia=filaMedia+(operador+" "+(" "*(len(numeroUno)-len(numeroDos)))+numeroDos)+" "*5
                filainferior=filainferior+("-"*len((operador+" "+(" "*(len(numeroUno)-len(numeroDos)))+numeroDos)))+" "*5
                if operador == "+":
                    resultado = resultado+(("  "+" "*(len(numeroDos)-len(numeroUno)))+(str(int(numeroUno)+int(numeroDos))))+" "*5
                else:
                    resultado = resultado+(("  "+" "*(len(numeroDos)-len(numeroUno)))+(str(int(numeroUno)-int(numeroDos))))+" "*5

            elif len(numeroUno)==len(numeroDos):
                filaSuperior=filaSuperior+"  "+numeroUno+" "*5
                filaMedia=filaMedia+(operador+" "+numeroDos)+" "*5
                filainferior=filainferior+("-"*(1+len((operador+numeroDos))))+" "*5
                if operador == "+":
                    resultado = resultado+" "+(str(int(numeroUno)+int(numeroDos)))+" "*5
                else:
                    resultado = resultado+" "+(str(int(numeroUno)-int(numeroDos)))+" "*5
            else:
                filaSuperior=filaSuperior+(("  "+" "*(len(numeroDos)-len(numeroUno)))+numeroUno)+" "*5
                filaMedia=filaMedia+(operador+" "+(" "*(len(numeroUno)-len(numeroDos)))+numeroDos)+" "*5
                filainferior=filainferior+("-"*len((operador+" "+(" "*(len(numeroUno)-len(numeroDos)))+numeroDos)))+" "*5
                if operador == "+":
                    resultado = resultado+" "+(str(int(numeroUno)+int(numeroDos)))+" "*5
                else:
                    resultado = resultado+" "+(str(int(numeroUno)-int(numeroDos)))+" "*5                

        print(filaSuperior)
        print(filaMedia)
        print(filainferior)
        if calcular:
            print(resultado)