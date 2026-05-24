# with open ("file1.txt") as f1, open ("file2.txt") as f2:
#     file1_num = [int(num) for num in f1]
#     file2_num = [int(num) for num in f2]
#     print(file1_num)
# result = [num for num in file1_num if num in file2_num]
# print(result)

student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

# for key, value in student_dict.items():
#     print(key)

import pandas

student_df = pandas.DataFrame(student_dict)

# for key, value in student_dict.items():
#     print(value)

for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)


