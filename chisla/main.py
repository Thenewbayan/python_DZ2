#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
#Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
#а Катя должна их отгадать. Для этого Петя делает две подсказки. 
#Он называет сумму этих чисел S и их произведение P. 
#Помогите Кате отгадать задуманные Петей числа.

#квадратное уравнение
summ=int(input("Введите сумму - натуральное число от 0 до 1000: "))
prod=int(input("Введите произведение - натуральное число от 0 до 1000: "))
discrim=(summ*summ)-4*prod
if (discrim<0):
    print ("ЗАдача не имеет решения с данными числами")
elif(discrim>0):
    y_number_1=(summ+(discrim**(0.5)))/(2)
    y_number_2=(summ-(discrim**(0.5)))/(2)
    x_number_1=summ-y_number_1
    x_number_2=summ-y_number_2
    #if(type(y_number_1)==int):
    print(f"число {y_number_1}  является натуральным и подходит")
    #elif((type(y_number_2)==int)):
    print(f"число {y_number_2} является натуральным и подходит")
    #elif((type(x_number_1)==int)):
    print(f"число {x_number_1} является натуральным и подходит")
    #else:
    print(f"число {x_number_2} является натуральным и подходит")
else: 
    y_number_1=summ/2
    x_number_1=summ-y_number_1
    #if(type(y_number_1)==int):
    print(f"число {y_number_1}  является натуральным и подходит")
    if ((type(x_number_1)==int)):
        print(f"число {x_number_1} является натуральным и подходит")
   
       
