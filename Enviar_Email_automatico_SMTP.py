import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Olá!</p>
    <p>Mensagem automatica</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'seuemail@gmail.com'
    msg['To'] = 'email_destinatário '
    password = 'suasenha' #Chave app autenticação.
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

# Enviar email
enviar_email()