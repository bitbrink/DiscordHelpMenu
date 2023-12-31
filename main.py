import discord
from discord.ext import commands
from discord import Button, ButtonStyle, InteractionType, ActionRow
from discord.ui import Button, View

intents = discord.Intents.default()
intents.typing = False
intents.presences = True
intents.messages = True
intents.guilds = True

intents.message_content = True

bot = commands.Bot(command_prefix="#", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

def is_staff_team():
    async def predicate(ctx):
        return discord.utils.get(ctx.author.roles, name="Staff Team") is not None
    return commands.check(predicate)

class InstallButtonView(View):
    def __init__(self):
        super().__init__()
        self.add_item(Button(style=ButtonStyle.primary, label="Technic Launcher", custom_id="install_button1"))
        self.add_item(Button(style=ButtonStyle.primary, label="Forge Modpack", custom_id="install_button2"))
        self.add_item(Button(style=ButtonStyle.primary, label="Custom Textures", custom_id="install_button3"))
        self.add_item(Button(style=ButtonStyle.primary, label="How to Play Guide", custom_id="install_button4"))

@bot.command()
@is_staff_team()
async def install(ctx): 
    await ctx.message.delete()
    view = InstallButtonView()
    await ctx.send(":question: Need help installing Pixelmon? Click one of the buttons below for help! \n\n**IP**: `play.desertmc.net`", view=view)

class LinkButtonView(View):
    def __init__(self):
        super().__init__()
        self.add_item(Button(style=ButtonStyle.primary, label="Website", custom_id="link_button1"))
        self.add_item(Button(style=ButtonStyle.primary, label="Store", custom_id="link_button2"))
        self.add_item(Button(style=ButtonStyle.primary, label="Vote Links", custom_id="link_button3"))
        self.add_item(Button(style=ButtonStyle.primary, label="Rules", custom_id="link_button4"))
        self.add_item(Button(style=ButtonStyle.primary, label="Discord", custom_id="link_button5"))


@bot.command()
@is_staff_team()
async def links(ctx):
    await ctx.message.delete()
    view = LinkButtonView()
    await ctx.send(":link: Here are some useful links that you will need throughout your time here:", view=view)


@bot.event
async def on_interaction(interaction):
    if interaction.type == discord.InteractionType.component:
        user = interaction.user


        if interaction.data["custom_id"] == "install_button1":
            await interaction.response.send_message(":video_game: **Technic Launcher Modpack Link**: <https://www.technicpack.net/modpack/desertmc-pixelmon.1846360> \n\nIf you already have Technic Launcher installed, you can just search **DesertMC Pixelmon** and install it!\n\nIf you do not have Technic Launcher installed, you can follow this video to get setup: <https://www.youtube.com/watch?v=tJLPjhvpZJY>\n\nRead our **How to Play** guide for more information: <https://desertmc.net/play/>", ephemeral=True)
        elif interaction.data["custom_id"] == "install_button2":
            await interaction.response.send_message(":question: **__Want to join using Forge?__**\n\n**1**. Download Forge 1.16.5 from <https://files.minecraftforge.net/net/minecraftforge/forge/index_1.16.5.html>\n\n**2**. Open the .jar and hit \"Install Client\"\n\n**3**. Go to your .minecraft folder (found in %appdata%)\n\n**4**. Create a folder called \"mods\" (sometimes already there)\n\n**5**. Install our modpack folder: https://files.desertmc.net/ReforgedModpack.zip\n\n**6**. Drag and drop the mods from the folder into the \"mods\" folder\n\n**7**. Open up the Minecraft Launcher, select your Installation version to Forge 1.16.5, and boom you're done!", ephemeral=True)
        elif interaction.data["custom_id"] == "install_button3":
            await interaction.response.send_message(":star2: Want to see our **Custom Textures** In-Game? If you are on Forge, you will need to download and install our Resource Pack:\n\n:link: https://files.desertmc.net/DesertMC-PixelmonResourcePack.zip\n\n*If you are on our Technic Modpack, you already can!*", ephemeral=True)
        elif interaction.data["custom_id"] == "install_button4":
            await interaction.response.send_message(":question: If you need help joining or installing Pixelmon, feel free to read our **How to Play** guide:\n\n<https://desertmc.net/play/>\n\nIf you need more help, please ask a staff member to assist you!", ephemeral=True)

        elif interaction.data["custom_id"] == "link_button1":
            await interaction.response.send_message(":globe_with_meridians: **Website**: <https://desertmc.net/>\n\nAll in-depth blogposts are released on our website, voting links, and sometimes special discount code drops!", ephemeral=True)
        elif interaction.data["custom_id"] == "link_button2":
            await interaction.response.send_message(":shopping_cart: **Store**: <https://store.desertmc.net/>\n\nPurchase ranks, crate keys, and more to support your adventure and others!", ephemeral=True)
        elif interaction.data["custom_id"] == "link_button3":
            await interaction.response.send_message(":free: **Vote Link**: <https://desertmc.net/vote/>\n\nVote on all of our voting sites to support DesertMC and in return receive **FREE** rewards!", ephemeral=True)
        elif interaction.data["custom_id"] == "link_button4":
            await interaction.response.send_message(":warning: **Rules**: <https://desertmc.net/rules/>\n\nYou can find all network-wide and Pixelmon specific rules on our website. Please review it and ask staff if you have any questions on any specific rule", ephemeral=True)
        elif interaction.data["custom_id"] == "link_button5":
            await interaction.response.send_message(":link: **Discord**: https://discord.gg/desertmc\n\nInvite your friends, build your town!", ephemeral=True)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Read <#830656686612021258> if you need help, or contact staff")
    else:
        await ctx.send(f"An error occurred: {error}")
        print(error)


bot.run('')