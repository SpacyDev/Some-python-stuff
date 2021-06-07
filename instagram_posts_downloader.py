import instaloader
USERNAME=input('input username: ')
bot = instaloader.Instaloader()
profile = instaloader.Profile.from_username(bot.context, USERNAME)
for post in profile.get_posts():
    bot.download_post(post, target=profile.username)

