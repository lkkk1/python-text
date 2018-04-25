#coding=utf-8
formatter = "%r %r %r %r"

print(formatter % (True, 2, 3, 4))
print(formatter % ("one","two","three","four"))
print(formatter % (formatter,formatter,formatter,formatter))
#为什么 %r 有时打印出来的是单引号，而我实际用的是双引号?

#Python 会用最有效的方式打印出字符串，而不是完全按照你写的方式来打印。这样做对于 %r 来说是可以接受的
print(formatter % (
    "I had this thing.哈哈",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))