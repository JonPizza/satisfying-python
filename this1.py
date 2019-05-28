from random import randint
from pygame.locals import *
import sys, time, pygame

pygame.init()
DISPLAY=pygame.display.set_mode((1200,800),0,32)
WHITE=(255, 255, 255)
BLUE=(0, 0, 255)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLACK=(0)

nums = [randint(0, 800) for x in range(1200)]

def show(nums):
	global DISPLAY

	DISPLAY.fill(WHITE)

	for i in range(len(nums)):
		if i%2 == 0:
			pygame.draw.rect(DISPLAY, RED, [i, 800, 1, -nums[i]])
		else:
			pygame.draw.rect(DISPLAY, BLUE, [i, 800, 1, -nums[i]])

	pygame.display.update()

	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()

def greater(n1, n2):
	return n1 > n2

def sort1_round(nums):
	for count in range(len(nums)-1):
		if greater(nums[count], nums[count+1]):
			x = nums[count]
			nums[count] = nums[count+1]
			nums[count+1] = x

		show(nums)
	return nums

def sort2_round(nums):
	for count in range(len(nums)-1):
		if not greater(nums[count], nums[count+1]):
			x = nums[count]
			nums[count] = nums[count+1]
			nums[count+1] = x
		show(nums)
	return nums

def sort3_round(nums):
	for count in range(len(nums)-1):
		if count % 2 == 1:
			if not greater(nums[count-1], nums[count+1]):
				x = nums[count-1]
				nums[count-1] = nums[count+1]
				nums[count+1] = x
				
		elif count != 0:
			if greater(nums[count-1], nums[count+1]):
				x = nums[count+1]
				nums[count+1] = nums[count-1]
				nums[count-1] = x

	show(nums)
	return nums

show(nums)
time.sleep(1)

while True:
	nums = sort3_round(nums)
	if nums[1::2] == sorted(nums[1::2]):
		time.sleep(1.5)
		nums = [randint(0, 800) for x in range(1200)]
