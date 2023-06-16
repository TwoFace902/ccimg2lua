wrote this code as fast as possible to jettison an image of house m.d. directly into my friends' eyes. so this is very limited/unoptimized right now.

i figure the bottleneck (at least in my usecase) is the amount of characters the imgtolua.py script generates. thus i attempt to limit it as much as possible. on the house image it generated 9k characters for 3k pixels, which i have no idea is good or not but its the furthest i can limit it.

technically its the number of lines that bottlenecks since i use a ctrl c-v script to input the code, but there is a character limit for inputting it seems in computercraft (about 500 chars?) so yep
