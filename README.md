# LifePulse — Smart Direct Donor-to-Acceptor Blood Connection Platform

Educational college mini-project built with Python, Flask, SQLite, SQLAlchemy ORM, Flask-Login and vanilla HTML/CSS/JavaScript.

## Safety disclaimer
This is only a software prototype. The donor matching feature is a **preliminary software filter** based on demonstration ABO/Rh rules. **Final donor eligibility, blood compatibility, infection screening, and transfusion decisions must be performed by qualified medical professionals at a licensed blood bank or hospital.** Demo screening records are not medical certificates.

## Features
- Donor and recipient registration/login with password hashing
- Role-based donor, recipient and admin dashboards
- Blood request CRUD flow
- Preliminary blood-group matching
- Haversine approximate-distance sorting
- Donor accept/reject workflow
- Verified blood bank directory
- Demo screening records
- In-app notifications
- Admin management and account disabling
- JSON API endpoints
- Responsive Bootstrap 5 UI
- SQLite database with seed data

## Installation
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
pip install -r requirements.txt
python seed.py
python app.py
```
Open http://127.0.0.1:5000/

## Demo credentials
- Admin: admin@lifepulse.demo / Admin@123
- Donor: donor@lifepulse.demo / Donor@123
- Recipient: recipient@lifepulse.demo / Recipient@123

These credentials are fictional and intended only for local educational demonstration.

## Database
SQLite file: `database.db`

Tables:
users, donors, recipients, blood_requests, donor_requests, blood_banks, screenings, notifications.

Run `python seed.py` to recreate the database and sample records.

## API
- `GET /api/donors?blood_group=O+&city=Hyderabad&availability=Available`
- `GET /api/donors/match?request_id=1`
- `GET /blood-banks/api`
- `GET /api/requests`
- `POST /api/donor-requests`
- `PUT /api/donor-requests/<id>`
- `GET /notifications/api` returns the authenticated user's notifications as JSON.

## Screenshots
Add screenshots of the home page, dashboards, matching page, admin page and blood-bank page here for your college report.

## Folder structure
See the project tree included in this ZIP.

## Limitations
- Location values are approximate demo coordinates.
- No external maps, SMS, email or payment service is required.
- Medical screening is intentionally not automated.
- Matching rules are educational and must not be used for clinical decisions.

## Future enhancements
- Hospital/blood-bank appointment integration
- Optional map visualization
- Email/SMS notifications through approved providers
- Audit logs
- Stronger account verification
- Production deployment with secure secrets and HTTPS

## Registration and location automation

Registration now requires **Confirm Password** and rejects mismatched passwords. City and area are used to automatically fill approximate latitude/longitude. LifePulse first checks its bundled South India location map; for an unsupported location it can fall back to the free OpenStreetMap Nominatim geocoder when internet access is available. Exact home coordinates should not be entered in this educational prototype.

## South India blood-bank directory seed

The included database contains demo directory records covering major cities across Andhra Pradesh, Telangana, Karnataka, Tamil Nadu, Kerala and Puducherry. These records are deliberately marked **Pending** and use fictional contact details; they are not claims of current real-world blood-bank availability. For real facilities and current availability, consult the Government of India's e-RaktKosh blood-centre directory. e-RaktKosh provides a blood-centre directory and nationwide blood-centre services.
