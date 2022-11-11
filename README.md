这个是从pycharm中创建的远程连接


一、新建仓库步骤：
1、点击Git->Github->Share Project on Github
2、在弹出的弹框中输入Github中新建仓库的名字以及仓库描述
3、repository name：仓库名称
    remote：远程
    description：描述
4、点击share按钮，选择需要提交的文件
    Commit Message：提交消息
    add files for initial commit：为初始提交添加文件
5、然后github上就自动创建了一个仓库，并把本地当前的项目传上去


二、更新仓库步骤：
1、右击项目，选择“Local History”->“Show History”
2、在弹出来的弹框中，选择最近一次的提交，并且右击选择“Revert”
3、再按照仓库更新的步骤进行一次提交即可


三、提交修改文件到GitHub
新增文件（红色），右键-->Git-->add，将新增的文件加入本地仓库，此时文件变绿色
修改文件（蓝色）
在项目右键-->Git-->Commit Directory，查看有变动的文件并输入Commit Message，点击Commit and Push...
提交后会进行语法检查，若存在错误或警告会给出确认提示，点击Commit，弹出Push框，点击Push，上传GitHub成功