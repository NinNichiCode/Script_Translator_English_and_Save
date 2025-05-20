import pyperclip
import keyboard
from deep_translator import GoogleTranslator
from tkinter import Tk, messagebox
import time
import os
import eng_to_ipa as ipa  # Để phiên âm từ tiếng Anh

# File kết quả
output_file = "translated_sentences.txt"

def show_popup(original, translated):
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)  
    messagebox.showinfo(" Dịch văn bản", f"🇬🇧 {original}\n\n➡\n\n🇻🇳 {translated}")
    root.destroy()

def process_text(text):
    """Nếu là 1 từ thì thêm phiên âm IPA"""
    if ' ' not in text and text.isalpha():
        pronunciation = ipa.convert(text)
        return f"{text} [{pronunciation}]"
    return text

def preprocess_text(text):
    """
    Loại bỏ ngắt dòng không cần thiết từ PDF.
    Nếu một dòng không kết thúc bằng dấu câu (.), thì nối với dòng kế tiếp.
    """
    lines = text.splitlines()
    result = ""
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        if i < len(lines) - 1:
            if stripped[-1] in ".!?;:":
                result += stripped + " "
            else:
                result += stripped + " "  # nối nếu không kết thúc bằng dấu câu
        else:
            result += stripped
    return result.strip()


def translate_only():
    print("--- Đã nhấn Ctrl+Alt+D ---")
    time.sleep(1)  # Chờ clipboard cập nhật
    raw_text = pyperclip.paste().strip()
    text = preprocess_text(raw_text)

    print(f" Nội dung Clipboard: '{text}'")

    if not text:
        print("Clipboard rỗng!")
        return

    try:
        translated = GoogleTranslator(source='en', target='vi').translate(text)
        text_display = process_text(text)
        print(f" Dịch: {text_display} => {translated}")
        show_popup(text_display, translated)
    except Exception as e:
        print(" Lỗi khi dịch:", e)

def translate_and_save():
    print("--- Đã nhấn Ctrl+Alt+S ---")
    time.sleep(1)
    raw_text = pyperclip.paste().strip()
    text = preprocess_text(raw_text)
    print(f" Nội dung Clipboard: '{text}'")

    if not text:
        print(" Clipboard rỗng!")
        return

    try:
        translated = GoogleTranslator(source='en', target='vi').translate(text)
        text_display = process_text(text)
        print(f" Dịch: {text_display} => {translated}")
        show_popup(text_display, translated)

        with open(output_file, "a", encoding="utf-8") as f:
            f.write("=========================\n")
            f.write(f"English: {text_display}\n")
            f.write(f"Vietnamese: {translated}\n\n")
        print(f" Đã lưu vào: {os.path.abspath(output_file)}")
    except Exception as e:
        print(" Lỗi khi dịch và lưu:", e)

# === Giao diện dòng lệnh ===
print(" Tool dịch & lưu đang chạy...")
print(" Cách dùng:")
print("1. Tô đen văn bản, nhấn Ctrl+C")
print("2. Ctrl+b → Chỉ dịch & hiện popup")
print("3. Ctrl+m → Dịch & lưu vào file")
print(f" Kết quả lưu tại: {os.path.abspath(output_file)}")

# === Gán phím tắt ===
keyboard.add_hotkey("ctrl+b", translate_only)
keyboard.add_hotkey("ctrl+m", translate_and_save)

keyboard.wait()
