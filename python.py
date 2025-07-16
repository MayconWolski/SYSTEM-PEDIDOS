from twilio.rest import Client

# Suas credenciais do Twilio
account_sid = "AC091a40eab207927b2c09c977f0d72296"
auth_token = "1ec162e3ae3ba99b56eacb011a90cb4b"
client = Client(account_sid, auth_token)

# Criando e enviando a mensagem
message = client.messages.create(
    from_="whatsapp:+14155238886",  # Sempre este número para o Twilio WhatsApp
    body="Olá, esta é uma mensagem de teste via Twilio!",
    to="whatsapp:+5511964943379"  # Seu número com DDI +55 (Brasil)
)

# Exibindo o SID da mensagem enviada
print("Mensagem enviada com sucesso! SID:", message.sid)
