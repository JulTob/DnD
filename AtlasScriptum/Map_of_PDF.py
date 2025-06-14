def create_pdf(character, filename='character_sheet.pdf'):
    doc = BaseDocTemplate(filename, pagesize=letter)
    width, height = letter

    # Calculate margins and frame dimensions
    margin = inch / 2
    column_gap = inch / 8
    usable_width = width - 2 * margin
    column_width = (usable_width - column_gap) / 2
    frame_height = height - 2 * margin

    # Define frames for columns
    frame_left = Frame(margin, margin, column_width, frame_height, id='left')
    frame_right = Frame(margin + column_width + column_gap, margin, column_width, frame_height, id='right')

    # Add frames to the template
    template = PageTemplate(id='TwoColumns', frames=[frame_left, frame_right])
    doc.addPageTemplates([template])

    # Define styles
    styles = getSampleStyleSheet()
    styles['Title'].fontName = 'Times-Bold'
    styles['Title'].fontSize = 18
    styles['Title'].leading = 22
    styles['Title'].alignment = 1  # Centered

    styles.add(ParagraphStyle(
        name='Heading',
        fontName='Times-Bold',
        fontSize=14,
        leading=18,
        alignment=0,  # Left-aligned
    ))
    styles.add(ParagraphStyle(
        name='Body',
        fontName='Times-Roman',
        fontSize=12,
        leading=14,
        alignment=0,  # Left-aligned
    ))

    elements = []

    # Title
    elements.append(Paragraph("Random D&D Character", styles['Title']))
    elements.append(Spacer(1, 12))

    # Left Column Content
    left_content = f"""
    <b>Species:</b> {character['Species']}<br/>
    <b>Class:</b> {character['Class']}<br/>
    <b>Background:</b> {character['Background']}<br/>
    """
    elements.append(Paragraph(left_content, styles['Body']))
    elements.append(FrameBreak())  # Move to the next frame (right column)

    # Right Column Content
    stats_content = "<b>Stats:</b><br/>"
    for stat, value in character['Stats'].items():
        mod = (value - 10) // 2
        stats_content += f"{stat}: {value} ({mod:+})<br/>"
    elements.append(Paragraph(stats_content, styles['Body']))
    elements.append(FrameBreak())

    doc.build(elements)
