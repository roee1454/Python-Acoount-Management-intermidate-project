with open("GUI\\login.py", "w+") as file:
    content = file.read()
    content = content.replace("self.", "")
    file.write(content)