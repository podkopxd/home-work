def test_function():
    def inner_function():
        print('I’m in the visibility area of the function test_function')

    inner_function()


test_function()
