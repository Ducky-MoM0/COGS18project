from functions import access_file, secret_file, create_password
import pytest
import mock
import builtins

def test_create_password():
    assert callable(create_password)
    with mock.patch.object(builtins, 'input', lambda _: '12345678'):
        assert create_password() == '12345678'
    with mock.patch.object(builtins, 'input', lambda _: 'abscde@3f'):
        assert create_password() == 'abscde@3f'
        
def test_secret_file():
    assert callable(secret_file)
    with mock.patch.object(builtins, 'input', lambda _: '12345678'):
        assert secret_file() == { '12345678' : 'https://youtu.be/dQw4w9WgXcQ'}

def test_access_file():
    assert callable(access_file)
    with mock.patch.object(builtins, 'input', lambda _: '12345678'):
        assert access_file() == True
    
    
    