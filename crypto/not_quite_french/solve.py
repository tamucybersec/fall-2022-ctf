alpha_num = "abcdefghijklmnopqrstuvwxyz1234567890_{}? "
alpha_len = len(alpha_num)

flag = ''
key = ''

ct = 'ss9nw63du7fz1dgc}_ef1bfk{oln?les_1ttf5ds}e?tqa2reetxpsa4idy9p s3qqxmwh_265{48600ceh8e0hnghg8ynvxk6f0733225lc}7 x4{?eh2xrin9gyk}ick'

crib = 'gigem{'
for i in range(len(crib)):
    key += alpha_num[alpha_num.index(ct[i]) - alpha_num.index(crib[i]) % alpha_len]
print(key)

flag += crib
key_len = 8

for i in range(len(key), len(ct)):
    flag += alpha_num[alpha_num.index(ct[i]) - alpha_num.index(ct[i-key_len]) % alpha_len]
print(flag)
