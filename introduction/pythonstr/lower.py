# coding:utf-8

message_en = 'How do you do? Xiaomu'
message_ch = '你好呀, XiaoMu'
message_mix = '你好呀，Xiaomu, 今天是星期3！'

message_en_lower = message_en.lower()
message_en_casefold = message_en.casefold()

message_ch_lower = message_ch.lower()
message_ch_casefold = message_ch.casefold()

message_mix_lower = message_mix.lower()
message_mix_casefold = message_mix.casefold()

print(message_en_lower, message_en_casefold, message_en)
print(message_ch_lower, message_ch_casefold)
print(message_mix_lower, message_mix_casefold)

empty = ''
empty_lower = empty.lower()
empty_casefold = empty.casefold()

print('.' + empty_lower + '.', '.' + empty_casefold + '.')
