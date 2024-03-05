import json
import os
import re
# # Your JSON data
# dir_list = os.listdir('./законы')
# dir_list = [x for x in dir_list if x.endswith('.json')]
# for dir in dir_list:
#     print(dir)
#     with open('./законы/' + dir, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#         def custom_sort(item):
#             # Extract the number after "Статья"
#             match = re.search(r'\d+', list(item.keys())[0])
#             if match:
#                 return int(match.group())
#             return 0
#
#
#         # Sort the data using the custom sorting function
#         sorted_data = sorted(data, key=custom_sort)
#         text = ""
#         for l in sorted_data:
#             for d in l:
#                 # print(d)
#                 key = d.strip() + ':'
#                 value = l[d].strip() + '\n'
#                 text += key
#                 text += value
#
#         with open('./законы/законы/' + dir.split('.')[0] +'.txt', 'w', encoding='utf-8') as f:
#             f.write(text)


dir_list = os.listdir('./кодексы')
dir_list = [x for x in dir_list if x.endswith('.json')]
for dir in dir_list:
    print(dir)
    with open('./кодексы/' + dir, 'r', encoding='utf-8') as f:
        data = json.load(f)
        def custom_sort(item):
            # Extract the number after "Статья"
            match = re.search(r'\d+', list(item.keys())[0])
            if match:
                return int(match.group())
            return 0


        # Sort the data using the custom sorting function
        sorted_data = sorted(data, key=custom_sort)
        text = ""
        for l in sorted_data:
            for d in l:
                # print(d)
                key = d.strip() + ':'
                value = l[d].strip() + '\n'
                text += key
                text += value

        with open('./кодексы/кодексы/' + dir.split('.')[0] +'.txt', 'w', encoding='utf-8') as f:
            f.write(text)
