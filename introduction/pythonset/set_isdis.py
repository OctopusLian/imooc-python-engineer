# coding:utf-8

company_not_allow = {'女', '喝酒', '抽烟', '睡懒觉'}

one_player = {'男', '跑步', '朝气', '喝酒'}
two_player = {'女', '生活规律', '跆拳道'}
three_player = {'男', '太极拳'}
four_player = {'男', '空手道', '年轻'}


print(company_not_allow.isdisjoint(one_player))
print(company_not_allow.isdisjoint(two_player))
print(company_not_allow.isdisjoint(three_player))
print(company_not_allow.isdisjoint(four_player))

