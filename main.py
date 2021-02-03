## PASCAL TRIANGLE

triangle_stage = 25
current_stage = 2

#print the first stage
previous_line = [1]
print(previous_line)

#print the remaining stages
for i in range(triangle_stage):
  current_line = [1]
  for j in range(1,current_stage):
    if(j < current_stage-1):
      current_line.append(previous_line[j-1] + previous_line[j])
    else:
      current_line.append(previous_line[j-1])
  print(current_line)
  current_stage += 1
  previous_line = current_line