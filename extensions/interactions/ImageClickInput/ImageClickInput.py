# coding: utf-8
#
# Copyright 2014 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, softwar
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from extensions.interactions import base


class ImageClickInput(base.BaseInteraction):
    """Interaction allowing multiple-choice selection on an image."""

    name = 'Область изобржения'
    description = 'Позволяет учащимся выбирать области изображения.'
    display_mode = base.DISPLAY_MODE_SUPPLEMENTAL
    _dependency_ids = []
    answer_type = 'ClickOnImage'
    instructions = 'Нажать на изображение'
    narrow_instructions = 'Показать изображение'
    needs_summary = False

    _customization_arg_specs = [{
        'name': 'imageAndRegions',
        'description': 'Изображение',
        'schema': {
            'type': 'custom',
            'obj_type': 'ImageWithRegions',
        },
        'default_value': {
            'imagePath': '',
            'labeledRegions': []
        },
    }, {
        'name': 'highlightRegionsOnHover',
        'description': 'Выделять область, когда ученик наводит на нее курсор',
        'schema': {
            'type': 'bool',
        },
        'default_value': False
    }]
