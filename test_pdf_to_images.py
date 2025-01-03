import unittest
from unittest.mock import patch, MagicMock
import os
from pdfToImg import convert_pdf_to_images, convert_pdfs_in_folder

class TestPDFToImages(unittest.TestCase):
    @patch("pdfToImg.convert_from_path")
    @patch("pdfToImg.os.makedirs")
    @patch("pdfToImg.os.path.splitext")
    @patch("pdfToImg.os.path.basename")
    def test_convert_pdf_to_images(self, mock_basename, mock_splitext, mock_makedirs, mock_convert_from_path):
        # Configurer les mocks
        mock_basename.return_value = "example.pdf"
        mock_splitext.return_value = ("example", ".pdf")
        mock_makedirs.return_value = None
        mock_convert_from_path.return_value = [MagicMock(), MagicMock()]  # Simuler deux images

        # Appeler la fonction avec un chemin fictif
        result = convert_pdf_to_images("dummy/path/example.pdf")

        # Vérifications
        self.assertEqual(len(result), 2)  # Deux images doivent être retournées
        mock_makedirs.assert_called_once_with("example", exist_ok=True)
        mock_convert_from_path.assert_called_once_with("dummy/path/example.pdf", dpi=400, fmt="png")

    @patch("pdfToImg.convert_pdf_to_images")
    @patch("pdfToImg.os.listdir")
    @patch("pdfToImg.os.path.exists")
    def test_convert_pdfs_in_folder(self, mock_exists, mock_listdir, mock_convert_pdf_to_images):
        # Configurer les mocks
        mock_exists.return_value = True
        mock_listdir.return_value = ["file1.pdf", "file2.pdf", "not_a_pdf.txt"]
        mock_convert_pdf_to_images.side_effect = lambda x: [f"{x}_image1.png", f"{x}_image2.png"]

        # Appeler la fonction avec un chemin fictif
        convert_pdfs_in_folder("dummy_folder")

        # Vérifier les appels aux mocks
        expected_calls = [
            unittest.mock.call(os.path.join("dummy_folder", "file1.pdf")),
            unittest.mock.call(os.path.join("dummy_folder", "file2.pdf"))
        ]
        mock_convert_pdf_to_images.assert_has_calls(expected_calls, any_order=True)

        # Vérifier que les fichiers non PDF ne sont pas traités
        self.assertEqual(mock_convert_pdf_to_images.call_count, 2)


if __name__ == "__main__":
    unittest.main()
