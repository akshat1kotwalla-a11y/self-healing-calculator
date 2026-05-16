import calculator

def test_addition():
	assert calculator.add(5,3)==8

def test_multiplication():
	assert multiply(4,2)==8

if __name__ == "__main__":
	test_addition()
	test_multiplication()
	print("All tests are passed")
