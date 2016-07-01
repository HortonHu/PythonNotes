Data type: string 'abc'
-----------------------

    print 'python'
    print 'I\'m OK'			# 加\有避免转义的作用
    print '\\\n\\'
    print '\\\t\\'
    print r'\\\t\\'      	# 使用r 来避免转义 raw strings
    print 'doesn\'t'  		# 使用\'来避免转义
    print '''line1
    line2'''							# 多行字符串
    
''和''''效果相同  
'''...'''or"""..."""中间可以任意添加''或者''''.它也可以当做一种注释 通常用于Documentation Strings
' "包含对方的时候均不需要转义
对于较长的语句 可以用\来续行 \后不能有也不应有任何字符

