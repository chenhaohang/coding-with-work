import os

# 设置包含txt文件的目录
directory = 'E:\池州\水文计算源数据\断面合并\断面0909'  # 替换为你的txt文件所在的文件夹路径

# 初始化一个空列表，用于存储合并后的内容
merged_content = []

# 遍历目录中的所有文件
for filename in os.listdir(directory):
    # 检查文件扩展名是否为.txt
    if filename.endswith('.txt'):
        # 构建文件的完整路径
        file_path = os.path.join(directory, filename)
        # 打开并读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            # 读取文件的所有行
            lines = file.readlines()
            # 将文件名添加到每一行的第三列
            for line in lines:
                merged_line = line.strip() + '\t' + filename + '\n'
                merged_content.append(merged_line)

# 将合并后的内容写入到一个新的文件中
output_file = 'merged_files.txt'  # 你可以自定义输出文件的名称
with open(output_file, 'w', encoding='utf-8') as file:
    file.writelines(merged_content)

print(f'All .txt files have been merged into {output_file}')