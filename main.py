import os, sys, random, time, selenium, tkinter
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master


root = Tk()
root.geometry('500x300')
root.title('If we pay, you pay with us.')
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)
row1_frame = Frame(root, bg='white', width=450, height=50, pady=3)
row1_frame.grid(row=1, sticky='ew')
row2_frame = Frame(root, bg='white', width=450, height=50, pady=3)
row2_frame.grid(row=2, sticky='ew')
row3_frame = Frame(root, bg='white', width=450, height=50, pady=3)
row3_frame.grid(row=3, sticky='ew')
row4_frame = Frame(root, bg='white', width=450, height=50, pady=3)
row4_frame.grid(row=4, sticky='ew')
row5_frame = Frame(root, bg='white', width=450, height=50, pady=3)
row5_frame.grid(row=5, sticky='ew')
row6_frame = Frame(root, bg='white', width=450, height=50, pady=3)
row6_frame.grid(row=0, sticky='ew')
L1 = Label(row1_frame, text='Chromedriver executable path')
L1.pack(side=LEFT)
pathBox = Entry(row1_frame, bd=1)
pathBox.pack(side=LEFT)
L2 = Label(row2_frame, text='Merchant Type')
L2.pack(side=LEFT)
merchantTypeBox = Entry(row2_frame, bd=1, width=5)
merchantTypeBox.pack(side=LEFT)
L2 = Label(row2_frame, text='Bill no.')
L2.pack(side=LEFT)
billNoBox = Entry(row2_frame, bd=1)
billNoBox.pack(side=LEFT)
L3 = Label(row3_frame, text='Amount to pay')
L3.grid(row=2, column=0)
L3.pack(side=LEFT)
amountBox = Entry(row3_frame, bd=1)
amountBox.pack(side=LEFT)
L4 = Label(row4_frame, text='Amount paid: ')
L4.grid(row=3, column=0)
L4.pack(side=LEFT)
buttonCommit = Button(row5_frame, height=1, width=10, text='Pay', command=(lambda : retrieve_input()))
buttonCommit.pack(side=RIGHT)
instructionText = Text(row6_frame, height=5, width=70)
instructionText.insert(END, '1. Download the right version of chromedriver (https://chromedriver.chromium.org/)\n')
instructionText.insert(END, '2. Make sure you have registered the bill on PPS\n')
instructionText.insert(END, '3. This script only works with PPS bank transfer, not credit card\n')
instructionText.pack(side='bottom')
instructionText.configure(state=DISABLED)

def pay_loop(path, billType, billCodfe, targetAmount):
    driver = webdriver.Chrome(executable_path=path)
    billLink = "confirmPayment('" + str(billType) + "',billAlias" + str(billType) + str(billCode) + ",'" + str(billCode) + "','N')"
    totalAmountPaid = 0
    driver.get('https://www.ppshk.com/pps/pps2/revamp2/template/pc/login_c.jsp')
    while 1:
        URL = driver.current_url
        if URL == 'https://www.ppshk.com/pps/AppUserLogin':
            break

    print('Login sucessful')
    while totalAmountPaid < targetAmount:
        driver.execute_script(billLink)
        print('clicked')
        amountPay = driver.find_element_by_name('AMOUNT')
        amountPay.click()
        paidAmount = random.randint(101, 110) / 100
        totalAmountPaid = totalAmountPaid + paidAmount
        amountPay.send_keys(str(paidAmount))
        print('amount paid: ' + str(totalAmountPaid))
        driver.execute_script('confirmSubmit()')
        driver.execute_script('confirmSubmit()')
        while 1:
            URL = driver.current_url
            if URL == 'https://www.ppshk.com/pps/AppPayBill':
                driver.execute_script("formSubmit('/pps/AppLoadBill',document.ppsForm.PMA.value,'')")
                break

        amountPaid = 'Amount paid: ' + str(totalAmountPaid)
        L4.configure(text=amountPaid)

    driver.close()


def retrieve_input():
    inputValue = amountBox.get()
    print(inputValue)
    pay_loop(pathBox.get(), merchantTypeBox.get(), billNoBox.get(), float(amountBox.get()))


app = Window(root)
root.mainloop()