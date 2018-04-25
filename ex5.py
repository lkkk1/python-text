#coding=utf-8
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches  英寸
weight = 180 # lbs   磅
kg = 0.454
cm = 2.54
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_cm = height * cm
weight_kg = weight * kg

print("Let's talk about %s." % name)
print("He's %d cm tall." % height_cm)
#print(int(cm)*int(height))
print("He's %d kg heavy." % weight_kg)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." %(eyes,hair))
print("His teeth are usually %s depending on the coffee." % teeth)

#this line is tricky,try to get is exactly right
print("If I add %d,%d,and %d I get %d." %(age,height,weight,age+height+weight))


h = 'world'
print("Hello %r" % h)   # %r简单粗暴
print("Hello %s" % h)   # %s更加智能

a=3**2
print(a)
