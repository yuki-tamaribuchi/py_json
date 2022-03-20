from my_json import dumps, loads

def test(data):
	print("data: ", data)
	dumps_data = dumps(data)
	print("dumps_data: ", dumps_data)
	loads_data = loads(dumps_data)
	print("loads_data: ", loads_data)
	print("match: ", data==loads_data)

	print("-----------------------------------------------------\r\n")


if __name__ == "__main__":
	data = {"sample": "hello", "sample2": "world"}
	test(data)

	data = {"sa\"m\"ple":"he\"ll\"o", "sa\"mp\"le2":"wo\"rl\"d"}
	test(data)

	data = {"int":123, "minus_int":-123}
	test(data)

	data = {"float": 1.23, "minus_float":-1.23}
	test(data)

	data = {"null": None}
	test(data)
	
	data = {"dict":{"sample":"hello", "sample2":"world"}}
	test(data)

	data = {"list": [1, 2, -3]}
	test(data)

	data = {"list": [1.23, 2.34, -3.45]}
	test(data)


	data = {"list": ["a", "b", "c"]}
	test(data)

	data = {"list": [1]}
	test(data)



	#error

	data = {"list": [[1,2,3], [4,5,6]]}
	test(data)


	#data = {"list_dict":[{"sample":"hello", "sample2":"world"}]}
	#test(data)