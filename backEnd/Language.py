import AI

def enhance_description(description:str,):
    return AI.ask(["This is a draft dicription of a product, edit it to be used as the final description for a listing on an Ecommerce website, (add what you think is missing **ONLY IF NECESSARY**):",description])

def enhance_Title(Title:str,):
    return AI.ask(["This is a draft Title of a product, Give alterenate titles for a listing on an Ecommerce website:",Title])

