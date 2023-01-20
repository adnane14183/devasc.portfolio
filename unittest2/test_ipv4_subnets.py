import unittest
import IPv4_subnets as t

class test_ipv4_subnets(unittest.TestCase):

    def test_get_netprefix(self):
        self.assertEqual(t.get_net_prefix('255.255.255.252'), '/30')

    def test_get_netmask(self):
        self.assertEqual(t.get_netmask('30'), '255.255.255.252')


if __name__ == '__main__':
    unittest.main()