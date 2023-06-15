from lxml import html
etree = html.etree
#xpath解析文件
#1.本地文件                                     etree.parse
#2.浏览器文件  response.read().decode('utf-8')   etree.HTML()
tree=etree.parse('xpath基本使用.html')
#tree.xpath('路径')
li_list=tree.xpath('//ul/li/text()')
print(li_list)
# print(len(li_list))
#查找所有带id属性的li标签
li_list2=tree.xpath('//ul/li[@id]')

print(li_list2)
##查找所有带id属性的li标签中class的属性值
l_list=tree.xpath('//ul/li[@id="l1"]/@class')
print(l_list)
#显示为字符/text()
li_list3=tree.xpath('//ul/li[@id]/text()')
print(li_list3)
#模糊查询 查询标签中id 包含l的数据
li_list4=tree.xpath('//ul/li[contains(@id,"l")]/text()')
print(li_list4)