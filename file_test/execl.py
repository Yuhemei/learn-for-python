import pandas as pd
import re


def extract_numbers(value):
    # 如果值不是字符串类型，直接返回原值
    if not isinstance(value, str):
        return value
    # 使用正则表达式提取数字
    numbers = "".join(re.findall(r"\d+", value))
    # 如果提取到数字则返回数字，否则返回原值
    return int(numbers) if numbers else value


def process_excel(input_file, output_file):
    try:
        # 读取Excel文件中的所有sheet
        excel_file = pd.ExcelFile(input_file)

        # 创建一个ExcelWriter对象来保存结果
        with pd.ExcelWriter(output_file) as writer:
            # 处理每个sheet
            for sheet_name in excel_file.sheet_names:
                # 读取当前sheet，不指定header
                df = pd.read_excel(input_file, sheet_name=sheet_name, header=None)

                # 对所有单元格应用提取数字的函数
                df_processed = df.applymap(extract_numbers)

                # 将处理后的数据写入新的Excel文件
                df_processed.to_excel(
                    writer, sheet_name=sheet_name, index=False, header=False
                )

        print(f"处理完成！结果已保存到 {output_file}")

    except Exception as e:
        print(f"处理过程中出现错误: {str(e)}")


if __name__ == "__main__":
    input_file = "T1B-raw-data.xlsx"  # 输入文件名
    output_file = "output.xlsx"  # 输出文件名
    process_excel(input_file, output_file)
