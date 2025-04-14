#https://flask.palletsprojects.com/es/main/blueprints/



class Route():
    def init_app(self, app):
        from app.controller import brand_bp, article_bp, notification_bp
        app.register_blueprint(brand_bp, url_prefix='/api/v1')
        app.register_blueprint(article_bp, url_prefix='/api/v1')
        app.register_blueprint(notification_bp, url_prefix='/api/v1')