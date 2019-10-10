import os
import pytest



if __name__ == '__main__':
    pytest.main(['-s','-q','--alluredir','./report'])
    os.system('allure generate report/ -o report/html --clean')
