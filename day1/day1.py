sum = 0

num_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

with open(file="input.txt", mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        num_code = ''
        first_num = True
        first_num_i = -1
        last_num_i = -1
        last_num = ''
        word_num = ''
        
        word_num_dict = {}
        
        for num in num_dict.keys():
            if num in line:
                first_i = line.find(num)
                last_i = line.rfind(num)
                
                word_num_dict[num] = [first_i, last_i, num_dict[num]]
            
        for i in range(len(line)):
            word_num = word_num + line[i]
            word = False
            word_str = ''
            
            if first_num and line[i].isnumeric():
                num_code = last_num = num_code + line[i]
                first_num_i = i
                last_num_i = i
                first_num = False
            elif line[i].isnumeric():
                last_num = line[i]
                last_num_i = i
                

        for num_info in word_num_dict.values():
            if num_info[0] < first_num_i:
                num_code = num_info[2]
                first_num_i = num_info[0]
            if num_info[1] > last_num_i:
                last_num = num_info[2]
                last_num_i = num_info[1]

        num_code = num_code + last_num
        print(num_code)
        sum = sum + int(num_code)
        

print(sum)