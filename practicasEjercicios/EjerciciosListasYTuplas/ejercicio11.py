vec1,vec2,producto=(1,2,3),(-1,0,2),0
for i in range(len(vec1)):
	producto += vec1[i] * vec2[i]
print("El producto escalar de {} y {} es {}".format(vec1,vec2,producto))