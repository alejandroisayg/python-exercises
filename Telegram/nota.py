from telegram import Update

from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "7954486028:AAHPizzSI4Zax8fcw8BHGMxeQ6P5mvsFY28" 

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    
    if texto.startswith("alex"):
        contenido = texto.replace("alex", "").strip()

        with open("notas.txt", "w") as archivo:
            archivo.write(contenido)

        await update.message.reply_text("Nota guardada exitosamente Alex.")
    else:
        await update.message.reply_text("Por favor, comienza tu mensaje con 'alex' para guardar una nota.") 
        
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, responder))

app.run_polling()