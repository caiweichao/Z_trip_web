import os
import pytest



if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir=./report'])
    os.system('allure serve ./report')
    os.system('allure generate  ./report/allure_results/ -o unit/allure_html')
