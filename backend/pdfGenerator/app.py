from flask import Flask, render_template, send_file
from datetime import datetime
from weasyprint import HTML
import io

# Initialize the Flask application
app = Flask(__name__)

# A simple route to generate an invoice page
@app.route('/generate_invoice')
def generate_invoice():
    # Example data for the invoice (normally, this would come from a database or form input)
    to_addr = {
        'company_name': 'Acme Corp',
        'person_name': 'John Dilly',
        'person_email': 'john@example.com',
        'grade': 'A+',  # Added grade
        'school': 'Sunshine High School'  # Added school
    }

    items = [
        {'title': 'Website Design', 'charge': 300.00},
        {'title': 'Hosting (3 months)', 'charge': 75.00},
        {'title': 'Domain Name (1 year)', 'charge': 10.00}
    ]

    # Data for the invoice (company address, etc.)
    today = datetime.today().strftime("%B %d, %Y")
    invoice_number = 123
    from_addr = {
        'company_name': 'YSPrep',
        'addr1': '2920 Huntington Dr. Suite 110B',
        'addr2': 'San Marino, CA 91108',
        'phone': '626-286-0200',
        'website': 'www.YSPrep.com',
        'email': 'YSPrep@gmail.com'
    }

    # Due date (first day of the current month)
    duedate = (datetime.today().replace(day=1).strftime("%B 1, %Y"))
    
    # Calculate total
    total = sum(item['charge'] for item in items)
    
    # Add a note
    note = "Thank you for your business! Please feel free to contact us for further assistance."

    # Render the HTML template
    rendered = render_template(
        'invoice.html',
        date=today,
        from_addr=from_addr,
        to_addr=to_addr,
        items=items,
        total=total,
        invoice_number=invoice_number,
        duedate=duedate,
        note=note
    )

    # Generate the PDF in memory
    html = HTML(string=rendered)
    pdf = html.write_pdf()

    # Return the PDF as a downloadable file
    return send_file(
        io.BytesIO(pdf),
        download_name='invoice.pdf',
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)
