import  python_pytest_function

import pytest

def test_api_requests():
    """test if api request status code is 200"""
    r = python_pytest_function.api_request()
    assert r.status_code == 200

def test_repo_count():
    """check if respo star count is  more than 1_000"""
    r = python_pytest_function.api_request()
    responsive_dict = r.json()
    assert 'items' in responsive_dict
    assert len(responsive_dict['items']) == 30

def test_total_repo():
    r = python_pytest_function.api_request()
    responsive_dict = r.json()
    assert responsive_dict['total_count'] > 1_000
