import misspy

bot = misspy.Bot("misskey.example.com", "TOKEN")

@bot.event("ready")
async def on_ready():
    print("logged in: @" + bot.user.username)
    await bot.connect(misspy.localTimeline)


@bot.event("note")
async def on_note(note: misspy.Context):
    if note.text is not None:
        name = note.user.username
        if note.user.name:
            name = note.user.name
        print("----------")
        print(name + ": " + note.text)

bot.run()