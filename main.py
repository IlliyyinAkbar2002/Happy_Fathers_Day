def generate_fathers_day_wish():
    message = "Happy Father's Day!"
    fonts = pyfiglet.FigletFont.getFonts()
    selected_font = random.choice(fonts)
    ascii_art = pyfiglet.figlet_format(message, font=selected_font)
    return ascii_art


fathers_day_wish = generate_fathers_day_wish()


print(fathers_day_wish)
