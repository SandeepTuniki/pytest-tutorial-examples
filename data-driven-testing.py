import pytest

def is_positive(number):
  if number >= 0:
    return True
  else:
    return False


def test_positive_case():
  assert is_positive(23) == True


def test_positive_case_1():
  assert is_positive(23) == True

def test_positive_case_2():
  assert is_positive(10) == True


@pytest.parameterize('number', [23, 10, 45, 0, 11])
def test_positive_cases(number):
  assert is_positive(number) == True


@pytest.parameterize('number', [-5, -22, -13, -54])
def test_negative_cases(number):
  assert is_positive(number) == False

  
@pytest.fixture
def positive_num():
  return 23

@pytest.fixture(params=[23, 10, 45, 0, 11])
def positive_nums(request):
  return request.param

