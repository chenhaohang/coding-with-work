def convert_original_to_final(original_file, final_file):
    with open(original_file, 'r') as infile, open(final_file, 'w') as outfile:
        # 写入目标文件的列标题
        outfile.write("RS\tstation\televation\n")
        
        # 初始化变量来存储当前的 RS 值
        current_rs = None
        
        # 按行读取原始文件
        for line in infile:
            line = line.strip()
            # 检查是否是新的段落标记（例如 K0+000.00）
            if line.startswith('K'):
                # 提取 RS 值（去除 'K' 和 '+'，然后转换为浮点数）
                current_rs = float(line.replace('K', '').replace('+', ''))
            elif line:
                # 提取 X 和 Y 坐标
                parts = line.split()
                x = float(parts[0])
                y = float(parts[1])
                # 将数据写入目标文件，RS 值、X 坐标和 Y 坐标
                outfile.write(f"{current_rs}\t{x}\t{y}\n")

# 调用函数，转换文件
convert_original_to_final('original.txt', 'final.txt')
print('处理完成,查看同目录下是否生成final.txt')