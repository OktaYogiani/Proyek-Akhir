import discord
import random
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

quiz_list=[{"question": "Mengapa suhu Bumi tidak naik secara perlahan, tapi kadang terasa makin cepat?", "options": ["A. Karena Matahari makin panas tiap tahun", "B. Karena perubahan di alam bisa saling memperkuat", "C. Karena manusia tinggal lebih dekat ke kota"], "answer": "B"},
           {"question": "Mengapa lautan dianggap paling “menyimpan” dampak pemanasan Bumi?", "options": ["A. Karena lautan sangat luas dan menyerap panas", "B. Karena lautan selalu dingin", "C. Karena lautan memantulkan cahaya Matahari"], "answer": "A"},
           {'question': "Pernyataan mana yang paling tepat", "options": ["A. Semua bencana alam terjadi karena perubahan iklim", 'B. Perubahan iklim membuat bencana lebih mudah terjadi', 'C. Perubahan iklim tidak berhubungan dengan bencana'], "answer": "B"},
           {'question': "Mengapa es di daerah kutub penting walau jauh dari kehidupan manusia?", "options": ["A. Karena jadi cadangan air minum", "B. Karena membantu memantulkan panas Matahari", "C. Karena mencegah gempa bumi"], "answer": 'B'},
           {"question": "Mengapa perubahan iklim sering terasa berbeda di tiap daerah?", "options":["A. Karena setiap wilayah punya kondisi alam berbeda", "B. Karena data cuaca tidak akurat", "C. Karena perubahan iklim hanya terjadi di tempat tertentu"], "answer": "A"},
           {"question": "Mengapa daerah miskin sering lebih terdampak perubahan iklim?", "options":["A. Karena wilayahnya selalu panas", "B. Karena lebih bergantung pada alam dan minim perlindungan", "C. Karena populasinya lebih besar"], "answer": "B"},
           {"question": "Mengapa perubahan iklim sering dianggap masalah masa depan padahal dampaknya sudah terasa?", "options":["A. Karena manusia cenderung meremehkan perubahan lambat", "B. Karena dampaknya baru muncul seratus tahun lagi","C. Karena media tidak membahasnya"], "answer": "A"}]

funfact_list=["Hujan makin deres bukan karena hujannya lebih rajin, tapi karena udara sekarang bisa “nampung” air lebih banyak.", 
          'Cuaca dingin hari ini nggak berarti pemanasan global bohong, sama kayak satu hari malas nggak bikin kamu gagal hidup.',
          'Tempat yang paling sedikit bikin masalah iklim sering jadi yang paling dulu kena dampaknya.',
          'Menunda ngurus perubahan iklim itu kayak nunda ke dokter—makin lama, makin mahal dan ribet.',
          'Perubahan iklim itu nggak nunggu semua orang siap, dia jalan terus.',
          "Laut itu penampung panas terbesar di dunia, makanya kita sering nggak sadar masalahnya sampai telat.",
          'Perubahan iklim itu kayak volume musik yang dinaikin dikit-dikit, sadar pas telinga udah sakit.',
          "Laut tuh kayak tabungan panas, kelihatannya aman sampai isinya tumpah.",
          'Tanam pohon penting, tapi kalau polusinya jalan terus, itu kayak ngepel lantai sambil bocor.',
          'Yang bikin perubahan iklim bahaya bukan karena dramatis, tapi karena pelan dan kelihatannya “biasa aja”.']

materi_list = ["Perubahan iklim adalah perubahan pola cuaca yang terjadi dalam waktu lama, bukan cuma hujan atau panas sesaat.",
    "Masalah utama perubahan iklim muncul karena aktivitas manusia yang bikin panas Bumi terjebak.",
    "Cuaca yang makin nggak bisa ditebak adalah salah satu tanda perubahan iklim.",
    "Laut menyerap banyak panas, makanya dampak perubahan iklim sering terasa terlambat.",
    "Es di kutub penting karena membantu memantulkan panas Matahari.",
    "Kalau es mencair, panas lebih banyak diserap dan Bumi makin cepat panas.",
    "Perubahan iklim bikin masalah lama seperti banjir dan kekeringan jadi lebih parah.",
    "Daerah yang paling sedikit menyumbang masalah sering jadi yang paling terdampak.",
    "Menanam pohon penting, tapi tidak cukup kalau polusi terus berjalan.",
    "Menghadapi perubahan iklim butuh perubahan kebiasaan dan sistem besar, bukan satu aksi saja."]

@bot.event
async def on_ready():
    print(f'Bot {bot.user} is online!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! Aku bot {bot.user}! \n \n'
                   "\n Ketik !menu untuk melihat layanan yang tersedia disini!")

@bot.command()
async def menu(ctx):
    await ctx.send(
        "Pilih menu:\n"
        "1. Materi Perubahan Iklim\n"
        "2. Fun Fact\n"
        "3. Quiz\n\n"
        "Ketik angka 1 / 2 / 3"
    )
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content in ['1','2','3']
    try:
        msg = await bot.wait_for("message", check=check, timeout=20.0)
    except:
        await ctx.send("Kamu kelamaan, ketik `!menu` lagi ya.")
        return
    if msg.content == '1':
        await materi(ctx)
    elif msg.content == '2':
        await funfact(ctx)
    elif msg.content == '3':
        await quiz(ctx)

@bot.command(name='quiz')
async def quiz(ctx):
    q=random.choice(quiz_list)
    question_text = f"{q['question']}\n" + "\n".join(q["options"]) + "\n\nKetik jawabanmu! (A/B/C/D)"
    await ctx.send(question_text)
    def check(m):
        return m.author==ctx.author and m.channel==ctx.channel and m.content.upper() in ['A', 'B', 'C', 'D']
    
    try:
        msg= await bot.wait_for("message", check=check, timeout=20.0)
    except:
        await ctx.send("Waktu anda habis!" + "\n\nCoba lagi dengan '!quiz'.")
        return 

    if msg.content.upper()==q["answer"]:
        await ctx.send("Jawabanmu benar!")
        await asyncio.sleep(4)
        await ctx.send("\n\nMau quiz lagi?\n"
                       "Ketik 1 untuk mau dan 2 untuk balik ke menu!")
        if msg.content == '1':
            await quiz(ctx)
        elif msg.content == '2':
            await menu(ctx)
    else:
        await ctx.send(f"Jawabanmu masih belum benar. Jawaban yang benar adalah {q['answer']}")
        await ctx.send("\n\nMau quiz lagi?\n"
                       "Ketik 1 untuk mau dan 2 untuk balik ke menu!")
        if msg.content == '1':
            await quiz(ctx)
        elif msg.content == '2':
            await menu(ctx)

@bot.command(name='funfact')
async def funfact(ctx):
    fact = random.choice(funfact_list)
    await ctx.send(f"Fun Fact:\n{fact}\n\n")
    await asyncio.sleep(4)
    await ctx.send("\n\nMau fun fact lagi?\n"
        "Ketik Y untuk lanjut, N untuk berhenti")

    def check(m):
        return (
            m.author == ctx.author and
            m.channel == ctx.channel and
            m.content.upper() in ['Y', 'N']
        )

    try:
        msg = await bot.wait_for("message", check=check, timeout=20.0)
    except:
        await ctx.send("Waktu habis! Ketik `!funfact` kalau mau lanjut.")
        return

    if msg.content.upper() == 'Y':
        await funfact(ctx)
    else:
        await ctx.send("Oke! Ketik `!menu` kalau mau pilih yang lain!")

@bot.command(name= 'materi')
async def materi(ctx):
    for materi in materi_list:
        await ctx.send(materi)
        await asyncio.sleep(4)
    await ctx.send(
        "\n\n Materi sudah selesai. Kamu mau pilih layanan yang mana lagi?\n"
        "1. Fun Fact\n"
        "2. Quiz\n\n"
        "Ketik angka 1 / 2"
    )
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content in ['1','2']
    try:
        msg = await bot.wait_for("message", check=check, timeout=20.0)
    except:
        await ctx.send("Kamu kelamaan, ketik `!menu` lagi ya.")
        return
    if msg.content == '1':
        await funfact(ctx)
    elif msg.content == '2':
        await quiz(ctx)

bot.run("KODEBOT")
