from PIL import Image, ImageDraw, ImageFont
def generate_certificate(name,certificateid,internshipfor,date):
    # Load the new template image
    template_path = "career/utils/certificate/internship/certificate_template.png"
    output_path = f"media/career/certificate/internship/{certificateid}.png"
    image = Image.open(template_path)

    # Initialize drawing context
    draw = ImageDraw.Draw(image)

    # Define font sizes
    font_size_name = 100
    font_size_description = 35
    font_size_verify= 20

    # Use default fonts
    font_name = ImageFont.truetype("career/utils/certificate/internship/Roboto-Bold.ttf", font_size_name)
    font_description = ImageFont.truetype("career/utils/certificate/internship/Roboto-Light.ttf", font_size_description)
    font_verify = ImageFont.truetype("career/utils/certificate/internship/Roboto-Light.ttf", font_size_verify)

    # Student details
    student_name = name
    description = (
        f"has successfully completed 4 weeks of a virtual internship program in {internshipfor} "
        f"with wonderful remarks at NEXEL in {date}. We were truly amazed by his/her showcased skills "
        "and invaluable contribution to the task and projects throughout the internship"
    )
    certificate_id = f"Certificate Id : {certificateid}"
    certificate_url = f"Certificate URL : www.nexel.in/career/certificate/verify/{certificateid}"

    # Add name to the image
    draw.text((140, 575), student_name, font=font_name, fill="black")

    draw.text((150, 1225), certificate_id, font=font_verify, fill="black")

    draw.text((150, 1268), certificate_url, font=font_verify, fill="black")

    # Draw the description
    description_lines = [
        f"has successfully completed 4 weeks of a virtual internship program in {internshipfor} ",
        f"with wonderful remarks at NEXEL in {date}. We were truly amazed by his/her showcased ",
        "skills and invaluable contribution to the task and projects throughout the internship"
    ]

    y_text = 750
    for line in description_lines:
        draw.text((150, y_text), line, font=font_description, fill="black")
        y_text += 70

    # Save the output image
    image.save(output_path)

    return output_path

