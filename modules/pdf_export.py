from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def export_report(report_text, output_path="Executive_Report.pdf"):
    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(output_path)

    story = []

    for line in report_text.split("\n"):
        story.append(Paragraph(line, styles["BodyText"]))

    doc.build(story)

    return output_path