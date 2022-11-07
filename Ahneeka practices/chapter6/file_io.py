# # todo open file for writing
# # todo create file if ti does not exist
# #  todo overwrite file if it exists
# # todo 1
# temp_file = open("temp.txt", "w")
# print("first line", file=temp_file)
# print("second line", file=temp_file)
# temp_file.close()
#
# # todo 2
input_file = open("temp.txt", "r")
output_file = open("output.txt", "w")
for line_str in input_file:
    new_str = ' '
    line_str = line_str.strip()  # todo get rid  of carriage return
    for char in line_str:
        new_str = char + new_str  # todo concat at the left (reverse)
    print(new_str, file=output_file)  # todo print to output_file

    # todo include a print to shell so we can observe progress
    print('line: {:12s} reverse is: {:s}'.format(line_str, new_str))
input_file.close()
output_file.close()


