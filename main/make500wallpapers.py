from PIL import Image, ImageDraw, ImageFont
import random
import requests
import textwrap
import os

url = 'https://api.quotable.io/random'


def create_wallpaper(quote, author, index):
    # Set wallpaper dimensions and properties
    width = 1072
    height = 1448
    dpi = 96
    bit_depth = 24

    # Create a black and white background
    background_color = (255, 255, 255)
    image = Image.new("RGB", (width, height), background_color)

    # Add the wrapped quote text
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts\RoxboroughCF-Regular.otf", size=50)  # You can change the font and size
    text_color = (0, 0, 0)
    text1_x = 100
    text1_y = height // 3 
    text2_x = 100
    text2_y = text1_y + 600

    # Wrap the quote text to fit within the image width
    wrapped_quote = textwrap.fill(quote, width=30)  # Adjust the width as needed
    draw.text((text1_x, text1_y), f'"{wrapped_quote}"', fill=text_color, font=font)
    draw.text((text2_x, text2_y), f' - {author}', fill=text_color, font=font)

    # Save the wallpaper
    image.save(f"book_wallpaper_{index}.png", dpi=(dpi, dpi), bits=bit_depth)


for i in range(1, 501):  # Create 10 different wallpapers
    response = requests.get(url)
    data = response.json()
    quote = data['content']
    author = data['author']
    if quote and author:
        create_wallpaper(quote, author, i)
        print(f"Wallpaper {i} created successfully as 'book_wallpaper_{i}.png'.")
    else:
        print(f"Failed to fetch a quote for wallpaper {i}. Please try again later.")