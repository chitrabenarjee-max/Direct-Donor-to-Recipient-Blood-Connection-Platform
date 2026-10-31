from flask import Flask, render_template, request
from flask_login import LoginManager, current_user
from flask_wtf import CSRFProtect
from config import Config
from models import db
from models.user import User
from routes.auth import auth_bp
from routes.donor import donor_bp
from routes.recipient import recipient_bp
from routes.requests import requests_bp
from routes.blood_bank import blood_bank_bp
from routes.notifications import notifications_bp
from routes.admin import admin_bp
from data_locations import LOCATION_COORDS
import json
import urllib.parse
import urllib.request

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    csrf = CSRFProtect(app)

    login_manager = LoginManager(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to continue."

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    app.register_blueprint(auth_bp)
    app.register_blueprint(donor_bp)
    app.register_blueprint(recipient_bp)
    app.register_blueprint(requests_bp)
    app.register_blueprint(blood_bank_bp)
    app.register_blueprint(notifications_bp)
    app.register_blueprint(admin_bp)

    @app.context_processor
    def inject_globals():
        unread = 0
        if current_user.is_authenticated:
            from models.notification import Notification
            unread = Notification.query.filter_by(user_id=current_user.id, is_read=False).count()
        return {"unread_notifications": unread, "location_coords": LOCATION_COORDS}

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/api/geocode")
    def geocode():
        city = request.args.get("city", "").strip()
        area = request.args.get("area", "").strip()
        if not city:
            return {"ok": False, "message": "City is required."}, 400
        # First use bundled approximate coordinates; this works offline.
        from data_locations import lookup_location
        coords = lookup_location(city, area)
        if coords:
            return {"ok": True, "latitude": coords[0], "longitude": coords[1], "source": "LifePulse local approximate map"}
        # Optional free OpenStreetMap Nominatim fallback. No API key is required.
        try:
            q = f"{area}, {city}, India" if area else f"{city}, India"
            url = "https://nominatim.openstreetmap.org/search?format=json&limit=1&q=" + urllib.parse.quote(q)
            req = urllib.request.Request(url, headers={"User-Agent": "LifePulse-College-Project/1.0"})
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            if data:
                return {"ok": True, "latitude": float(data[0]["lat"]), "longitude": float(data[0]["lon"]), "source": "OpenStreetMap Nominatim approximate geocode"}
        except Exception:
            pass
        return {"ok": False, "message": "Location not found. Try a nearby area name or a supported city."}, 404

    @app.route("/profile")
    def profile():
        return render_template("profile.html", user=current_user)

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_error(e):
        db.session.rollback()
        return render_template("500.html"), 500

    with app.app_context():
        db.create_all()
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
