import os
"""
记得关闭文件
file = os.open("a.txt")
os.close(file)
"""

# 当前工作目录
os.getcwd()

# 改变当前工作目录到指定的路径
os.chdir(path)

# 列出目录下所有文件和目录名
os.listdir(dirpath)

# 删除
os.remove()

# 递归删除
os.removedirs(path)

# 将src改名为dst
os.rename(src, dst)

# 递归文件夹创建函数
os.makedirs(path)

# 以数字权限模式创建目录。默认的模式为 0777 (八进制)
os.mkdir(path)
os.mkdir(path, mode)

# 打开一个文件
# os.O_RDONLY: 以只读的方式打开
# os.O_WRONLY: 以只写的方式打开
# os.O_RDWR : 以读写的方式打开
# os.O_NONBLOCK: 打开时不阻塞
# os.O_APPEND: 以追加的方式打开
# os.O_CREAT: 创建并打开一个新文件
# os.O_TRUNC: 打开一个文件并截断它的长度为零（必须有写权限）
# os.O_EXCL: 如果指定的文件存在，返回错误
# os.O_SHLOCK: 自动获取共享锁
# os.O_EXLOCK: 自动获取独立锁
# os.O_DIRECT: 消除或减少缓存效果
# os.O_FSYNC : 同步写入
# os.O_NOFOLLOW: 不追踪软链接
os.open(file, flags, mode)
os.open("a.txt", os.O_RDWR|os.O_CREAT)

# ####################################################
"""
os.path
"""

# 返回文件名
os.path.basename(path)

# 返回文件路径
os.path.dirname(path)

# 显示path的绝对路径
os.path.abspath(path)

# 显示文件的大小。不存在则返回错误
os.path.getsize(path)

# 把目录和文件名合成一个路径
os.path.join(path1, path2)

# 转换path的大小写和斜杠
os.path.normcase(path)

# 返回path的真实路径
os.path.realpath(path)

# 从start开始计算相对路径
os.path.relpath(path[, start])

# 判断是否为绝对路径
os.path.isabs(path)

# 判断路径是否为文件
os.path.isfile()

# 判断路径是否为目录
os.path.isdir()

# 判断路径是否为链接
os.path.islink()

# 判断路径是否为挂载点
os.path.ismount()

# 路径存在则返回True,路径损坏也返回True
os.path.lexists
