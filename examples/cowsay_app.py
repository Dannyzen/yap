import asyncio
from fast_voice.client.core import VoiceClient

def cowsay(text):
    cow = r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
    """
    lines = []
    width = 40
    for i in range(0, len(text), width):
        lines.append(text[i:i+width])
    
    formatted_text = "\n".join(lines)
    top_bar = "_" * (min(len(text), width) + 2)
    bottom_bar = "-" * (min(len(text), width) + 2)
    
    print(f" {top_bar}")
    for line in lines:
        print(f"< {line} >")
    print(f" {bottom_bar}")
    print(cow)

async def main():
    client = VoiceClient()
    
    def on_transcribed(text):
        cowsay(text or "Moo? (No speech detected)")
        
    try:
        # Run for 10 seconds
        await client.run(duration=10, on_transcription=None, on_live_update=on_transcribed)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    asyncio.run(main())
