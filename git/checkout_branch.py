import os
import sys
import json
import subprocess

  
# 读取配置文件
def readConfig():
    with open("/Users/carlxu/Documents/AppProject/carl_script_tool/buildApk/apk_config.json", "r") as f:
        config = json.load(f)
    return config

# 获取当前代码本地的所有本地分支
def getLocalBranch():
     #  进入Flutter项目根目录
    os.chdir(config["projectPath"])
    # 获取所有本地分支
    localBranch = subprocess.check_output("git branch", shell=True).decode("utf-8")
    #  打印所有本地分支
    print(localBranch)
    return localBranch  

 
 # 从上面获取到的分支列表中，让用户选择一个并选择结果返回
def selectBranch(localBranch):
    # 选择分支
    selectBranch = input("请输入选择的分支名称：")  
    print(selectBranch)   
    return selectBranch

# 切换分支
def checkoutBranch(selectBranchName):
    #  先暂存当前分支的修改
    subprocess.call("git stash", shell=True)
    
    # 切换分支
    subprocess.call("git checkout " + selectBranchName, shell=True)

    # 判断是否有切换成功    
    if selectBranchName == subprocess.check_output("git rev-parse --abbrev-ref HEAD", shell=True).decode("utf-8").strip():
        print("切换分支成功")
    else:
        print("切换分支失败")


# 执行flutter clean 和 flutter pub get
def flutterCleanAndPubGet(config):
    # 执行flutter clean
    subprocess.call("flutter clean", shell=True)
    # 执行flutter pub get
    subprocess.call("flutter pub get", shell=True)

        
    
if __name__ == "__main__":
    # 读取配置文件
    config = readConfig()
    
     # 获取当前代码本地的所有本地分支
    localBranch = getLocalBranch()
    
    selectBranchName = selectBranch(localBranch);
   
    checkoutBranch(selectBranchName) 
    
    flutterCleanAndPubGet(config);
    