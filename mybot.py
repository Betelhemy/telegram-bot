from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Replace with your GitHub repo URL
GITHUB_REPO_URL = "https://github.com/MahiAlex38/C-Modular-programming"

# Define the command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Use /repo to get the GitHub link.")

async def repo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Here is the GitHub repository:\n{GITHUB_REPO_URL}")

# Start the bot
if __name__ == '__main__':
    TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("repo", repo))

    print("Bot is running...")
    app.run_polling()