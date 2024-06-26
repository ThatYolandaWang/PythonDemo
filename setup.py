from setuptools  import setup

setup(
    # 指定项目名称，我们在后期打包时，这就是打包的包名称，当然打包时的名称可能还会包含下面的版本号哟~
    name='pythondemo',
    # 指定版本号
    version='0.1.1',
    # 这是对当前项目的一个描述
    description='Python automatic operation and maintenance platform',
    # 作者是谁，指的是此项目开发的人，这里就写你自己的名字即可
    author='yinzhengjie',
    # 作者的邮箱
    author_email='wangying123820@gmail.com',
    # 指定包名，即你需要打包的包名称，要实际在你本地存在哟，它会将指定包名下的所有"*.py"文件进行打包哟，但不会递归去拷贝所有的子包内容。
    # 综上所述，我们如果想要把一个包的所有"*.py"文件进行打包，应该在packages列表写下所有包的层级关系哟~这样就开源将指定包路径的所有".py"文件进行打包!
    packages=['code'],
)