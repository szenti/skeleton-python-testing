import unittest

from grappa import expect

class TestSomething(unittest.TestCase):

    def test_passes(self):
        expect({"success": True}).to.have.key("success").that.equal(True)
    
    @unittest.skip
    def test_breaks(self):
        expect(True).to.equal(False)

        expect({}).to.have.key()