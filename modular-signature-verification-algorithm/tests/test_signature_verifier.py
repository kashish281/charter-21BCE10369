import unittest
from src.signature_verifier import SignatureVerifier

class TestSignatureVerifier(unittest.TestCase):
    def setUp(self):
        self.verifier = SignatureVerifier()

    def test_verify_ecdsa_signature(self):
        address = "0xExampleAddress"
        signature_data = b"\x00\x01\x02"  # Example byte data
        signed_hash = b"\x00" * 32  # Example hash
        result = self.verifier.verify_signature(address, signature_data, signed_hash, scheme_type="ecdsa")
        self.assertTrue(result)

    def test_verify_schnorr_signature(self):
        address = "0xExampleAddress"
        signature_data = b"\x00\x01\x02"  # Example byte data
        signed_hash = b"\x00" * 32  # Example hash
        result = self.verifier.verify_signature(address, signature_data, signed_hash, scheme_type="schnorr")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()

