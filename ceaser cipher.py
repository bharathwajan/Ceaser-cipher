text=input('enter the secrest message : ')
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
key=int(input('enter the key value : '))
print('CEASER CIPHER')
if text!="":
    for i in text:
        if i.isupper()==True:
            i=i.lower()
            if i in alphabets:#checking whether the input is in list for avoiding space errors
                equ=alphabets.index(i)+key
                if equ > 25:#if key value goes beyond 25 this will help
                    x=equ-25
                    y=x-1
                    temp=alphabets[y]
                    print(temp.upper(),end = '')
                else :
                    tempp=alphabets[equ]
                    print(tempp.upper(),end = '')
            else:#if the input string contains any special char this will print that 
                print(i,end ='')
        else:
        
            if i in alphabets:#checking whether the input is in list for avoiding space errors
                equ=alphabets.index(i)+key
                if equ > 25:#if key value goes beyond 25 this will help
                    x=equ-25
                    y=x-1
                    print(alphabets[y],end = '')
                else :
                    print(alphabets[equ],end = '')
            else:
                print(i,end ='')
else:
    print('you have entered the empty string')
        
