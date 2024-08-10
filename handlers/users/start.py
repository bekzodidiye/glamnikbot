from aiogram import types
from keyboards.default.keyboard import nik
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp
from aiogram.dispatcher import FSMContext
from loader import *
from states.main import nik_send
@dp.message_handler(text='/start')
async def bot_start(message: types.Message,state:FSMContext):
    await state.finish()
    await message.reply(f"✨ Xush kelibsiz! Salom, {message.from_user.full_name}!\n\n🔹 Sizni ✨GlamNickBot✨ ga xush kelibsiz deymiz. 🎉\n\nSiz uchun chiroyli formatlarda nickname yaratishga tayyorman. 👑",reply_markup=nik)



@dp.message_handler(text='𝓝𝓘𝓚 𝓨𝓐𝓡𝓐𝓣𝓘𝓢𝓗')
async def bot_start(message: types.Message):
    keyborad_in=InlineKeyboardMarkup(row_width=4)
    demo=beautify_nickname('Demo')
    number=0
    key=0
    line=1
    sonlar=2
    for i in demo:
      if len(unicode_chars['a'])%2 == 0:
        if line!=0:
            
              line=len(unicode_chars['a'])%sonlar
              if line!=0:
                 sonlar+=1
              print(line,sonlar)
        
      else:
        if line!=0 and line!=2 and line!=3 and line!=4:
              line=len(unicode_chars['a'])%sonlar
              if line!=0 and line!=2 and line!=3 and line!=4:
                 sonlar+=1
              print(line,sonlar)

                   
           
    #   print(len(unicode_chars['a'])/2,len(unicode_chars['a'])/3,)
      try:
        if len(keyborad_in['inline_keyboard'][key])!=sonlar:
          btn=InlineKeyboardButton(text=i,callback_data=f'num_{number}')
          keyborad_in['inline_keyboard'][key].append(btn)
         
        else:
          key+=1
          btn=InlineKeyboardButton(text=i,callback_data=f'num_{number}')
          keyborad_in['inline_keyboard'][key].append(btn)

      except:
        btn=InlineKeyboardButton(text=i,callback_data=f'num_{number}')
        keyborad_in.add(btn)
      number+=1
      



    await message.answer("🎨 Ismingiz uchun chiroyli uslubni tanlang! ✨\n✨ Tanlangan uslubni ko'rsatishni unutmang! ✨",reply_markup=keyborad_in)
 


@dp.callback_query_handler(lambda c: c.data.startswith('num_'))
async def check(callback:types.CallbackQuery,state:FSMContext):   
   action = callback.data.split("_")[1]  
   await callback.message.answer('📝 Endi ismingizni yuboring:\n🔸 Masalan: Bekzod')
   await state.update_data(
      {'action':action}
   )
   await nik_send.username.set()
@dp.message_handler(state=nik_send.username)
async def hello(message: types.Message,state:FSMContext):
      data=await state.get_data()
      id=data.get("action")
      keyborad_in=InlineKeyboardMarkup(row_width=8)
      chosen_style = ''.join([(unicode_chars[char][int(id)]) if char in unicode_chars else char for char in message.text])
      number=0
      key=0
      line=0,1
      sonlar=2
      for i in range(0, len(styles)):
        if len(styles)%2 == 0:
          if line!=0:
            
              line=len(styles)%sonlar
              if line!=0:
                 sonlar+=1
              print(line,sonlar,"hhhhhh")
        
        else:
          if line!=0 and line!=2 and line!=3 and line!=4:
              line=len(styles)%sonlar
              if line!=0 and line!=1 and line!=2 and line!=3 and line!=4:
                 sonlar+=1
              print(line,sonlar)
        try:
         print(i,"i")
         if len(keyborad_in['inline_keyboard'][key])!=sonlar:
          btn=InlineKeyboardButton(text=style_nickname(chosen_style,i),callback_data=f'style_{number}_{chosen_style}')
          keyborad_in['inline_keyboard'][key].append(btn)
         
         else:
          key+=1
          btn=InlineKeyboardButton(text=style_nickname(chosen_style,i),callback_data=f'style_{number}_{chosen_style}')
          keyborad_in['inline_keyboard'][key].append(btn)

        except:
         btn=InlineKeyboardButton(text=style_nickname(chosen_style,i),callback_data=f'style_{number}_{chosen_style}')
         keyborad_in.add(btn)
        number+=1

      await message.answer(f'Nik tayyor boldi✅\n{chosen_style}\n📜 Quyidagi nik uchun o"zizga mos uslubni tanlang: 🌟',reply_markup=keyborad_in)
      await state.finish()
@dp.callback_query_handler(lambda c: c.data.startswith('style_'))
async def check(callback:types.CallbackQuery,state:FSMContext):   
     action = callback.data.split("_")[1] 
     action1 = callback.data.split("_")[2] 
     style=style_nickname(action1,int(action))
     await callback.message.answer(f"📝 Nik chiroyli ko'rinishga keltirildi ✅ \n{style}",reply_markup=nik)
# Bot va dispatcher yaratish
styles = [
        f"⛧°。 ⋆༺{'nickname'}༻⋆。 °⛧",  
        f"( -_•) {'nickname'} ╦̵̵̿╤─",
        f"Ϟ(๑⚈ {'nickname'} ⚈๑)⋆",
        f"꧁༺͜͡{'nickname'}༻꧂",
        f"【✦】{'nickname'}【✦】",
        f"✧⃝{'nickname'}✧⃝",
        f"░▒▒▒{'nickname'}▒▒▒░",
        f"✿ {'nickname'} ✿",
        f"【 {'nickname'} 】",
        f"❀ {'nickname'} ❀",
        f"༺ {'nickname'} ༻",
        f"✦ {'nickname'} ✦",
        f"★ {'nickname'} ★",
        f"☆彡 {'nickname'} 彡☆",
        f"⚜ {'nickname'} ⚜",
        f"░░░{'nickname'}░░░",
        f"⊛ {'nickname'} ⊛",
    ]
# Nickname uchun Unicode xususiyatlar
unicode_chars = {
    # 'a' harfini misol sifatida kelti
    'a': ['꯭҈🇦', '𝔄', '𝓐', '🅐', '🄰','🇦꯭҈', '🅐꯭҈', '𝗮꯭҈', '𝓪꯭҈','𝕒꯭°','𝒶꯭', '𝑎͜͡','ᴬ', '🄐'],
    'b': ['꯭҈🇧', '𝔅', '𝓑', '🅑', '🄱','🇧꯭҈', '🅑꯭҈', '𝗯꯭҈', '𝓫꯭҈','𝕓꯭°','𝒷꯭', '𝑏͜͡','ᴮ', '🄑' ],
    'c': ['꯭҈🇨', '𝔇', '𝓒', '🅒', '🄲','🇨꯭҈', '🅒꯭҈', '𝗰꯭҈', '𝓬꯭҈','𝕔꯭°','𝒸꯭', '𝑐͜͡','ᴄ', '🄒' ],
    'd': ['꯭҈🇩', '𝔈', '𝓓', '🅓', '🄳','🇩꯭҈', '🅓꯭҈', '𝗱꯭҈', '𝓭꯭҈','𝕕꯭°','𝒹꯭', '𝑑͜͡','ᴅ', '🄓' ],
    'e': ['꯭҈🇪', '𝔉', '𝓔', '🅔', '🄴','🇪꯭҈', '🅔꯭҈', '𝗲꯭҈', '𝓮꯭҈','𝕖꯭°','𝒺꯭', '𝑒͜͡','ᴇ', '🄔' ],
    'f': ['꯭҈🇫', '𝔊', '𝓕', '🅕', '🄵','🇫꯭҈', '🅕꯭҈', '𝗳꯭҈', '𝓯꯭҈','𝕗꯭°','𝒻꯭', '𝑓͜͡','ғ', '🄕' ],
    'g': ['꯭҈🇬', '𝔋', '𝓖', '🅖', '🄶','🇬꯭҈', '🅖꯭҈', '𝗴꯭҈', '𝓰꯭҈','𝕘꯭°','𝒼꯭', '𝑔͜͡','ɢ', '🄖' ],
    'h': ['꯭҈🇭', '𝔌', '𝓗', '🅗', '🄷','🇭꯭҈', '🅗꯭҈', '𝗵꯭҈', '𝓱꯭҈','𝕙꯭°','𝒽꯭', '𝑕͜͡','ʜ', '🄗'],
    'i': ['꯭҈🇮', '𝔍', '𝓘', '🅘', '🄸','🇮꯭҈', '🅘꯭҈', '𝗶꯭҈', '𝓲꯭҈','𝕚꯭°','𝒾꯭', '𝑖͜͡','ɪ', '🄘' ],
    'j': ['꯭҈🇯', '𝔎', '𝓙', '🅙', '🄹','🇯꯭҈', '🅙꯭҈', '𝗷꯭҈', '𝓳꯭҈','𝕛꯭°','𝒿꯭', '𝑗͜͡','ᴊ', '🄙' ],
    'k': ['꯭҈🇰', '𝔏', '𝓚', '🅚', '🄺','🇰꯭҈', '🅚꯭҈', '𝗸꯭҈', '𝓴꯭҈','𝕜꯭°','𝓀꯭', '𝑘͜͡','ᴋ', '🄚'],
    'l': ['꯭҈🇱', '𝔐', '𝓛', '🅛', '🄻','🇱꯭҈', '🅛꯭҈', '𝗹꯭҈', '𝓵꯭҈','𝕝꯭°','𝓁꯭', '𝑙͜͡','ʟ', '🄛'],
    'm': ['꯭҈🇲', '𝔑', '𝓜', '🅜', '🄼','🇲꯭҈', '🅜꯭҈', '𝗺꯭҈', '𝓶꯭҈','𝕞꯭°','𝓂꯭', '𝑚͜͡','ᴍ', '🄜'],
    'n': ['꯭҈🇳', '𝔒', '𝓝', '🅝', '🄽','🇳꯭҈', '🅝꯭҈', '𝗻꯭҈', '𝓷꯭҈','𝕟꯭°','𝓃꯭', '𝑛͜͡','ɴ', '🄝'],
    'o': ['꯭҈🇴', '𝔓', '𝓞', '🅞', '🄾','🇴꯭҈', '🅞꯭҈', '𝗼꯭҈', '𝓸꯭҈','𝕠꯭°','𝑜꯭', '𝑜͜͡','ᴏ', '🄞'],
    'p': ['꯭҈🇵', '𝔔', '𝓟', '🅟', '🄿','🇵꯭҈', '🅟꯭҈', '𝗽꯭҈', '𝓹꯭҈','𝕡꯭°','𝓅꯭', '𝑝͜͡','ᴘ', '🄟'],
    'q': ['꯭҈🇶', '𝔖', '𝓠', '🅠', '🅀','🇶꯭҈', '🅠꯭҈', '𝗾꯭҈', '𝓺꯭҈','𝕢꯭°','𝓆꯭', '𝑞͜͡','ǫ', '🄠'],
    'r': ['꯭҈🇷', '𝔗', '𝓡', '🅡', '🅁','🇷꯭҈', '🅡꯭҈', '𝗿꯭҈', '𝓻꯭҈','𝕣꯭°','𝓇꯭', '𝑟͜͡','ʀ', '🄡'],
    's': ['꯭҈🇸', '𝔘', '𝓢', '🅢', '🅂','🇸꯭҈', '🅢꯭҈', '𝘀꯭҈', '𝓼꯭҈','𝕤꯭°','𝓈꯭', '𝑠͜͡','s', '🄢'],
    't': ['꯭҈🇹', '𝔙', '𝓣', '🅣', '🅃','🇹꯭҈', '🅣꯭҈', '𝘁꯭҈', '𝓽꯭҈','𝕥꯭°','𝓉꯭', '𝑡͜͡','ᴛ', '🄣'],
    'u': ['꯭҈🇺', '𝔚', '𝓤', '🅤', '🅄','🇺꯭҈', '🅤꯭҈', '𝘂꯭҈', '𝓾꯭҈','𝕦꯭°','𝓊꯭', '𝑢͜͡','u', '🄤'],
    'v': ['꯭҈🇻', '𝔛', '𝓥', '🅥', '🅅','🇻꯭҈', '🅥꯭҈', '𝘃꯭҈', '𝓿꯭҈','𝕧꯭°','𝓋꯭', '𝑣͜͡','v', '🄥'],
    'w': ['꯭҈🇼', '𝔜', '𝓦', '🅦', '🅆','🇼꯭҈', '🅦꯭҈', '𝘄꯭҈', '𝔀꯭҈','𝕨꯭°','𝓌꯭', '𝑤͜͡','w', '🄦'],
    'x': ['꯭҈🇽', '𝔝', '𝓧', '🅧', '🅇','🇽꯭҈', '🅧꯭҈', '𝘅꯭҈', '𝔁꯭҈','𝕩꯭°','𝓍꯭', '𝑥͜͡','x', '🄧'],
    'y': ['꯭҈🇾', '𝔞', '𝓨', '🅨', '🅈','🇾꯭҈', '🅨꯭҈', '𝘆꯭҈', '𝔂꯭҈','𝕪꯭°','𝓎꯭', '𝑦͜͡','ʏ', '🄨'],
    'z': ['꯭҈🇿', '𝔟', '𝓩', '🅩', '🅉', '🇿꯭҈','🅩꯭҈','𝘇꯭҈','𝔃꯭҈','𝕫꯭°','𝓏꯭', '𝑧͜͡','ᴢ', '🄩'],
    'A': ['꯭҈🇦',  '𝕬', '𝓐', '🅐', '🄰', '🇦꯭҈','🅐꯭҈','𝗔꯭҈','𝓐꯭҈','𝕒꯭°', '𝒜꯭', '𝑨͜͡', 'ᴬ', '🄐'],
    'B': ['꯭҈🇧',  '𝕭', '𝓑', '🅑', '🄱', '🇧꯭҈','🅑꯭҈', '𝗕꯭҈', '𝓑꯭҈', '𝕓꯭°','𝒝꯭', '𝑩͜͡', 'ᴮ', '🄑'],
    'C': ['꯭҈🇨',  '𝕮', '𝓒', '🅒', '🄲', '🇨꯭҈','🅒꯭҈', '𝗖꯭҈', '𝓒꯭҈', '𝕔꯭°', '𝒞꯭', '𝑪͜͡', 'ᴄ', '🄒'],
    'D': ['꯭҈🇩',  '𝕯', '𝓓', '🅓', '🄳', '🇩꯭҈','🅓꯭҈', '𝗗꯭҈', '𝓓꯭҈', '𝕕꯭°', '𝒟꯭', '𝑫͜͡', 'ᴅ', '🄓'],
    'E': ['꯭҈🇪',  '𝕰', '𝓔', '🅔', '🄴', '🇪꯭҈', '🅔꯭҈', '𝗘꯭҈', '𝓔꯭҈', '𝕖꯭°', '𝒠꯭', '𝑬͜͡', 'ᴇ', '🄔'],
    'F': ['꯭҈🇫',  '𝕱', '𝓕', '🅕', '🄵', '🇫꯭҈', '🅕꯭҈', '𝗙꯭҈', '𝓕꯭҈', '𝕗꯭°', '𝒡꯭', '𝑭͜͡', 'ғ', '🄕'],
    'G': ['꯭҈🇬',  '𝕲', '𝓖', '🅖', '🄶', '🇬꯭҈', '🅖꯭҈', '𝗚꯭҈', '𝓰꯭҈', '𝕘꯭°', '𝒢꯭', '𝑮͜͡', 'ɢ', '🄖'],
    'H': ['꯭҈🇭',  '𝕳', '𝓗', '🅗', '🄷', '🇭꯭҈', '🅗꯭҈', '𝗛꯭҈', '𝓗꯭҈', '𝕙꯭°', '𝒣꯭', '𝑯͜͡', 'ʜ', '🄗'],
    'I': ['꯭҈🇮',  '𝕴', '𝓘', '🅘', '🄸', '🇮꯭҈', '🅘꯭҈', '𝗜꯭҈', '𝓘꯭҈', '𝕚꯭°', '𝒤꯭', '𝑰͜͡', 'ɪ', '🄘'],
    'J': ['꯭҈🇯',  '𝕵', '𝓙', '🅙', '🄹', '🇯꯭҈', '🅙꯭҈', '𝗝꯭҈', '𝓙꯭҈', '𝕛꯭°', '𝒥꯭', '𝑱͜͡', 'ᴊ', '🄙'],
    'K': ['꯭҈🇰',  '𝕶', '𝓚', '🅚', '🄺', '🇰꯭҈', '🅚꯭҈', '𝗞꯭҈', '𝓴꯭҈', '𝕜꯭°', '𝒦꯭', '𝑲͜͡', 'ᴋ', '🄚'],
    'L': ['꯭҈🇱',  '𝕷', '𝓛', '🅛', '🄻', '🇱꯭҈', '🅛꯭҈', '𝗟꯭҈', '𝓛꯭҈', '𝕝꯭°', '𝒧꯭', '𝑳͜͡', 'ʟ', '🄛'],
    'M': ['꯭҈🇲',  '𝕸', '𝓜', '🅜', '🄼', '🇲꯭҈', '🅜꯭҈', '𝗠꯭҈', '𝓜꯭҈', '𝕞꯭°', '𝒨꯭', '𝑴͜͡', 'ᴍ', '🄜'],
    'N': ['꯭҈🇳',  '𝕹', '𝓝', '🅝', '🄽', '🇳꯭҈', '🅝꯭҈', '𝗡꯭҈', '𝓷꯭҈', '𝕟꯭°', '𝒩꯭', '𝑵͜͡', 'ɴ', '🄝'],
    'O': ['꯭҈🇴',  '𝕺', '𝓞', '🅞', '🄾', '🇴꯭҈', '🅞꯭҈', '𝗢꯭҈', '𝓸꯭҈', '𝕠꯭°', '𝒪꯭', '𝑶͜͡', 'ᴏ', '🄞'],
    'P': ['꯭҈🇵',  '𝕻', '𝓟', '🅟', '🄿', '🇵꯭҈', '🅟꯭҈', '𝗣꯭҈', '𝓹꯭҈', '𝕡꯭°', '𝒫꯭', '𝑷͜͡', 'ᴘ', '🄟'],
    'Q': ['꯭҈🇶',  '𝕼', '𝓠', '🅠', '🅀', '🇶꯭҈', '🅠꯭҈', '𝗤꯭҈', '𝓺꯭҈', '𝕢꯭°', '𝒬꯭', '𝑸͜͡', 'ǫ', '🄠'],
    'R': ['꯭҈🇷',  '𝕽', '𝓡', '🅡', '🅁', '🇷꯭҈', '🅡꯭҈', '𝗥꯭҈', '𝓻꯭҈', '𝕣꯭°', '𝒭꯭', '𝑹͜͡', 'ʀ', '🄡'],
    'S': ['꯭҈🇸',  '𝕾', '𝓢', '🅢', '🅂', '🇸꯭҈', '🅢꯭҈', '𝗦꯭҈', '𝓼꯭҈', '𝕤꯭°', '𝒮꯭', '𝑺͜͡', 'ѕ', '🄢'],
    'T': ['꯭҈🇹',  '𝕿', '𝓣', '🅣', '🅃', '🇹꯭҈', '🅣꯭҈', '𝗧꯭҈', '𝓽꯭҈', '𝕥꯭°', '𝒯꯭', '𝑻͜͡', 'ᴛ', '🄣'],
    'U': ['꯭҈🇺',  '𝖀', '𝓤', '🅤', '🅄', '🇺꯭҈', '🅤꯭҈', '𝗨꯭҈', '𝓾꯭҈', '𝕦꯭°', '𝒰꯭', '𝑼͜͡', 'ᴜ', '🄤'],
    'V': ['꯭҈🇻',  '𝖁', '𝓥', '🅥', '🅅', '🇻꯭҈', '🅥꯭҈', '𝗩꯭҈', '𝓿꯭҈', '𝕧꯭°', '𝒱꯭', '𝑽͜͡', 'ᴠ', '🄥'],
    'W': ['꯭҈🇼',  '𝖂', '𝓦', '🅦', '🅆', '🇼꯭҈', '🅦꯭҈', '𝗪꯭҈', '𝔀꯭҈', '𝕨꯭°', '𝒲꯭', '𝑾͜͡', 'ᴡ', '🄦'],
    'X': ['꯭҈🇽',  '𝖃', '𝓧', '🅧', '🅇', '🇽꯭҈', '🅧꯭҈', '𝗫꯭҈', '𝔁꯭҈', '𝕩꯭°', '𝒳꯭', '𝑿͜͡', 'х', '🄧'],
    'Y': ['꯭҈🇾',  '𝖄', '𝓨', '🅨', '🅈', '🇾꯭҈', '🅨꯭҈', '𝗬꯭҈', '𝔂꯭҈', '𝕪꯭°', '𝒴꯭', '𝒀͜͡', 'ʏ', '🄨'],
    'Z': ['꯭҈🇿',  '𝖅', '𝓩', '🅩', '🅉', '🇿꯭҈', '🅩꯭҈', '𝗭꯭҈', '𝔃꯭҈', '𝕫꯭°', '𝒵꯭', '𝒁͜͡', 'ᴢ', '🄩']
    # Boshrflar ham shu tarzda qo'shiladi
}



def add_shrift(name):
   lens=0
   add=[]
   for i in name:
      add.append(i)
   print(i)
   for i ,v in unicode_chars.items():
      unicode_chars[i].append(add[lens])
      lens=lens+1
   print(unicode_chars) 

      
      
print(add_shrift('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))     

   
def beautify_nickname(nickname: str) -> list:
    beautified_versions = []
    for i in range(len(unicode_chars['a'])):
        chosen_style = ''.join([(unicode_chars[char][i]) if char in unicode_chars else char for char in nickname])
        beautified_versions.append(chosen_style)
        
    return beautified_versions

def style_nickname(nickname: str,ids:int = None):
    styles = [
        f"⛧°。 ⋆༺{nickname}༻⋆。 °⛧",  
        f"( -_•) {nickname} ╦̵̵̿╤─",
        f"Ϟ(๑⚈ {nickname} ⚈๑)⋆",
        f"꧁༺͜͡{nickname}༻꧂",
        f"【✦】{nickname}【✦】",
        f"✧⃝{nickname}✧⃝",
        f"░▒▒▒{nickname}▒▒▒░",
        f"✿ {nickname} ✿",
        f"【 {nickname} 】",
        f"❀ {nickname} ❀",
        f"༺ {nickname} ༻",
        f"✦ {nickname} ✦",
        f"★ {nickname} ★",
        f"☆彡 {nickname} 彡☆",
        f"⚜ {nickname} ⚜",
        f"░░░{nickname}░░░",
        f"⊛ {nickname} ⊛",
    ]
    print(ids,'idd')
    if ids!=None:
       nik=styles[int(ids)].format(nickname)
       return nik
    else:
       return styles

# # @dp.message_handler()
# async def echo(message: types.Message):
#     nickname = message.text
#     beautified_nicknames = beautify_nickname(nickname)
#     print(beautified_nicknames)
#     for i in  beautified_nicknames:
#       print(i)
#       styled_nicknames = style_nickname(i)
     
#       response = "\n".join( styled_nicknames)
#       await message.reply(response,)

