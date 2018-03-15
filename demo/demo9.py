#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'a test demo9'
__author__='XYD'
class Screen(object):
	@property
	def width(self):
		return self._width
		
	@width.setter
	def width(self,value):
		if value < 0:
			raise ValueError('width must be >0')
		self._width = value
		
	@property
	def height(self):
		return self._height
		
	@height.setter
	def height(self,value):
		if value < 0:
			raise ValueError('height must be >0')
		self._height = value
	
	@property
	def resolution(self):
		return self._width * self._height
		
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')