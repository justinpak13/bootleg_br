import random 

def transform(text):
    transformed_text = []
    for word in text.split():
        divisor = random.randint(max(round(len(word)*0.2),1),round(len(word)*0.8))
        formatted_word = f'<bionic>{word[:divisor]}</bionic><regular>{word[divisor:]}</regular>'
        transformed_text.append(formatted_word)
    transformed_text.append('\n')
    return ' '.join(transformed_text)