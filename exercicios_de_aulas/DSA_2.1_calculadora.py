soma = lambda x,y:x+y
sub = lambda x,y:x-y
div = lambda x,y:x/y
mult= lambda x,y:x*y

op =1

print("--MENU--\n 1.soma\n 2.subtração\n 3.Divisão\n 4.Multiplicação\n 0.sair")
while op !=0:
    op = int(input("\n escolha:"))
    if op >= 5: 
        print("OP imvalida!!")
        continue
    
    if op == 0:
        break
    
    num1 = int(input("Entre com o numero: "))
    num2 = int(input("Entre com o numero: "))
    match op:
        case 1: print("%i + %i = %i"%(num1,num2,soma(num1,num2)))
        case 2: print("%i - %i = %i"%(num1,num2,sub(num1,num2)))
        case 3: print("%i / %i = %f"%(num1,num2,div(num1,num2)))
        case 4: print("%i X %i = %i"%(num1,num2,mult(num1,num2)))

        
            
