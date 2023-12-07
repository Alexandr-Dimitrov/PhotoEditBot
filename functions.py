from PIL import Image
from aiogram.types import FSInputFile

class functions:

    def getpath(userid):
        return f"saved\{str(userid)}.png"
    
    def getphoto(userid):
        return Image.open(functions.getpath(userid))
    
    def saveimg(img,userid):
        img.save(functions.getpath(userid))

    def sendphoto(message,userid,bot):
        path = functions.getpath(userid)
        photo = FSInputFile(path)
        return bot.send_photo(chat_id=message.chat.id, photo=photo)