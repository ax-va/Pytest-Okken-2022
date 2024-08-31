## pytest vs. unittest

| pytest               | unittest               |
|----------------------|------------------------|
| assert something     | assertTrue(something)  |
| assert not something | assertFalse(something) |
| assert a == b        | assertEqual(a, b)      |
| assert a != b        | assertNotEqual(a, b)   |
| assert a is None     | assertIsNone(a)        |
| assert a is not None | assertIsNotNone(a)     |
| assert a <= b        | assertLessEqual(a, b)  |
| ...                  | ...                    |

pytest rewrites the `assert` statement to tell more about why assertions failed