def blueprints():
    from .turmas_controller import bp as turmas_bp
    from .qrcode_controller import bp as qrcode_bp
    return [turmas_bp, qrcode_bp]
