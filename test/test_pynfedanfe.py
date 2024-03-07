import os
import unittest
from xml.etree import ElementTree as ET
from io import BytesIO

from pynfedanfe import danfe


class TestPynfedance(unittest.TestCase):
    def setUp(self):
        test_data_path = os.path.join(
            os.path.dirname(__file__), "data", "NFe_teste_cee.xml"
        )
        with open(test_data_path, "r") as f:
            self.cce_xml = f.read()
        self.xml_root = ET.fromstring(self.cce_xml)

    def test_format_cnpj_cpf(self):
        nfedanfe_instance = danfe
        cpf = nfedanfe_instance.format_cnpj_cpf("76586507812")
        self.assertEqual("765.865.078-12", cpf)

    def test_format_number(self):
        nfedanfe_instance = danfe
        number = nfedanfe_instance.format_number("19500")
        self.assertEqual("19.500,00", number)

    def test_tagtext_found(self):
        nfedanfe_instance = danfe
        text = nfedanfe_instance.tagtext(self.xml_root, "cTag")
        self.assertEqual(text, "")

    def test_create_danfe_pdf(self):
        self.xml_root = ET.fromstring(self.cce_xml)

        object_danfe = danfe.danfe(
            list_xml=[self.xml_root],
        )

        tmpDanfe = BytesIO()
        object_danfe.writeto_pdf(tmpDanfe)
        danfe_pdf = tmpDanfe.getvalue()
        tmpDanfe.close()
        self.assertTrue(len(danfe_pdf) > 0)


if __name__ == "__main__":
    unittest.main()
