import qrcode


class QR:
    def __init__(self) -> None:
        self.__image_name = "qr.png"
        self.qr_img = None

    def create_qr_image(self, qr_data):
        self.qr_img = qrcode.make(qr_data)
        self.qr_img.save(self.__image_name)
