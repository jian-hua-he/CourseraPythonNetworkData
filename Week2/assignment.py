import re

sample_file_name = 'sample_regex_sum_42.txt'
actual_file_name = 'actual_regex_sum_252080.txt'
file = open(actual_file_name, encoding='utf-8')

num_sum = 0
count = 0
for line in file:
	for number in re.findall(r'([0-9]+)', line):
		count = count + 1
		num_sum = num_sum + int(number)

print('Count is: ' + str(count))
print('Sum is: ' + str(num_sum))
