import re

'''
1-string literals
2-keywords
3-seperators
4-operators
5-identifiers
6-integer literals
7-float literals
'''
s0 = "HEY"
s1 = "int     A1=5"
s2 = "float BBB2     =1034.2"
s3 = "float     cresult     =     A1     +BBB2     *      BBB2"
s4 = "if     (cresult     >10):"
s5 = "print(\"TinyPie    \"    )"

re1_op = "=|\+|>|\*"#works
re2_keyW = "if|else|int|float"#works
re3_Sep = "\(|\)|\"|:|;"#works
re4_ID = "[_a-zA-Z][_a-zA-Z0-9]*"#works
re5_SgLit = "\".+\""#works
re6_int = "\d+"#works
re7_float = "\d+\.\d+"#works

def lex(s):
	LexedLine = []
	rec = s.split()
	print(s)
	print("this is rec:")
	print(rec)
	for x in rec :
		while len(x) > 0: 
			if re.match(re5_SgLit, x) != None:
				m_obj = re.match(re5_SgLit, x)
				ap = x[0:m_obj.end()]
				x = x[m_obj.end():]
				LexedLine.append("<String Literal: " + ap + ">")
			elif re.match(re2_keyW, x) != None:
				m_obj = re.match(re2_keyW, x)
				ap = x[0:m_obj.end()]
				x = x[m_obj.end():]
				LexedLine.append("<Keyword: " + ap + ">")
			elif re.match(re3_Sep, x) != None:
				m_obj = re.match(re3_Sep, x)
				ap = x[0:m_obj.end()]
				x = x[m_obj.end():]
				LexedLine.append("<Seperator: " + ap + ">")
			elif re.match(re1_op, x) != None:
				m_obj = re.match(re1_op, x)
				ap = x[0:m_obj.end()]
				x = x[m_obj.end():]
				LexedLine.append("<Operator: " + ap + ">")
			elif re.match(re4_ID, x) != None:
				m_obj = re.match(re4_ID, x)
				ap = x[0:m_obj.end()]
				x = x[m_obj.end():]
				LexedLine.append("<Identifier: " + ap + ">")
			elif re.match(re7_float, x) != None:
				m_obj = re.match(re7_float, x)
				ap = x[0:m_obj.end()]
				x = x[m_obj.end():]
				LexedLine.append("<Float Literal: " + ap + ">")
			elif re.match(re6_int,x) != None:
				m_obj = re.match(re6_int, x)
				ap = x[0:m_obj.end()]
				x = x[m_obj.end():]
				LexedLine.append("<Integer Literal: " + ap + ">")
			
	return LexedLine

print(lex(s1))
print(lex(s2))
print(lex(s3))
print(lex(s4))
print(lex(s5))
