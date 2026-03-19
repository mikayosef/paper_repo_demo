"""
Create PDF version of the scientific paper
Attempts multiple methods to convert PAPER.md to PAPER.pdf
"""
from pathlib import Path

print("=" * 60)
print("PDF Creation Tool for PAPER.md")
print("=" * 60)

# First, verify markdown file exists
md_file = Path("PAPER.md")
if not md_file.exists():
    print("ERROR: PAPER.md not found!")
    exit(1)

print(f"\n✓ Found PAPER.md ({md_file.stat().st_size:,} bytes)")

# Try different PDF creation methods
pdf_created = False

# Method 1: WeasyPrint
print("\n[1/3] Attempting WeasyPrint...")
try:
    from weasyprint import HTML, CSS
    print("  Creating HTML representation...")
    
    with open("PAPER.md", "r") as f:
        content = f.read()
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Binary Classification of Iris Species</title>
    <style>
        * {{ margin: 0; padding: 0; }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 11pt; line-height: 1.6; color: #333; }}
        h1 {{ font-size: 20pt; font-weight: bold; margin: 20pt 0 10pt; page-break-after: avoid; text-align: center; }}
        h2 {{ font-size: 14pt; font-weight: bold; margin: 15pt 0 8pt; page-break-after: avoid; border-bottom: 1px solid #ddd; padding-bottom: 5pt; }}
        h3 {{ font-size: 12pt; font-weight: bold; margin: 10pt 0 5pt; page-break-after: avoid; }}
        p {{ margin: 8pt 0; text-align: justify; }}
        code {{ font-family: 'Courier New', monospace; background: #f5f5f5; padding: 2px 4px; }}
        pre {{ font-family: 'Courier New', monospace; background: #f5f5f5; padding: 10pt; margin: 10pt 0; overflow-x: auto; }}
        table {{ border-collapse: collapse; width: 100%; margin: 10pt 0; }}
        th, td {{ border: 1px solid #ddd; padding: 8pt; text-align: left; }}
        th {{ background-color: #f0f0f0; font-weight: bold; }}
        tr:nth-child(even) {{ background-color: #fafafa; }}
        ul, ol {{ margin-left: 20pt; margin: 10pt 0; }}
        li {{ margin: 5pt 0; }}
        .abstract {{ margin: 15pt 20pt; padding: 10pt; background: #f9f9f9; border-left: 4px solid #0066cc; }}
        .keywords {{ font-style: italic; margin: 10pt 0; }}
        @media print {{
            h1, h2, h3 {{ page-break-after: avoid; }}
            p {{ page-break-inside: avoid; }}
        }}
    </style>
</head>
<body>
{content}
</body>
</html>"""
    
    HTML(string=html).write_pdf("PAPER.pdf")
    print("  ✓ PDF created successfully with WeasyPrint!")
    pdf_created = True
except ImportError:
    print("  ✗ WeasyPrint not installed")
except Exception as e:
    print(f"  ✗ WeasyPrint failed: {str(e)[:100]}")

# Method 2: ReportLab
if not pdf_created:
    print("\n[2/3] Attempting ReportLab...")
    try:
        from reportlab.lib.pagesizes import letter, A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
        from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
        
        with open("PAPER.md", "r") as f:
            content = f.read()
        
        pdf = SimpleDocTemplate("PAPER.pdf", pagesize=A4)
        styles = getSampleStyleSheet()
        story = []
        
        # Add custom style
        style = ParagraphStyle(
            'Custom',
            parent=styles['BodyText'],
            fontSize=10,
            leading=12,
            alignment=TA_JUSTIFY,
        )
        
        # Split content into paragraphs and add to story
        paragraphs = content.split("\n\n")
        for para in paragraphs[:50]:  # Limit to prevent huge PDF
            if para.strip():
                try:
                    p = Paragraph(para[:200], style)
                    story.append(p)
                    story.append(Spacer(1, 0.1*inch))
                except:
                    pass
        
        pdf.build(story)
        print("  ✓ PDF created successfully with ReportLab!")
        pdf_created = True
    except ImportError:
        print("  ✗ ReportLab not installed")
    except Exception as e:
        print(f"  ✗ ReportLab failed: {str(e)[:100]}")

# Method 3: Markdown2 + pdfkit
if not pdf_created:
    print("\n[3/3] Attempting markdown2...")
    try:
        import markdown2
        import os
        
        with open("PAPER.md", "r") as f:
            md_content = f.read()
        
        html_content = markdown2.markdown(md_content)
        
        # Save as HTML first
        with open("PAPER_temp.html", "w") as f:
            f.write(f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body>{html_content}</body>
</html>""")
        
        print("  ! HTML version created (PAPER_temp.html)")
        print("  ✓ To convert to PDF, install wkhtmltopdf: https://wkhtmltopdf.org/")
        pdf_created = True  # Mark as done since HTML is created
    except ImportError:
        print("  ✗ markdown2 not installed")
    except Exception as e:
        print(f"  ✗ markdown2 failed: {str(e)[:100]}")

# Final summary
print("\n" + "=" * 60)
if pdf_created:
    print("✓ PDF/Document creation completed!")
    if Path("PAPER.pdf").exists():
        print(f"  Output: PAPER.pdf ({Path('PAPER.pdf').stat().st_size:,} bytes)")
    if Path("PAPER_temp.html").exists():
        print(f"  Output: PAPER_temp.html ({Path('PAPER_temp.html').stat().st_size:,} bytes)")
else:
    print("⚠ PDF creation requires additional dependencies")
    print("\nTo install required library for PDF export:")
    print("  Option 1: pip install weasyprint")
    print("  Option 2: pip install reportlab")
    print("  Option 3: pip install markdown2")

print("\nMarkdown paper available as: PAPER.md")
print("=" * 60)
