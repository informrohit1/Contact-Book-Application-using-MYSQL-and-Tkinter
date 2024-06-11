from tkinter import *

first_num = sec_num = operator = None


def new_digit(digit):
    print(digit)
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)


def clear():
    result_label.config(text='')


def get_operator(op):
    global first_num, operator
    first_num = int(result_label['text'])
    operator = op
    result_label.config(text='')


def get_result():
    global first_num,sec_num,operator

    sec_num = int(result_label['text'])

    if operator == '+':
        result_label.config(text=str(first_num + sec_num))
    elif operator == '-':
        result_label.config(text=str(first_num - sec_num))
    elif operator == '*':
        result_label.config(text=str(first_num * sec_num))
    else:
        if sec_num == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first_num / sec_num,2)))


root = Tk()

root.title('Calculator')
root.iconbitmap('favicon.ico')
# root.maxsize(550, 500)
# root.minsize(450, 400)
root.geometry("320x440")
root.resizable(0, 0)
root.configure(background='black')

result_label = Label(root, text='', bg='black', fg='white')
result_label.grid(row=0, column=0, columnspan=10, pady=(50, 25), sticky='w')
result_label.config(font=('verdana', 30, 'bold'))

btn7 = Button(root, text='7',bg='Yellow',fg='Black',width=5,height=2,command=lambda :new_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',15))

btn8 = Button(root, text='8',bg='Yellow',fg='Black',width=5,height=2,command=lambda :new_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',15))

btn9 = Button(root, text='9',bg='Yellow',fg='Black',width=5,height=2,command=lambda :new_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',15))

btnadd = Button(root, text='+',bg='Yellow',fg='Black',width=5,height=2,command=lambda : get_operator('+'))
btnadd.grid(row=1,column=3)
btnadd.config(font=('verdana',15))


btn4 = Button(root, text='4',bg='Yellow',fg='Black',width=5,height=2,command=lambda :new_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',15))

btn5 = Button(root, text='5',bg='Yellow',fg='Black',width=5,height=2,command=lambda :new_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',15))

btn6 = Button(root, text='6',bg='Yellow',fg='Black',width=5,height=2,command=lambda :new_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',15))

btnsub = Button(root, text='-',bg='Yellow',fg='Black',width=5,height=2,command=lambda : get_operator('-'))
btnsub.grid(row=2,column=3)
btnsub.config(font=('verdana',15))


btn1 = Button(root, text='1',bg='Yellow',fg='Black',width=5,height=2,command=lambda :new_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',15))

btn2 = Button(root, text='2',bg='Yellow',fg='Black',width=5,height=2,command=lambda :new_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',15))

btn3 = Button(root, text='3',bg='Yellow',fg='Black',width=5,height=2,command=lambda :new_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',15))

btnmul = Button(root, text='*',bg='Yellow',fg='Black',width=5,height=2,command=lambda : get_operator('*'))
btnmul.grid(row=3,column=3)
btnmul.config(font=('verdana',15))


btn0 = Button(root, text='0',bg='Yellow',fg='Black',width=5,height=2,command=lambda :new_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',15))

btnclr = Button(root, text='Clr',bg='Yellow',fg='Black',width=5,height=2,command=lambda:clear())
btnclr.grid(row=4,column=0)
btnclr.config(font=('verdana',15))

btneq = Button(root, text='=',bg='Yellow',fg='Black',width=5,height=2,command=lambda:get_result())
btneq.grid(row=4,column=2)
btneq.config(font=('verdana',15))

btndiv = Button(root, text='/',bg='Yellow',fg='Black',width=5,height=2,command=lambda : get_operator('/'))
btndiv.grid(row=4,column=3)
btndiv.config(font=('verdana',15))

root.mainloop()