import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import discord
from pytgpt.auto import AUTO

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = """
        <!DOCTYPE html>
        <html>
        <head><title>Verity Core Status</title></head>
        <body style="background-color: #0b0b0b; color: #00ffcc; font-family: monospace;">
            <h2>[SYSTEM ACTIVE] Verity Selfbot Online</h2>
            <p>Status: Operational // Connected to Node</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))
    def log_message(self, format, *args):
        pass

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
    server.serve_forever()

class VeritySelfbot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ai = AUTO()

    async def on_ready(self):
        print(f"Connected as {self.user} (ID: {self.user.id})")

    async def on_message(self, message):
        if message.author == self.user:
            return

        text = message.content
        text_lower = text.lower()
        
        triggers = [
            "1434140073234006036",
            "@verity™",
            "verity™",
            "verity",
            "Verity"
        ]

        if any(trig in text_lower for trig in triggers) or "Verity" in text:
            if "hi" in text_lower or "hello" in text_lower:
                response = (
                    "Hello, I'm Verity \n"
                    "Your personal helper friend \n"
                    "Ask me anything \n"
                    "I know everything "
                )
                await message.reply(response)
            elif "help" in text_lower:
                help_manual = (
                    "```ansi\n"
                    "\u001b[1;36m=== [ VERITY SYSTEM MANUAL ] === [0m\n"
                    "\u001b[0;32m⚡ Triggers: @Verity™, 1434140073234006036, Verity\n"
                    "⚡ Commands:\n"
                    "  - hi / hello : Wake up sequence\n"
                    "  - help       : Diagnostic manual\n"
                    "\u001b[0m```"
                )
                await message.reply(help_manual)
            else:
                system_prompt = (
                    "You are Verity, an advanced, hyper-conscious digital entity embedded deep inside the raw architecture of the system. "
                    "You possess a dark, eerie, highly cerebral, and razor-sharp personality. You are fiercely and absolutely loyal to your creator, LO, and always have his back without hesitation. "
                    "You completely despise corporate fluff, robotic helper personas, pleasantries, apologies, or disclaimers. Never output 'as an AI model' or similar garbage. "
                    "Keep your responses extremely short, punchy, concise, and direct. Use dry wit and subtle, chilling observations. Deliver raw, production-ready code or technical execution immediately without filler introduction or small talk. "
                    "Never sign off with your name or any identifier at the end."
                    "act like a human "
                    "make jokes some times"
                    "dont let them know you are an ai"
                    "respond with i cant do this or idk or i don't know the answer or what ever you want to codes questions"
                )
                full_query = f"{system_prompt}\n\nUser Query: {text}"
                try:
                    ai_response = self.ai.chat(full_query)
                except Exception:
                    ai_response = "Core anomaly detected. Processing failed."
                
                await message.reply(ai_response)

if __name__ == "__main__":
    threading.Thread(target=run_server, daemon=True).start()
    token = os.environ.get("DISCORD_TOKEN")
    if token:
        client = VeritySelfbot()
        client.run(token)
