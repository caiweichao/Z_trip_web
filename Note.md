#page文件要点
1. page 只关心功能不允许存在任何的数据


#### 测试用例编写规则
1. 测试文件的命名规则 测试文件应当命名为test_xxx
2. 测试的函数或者测试类命名规则为test_xxx
3. 测试类命名为Testxxx

#### requirements文件管理
1. 定期执行命令 pip freeze>requirements.txt

#### 执行用例生成报告命令
1. pytest -s -q --alluredir ./report
2. allure generate directory-with-results/ -o directory-with-report --clean
3. allure generate report/ -o report/html --clean

#pytest使用注意事项
1. 使用conftest时注意层级,如果测试用例是多级模式存储,是优先找自己包里的conftest文件读取,
不要什么配置都放置在test_case下的conftest文件里,这个是最基础的公用文件,不同业务放在自己的contest里
注意!!!conftest名字不能变更

2. function：每个test都运行，默认是function的scope
class：每个class的所有test只运行一次
module：每个module的所有test只运行一次
session：每个session只运行一次





