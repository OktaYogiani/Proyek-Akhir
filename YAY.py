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

video_list=[
    {"title": "TERNYATA!!! PERUBAHAN IKLIM ITU....?",
    "url": "https://youtu.be/29jyaPIWzFI?si=jaQJ1pGae4DbSApM",
    "thumbnail": "data:image/jpeg;base64,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",
    "description": "Penjelasan singkat dan mudah dipahami untuk memahami apa itu perubahan iklim."},
    {"title": "Yuk Ketahui Pentingnya Perubahan Iklim!",
    "url": "https://youtu.be/kyqy6XiqWx4?si=LRM9BN7D_NeTYug_",
    "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-zlPf60w3LcM2bhgI7RBjNR2xEAKQl1ln9g&s",
    "description": "Animasi Kartun Explainer Perubahan Iklim yang mudah dimengerti."},
    {"tittle": "Apa Dampak Nyata Perubahan Iklim Saat Ini?",
    "url": "https://youtu.be/flNmZ1Mw464?si=BtxqaNcWwmxUUzTK",
    "description": "Penjelasan mengenai dampak Perubahan Iklim",
    "thumbnail": "data:image/jpeg;base64,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"
    }]

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
        msg = await bot.wait_for("message", check=check, timeout=10.0)
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
    else:
        await ctx.send(f"Jawabanmu masih belum benar. Jawaban yang benar adalah {q['answer']}")

    await asyncio.sleep(1)
    await ctx.send(
        "\nMau quiz lagi?\n"
        "Ketik 1 untuk mau\n"
        "Ketik 2 untuk balik ke menu")
    def check_next(m):
        return (
            m.author == ctx.author and
            m.channel == ctx.channel and
            m.content in ['1', '2'])
    try:
        next_msg = await bot.wait_for("message", check=check_next, timeout=20.0)
    except:
        await ctx.send("Oke, ketik `!menu` kalau mau lanjut nanti")
        return
    if next_msg.content == '1':
        await quiz(ctx)
    else:
        await menu(ctx)

@bot.command(name='funfact')
async def funfact(ctx):
    fact = random.choice(funfact_list)
    await ctx.send(f"Fun Fact:\n{fact}\n\n")
    await asyncio.sleep(4)
    await ctx.send("\n\nMau fun fact lagi?\n"
        "Ketik 1 untuk lanjut, 2 untuk berhenti")

    def check(m):
        return (
            m.author == ctx.author and
            m.channel == ctx.channel and
            m.content.upper() in ['1', '2'])
    try:
        msg = await bot.wait_for("message", check=check, timeout=20.0)
    except:
        await ctx.send("Waktu habis! Ketik `!funfact` kalau mau lanjut.")
        return

    if msg.content.upper() == '1':
        await funfact(ctx)
    else:
        await ctx.send("Oke! Ketik `!menu` kalau mau pilih yang lain!")

@bot.command(name= 'materi')
async def materi(ctx):
    await ctx.send(
        "\nMau materi berupa teks atau video?\n"
        "Ketik 1 untuk teks\n"
        "Ketik 2 video")
    def check_yes(m):
        return (
            m.author == ctx.author and
            m.channel == ctx.channel and
            m.content in ['1', '2'])
    try:
        next_msg = await bot.wait_for("message", check=check_yes, timeout=20.0)
    except:
        await ctx.send("Oke, ketik `!menu` kalau mau lanjut nanti")
        return
    if next_msg.content == '1':
        for materi in materi_list:
            await ctx.send(materi)
            await asyncio.sleep(4)
    else:
        for video in video_list:
            buffer = f"""
title: {video['title']}
url: {video['url']}
description: {video['description']}
thumbnail: {video['thumbnail']}
"""
            await ctx.send(buffer)
            await asyncio.sleep(3)

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

bot.run("KODE")
