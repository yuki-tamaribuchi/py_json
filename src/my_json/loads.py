import re


def delete_double_quotation_escape(string):
	string = string.replace("\\\\\"", "\"")
	return string


def loads_array(data):
	data = data[1:-1]
	data = data.split(", ")
	new_data = []
	for elem in data:
		if re.match(r"^[+-]?[0-9]+?$", elem):
			elem = int(elem)
		elif re.match(r"^[+-]?[0-9]*?\.[0-9]+?$", elem):
			elem = float(elem)
		elif re.match(r"\[.+?\]", elem):
			elem = loads_array(elem)
		else:
			elem = elem[1:-1]
		new_data.append(elem)
	return new_data



def loads(data):
	data = data[1:-1]


	item_list = re.compile(r"(\".+?\"):\s(\"[A-Za-z0-9\\\"]+\"|[+-]?[0-9]+\.?[0-9]*|\{.+?:\s.+?\}|\[\[.+?\]\]|\[.+?\]|null)").findall(data)

	data_dict = {}
	for k, v in item_list:
		k = delete_double_quotation_escape(k)
		v = delete_double_quotation_escape(v)
		k = k[1:-1]

		if v == "null":
			v = None
		else:
			if re.match(r"^[+-]?[0-9]+?$", v):
				v = int(v)
			elif re.match(r"^[+-]?[0-9]*?\.[0-9]+?$", v):
				v = float(v)
			elif re.match(r"^\{.+?\}", v):
				v = loads(v)
			elif re.match(r"\[.+?\]", v):
				v = loads_array(v)
			else:
				v = v[1:-1]

		data_dict[k] = v

	return data_dict