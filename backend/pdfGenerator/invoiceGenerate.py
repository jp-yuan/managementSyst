from fpdf import FPDF
from datetime import date

class InvoiceGenerator:
    def __init__(self, invoice_number, date_of_issue, company_name, company_address, client_name, client_address, client_school, client_grade, branch, items, note):
        self.invoice_number = invoice_number
        self.date_of_issue = date_of_issue
        self.company_name = company_name
        self.company_address = company_address
        self.client_name = client_name
        self.client_address = client_address
        self.client_school = client_school
        self.client_grade = client_grade
        self.branch = branch
        self.items = items
        self.note = note
        self.pdf = FPDF()

    def add_header(self):
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(200, 10, txt="INVOICE", ln=True, align='C')
        self.pdf.ln(10)

        # Company details (aligned to the right)
        self.pdf.set_font("Arial", 'B', 12)
        self.pdf.cell(300, 10, f"{self.company_name}", ln=True, align='R')
        self.pdf.set_font("Arial", '', 12)
        self.pdf.cell(300, 10, f"{self.company_address}", ln=True, align='R')
        self.pdf.ln(10)

        # Client details (still aligned to the left)
        self.pdf.set_font("Arial", 'B', 12)
        self.pdf.cell(100, 10, f"Bill To: {self.client_name}", ln=True)
        self.pdf.set_font("Arial", '', 12)
        self.pdf.cell(100, 10, f"{self.client_address}", ln=True)
        self.pdf.cell(100, 10, f"School: {self.client_school}", ln=True)
        self.pdf.cell(100, 10, f"Grade: {self.client_grade}", ln=True)
        self.pdf.ln(10)

        # Additional Information
        self.pdf.set_font("Arial", 'B', 12)
        self.pdf.cell(100, 10, f"Branch: {self.branch}", ln=True)
        self.pdf.ln(5)

        # Invoice date and number (aligned to the right)
        self.pdf.set_font("Arial", '', 12)
        self.pdf.cell(100, 10, f"Invoice Number: {self.invoice_number}", ln=True, align='R')
        self.pdf.cell(100, 10, f"Date: {self.date_of_issue}", ln=True, align='R')
        self.pdf.ln(10)

            
    def add_items(self):
        # Table header
        self.pdf.set_font("Arial", 'B', 12)
        self.pdf.cell(100, 10, 'Description', 1, 0, 'C')
        self.pdf.cell(30, 10, 'Unit Price', 1, 0, 'C')
        self.pdf.cell(30, 10, 'Quantity', 1, 0, 'C')
        self.pdf.cell(30, 10, 'Total', 1, 1, 'C')
        
        # Table content
        self.pdf.set_font("Arial", '', 12)
        total_amount = 0
        for item in self.items:
            description, unit_price, quantity = item
            total_item = unit_price * quantity
            self.pdf.cell(100, 10, description, 1)
            self.pdf.cell(30, 10, f"${unit_price:.2f}", 1, 0, 'C')
            self.pdf.cell(30, 10, f"{quantity}", 1, 0, 'C')
            self.pdf.cell(30, 10, f"${total_item:.2f}", 1, 1, 'C')
            total_amount += total_item
        
        # Total Amount
        self.pdf.ln(5)
        self.pdf.set_font("Arial", 'B', 12)
        self.pdf.cell(160, 10, 'TOTAL', 1)
        self.pdf.cell(30, 10, f"${total_amount:.2f}", 1, 1, 'C')

    def add_footer(self):
        # Note/Message
        self.pdf.ln(10)
        self.pdf.set_font("Arial", 'I', 12)
        self.pdf.multi_cell(0, 10, f"Note: {self.note}")
        
        # Payment Information
        self.pdf.ln(10)
        self.pdf.set_font("Arial", 'B', 12)
        self.pdf.cell(200, 10, "Payment Information", ln=True, align='C')
        
        # Zelle info
        self.pdf.set_font("Arial", '', 12)
        self.pdf.multi_cell(0, 10, "Zelle Information:\nEmail: stevepark.vs@gmail.com\nCompany Name: Veritas Scholars")
        
        # Venmo info
        self.pdf.ln(5)
        self.pdf.multi_cell(0, 10, "Venmo Information:\nVenmo ID: @YoungScholars-1200")
        
        # Check payment info
        self.pdf.ln(5)
        self.pdf.multi_cell(0, 10, "Make all checks payable to:\nYoung Scholars")
        
        # Thank you message
        self.pdf.ln(5)
        self.pdf.set_font("Arial", 'I', 12)
        self.pdf.cell(200, 10, txt="Thank you for your business!", ln=True, align='C')

    def generate_pdf(self, filename="invoice.pdf"):
        self.pdf.add_page()
        self.add_header()
        self.add_items()
        self.add_footer()
        self.pdf.output(filename)

# Example Usage
invoice_number = "INV12345"
date_of_issue = date.today().strftime("%B %d, %Y")
company_name = "Tech Solutions LLC"
company_address = "123 Tech Street, Silicon Valley, CA"
client_name = "John Doe"
client_address = "456 Elm St, Springfield, IL"
client_school = "Springfield High School"
client_grade = "10th Grade"
branch = "Main Branch"
items = [
    ("Web Development Service", 50, 5),  # Description, Unit Price, Quantity
    ("SEO Optimization", 30, 3),
    ("Hosting Fee", 10, 12)
]
note = "This is a special service package. Please ensure payment is made by the due date."

invoice = InvoiceGenerator(invoice_number, date_of_issue, company_name, company_address, client_name, client_address, client_school, client_grade, branch, items, note)
invoice.generate_pdf("invoice_output_with_payment_info.pdf")
