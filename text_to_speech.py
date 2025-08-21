from gtts import gTTS
import asyncio 
import edge_tts
from playsound import playsound
import pyttsx3


## gtts
def google(text,leng='en',filename="google_gttx.mp3"):
    tts = gTTS(text=text,lang='en',slow=False)
    tts.save(filename)
    print(f"File save as {filename}")
    playsound(filename)

# Edge 
def eDge(text,voice="zh-CN-XiaoxiaoNeural",filename = "edge_tts.mp3"):
    async def main():
        say = edge_tts.Communicate(text,voice)
        await say.save(filename)
        print(f"File save as name {filename}")
        playsound(filename)

    asyncio.run(main())

    

# pyttsx
def pyttsx3_tts(text, voice=None, rate=150, volume=1.0):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")

    if voice is not None and voice < len(voices):
        engine.setProperty("voice", voices[voice].id)

    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)

    print("[pyttsx3] Speaking...")
    engine.say(text)
    engine.runAndWait()


def main():
    print("===Enter the speech Project ===")
    text = input("Enter the text to convert into voice: ")

    print("\n Enter engin")
    print("1. Google gtts")
    print("2 Microsoft edge TTS")
    print("3 pyttx3")
    choose = int(input("\nEnter your choice from 1-3: "))

    if choose==1:
        google(text)

    elif choose ==2:
        eDge(text)
        
    elif choose ==3:
        print("\n Available voice depend on your system.")
        pyttsx3_tts(text,voice=0)

    else:
        print("Invaild choice>>>>>>>")


if __name__ == "__main__":
    main()