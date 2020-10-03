import qrcode
from lib.file import get_full_path
from PIL import Image, ImageDraw, ImageFont


def qr_generate(arg_data, out_path='', label=None, label_font=20, embed_img=None):
    if embed_img is not None:
        face = Image.open(get_full_path('resources', 'images', 'logo.jpg'))

    qr_code = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    qr_code.add_data(str(arg_data))
    qr_code.make()
    img_qr = qr_code.make_image().convert('L')
    if embed_img is not None:
        face = Image.open(embed_img)
        pos = ((img_qr.size[0] - face.size[0]) // 2, (img_qr.size[1] - face.size[1]) // 2)
        img_qr.paste(face, pos)
    if label is not None:
        draw = ImageDraw.Draw(img_qr)
        font = ImageFont.truetype("arial.ttf", label_font)
        draw.text((50, 340), label, font=font)

    img_qr.save(out_path)


qr_generate('master_data',
            out_path=get_full_path('resources', 'generated', 'qr_codes') + '/' + 'qr_generated.png',
            label='This is a sample label', embed_img=get_full_path('resources', 'images', 'logo.jpg'))
#
# qr_generate('master_data',
#             out_path=get_full_path('resources', 'generated', 'qr_codes') + '/' + 'qr_generated.png')
