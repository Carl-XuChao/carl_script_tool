# 如何运行当前脚本并且输入分支名称
# sh update_apk.sh

cd '/Users/carlxu/Documents/project/flutter'

# 请把branch_list变量里面的内容过滤一下, 去掉其中带后缀名称.jks和.md, .yaml的
branch_list=`git branch -l | grep -vE '.jks|.md|.yaml'`

# 提示用户下面是所有本地已经来取的分支列表
echo '本地分支列表'
# 在终端中展示branch_list变量的内容, 以便用户选择
echo $branch_list

echo '-----------------------'

# 请在终端提示用户输入分支名称
echo "请输入分支名称"

# 请把用户输入的内容保存到一个变量中
read branch_name


# 判断输入的变量是否为空
if [ -z "$branch_name" ]; then
    echo "请输入分支名称"
    exit 1
fi

# 进入到flutter项目目录 
cd /Users/carlxu/Documents/project/flutter

# 暂存当前分支改动，并且切换到新分支  
echo '开始暂存代码并切换分支'
git stash

# 切换分支
echo '切换分支'
git checkout $branch_name

# 拉取最新代码
echo '更新代码'
git pull

# 清除缓存
echo '清除缓存'
flutter clean

# 获取依赖
echo '获取依赖'
flutter packages get

