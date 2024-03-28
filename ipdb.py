import os
import requests

# 获取当前py文件的目录路径
output_folder = "notls"
output_filename = "ipdb.txt"

# 定义要访问的URLs
urls = [
    "https://raw.githubusercontent.com/ymyuuu/IPDB/main/bestproxy.txt",
    "https://raw.githubusercontent.com/ymyuuu/IPDB/main/bestcf.txt"
]

# 在仓库根目录下定义输出文件路径
output_file = os.path.join(output_folder, output_filename)

# 打开或创建ipdb.txt文件进行写入
with open(output_file, "w", encoding="utf-8") as file:
    # 遍历每个数据源的URL
    for url in urls:
        # 发送GET请求获取数据
        response = requests.get(url)

        # 检查请求是否成功
        if response.status_code == 200:
            # 解析响应文本，并以每行为单位进行处理
            lines = response.text.strip().split('\n')

            # 遍历每一行数据
            for line in lines:
                # 确定备注
                remark = "IPDB-PROXY" if "bestproxy" in url else "IPDB-CF"
                
                # 每行添加端口号和备注，然后写入文件
                file.write(f"{line.strip()}:2052#{remark}\n")  # 假设端口号都为2052

            print(f"已将 {url} 的数据写入到ipdb.txt文件中。")
        else:
            print(f"请求 {url} 失败，状态码：{response.status_code}")
