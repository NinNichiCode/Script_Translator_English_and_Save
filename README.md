#  English-to-Vietnamese Clipboard Translator with IPA Support

A simple Python tool that allows you to **translate English text** directly from your clipboard to **Vietnamese**, with **IPA phonetic transcription for single English words**. It also supports saving translations to a file and viewing popups for quick feedback.

---

##  Features

-  Translate copied English text to Vietnamese using Google Translate
-  Automatically adds **IPA transcription** for single English words (e.g., `school [skuːl]`)
-  Show a popup with original and translated text
-  Optionally save all translations to a local `.txt` file
-  Trigger actions instantly with global keyboard shortcuts

---

##  Requirements

Make sure you have **Python 3.6+** installed. Then install the dependencies:

pip install pyperclip keyboard deep-translator eng_to_ipa

--- 
Use the following shortcuts:

Shortcut	Action
Ctrl + B	Translate and show popup only
Ctrl + M	Translate, show popup, and save to file

For Example

Copy this sentence:

He has versatile experience.

Then press Ctrl + B.

You'll see a popup like:

🇬🇧 He has versatile experience.

-->

🇻🇳 Anh ấy có kinh nghiệm đa năng

If you press Ctrl + M, this translation will also be saved to the text file.
