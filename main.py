from tkinter import *
from tkinter import messagebox
from telesign.messaging import MessagingClient

def EnviarSMS():
    customer_id = '*****************************'
    api_key = '**********************'
    phone_number = '55' + txtNumero.get()
    message = txtMensagem.get()
    message_type = 'ARN'
    messaging = MessagingClient(customer_id, api_key)
    response = messaging.message(phone_number, message, message_type)
    if response.status_code == 200:
        messagebox.showinfo('sucess', 'SMS enviado com sucesso!')
    else:
        messagebox.showinfo('error', 'Falha ao enviar SMS, vefique o número e tente novamente')



main = Tk()
main.title('SMS via Python')
main.geometry('200x200')

rows = 0
while rows < 10:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1

txtNumero = Entry(main)
txtNumero.insert(0, 'Digite seu número')
txtNumero.grid(row=1, column=5, sticky='NS')

txtMensagem = Entry(main)
txtMensagem.insert(0, 'Digite sua mensagem')
txtMensagem.grid(row=3, column=5, sticky='NS')

btnEnviar = Button(main, text='Enviar', command=EnviarSMS)
btnEnviar.grid(row=5, column=5, sticky='NESW')
main.mainloop()

