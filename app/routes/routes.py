#https://flask.palletsprojects.com/es/main/blueprints/



class Route():
    def init_app(self, app):
        from app.controller import brand_bp
        app.register_blueprint(brand_bp, url_prefix='/api/v1')