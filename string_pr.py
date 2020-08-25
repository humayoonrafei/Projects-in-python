def common_letters(string_one,string_two):
  new_list=[]
  for i in string_one:
    if i in string_two:
      if not i in new_list:
        new_list.append(i)
  return new_list

print (common_letters("manhattan","sanfrancisco"))