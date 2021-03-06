from practical_6.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(visual_basic)
print(ruby)
print(python)


programming_languages = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
for code_name in programming_languages:
    if code_name.is_dynamic():#checks if the code is dynamic
        print(code_name.language)
