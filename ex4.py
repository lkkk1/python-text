#coding=utf-8
cars = 100  #车的数量
space_in_a_car = 4.0  #下划线字符通常被当做字符串中的假想空格用来分隔字符。
drivers = 30  #司机数量
passengers = 90  #乘客数量
cars_not_driven = cars - drivers  #未用车的数量
cars_driven = drivers  #用车的数量
carpool_capacity = cars_driven * space_in_a_car    #可用车的容纳人数总和 (包含司机在内)   #carpool  拼车
average_passengers_per_car = passengers / cars_driven #平均每辆车的乘客数


print('There are',cars,'cars available.')
print('There are only',drivers,'drivers available')
print('There will be',cars_not_driven,'empty cars today')
print('We can transport',carpool_capacity,'people today')
print('We have',passengers,'to carpool today')
print('We need to put about',average_passengers_per_car,'in each car')


