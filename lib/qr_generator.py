import qrcode
from lib.file import get_full_path
from lib.common import AppConfig
from PIL import Image, ImageDraw, ImageFont
import json


def qr_generate(arg_data, out_path='', label=None, label_font=18, embed_img=None):
    if embed_img is not None:
        face = Image.open(get_full_path('resources', 'images', 'logo.jpg'))

    qr_code = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    qr_code.add_data(str(arg_data))
    qr_code.make()
    img_qr = qr_code.make_image().convert('L')

    if embed_img is not None:
        size = 50, 50
        face = Image.open(embed_img)
        face.thumbnail(size, Image.ANTIALIAS)
        pos = ((img_qr.size[0] - face.size[0]) // 2, (img_qr.size[1] - face.size[1]) // 2)
        img_qr.paste(face, pos)

    if label is not None:
        draw = ImageDraw.Draw(img_qr)
        font = ImageFont.truetype("arial.ttf", label_font)
        draw.text((50, img_qr.size[1] - 30), label, font=font)

    img_qr.save(out_path)


def generate_rover_control_system():
    qr_cfg = AppConfig().config['rover_qr_configs']
    out_path = qr_cfg['out_path'].split('/')
    embed_logo = qr_cfg['embed_log'].split('/')
    app_name = qr_cfg['qr_app_name']
    actions = qr_cfg['action_configs']

    for action, value in dict(actions).items():
        action_id = value['qr_action_id']
        action_detail = value['qr_action_details']
        qr_label = f'{app_name} - {action_id} - {action_detail}'
        out_name = f'{action_id}_{action}.png'
        dict_data = {'app_name': app_name,
                     'action_id': action_id,
                     'action': action,
                     'action_detail': action_detail}
        json_data = json.dumps(dict_data)

        qr_generate(json_data,
                    out_path=get_full_path(*out_path) + '/' + out_name,
                    label=qr_label, embed_img=get_full_path(*embed_logo))


generate_rover_control_system()