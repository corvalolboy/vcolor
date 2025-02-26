from ansi_formatter import AnsiFormatter

if __name__ == "__main__":
    print(AnsiFormatter.color_text("Жирный красный текст", color="red", style="bold"))
    print(AnsiFormatter.color_text("Синий текст на желтом фоне", color="blue", background="yellow"))
    print(AnsiFormatter.rgb_text("Произвольный RGB цвет", 255, 165, 0))
    print(AnsiFormatter.rgb_background("Текст с кастомным фоном", 128, 0, 128))
