from routes.landing import landing_bp
from routes.register import register_bp
from routes.login import login_bp
from routes.index import index_bp
from routes.logout import logout_bp
from routes.delete import delete_bp
from routes.otp import otp_bp

all_blueprints = [
    landing_bp,
    register_bp,
    login_bp,
    index_bp,
    logout_bp,
    delete_bp,
    otp_bp,
]


def register_routes(app):
    """Registers all blueprints and creates endpoint aliases for clean route management."""
    for bp in all_blueprints:
        app.register_blueprint(bp)

    # Allow unqualified url_for calls (e.g. url_for('login'), url_for('register'))
    # used in templates and redirects without breaking blueprint namespacing
    for rule in list(app.url_map.iter_rules()):
        if '.' in rule.endpoint:
            short_endpoint = rule.endpoint.split('.', 1)[1]
            if short_endpoint not in app.view_functions:
                app.add_url_rule(
                    rule.rule,
                    endpoint=short_endpoint,
                    view_func=app.view_functions[rule.endpoint],
                    methods=rule.methods,
                )


__all__ = [
    'register_routes',
    'all_blueprints',
    'landing_bp',
    'register_bp',
    'login_bp',
    'index_bp',
    'logout_bp',
    'delete_bp',
    'otp_bp',
]
