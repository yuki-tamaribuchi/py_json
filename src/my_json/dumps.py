def espace_double_quotation(string):
	string = string.replace("\"", "\\\\\"")
	return string

def convert_list(data):
	item_list = []
	for item in data:
		if type(item) == str:
			item_list.append("\""+item+"\"")
		elif type(item) == dict:
			item = dumps(item)
			item_list.append(item)
		elif type(item) == list:
			item = convert_list(item)
			item_list.append(item)
		else:
			item_list.append(str(item))
	return "[" + ", ".join(item_list) + "]"
	

def dumps(data):
	assert(type(data)==dict)

	item_list = []
	
	for k, v in data.items():
		k = espace_double_quotation(k)
		k = "\"" + k + "\""

		if v is None:
			v = "null"
		elif type(v) == str:
			v = espace_double_quotation(v)
			v = "\"" + v + "\""
		elif type(v) == dict:
			v = dumps(v)
		elif type(v) == list:
			v = convert_list(v)
		elif type(v) in [int, float]:
			pass
		else:
			print("Type {} is not supported.".format(type(v)))
			raise Exception

		item_list.append("{}: {}".format(k ,v))
	
	return "{" + ", ".join(item_list) + "}"		