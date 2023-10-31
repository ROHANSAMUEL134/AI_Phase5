import openai

print(" ____________________   ___________________     ___________              __________ \t\t\tDeveloped by:")
print("|____________________| |___________________\   |___________\            /__________|\t\t\t1)ROHAN SAMUEL J")
print(" ____________________   _____________________   _____________          ____________ \t\t\t2)MONESH KUAMR C")
print("|____________________| |_____________________\ |_____________\        /____________|\t\t\t3)P.K.M.HARICHEAN")
print("       ________            ______      ______        __________      __________     \t\t\t4)A.JEEVA")
print("      |________|          |______|    |______|      |__________\    /__________|    \t\t\t5)M.NITHISH KRISHANAN")
print("       ________            ___________________       ____________  ____________     ")
print("      |________|          |__________________/      |_____|\_____\/_____/|_____|    ")
print("       ________            __________________        _____  ____________  _____     ")
print("      |________|          |__________________\      |_____| \__________/ |_____|    \t\t\tCourse Name:")
print("       ________            ______      ______        _____    ________    _____     \t\t\tARTIFICIAL INTELLIGENCE")
print("      |________|          |______|    |______/      |_____|   \______/   |_____|    ")
print(" ____________________   ______________________  __________      ____      _________ ")
print("|____________________| |_____________________/ |__________|     \__/     |_________|\t\t\tProject Title:")
print(" ____________________   ____________________    __________       __       _________ \t\t\tCHATBOT USING PYTHON")
print("|____________________| |___________________/   |__________|      \/      |_________|")

print("\n\n\n")
print("\t\t\t\t CHATBOT")
print("\t\t\t\t ~~~~~~~")

openai.api_key = "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"
while True:
    model_engine = "text-davinci-003"
    prompt = input('\n\nEnter any request: ')
    if 'exit' in prompt or 'quit' in prompt:
        break
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    print(response)
    print("===================================================================================================================================================================")
