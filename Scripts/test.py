import allure
class Test_aa:

    def test_01(self):
        allure.attach("描述","描述内容")
        with open("./Screen/test_0011.png","rb")as f:
            allure.attach("截图名字",f.read(),allure.attach_type.PNG)
    def test_002(self):
        assert 1,self.test_01()

    def test_003(self):
        assert 0,self.test_01()


