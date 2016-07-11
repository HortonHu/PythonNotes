# -*- coding:utf-8 -*-


# PIL（Python Imaging Library） 现在已经用Pillow替代PIL了 因为PIL已经不再维护
from PIL import Image           # 不能用import image形式
im_local = 'pic.jpg'
im = Image.open(im_local)
print im.format, im.size, im.mode
im.thumbnail((im.size[0]/2, im.size[1]/2))      # 缩放到50%:
im.save('half_pic.jpg')


# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全
# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图

