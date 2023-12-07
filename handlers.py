from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message

from library import Form, Strings, bot
from functions import functions

from PIL import ImageFilter, ImageOps, ImageEnhance

router = Router()

@router.message(Command("start"))
async def start(message: Message, state):
    await message.answer(text=Strings.start)
    await state.set_state(Form.main)

@router.message(Form.main, Command("help"))
async def help(message: Message, state):
    await message.answer(text=Strings.help)

@router.message(Form.main, Command("get"))
async def get_photo(message: Message, state):
    await message.answer(text="Пришлите изображение для редактирования.")
    await state.set_state(Form.getimage)

@router.message(Form.getimage)
async def get_photo_main(message: Message, state):
    photos = message.photo
    if(photos!=None):
        userid = message.from_user.id
        path = functions.getpath(userid)
        photo = photos[2]
        file = await bot.get_file(photo.file_id)
        await bot.download_file(file.file_path,path)
        await state.set_state(Form.main)
        await message.answer(text="Изображение успешно получено!\nТеперь можно использовать команды из /help")
    else:
        await message.answer(text="Неправильный формат")

@router.message(Form.main, Command("resize"))
async def resize(message: Message, state):
    userid = message.from_user.id
    size = functions.getphoto(userid).size
    await message.answer(text=f"Напишите новый размер изображения через пробел. Текущий размер: {size[0]} {size[1]}")
    await state.set_state(Form.resizearg)

@router.message(Form.resizearg)
async def resize_main(message: Message, state):
    userid = message.from_user.id
    photo = functions.getphoto(userid)
    sizeget = tuple(map(int,message.text.split()))
    try:
        changed = photo.resize(sizeget)
        functions.saveimg(changed,userid)
        await functions.sendphoto(message,userid,bot)
        await state.set_state(Form.main)
    except:
        await message.answer(text="Формат неправилен.")

@router.message(Form.main, Command("discolor"))
async def discolor(message: Message):
    userid = message.from_user.id
    photo = functions.getphoto(userid)
    changed = photo.convert("L")
    functions.saveimg(changed,userid)
    await functions.sendphoto(message,userid,bot)

@router.message(Form.main, Command("blur"))
async def discolor(message: Message):
    userid = message.from_user.id
    photo = functions.getphoto(userid)
    changed = photo.filter(ImageFilter.BLUR)
    functions.saveimg(changed,userid)
    await functions.sendphoto(message,userid,bot)

@router.message(Form.main, Command("reverse"))
async def reverse(message: Message):
    userid = message.from_user.id
    photo = functions.getphoto(userid)
    changed = ImageOps.invert(photo)
    functions.saveimg(changed,userid)
    await functions.sendphoto(message,userid,bot)

@router.message(Form.main, Command("edges"))
async def edges(message: Message):
    userid = message.from_user.id
    photo = functions.getphoto(userid)
    changed = photo.filter(ImageFilter.FIND_EDGES)
    functions.saveimg(changed,userid)
    await functions.sendphoto(message,userid,bot)

@router.message(Form.main, Command("sharpen"))
async def smooth(message: Message, state):
    await message.answer(text=f"Напишите насколько хотите увеличить резкость от 1 до 15.")
    await state.set_state(Form.sharpenarg)

@router.message(Form.sharpenarg)
async def rotatemain(message: Message, state):
    cin = message.text
    cint = 0
    userid = message.from_user.id
    photo = functions.getphoto(userid)
    try:
        cint = int(cin)
        if(cint<0 or cint>15):
            await message.answer(text="Неправильный формат")
        else:
            for _ in range(0,cint+1):
                changed = photo.filter(ImageFilter.SHARPEN)
                functions.saveimg(changed,userid)
            await functions.sendphoto(message,userid,bot)
            await state.set_state(Form.main)
    except:
        await message.answer(text="Неправильный формат")

@router.message(Form.main, Command("rotate"))
async def rotate(message: Message, state):
    await message.answer(text=f"Напишите угол поворота числом.")
    await state.set_state(Form.rotatearg)

@router.message(Form.rotatearg)
async def rotatemain(message: Message, state):
    cin = message.text
    userid = message.from_user.id
    photo = functions.getphoto(userid)
    try:
        cint = int(cin)
        changed = photo.rotate(cint)
        functions.saveimg(changed,userid)
        await functions.sendphoto(message,userid,bot)
        await state.set_state(Form.main)
    except:
        await message.answer(text="Неправильный формат")
    
@router.message(Form.main, Command("bright"))
async def bright(message: Message, state):
    await message.answer(text=f"Напишите насколько затемнить изображение от 1 до 100.")
    await state.set_state(Form.brightarg)

@router.message(Form.brightarg)
async def bright2(message: Message, state):
    cin = message.text
    userid = message.from_user.id
    photo = functions.getphoto(userid)
    try:
        cint = int(cin)
        if(cint<0 or cint>100):
            await message.answer(text="Неправильный формат")
        else:
            cfloat = (100-cint)/100
            enhancer = ImageEnhance.Brightness(photo)
            changed = enhancer.enhance(cfloat)
            functions.saveimg(changed,userid)
            await functions.sendphoto(message,userid,bot)
            await state.set_state(Form.main)
    except:
        await message.answer(text="Неправильный формат")

@router.message(Form.main, Command("contrast"))
async def contrast(message: Message, state):
    await message.answer(text=f"Напишите насколько повысить контраст изображение от 1 до 100.")
    await state.set_state(Form.contrastarg)

@router.message(Form.contrastarg)
async def contrast2(message: Message, state):
    cin = message.text
    userid = message.from_user.id
    photo = functions.getphoto(userid)
    try:
        cint = int(cin)
        if(cint<0 or cint>100):
            await message.answer(text="Неправильный формат")
        else:
            cint += 200
            cfloat = (100-cint)/100*-1
            enhancer = ImageEnhance.Contrast(photo)
            changed = enhancer.enhance(cfloat)
            functions.saveimg(changed,userid)
            await functions.sendphoto(message,userid,bot)
            await state.set_state(Form.main)
    except:
        await message.answer(text="Неправильный формат")