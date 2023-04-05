# 如何运行这个脚本
# 1. 将这个脚本放到Flutter项目根目录
# 2. 在Flutter项目根目录创建一个apk_config.json文件
# 3. 在apk_config.json文件中写入如下内容
# {
#     "exportPath": "/Users/xxx/Desktop"
#     "projectPath": "/Users/xxx/Desktop/FlutterProject/flutter_app",
# }
# 4. 在终端中执行 python3 build_apk.py
# 5. 等待打包完成，apk会导出到电脑桌面
    

# 实现一个flutter apk的打包脚本
# 1. 读取配置文件
# 2. 执行打包命令
# 4. 导出apk并且根据当前代码分支+时间重命名
# 5. 保存apk到电脑桌面
    
import os
import sys
import time
import json
import shutil
import subprocess

# 读取配置文件
def readConfig():
    with open("/Users/carlxu/Documents/AppProject/carl_script_tool/buildApk/apk_config.json", "r") as f:
        config = json.load(f)
    return config

# 执行flutter clean 和 flutter pub get
def flutterCleanAndPubGet(config):
    #  进入Flutter项目根目录
    os.chdir(config["projectPath"])
    # 执行flutter clean
    subprocess.call("flutter clean", shell=True)
    # 执行flutter pub get
    subprocess.call("flutter pub get", shell=True)

# 执行打包命令
def buildApk(config):
    
    # 打包命令
    command = "flutter build apk"
    # 执行打包命令
    subprocess.call(command, shell=True)
    # 获取当前代码分支
    branch = subprocess.check_output("git rev-parse --abbrev-ref HEAD", shell=True).decode("utf-8").strip()
    # 获取当前时间
    now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # 重命名apk
    apkName = branch + "_" + now + ".apk"
    # 重命名apk
    shutil.move("build/app/outputs/flutter-apk/app-release.apk", "build/app/outputs/flutter-apk/" + apkName)
    # 导出apk到电脑桌面
    shutil.copy("build/app/outputs/flutter-apk/" + apkName, config["exportPath"] + "/" + apkName)

if __name__ == "__main__":
    # 读取配置文件
    config = readConfig()
    
    # 执行flutter clean 和 flutter pub get
    flutterCleanAndPubGet(config);
    
    # 执行打包命令
    buildApk(config)


