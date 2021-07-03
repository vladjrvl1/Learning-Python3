class Solution:
    def __init__(self):
        self.student_info = None
        self.height_data = None

    def read_file_to_list(self, file) -> list[str]:
        with open(file, 'r') as f:
            self.student_info = f.readlines()
            return self.student_info

    def height_data_formatting(self, strs: list[str]) -> dict[int:[int, int]]:
        for i in strs:
            self.height_data = {i: [0, 0] for i in range(1, 12)}
            class_number = int(i[:i.find('\t')])
            height = int(i[i.find('\t', 3) + 1:i.find('\n')])
            self.height_data[class_number][0] += height
            self.height_data[class_number][1] += 1
        return self.height_data

    def save_height_data_to_file(self, file) -> None:
        with open(file, 'w') as f:
            for key, value in self.height_data.items():
                if value[1] != 0:
                    f.write(f'{key} {str(round(value[0] / value[1], 5))}\n')
                else:
                    f.write(f'{key} -\n')


s = Solution()
strs = s.read_file_to_list('data.txt')
s.height_data_formatting(strs)
s.save_height_data_to_file('data_answer.txt')

# d = {i: [0, 0] for i in range(1, 12)}
# with open('data.txt', 'r') as f:
#     height_data = f.readlines()
#
# for i in height_data:
#     class_number = int(i[:i.find('\t')])
#     d[class_number][1] += 1
#     height = int(i[i.find('\t', 3) + 1:i.find('\n')])
#     d[class_number][0] += height
#
# with open('data_answer.txt', 'w') as f:
#     for key, value in d.items():
#         if value[1] != 0:
#             f.write(f'{key} {str(round(value[0] / value[1], 5))}\n')
#         else:
#             f.write(f'{key} -\n')
#
# print(d)
