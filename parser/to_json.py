import json
import re


with open('new.txt', 'r',encoding='utf-8') as f:
    content = f.read()


text = content
def split_text_by_phrases(text, phrase1, phrase2):
    # Find the indices where the phrases occur
    index1 = text.find(phrase1)
    index2 = text.find(phrase2)

    # Ensure both phrases are found
    if index1 != -1 and index2 != -1:
        # Extract the sections based on the phrase indices
        first_section = text[:index2].strip()  # section before the second phrase
        second_section = text[index2:].strip()  # section from the second phrase onwards
        return first_section, second_section
    else:
        # Phrases not found
        return None, None
phrase1 = "ОБЩАЯ ЧАСТЬ"
phrase2 = "ОСОБЕННАЯ ЧАСТЬ"

section1, section2 = split_text_by_phrases(text, phrase1, phrase2)
# Define the pattern to match sections starting with "РАЗДЕЛ"
# sections = re.split(r'(?=ЧАСТЬ \d+\.)', text)

# print(section1)
d_json = {}
def split_text(target, text, start):
    d_json[start] = []
    statyas = {}
    sections = re.split(rf'(?={target} \d+\.)', text)
    for section in sections:
        subsections = re.split(r'(?=Статья \d+\.)', section)

        temp = {}
        for i in range(1, len(subsections)):
            st_match = re.search(r'(Статья \d+\..+)', subsections[i])
            l = subsections[i].split(st_match.group(1))
            temp[st_match.group(1).strip()] = l[1]
       # statyas[]
        print(temp)
        if len(subsections) > 1:
            statyas[subsections[0].strip()] = temp

    d_json[start] = statyas

split_text("РАЗДЕЛ", section1, "ОБЩАЯ ЧАСТЬ")
split_text("Глава", section2, "ОСОБЕННАЯ ЧАСТЬ")

# print(d_json)
with open("test.json", "w", encoding='utf-8') as outfile:
    json.dump(d_json, outfile, ensure_ascii=False, indent=4)
# print(section1)
text = section1
sections = re.split(r'(?=РАЗДЕЛ \d+\.)', text)
# print(sections)
# Extracting words before each "Статья"
for section in sections:
    subsections = re.split(r'(?=Статья \d+\.)', section)
    # print(subsections)
    for i in range(1, len(subsections)):
        words_before_st = re.findall(r'\b\w+\b(?= Статья )', subsections[i-1])
        # if words_before_st:
        #     print(' '.join(words_before_st))
        # print(subsections[i])