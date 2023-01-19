# Info Scan使用说明



关注微信公众号：乌托邦安全团队 不定期更新实用小工具

#### 安装模块：

```
pip -r install requirements.txt
```



#### 参数说明

```
-f FILE, --file FILE  指定扫描文件
-o OUTFILE, --outfile OUTFILE 导出文件
-t T                  指定线程数,默认10
-D DIC, --Dic DIC     指定字典文件,默认dict.txt
-size SIZE            指定文件字节大小,默认3500000(用于过滤误报)
```

![image-20230119195424045](C:\Users\86184\AppData\Roaming\Typora\typora-user-images\image-20230119195424045.png)

#### 运行结果

字典可自行更改

*domain\*关键字可以将域名用于测试泄露的文件名进行测试,文件后缀可自定义

![image-20230119195851865](C:\Users\86184\AppData\Roaming\Typora\typora-user-images\image-20230119195851865.png)

url.txt(待扫描文件)里域名后不能有文件路径

![image-20230119195710487](C:\Users\86184\AppData\Roaming\Typora\typora-user-images\image-20230119195710487.png)



![image-20230119195800345](C:\Users\86184\AppData\Roaming\Typora\typora-user-images\image-20230119195800345.png)







