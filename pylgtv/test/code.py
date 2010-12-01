import sys, unittest
sys.path.append('../../')
import pylgtv.televisions.lg.lh3000 as lg_lh3000
from pylgtv import FeatureNotAvailableError, BaseDriver

class TestPyLGTV(unittest.TestCase):
        def setUp(self):
                pass
        def tearDown(self):
                pass

        def test_featurenotavailerr(self):
                err = FeatureNotAvailableError('test')
                self.assertEqual(err.feature, 'test')
                self.assertEqual(err.msg, "Feature 'test' is not available")
                self.assertEqual(err.msg, str(err))
                self.assertEqual(err.msg, repr(err))


if __name__ == "__main__":
        unittest.main()
