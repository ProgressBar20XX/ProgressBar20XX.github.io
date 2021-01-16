# pip3 install yagmail
# use yagmail to send gmail.
# The excution speed is slower than the other scripter, but should have no effect. But gmail process it much fast, almost instantly
import yagmail

yag = yagmail.SMTP('Progressbar20XX@gmail.com','kzoyvjckjltatdgt')
contents = [
    "This is the body, and here is just text http://somedomain/image.png",
    "You can find an audio file attached.",
    '/local/path/to/song.mp3',
    'readme.md',
    'another text',
    'it is just a line breaker',
    'From radish',
    '<img src="https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-1/cp0/p40x40/72034413_2280004992127649_870997643684216832_n.jpg?_nc_cat=110&_nc_sid=dbb9e7&_nc_oc=AQk_pczjSlIB9MfhrWhTOAQ2M5NLOMawBgj3o__t6X4vK3-5K62D_26Sea1fmyQHnNiIwsQKkZA5zky4RLzlG-DL&_nc_ht=scontent-lax3-1.xx&oh=446bcb2d9769120468ce58526b58abbd&oe=5EEF2ABF">'
]
yag.send('240155787@qq.com', 'yagmail is awesome', contents)

print(' finish sending email through yagmail')

# Alternatively, with a simple one-liner:
# yagmail.SMTP('mygmailusername').send('to@someone.com', 'subject', contents)
