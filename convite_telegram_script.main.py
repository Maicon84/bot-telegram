from telethon import TelegramClient, events
import asyncio

# Substitua com suas credenciais
api_id = '21669381'
api_hash = '1117cbf41de2f6b5a4f5bc2244dcb4dd'
phone = '+5511981276707'

# Link do grupo de afiliados
link_do_grupo = 'https://t.me/+KEhuKSbuKwU0ZDZh'

# Inicializa o cliente do Telethon
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)

    # Obtém os grupos que o usuário é membro
    me = await client.get_me()
    print(f"Logado como: {me.username}")

    # Obtém todos os chats/grupos que o usuário participa
    chats = await client.get_dialogs()

    # Filtra para encontrar apenas grupos
    grupos = [chat for chat in chats if chat.is_group]

    print("Grupos encontrados:")
    for grupo in grupos:
        print(f"Grupo encontrado: {grupo.name} (ID: {grupo.id})")
        
    # Define uma função para enviar o convite no grupo
    @client.on(events.NewMessage(chats=[grupo.id for grupo in grupos]))
    async def responder_evento(event):
        try:
            await event.reply(f"Olá! Participe do nosso grupo de descontos: {link_do_grupo}")
            print(f"Convite enviado para {event.chat.title}")
        except Exception as e:
            print(f"Erro ao enviar convite: {e}")

    print("Bot ativo...")
    await client.run_until_disconnected()

# Executa o cliente
asyncio.run(main())
