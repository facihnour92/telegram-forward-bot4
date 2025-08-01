import os
from pyrogram import Client, filters

api_id = int(os.environ["20582592"])
api_hash = os.environ["929cf7d1c62dd06032b6da5fc44e2dce"]
session_string = os.environ["BAE6EMAAS94PnnYjA9wOh_jl75GZhLofSRxurxQrNhDm2p2G-WC1L9oNY97MtUibgTxuH8wVtRwufknbJAGzE5AZFGdDNc8jIEyVpdF6S2Kr2PkZkoHiyKGreOFD39ScVjTqLBTLpwo-MUEpHSE7GKSyIVRNpiBGgJPdqgjqIsQzDFOooE-IXgWXSxKp6Kw0GYrpgW122sVD53sWoPxDuNVMUGO35VkbilMSqn6_MHKTASqhPASS-jM4bWSSgrdKHdbM9EbLCeEF1GxUF93a5owREkxz1Y3LT7tQLBftVLi9ECod11eqVr6xhkpfA7B5R7QGDA8Pnw1WnUIsa0mXmGeGaPMPXAAAAAAxxfmyAA"]
from_chat_id = int(os.environ["-1002047448150"])
to_chat_id = int(os.environ["5875342149"])

app = Client(
    session_string=session_string,
    api_id=api_id,
    api_hash=api_hash
)

@app.on_message(filters.chat(from_chat_id))
async def forward_message(client, message):
    try:
        await message.forward(to_chat_id)
        print(f"✅ Message forwarded from {from_chat_id} to {to_chat_id}")
    except Exception as e:
        print(f"❌ Failed to forward message: {e}")

app.run()