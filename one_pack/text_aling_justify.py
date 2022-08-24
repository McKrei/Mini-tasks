'''
Your task in this Kata is to emulate text justification in monospace font.
You will be given a single-lined text and the expected justification width.
The longest word will never be greater than this width.

Here are the rules:

    Use spaces to fill in the gaps between words.
    Each line should contain as many words as possible.
    Use '\n' to separate lines.
    Gap between words can't differ by more than one space.
    Lines should end with a word not a space.
    '\n' is not included in the length of a line.
    Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
    Last line should not be justified, use only one space between words.
    Last line should not contain '\n'
    Strings with one word do not need gaps ('somelongword\n').
'''


# def justify(text, width):
#     text_list = text.split()
#     if len(text_list) < 2:
#         return text
#     result_text = ''
#     result = []
#     line = []
#     length = width -1
#     space = -1

#     for word in text_list:
#         len_word = len(word)
#         if len_word <= length - space:
#             line.append(word)
#             length -= len(word)
#             space += 1
#         else:
#             if space > 0:
#                 space = length // space if length > space else 1
#             else:
#                 space = 0
#             start_space = space % (length + 1) if length > 0 else 0
#             if len(line) > 1:
#                 for el in line[:-1]:
#                     if start_space > 0:
#                         result_text += el + (' ' * (space + 1))
#                         start_space -= 1
#                     else:
#                         result_text += el + (' ' * (space))
#             result_text += line[-1] + '\n'
#             space = -1
#             length = width - len_word - 1
#             line = [word]
#     return result_text + ' '.join(line)


# print(justify('123 45 6', 7))
# assert justify('123 45 6', 7) == '123  45\n6'
