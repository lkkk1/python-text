#coding = utf-8
print("Let's practice everything.")

print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

#"""可以全部输出，但转义符号正常工作"""
poem="""
\t The lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("___________")
print (poem)
print("___________")

five = 10-2+3-6
print("This should be five:%s"%five)

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans,jars,crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)

print("With a staring point of: %d"%start_point)
print("We'd have %d beans,%d jas,and%d crates."%(beans,jars,crates))

start_point = start_point / 10

print("We can also do that this way:")
#包含多个return返回值的函数调用过程可以直接参与格式化输出。
print("We'd have %d beans,%djars,and %d crates."%secret_formula(start_point))
