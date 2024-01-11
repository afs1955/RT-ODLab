# Transform config


# ----------------------- YOLOv5-Style Transform -----------------------
yolov5_x_trans_config = {
    'aug_type': 'yolov5',
    # Basic Augment
    'degrees': 0.0,
    'translate': 0.2,
    'scale': [0.1, 2.0],
    'shear': 0.0,
    'perspective': 0.0,
    'hsv_h': 0.015,
    'hsv_s': 0.7,
    'hsv_v': 0.4,
    'use_ablu': True,
    # Mosaic & Mixup
    'mosaic_prob': 1.0,
    'mixup_prob': 0.2,
    'mosaic_type': 'yolov5_mosaic',
    'mixup_type': 'yolov5_mixup',
    'mixup_scale': [0.5, 1.5]   # "mixup_scale" is not used for YOLOv5MixUp
}

yolov5_l_trans_config = {
    'aug_type': 'yolov5',
    # Basic Augment
    'degrees': 0.0,
    'translate': 0.2,
    'scale': [0.1, 2.0],
    'shear': 0.0,
    'perspective': 0.0,
    'hsv_h': 0.015,
    'hsv_s': 0.7,
    'hsv_v': 0.4,
    'use_ablu': True,
    # Mosaic & Mixup
    'mosaic_prob': 1.0,
    'mixup_prob': 0.15,
    'mosaic_type': 'yolov5_mosaic',
    'mixup_type': 'yolov5_mixup',
    'mixup_scale': [0.5, 1.5]   # "mixup_scale" is not used for YOLOv5MixUp
}

yolov5_m_trans_config = {
    'aug_type': 'yolov5',
    # Basic Augment
    'degrees': 0.0,
    'translate': 0.2,
    'scale': [0.1, 2.0],
    'shear': 0.0,
    'perspective': 0.0,
    'hsv_h': 0.015,
    'hsv_s': 0.7,
    'hsv_v': 0.4,
    'use_ablu': True,
    # Mosaic & Mixup
    'mosaic_prob': 1.0,
    'mixup_prob': 0.10,
    'mosaic_type': 'yolov5_mosaic',
    'mixup_type': 'yolov5_mixup',
    'mixup_scale': [0.5, 1.5]   # "mixup_scale" is not used for YOLOv5MixUp
}

yolov5_s_trans_config = {
    'aug_type': 'yolov5',
    # Basic Augment
    'degrees': 0.0,
    'translate': 0.2,
    'scale': [0.1, 2.0],
    'shear': 0.0,
    'perspective': 0.0,
    'hsv_h': 0.015,
    'hsv_s': 0.7,
    'hsv_v': 0.4,
    'use_ablu': True,
    # Mosaic & Mixup
    'mosaic_prob': 1.0,
    'mixup_prob': 0.0,
    'mosaic_type': 'yolov5_mosaic',
    'mixup_type': 'yolov5_mixup',
    'mixup_scale': [0.5, 1.5]   # "mixup_scale" is not used for YOLOv5MixUp
}

yolov5_n_trans_config = {
    'aug_type': 'yolov5',
    # Basic Augment
    'degrees': 0.0,
    'translate': 0.1,
    'scale': [0.5, 1.5],
    'shear': 0.0,
    'perspective': 0.0,
    'hsv_h': 0.015,
    'hsv_s': 0.7,
    'hsv_v': 0.4,
    'use_ablu': True,
    # Mosaic & Mixup
    'mosaic_prob': 1.0,
    'mixup_prob': 0.0,
    'mosaic_type': 'yolov5_mosaic',
    'mixup_type': 'yolov5_mixup',
    'mixup_scale': [0.5, 1.5]   # "mixup_scale" is not used for YOLOv5MixUp
}

yolov5_p_trans_config = {
    'aug_type': 'yolov5',
    # Basic Augment
    'degrees': 0.0,
    'translate': 0.1,
    'scale': [0.5, 1.5],
    'shear': 0.0,
    'perspective': 0.0,
    'hsv_h': 0.015,
    'hsv_s': 0.7,
    'hsv_v': 0.4,
    'use_ablu': True,
    # Mosaic & Mixup
    'mosaic_prob': 0.5,
    'mixup_prob': 0.0,
    'mosaic_type': 'yolov5_mosaic',
    'mixup_type': 'yolov5_mixup',
    'mixup_scale': [0.5, 1.5]   # "mixup_scale" is not used for YOLOv5MixUp
}


# ----------------------- YOLOX-Style Transform -----------------------
yolox_x_trans_config = {
    'aug_type': 'yolov5',
    # Basic Augment
    'degrees': 10.0,
    'translate': 0.1,
    'scale': [0.1, 2.0],
    'shear': 2.0,
    'perspective': 0.0,
    'hsv_h': 0.015,
    'hsv_s': 0.7,
    'hsv_v': 0.4,
    'use_ablu': False,
    # Mosaic & Mixup
    'mosaic_prob': 1.0,
    'mixup_prob': 1.0,
    'mosaic_type': 'yolov5_mosaic',
    'mixup_type': 'yolox_mixup',
    'mixup_scale': [0.5, 1.5]
}

yolox_l_trans_config = {
    'aug_type': 'yolov5',
    # Basic Augment
    'degrees': 10.0,
    'translate': 0.1,
    'scale': [0.1, 2.0],
    'shear': 2.0,
    'perspective': 0.0,
    'hsv_h': 0.015,
    'hsv_s': 0.7,
    'hsv_v': 0.4,
    'use_ablu': False,
    # Mosaic & Mixup
    'mosaic_prob': 1.0,
    'mixup_prob': 1.0,
    'mosaic_type': 'yolov5_mosaic',
    'mixup_type': 'yolox_mixup',
    'mixup_scale': [0.5, 1.5]   # "mixup_scale" is not used for YOLOv5MixUp
}

yolox_m_trans_config = {
    'aug_type': 'yolov5',
    # Basic Augment
    'degrees': 10.0,
    'translate': 0.1,
    'scale': [0.1, 2.0],
    'shear': 2.0,
    'perspective': 0.0,
    'hsv_h': 0.015,
    'hsv_s': 0.7,
    'hsv_v': 0.4,
    'use_ablu': False,
    # Mosaic & Mixup
    'mosaic_prob': 1.0,
    'mixup_prob': 1.0,
    'mosaic_type': 'yolov5_mosaic',
    'mixup_type': 'yolox_mixup',
    'mixup_scale': [0.5, 1.5]   # "mixup_scale" is not used for YOLOv5MixUp
}

yolox_s_trans_config = {
    'aug_type': 'yolov5',
    # Basic Augment
    'degrees': 10.0,
    'translate': 0.1,
    'scale': [0.1, 2.0],
    'shear': 2.0,
    'perspective': 0.0,
    'hsv_h': 0.015,
    'hsv_s': 0.7,
    'hsv_v': 0.4,
    'use_ablu': False,
    # Mosaic & Mixup
    'mosaic_prob': 1.0,
    'mixup_prob': 1.0,
    'mosaic_type': 'yolov5_mosaic',
    'mixup_type': 'yolox_mixup',
    'mixup_scale': [0.5, 1.5]   # "mixup_scale" is not used for YOLOv5MixUp
}

yolox_n_trans_config = {
    'aug_type': 'yolov5',
    # Basic Augment
    'degrees': 10.0,
    'translate': 0.1,
    'scale': [0.5, 1.5],
    'shear': 2.0,
    'perspective': 0.0,
    'hsv_h': 0.015,
    'hsv_s': 0.7,
    'hsv_v': 0.4,
    'use_ablu': False,
    # Mosaic & Mixup
    'mosaic_prob': 1.0,
    'mixup_prob': 0.5,
    'mosaic_type': 'yolov5_mosaic',
    'mixup_type': 'yolox_mixup',
    'mixup_scale': [0.5, 1.5]   # "mixup_scale" is not used for YOLOv5MixUp
}

yolox_p_trans_config = {
    'aug_type': 'yolov5',
    # Basic Augment
    'degrees': 10.0,
    'translate': 0.1,
    'scale': [0.5, 1.5],
    'shear': 2.0,
    'perspective': 0.0,
    'hsv_h': 0.015,
    'hsv_s': 0.7,
    'hsv_v': 0.4,
    'use_ablu': False,
    # Mosaic & Mixup
    'mosaic_prob': 0.5,
    'mixup_prob': 0.0,
    'mosaic_type': 'yolov5_mosaic',
    'mixup_type': 'yolox_mixup',
    'mixup_scale': [0.5, 1.5]   # "mixup_scale" is not used for YOLOv5MixUp
}


# ----------------------- SSD-Style Transform -----------------------
ssd_trans_config = {
    'aug_type': 'ssd',
    'use_ablu': False,
    # Mosaic & Mixup are not used for SSD-style augmentation
    'mosaic_prob': 0.,
    'mixup_prob': 0.,
    'mosaic_type': 'yolov5_mosaic',
    'mixup_type': 'yolov5_mixup',
    'mixup_scale': [0.5, 1.5]
}
