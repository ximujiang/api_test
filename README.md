# API_TEST
接口自动化测试框架
python+pytest+allure+Jenkins

## 1.用例分层
### 1.1 **API定义层**
描述接口request请求,定义接口url、请求方式等
### 1.2 **service层**
这一层之所以叫做service(服务)层，是因为它的作用是用来提供测试用例所需要的各种“服务”，好比参数构建、接口请求、数据处理、测试步骤
+ ### apiObject
单接口的预处理层，这一层主要作用是单接口入参的构造，接口的请求与响应值返回
+ ### caseService
多接口的预处理层，这一层主要是测试步骤（teststep）或场景的有序集合
+ ### util
这一层主要放置针对当前业务的接口需要处理的数据
在实际编写测试步骤时，可能部分接口的参数是通过其他接口获取后经过处理才可以使用，或是修改数据格式，或是修改字段名称，亦或是某些value的加解密处理等
### 1.3 testcase层
其中各个用例之间应该是相互独立，互不干扰，不存在依赖关系，每个用例都可以单独运行
### 1.4 testdata层
此层用来管理测试数据，作为参数化场景的数据驱动
+ 参数化： 所谓参数化，简单来说就是将入参利用变量的形式传入，不要将参数写死，增加灵活性，好比搜索商品的接口，不同的关键字和搜索范围作为入参，就会得到不同的搜索结果。上面的例子中其实已经是参数化了

+ 数据驱动：对于参数，我们可以将其放入一个文件中，可以存放多个入参，形成一个参数列表的形式，然后从中读取参数传入接口即可。常见做数据驱动的有json、csv、yaml等
### 1.5 rawData层
这一层是存放接口原始入参的地方

某些接口的入参可能很多，其中很多参数值又可能是固定不变的，构建入参的时候我们只想对"变"的值进行动态的维护，而不维护的值就使用原始参数中的默认值，以此减少工作量(emmm…可能也就是CV大法的量吧~)
再者就是数据驱动的数据文件中只维护需要修改的参数，使数据文件更简洁，可阅读性更强
