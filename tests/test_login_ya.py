import configparser
import pytest
from main import login_ya

config = configparser.ConfigParser()
config.read('tests/token.ini')
ya_login1 = config['DEFAULT']['ya_login1']
ya_login2 = config['DEFAULT']['ya_login2']
ya_pass1 = config['DEFAULT']['ya_pass1']
ya_pass2 = config['DEFAULT']['ya_pass2']
FIXTURES = [(ya_login1, ya_pass1, 'Яндекс ID'), (ya_login2, ya_pass2, 'Яндекс ID')]

@pytest.mark.parametrize('a, b, etalon', FIXTURES)
def test_login_ya(a, b, etalon):
    result = login_ya(a, b)
    assert result == etalon

