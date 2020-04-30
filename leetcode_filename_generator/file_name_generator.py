import pyperclip
file_name = pyperclip.paste()
pyperclip.copy(file_name.lower().replace(".", "_").replace(" ", "_").replace("__", "_").replace("\n", ""))  # now the clipboard content will be string "abc"
