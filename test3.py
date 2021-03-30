string = 'http://www.domain.com/?s=some&two=20'
cut_string = string.split('&')
new_string = cut_string[0]
print(new_string)