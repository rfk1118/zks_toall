# zks_toall

# 私钥
* 在account.txt里面一行为一个私钥
```
0x123
0x123
0x123
```
# 代码修改

address = '交易所地址'
mul = 110

* 代码中有两个参数，一个是归集的交易所地址，自己修改
* mul = 110 这里是算出来精准gas后在给了1.1倍，防止error

# 安装依赖

pip install -r requirements.txt

# 运行

python main.py