#!/usr/bin/env python3
import cowsay, datetime
from random import choice
from cuaca import weather

def main():
    chara = ["tux", "pig", "milk", "cow", "daemon", "fox", "kitty", "meow"]
    get_chara = choice(chara)
    current_time = datetime.datetime.now().hour
    period = get_period(current_time)

    print(cowsay.get_output_string(get_chara, "Selamat " + period + weather()))

def get_period(hour):
    if 4 <= hour <= 10:
        return "Pagi"
    elif 10 < hour <= 14:
        return "Siang"
    elif 14 < hour < 18:
        return "Sore"
    else:
        return "Malam"
    
main()
