"""
- An *indirect parameter* is one that gets passed to a fixture before it gets sent to the test function.

- Indirect parameters can also be used to select a subset of values from a parametrized fixture.
->
Set the parameter values with the test function, instead of with the fixture function.
->
Use the same fixture with different parameter values passed in test functions.

...

"""
import pytest


@pytest.fixture()
def user(request):
	role = request.param
	print(f"\nLog in as {role}")
	yield role
	print(f"\nLog out {role}")


# Set `indirect=True` to make all parameters to be indirect or `indirect=["param1", "param2"]` for selected parameters
@pytest.mark.parametrize("user", ["admin", "member", "visitor"], indirect=True)
def test_access_rights(user):
	print(f"Test access rights for {user}")


"""
$ cd 16*
$ pytest -v -s -k "16-4 and test_access_rights"
***
test_16-4--indirect-parametrization.py::test_access_rights[admin]
Log in as admin
Test access rights for admin
PASSED
Log out admin

test_16-4--indirect-parametrization.py::test_access_rights[member] 
Log in as member
Test access rights for member
PASSED
Log out member

test_16-4--indirect-parametrization.py::test_access_rights[visitor] 
Log in as visitor
Test access rights for visitor
PASSED
Log out visitor
***
"""


@pytest.fixture()
def user_status(request):
	status = request.param
	print("\nEXTRA INFO: " + f"{status=}")
	return status


@pytest.mark.parametrize(
	"user, user_status",
	[
		("admin", "deleted"),
		("member", "offline"),
		("visitor", "online"),
	],
	indirect=["user_status"],
)
def test_status(user, user_status):
	print(f"Test status `{user_status}` for {user}")


"""
$ cd 16*
$ pytest -v -s -k "16-4 and test_status"
***
test_16-4--indirect-parametrization.py::test_status[admin-deleted] 
EXTRA INFO: status='deleted'
Test status `deleted` for admin
PASSED
test_16-4--indirect-parametrization.py::test_status[member-offline] 
EXTRA INFO: status='offline'
Test status `offline` for member
PASSED
test_16-4--indirect-parametrization.py::test_status[visitor-online] 
EXTRA INFO: status='online'
Test status `online` for visitor
PASSED
***
"""


# # # Selecting a subset of fixture parameters

@pytest.fixture(params=["admin", "member", "visitor"])
def user_role(request):
	...


def test_everyone(user_role):
	...


# Select just `"admin"` from `user_role`
@pytest.mark.parametrize("user_role", ["admin"], indirect=["user_role"])
def test_just_admin(user_role):
	...


"""
$ cd 16*
$ pytest -v -k "16-4 and (test_everyone or test_just_admin)"
***
test_16-4--indirect-parametrization.py::test_everyone[admin] PASSED                                               [ 25%]
test_16-4--indirect-parametrization.py::test_everyone[member] PASSED                                              [ 50%]
test_16-4--indirect-parametrization.py::test_everyone[visitor] PASSED                                             [ 75%]
test_16-4--indirect-parametrization.py::test_just_admin[admin] PASSED                                             [100%]
***
"""

# # # Creating an optional indirect fixture

...