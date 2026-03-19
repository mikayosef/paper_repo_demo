"""
Convert PAPER.md to PDF format
"""
import subprocess
import sys
import os

# Check if pandoc is installed
try:
    subprocess.run(['pandoc', '--version'], capture_output=True, check=True)
    # If pandoc is installed, use it
    subprocess.run([
        'pandoc',
        'PAPER.md',
        '-o',
        'PAPER.pdf',
        '--pdf-engine=xelatex'
    ], check=True)
    print("✓ PDF created successfully using pandoc")
except (FileNotFoundError, subprocess.CalledProcessError):
    # Fallback: use python-pptx or weasyprint if available
    try:
        from weasyprint import HTML, CSS
        HTML('PAPER.md').write_pdf('PAPER.pdf')
        print("✓ PDF created successfully using weasyprint")
    except ImportError:
        try:
            # Fallback to simple text-based approach
            import pypandoc
            pypandoc.convert_file('PAPER.md', 'pdf', outputfile='PAPER.pdf')
            print("✓ PDF created successfully using pypandoc")
        except (ImportError, Exception):
            print("! PDF conversion failed. Pandoc not installed.")
            print("  Install pandoc from https://pandoc.org/installing.html")
            print("  Or install WeasyPrint: pip install weasyprint")
            sys.exit(1)
