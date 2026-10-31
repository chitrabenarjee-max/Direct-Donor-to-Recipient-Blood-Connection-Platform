from datetime import date, time, timedelta
from app import create_app
from models import db
from models.user import User
from models.donor import Donor
from models.recipient import Recipient
from models.blood_request import BloodRequest
from models.donor_request import DonorRequest
from models.blood_bank import BloodBank
from models.screening import Screening
from models.notification import Notification

app = create_app()

def add_user(name, email, phone, password, role, blood, city="Hyderabad", area="Central", lat=17.385, lon=78.487):
    u = User(full_name=name, email=email, phone=phone, role=role, blood_group=blood,
             city=city, area=area, latitude=lat, longitude=lon,
             date_of_birth=date(1998, 5, 15))
    u.set_password(password)
    db.session.add(u); db.session.flush()
    if role == "donor": db.session.add(Donor(user_id=u.id, availability="Available"))
    elif role == "recipient": db.session.add(Recipient(user_id=u.id))
    return u

with app.app_context():
    db.drop_all()
    db.create_all()

    admin = add_user("LifePulse Admin", "admin@lifepulse.demo", "9000000001", "Admin@123", "admin", None)
    donors = [
        add_user("Rahul Kumar", "rahul@lifepulse.demo", "9000000011", "Donor@123", "donor", "O+", area="Banjara Hills", lat=17.415, lon=78.448),
        add_user("Aisha Khan", "aisha@lifepulse.demo", "9000000012", "Donor@123", "donor", "A+", area="Mehdipatnam", lat=17.394, lon=78.431),
        add_user("Arjun Reddy", "arjun@lifepulse.demo", "9000000013", "Donor@123", "donor", "B+", area="Kukatpally", lat=17.494, lon=78.399),
        add_user("Sana Fatima", "sana@lifepulse.demo", "9000000014", "Donor@123", "donor", "O-", area="Tolichowki", lat=17.400, lon=78.410),
        add_user("Vikram Rao", "vikram@lifepulse.demo", "9000000015", "Donor@123", "donor", "AB+", area="Secunderabad", lat=17.440, lon=78.498),
    ]
    recipients = [
        add_user("Priya Sharma", "priya@lifepulse.demo", "9000000021", "Recipient@123", "recipient", "A+", area="Somajiguda"),
        add_user("Mohammed Sameer", "sameer@lifepulse.demo", "9000000022", "Recipient@123", "recipient", "O+", area="Nampally"),
        add_user("Neha Patel", "neha@lifepulse.demo", "9000000023", "Recipient@123", "recipient", "B+", area="Begumpet"),
    ]
    db.session.commit()

    banks = [
        ("CityCare Blood Bank","DEMO-SI-001","Demo directory address, Hyderabad","Hyderabad","9000000001","bank1@lifepulse.demo",17.381000,78.482500,"Pending"),
        ("LifeSaver Blood Centre","DEMO-SI-002","Demo directory address, Hyderabad","Hyderabad","9000000002","bank2@lifepulse.demo",17.389000,78.491500,"Pending"),
        ("RedHope Blood Bank","DEMO-SI-003","Demo directory address, Hyderabad","Hyderabad","9000000003","bank3@lifepulse.demo",17.397000,78.500500,"Pending"),
        ("Krishna Demo Blood Centre","DEMO-SI-004","Demo directory address, Vijayawada","Vijayawada","9000000004","bank4@lifepulse.demo",16.502000,80.643500,"Pending"),
        ("Amaravati Demo Blood Bank","DEMO-SI-005","Demo directory address, Vijayawada","Vijayawada","9000000005","bank5@lifepulse.demo",16.510000,80.652500,"Pending"),
        ("Coastal Demo Blood Bank","DEMO-SI-006","Demo directory address, Visakhapatnam","Visakhapatnam","9000000006","bank6@lifepulse.demo",17.683000,83.214500,"Pending"),
        ("Vizag Life Blood Centre","DEMO-SI-007","Demo directory address, Visakhapatnam","Visakhapatnam","9000000007","bank7@lifepulse.demo",17.691000,83.223500,"Pending"),
        ("Tirumala Demo Blood Centre","DEMO-SI-008","Demo directory address, Tirupati","Tirupati","9000000008","bank8@lifepulse.demo",13.625000,79.414500,"Pending"),
        ("Rayalaseema Demo Blood Bank","DEMO-SI-009","Demo directory address, Tirupati","Tirupati","9000000009","bank9@lifepulse.demo",13.633000,79.423500,"Pending"),
        ("Kurnool Demo Blood Centre","DEMO-SI-010","Demo directory address, Kurnool","Kurnool","9000000010","bank10@lifepulse.demo",15.824000,78.032500,"Pending"),
        ("Guntur Demo Blood Bank","DEMO-SI-011","Demo directory address, Guntur","Guntur","9000000011","bank11@lifepulse.demo",16.303000,80.431500,"Pending"),
        ("Bengaluru Demo Blood Centre","DEMO-SI-012","Demo directory address, Bengaluru","Bengaluru","9000000012","bank12@lifepulse.demo",12.968000,77.590500,"Pending"),
        ("Bangalore Life Blood Bank","DEMO-SI-013","Demo directory address, Bengaluru","Bengaluru","9000000013","bank13@lifepulse.demo",12.976000,77.599500,"Pending"),
        ("Garden City Demo Blood Bank","DEMO-SI-014","Demo directory address, Bengaluru","Bengaluru","9000000014","bank14@lifepulse.demo",12.984000,77.608500,"Pending"),
        ("Mysuru Demo Blood Centre","DEMO-SI-015","Demo directory address, Mysuru","Mysuru","9000000015","bank15@lifepulse.demo",12.292000,76.634500,"Pending"),
        ("Mysore Life Blood Bank","DEMO-SI-016","Demo directory address, Mysuru","Mysuru","9000000016","bank16@lifepulse.demo",12.300000,76.643500,"Pending"),
        ("Mangaluru Demo Blood Centre","DEMO-SI-017","Demo directory address, Mangaluru","Mangaluru","9000000017","bank17@lifepulse.demo",12.910000,74.851500,"Pending"),
        ("Coastal Karnataka Demo Blood Bank","DEMO-SI-018","Demo directory address, Mangaluru","Mangaluru","9000000018","bank18@lifepulse.demo",12.918000,74.860500,"Pending"),
        ("Hubballi Demo Blood Centre","DEMO-SI-019","Demo directory address, Hubballi","Hubballi","9000000019","bank19@lifepulse.demo",15.361000,75.119500,"Pending"),
        ("Chennai Demo Blood Centre","DEMO-SI-020","Demo directory address, Chennai","Chennai","9000000020","bank20@lifepulse.demo",13.079000,80.266500,"Pending"),
        ("Tamil Nadu Life Blood Bank","DEMO-SI-021","Demo directory address, Chennai","Chennai","9000000021","bank21@lifepulse.demo",13.087000,80.275500,"Pending"),
        ("Chennai Community Blood Centre","DEMO-SI-022","Demo directory address, Chennai","Chennai","9000000022","bank22@lifepulse.demo",13.095000,80.284500,"Pending"),
        ("Coimbatore Demo Blood Centre","DEMO-SI-023","Demo directory address, Coimbatore","Coimbatore","9000000023","bank23@lifepulse.demo",11.013000,76.951500,"Pending"),
        ("Kovai Life Blood Bank","DEMO-SI-024","Demo directory address, Coimbatore","Coimbatore","9000000024","bank24@lifepulse.demo",11.021000,76.960500,"Pending"),
        ("Madurai Demo Blood Centre","DEMO-SI-025","Demo directory address, Madurai","Madurai","9000000025","bank25@lifepulse.demo",9.921000,78.115500,"Pending"),
        ("Madurai Community Blood Bank","DEMO-SI-026","Demo directory address, Madurai","Madurai","9000000026","bank26@lifepulse.demo",9.929000,78.124500,"Pending"),
        ("Trichy Demo Blood Centre","DEMO-SI-027","Demo directory address, Tiruchirappalli","Tiruchirappalli","9000000027","bank27@lifepulse.demo",10.787000,78.700500,"Pending"),
        ("Salem Demo Blood Centre","DEMO-SI-028","Demo directory address, Salem","Salem","9000000028","bank28@lifepulse.demo",11.660000,78.141500,"Pending"),
        ("Kochi Demo Blood Centre","DEMO-SI-029","Demo directory address, Kochi","Kochi","9000000029","bank29@lifepulse.demo",9.927000,76.262500,"Pending"),
        ("Ernakulam Life Blood Bank","DEMO-SI-030","Demo directory address, Kochi","Kochi","9000000030","bank30@lifepulse.demo",9.935000,76.271500,"Pending"),
        ("Kerala Community Blood Centre","DEMO-SI-031","Demo directory address, Kochi","Kochi","9000000031","bank31@lifepulse.demo",9.943000,76.280500,"Pending"),
        ("Thiruvananthapuram Demo Blood Centre","DEMO-SI-032","Demo directory address, Thiruvananthapuram","Thiruvananthapuram","9000000032","bank32@lifepulse.demo",8.520000,76.932500,"Pending"),
        ("Trivandrum Life Blood Bank","DEMO-SI-033","Demo directory address, Thiruvananthapuram","Thiruvananthapuram","9000000033","bank33@lifepulse.demo",8.528000,76.941500,"Pending"),
        ("Kozhikode Demo Blood Centre","DEMO-SI-034","Demo directory address, Kozhikode","Kozhikode","9000000034","bank34@lifepulse.demo",11.255000,75.775500,"Pending"),
        ("Thrissur Demo Blood Centre","DEMO-SI-035","Demo directory address, Thrissur","Thrissur","9000000035","bank35@lifepulse.demo",10.524000,76.209500,"Pending"),
        ("Kollam Demo Blood Centre","DEMO-SI-036","Demo directory address, Kollam","Kollam","9000000036","bank36@lifepulse.demo",8.889000,76.609500,"Pending"),
        ("Puducherry Demo Blood Centre","DEMO-SI-037","Demo directory address, Puducherry","Puducherry","9000000037","bank37@lifepulse.demo",11.910000,79.810500,"Pending"),
        ("Pondicherry Community Blood Bank","DEMO-SI-038","Demo directory address, Puducherry","Puducherry","9000000038","bank38@lifepulse.demo",11.918000,79.819500,"Pending"),
    ]
    bank_objs=[]
    for x in banks:
        b=BloodBank(name=x[0],license_id=x[1],address=x[2],city=x[3],phone=x[4],email=x[5],
                    latitude=x[6],longitude=x[7],verification_status=x[8])
        db.session.add(b); bank_objs.append(b)
    db.session.commit()

    reqs=[]
    for i,(rec,bg,urg,status) in enumerate([
        (recipients[0],"A+","Urgent","Pending"),
        (recipients[1],"O+","Critical","Accepted"),
        (recipients[2],"B+","Normal","Completed"),
        (recipients[0],"A+","Normal","Cancelled"),
        (recipients[1],"O+","Urgent","Pending"),
    ]):
        r=BloodRequest(recipient_id=rec.recipient.id,blood_group=bg,units=2 if i%2==0 else 1,
                       urgency=urg,hospital_name="DemoCare Hospital",hospital_address="100 Hospital Road",
                       city="Hyderabad",latitude=rec.latitude or 17.385,longitude=rec.longitude or 78.487,
                       required_date=date.today()+timedelta(days=i+1),required_time=time(10+i,30),
                       notes="Fictional educational demo request.",status=status)
        db.session.add(r); reqs.append(r)
    db.session.commit()

    statuses=["Pending","Accepted","Rejected","Completed","Pending","Cancelled","Accepted","Pending"]
    for i,status in enumerate(statuses):
        dr=DonorRequest(recipient_id=reqs[i%len(reqs)].recipient_id, donor_id=donors[i%len(donors)].donor.id,
                        blood_request_id=reqs[i%len(reqs)].id,status=status)
        db.session.add(dr)
    db.session.commit()

    for i in range(5):
        dr=DonorRequest.query.offset(i).first()
        s=Screening(donor_request_id=dr.id, donor_id=dr.donor_id, blood_bank_id=bank_objs[i].id,
                    screening_date=date.today()-timedelta(days=i),
                    hemoglobin_checked=(i%2==0), blood_group_confirmed=(i%2==0),
                    infection_screening_completed=(i%3==0),
                    medical_officer_notes="DEMO RECORD ONLY; not a medical certification.",
                    final_screening_status=["Pending","Cleared by medical staff","Not cleared","Pending","Cleared by medical staff"][i])
        db.session.add(s)

    all_users = [admin] + donors + recipients
    messages = [
        "Welcome to LifePulse demo.",
        "New blood request available near your area.",
        "Preliminary matching is not medical approval.",
        "Please proceed to a verified blood bank for screening.",
        "Your donor request has been accepted.",
        "A request is waiting for your response.",
        "Blood bank verification status updated.",
        "Remember: licensed medical staff make final decisions.",
        "Demo notification for project presentation.",
        "Stay informed about active blood requests."
    ]
    for i,msg in enumerate(messages):
        db.session.add(Notification(user_id=all_users[i%len(all_users)].id,message=msg,type="info"))
    db.session.commit()
    print("Seed complete: database.db initialized with demo data.")
