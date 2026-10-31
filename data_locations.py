# Approximate city/area coordinates for the educational prototype.
# These are not precise residential locations and should not be treated as GPS data.
LOCATION_COORDS = {
    'Kurnool': {'Kurnool': (15.8281, 78.0373)},
    'Hyderabad': {'Banjara Hills': (17.4156, 78.4484), 'Mehdipatnam': (17.3939, 78.4315), 'Kukatpally': (17.4849, 78.4138), 'Tolichowki': (17.4001, 78.4100), 'Secunderabad': (17.4399, 78.4983), 'Somajiguda': (17.4239, 78.4738), 'Nampally': (17.3850, 78.4867), 'Begumpet': (17.4447, 78.4622), 'Hitech City': (17.4435, 78.3772), 'Central': (17.3850, 78.4867)},
    'Vijayawada': {'Benz Circle': (16.5062, 80.6480), 'Governorpet': (16.5142, 80.6346), 'Central': (16.5062, 80.6480)},
    'Visakhapatnam': {'Dwaraka Nagar': (17.7220, 83.3047), 'MVP Colony': (17.7394, 83.3272), 'Central': (17.6868, 83.2185)},
    'Tirupati': {'Tirupati': (13.6288, 79.4192), 'Central': (13.6288, 79.4192)},
    'Guntur': {'Arundelpet': (16.3067, 80.4365), 'Central': (16.3067, 80.4365)},
    'Nellore': {'Nellore': (14.4426, 79.9865), 'Central': (14.4426, 79.9865)},
    'Warangal': {'Hanamkonda': (18.0000, 79.5800), 'Central': (17.9689, 79.5941)},
    'Karimnagar': {'Karimnagar': (18.4386, 79.1288), 'Central': (18.4386, 79.1288)},
    'Bengaluru': {'Koramangala': (12.9352, 77.6245), 'Indiranagar': (12.9784, 77.6408), 'Jayanagar': (12.9250, 77.5938), 'Whitefield': (12.9698, 77.7499), 'Central': (12.9716, 77.5946)},
    'Mysuru': {'Vijayanagar': (12.3310, 76.6060), 'Central': (12.2958, 76.6394)},
    'Mangaluru': {'Hampankatta': (12.8698, 74.8431), 'Central': (12.9141, 74.8560)},
    'Hubballi': {'Hubballi': (15.3647, 75.1240), 'Central': (15.3647, 75.1240)},
    'Belagavi': {'Belagavi': (15.8497, 74.4977), 'Central': (15.8497, 74.4977)},
    'Chennai': {'T Nagar': (13.0418, 80.2341), 'Adyar': (13.0012, 80.2565), 'Anna Nagar': (13.0850, 80.2101), 'Velachery': (12.9815, 80.2180), 'Central': (13.0827, 80.2707)},
    'Coimbatore': {'RS Puram': (11.0050, 76.9525), 'Gandhipuram': (11.0168, 76.9670), 'Central': (11.0168, 76.9558)},
    'Madurai': {'KK Nagar': (9.9272, 78.1365), 'Central': (9.9252, 78.1198)},
    'Tiruchirappalli': {'Srirangam': (10.8624, 78.6837), 'Central': (10.7905, 78.7047)},
    'Salem': {'Salem': (11.6643, 78.1460), 'Central': (11.6643, 78.1460)},
    'Tirunelveli': {'Tirunelveli': (8.7139, 77.7567), 'Central': (8.7139, 77.7567)},
    'Kochi': {'Ernakulam': (9.9816, 76.2999), 'Kakkanad': (10.0159, 76.3419), 'Central': (9.9312, 76.2673)},
    'Thiruvananthapuram': {'Kowdiar': (8.5241, 76.9366), 'Central': (8.5241, 76.9366)},
    'Kozhikode': {'Kozhikode': (11.2588, 75.7804), 'Central': (11.2588, 75.7804)},
    'Thrissur': {'Thrissur': (10.5276, 76.2144), 'Central': (10.5276, 76.2144)},
    'Kollam': {'Kollam': (8.8932, 76.6141), 'Central': (8.8932, 76.6141)},
    'Puducherry': {'White Town': (11.9341, 79.8301), 'Central': (11.9139, 79.8145)},
}

def lookup_location(city, area):
    city = (city or '').strip()
    area = (area or '').strip()
    for c, areas in LOCATION_COORDS.items():
        if c.lower() == city.lower():
            for a, coords in areas.items():
                if a.lower() == area.lower(): return coords
            return next(iter(areas.values()))
    return None
