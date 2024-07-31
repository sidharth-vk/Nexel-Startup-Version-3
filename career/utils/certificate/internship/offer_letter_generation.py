from PIL import Image, ImageDraw, ImageFont
from django.utils.dateformat import format

def generate_offerletter(name, certificateid, internshipfor, date_of_issue, email):
    # Load the new template image
    template_path = "career/utils/certificate/internship/offer_letter_template.png"
    output_path = f"media/career/certificate/offerletter/{certificateid}.png"
    image = Image.open(template_path)

    # Initialize drawing context
    draw = ImageDraw.Draw(image)

    # Define font sizes
    font_size_name = 35
    font_size_address = 30

    # Use default fonts
    font_name = ImageFont.truetype("career/utils/certificate/internship/Roboto-Bold.ttf", font_size_name)
    font_address = ImageFont.truetype("career/utils/certificate/internship/Roboto-Light.ttf", font_size_address)
    
    # Format the date
    formatted_date = format(date_of_issue, 'd M Y')  # Formats date as '29 Jul 2024'
    
    # Student details
    student_name = name
    std_email_id = email
    std_domain = f"Domain: {internshipfor}"
    std_commence_date = f"Commence Date: {formatted_date}"

    # Add text to the image
    draw.text((140, 550), student_name, font=font_address, fill="black")
    draw.text((140, 605), std_email_id, font=font_address, fill="black")
    draw.text((140, 932), std_domain, font=font_name, fill="black")
    draw.text((140, 990), std_commence_date, font=font_name, fill="black")

    # Save the output image
    image.save(output_path)

    return output_path
