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


class GraphInput(base.BaseInteraction):
    """Interaction for evaluating graphs."""

    name = 'Теория графов'
    description = 'Позволяет учащимся создавать и манипулировать графами.'
    display_mode = base.DISPLAY_MODE_SUPPLEMENTAL
    is_trainable = False
    _dependency_ids = []
    answer_type = 'Граф'
    instructions = 'Создать граф'
    narrow_instructions = 'Показать граф'
    needs_summary = True

    _customization_arg_specs = [{
        'name': 'graph',
        'description': 'Начальный граф',
        'schema': {
            'type': 'custom',
            'obj_type': 'Graph',
        },
        'default_value': {
            'vertices': [{
                'x': 150.0,
                'y': 50.0,
                'label': '',
            }, {
                'x': 200.0,
                'y': 50.0,
                'label': '',
            }, {
                'x': 150.0,
                'y': 100.0,
                'label': '',
            }],
            'edges': [{
                'src': 0,
                'dst': 1,
                'weight': 1,
            }, {
                'src': 1,
                'dst': 2,
                'weight': 1,
            }],
            'isLabeled': False,
            'isDirected': False,
            'isWeighted': False,
        }
    }, {
        'name': 'canAddVertex',
        'description': 'Разрешить ученику добавлять вершины',
        'schema': {
            'type': 'bool',
        },
        'default_value': False
    }, {
        'name': 'canDeleteVertex',
        'description': 'Разрешить ученику удалять вершины',
        'schema': {
            'type': 'bool',
        },
        'default_value': False
    }, {
        'name': 'canMoveVertex',
        'description': 'Разрешить ученику передвигать вершины',
        'schema': {
            'type': 'bool',
        },
        'default_value': True
    }, {
        'name': 'canEditVertexLabel',
        'description': 'Разрешить учащимся редактировать метки вершинs',
        'schema': {
            'type': 'bool',
        },
        'default_value': False
    }, {
        'name': 'canAddEdge',
        'description': 'Разрешить учащемуся добавлять ребра',
        'schema': {
            'type': 'bool',
        },
        'default_value': True
    }, {
        'name': 'canDeleteEdge',
        'description': 'Разрешить учащемуся удалять ребра',
        'schema': {
            'type': 'bool',
        },
        'default_value': True
    }, {
        'name': 'canEditEdgeWeight',
        'description': 'Разрешить учащемуся редактировать ребра',
        'schema': {
            'type': 'bool',
        },
        'default_value': False
    }]
